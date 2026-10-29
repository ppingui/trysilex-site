#!/usr/bin/env python3
"""Static site generator for trysilex.com.

Stdlib only. Reads page fragments from src/pages/*.html (English) and
src/pages/<locale>/*.html (translations), wraps them in src/_base.html, and
writes plain HTML to the repo root so GitHub Pages can serve it with no build
step. Run: python3 build.py

Languages: per-locale strings and verified crisis resources live in i18n.py.
A translated page names its English source in its meta ("en": "<english slug>");
pages sharing a source are one hreflang group, each listing every other version
plus an x-default pointing at English.
"""

from __future__ import annotations

import html
import json
import re
import shutil
import unicodedata
from pathlib import Path

from i18n import LOCALES, pretty_date
from to_markdown import page_markdown

ROOT = Path(__file__).parent
SRC = ROOT / "src"
PAGES = SRC / "pages"

SITE = "https://trysilex.com"
BRAND = "Silex"
BRAND_FULL = "Silex — Stop Gambling"
APP_ID = "6798826038"
AUTHOR = "Kyrylo Lozovyi"

# The same person builds vitalityrize.me, and both sites reference one Person
# node by the same @id so search engines merge the entity rather than seeing
# two unrelated developers with the same name.
PERSON_ID = "https://www.vitalityrize.me/#kyrylo"
PERSON_SAME_AS = [
    "https://github.com/ppingui",
    "https://www.vitalityrize.me/about/",
]

# Set to True the moment 1.0 clears App Review. Flips every CTA on the site.
APP_STORE_LIVE = True

# Apple provider token from App Store Connect (Analytics → Campaigns). Until it
# is filled in, links carry no campaign params rather than broken ones.
PROVIDER_TOKEN = ""

# Cloudflare Web Analytics beacon token (cookieless). Empty = no analytics.
ANALYTICS_TOKEN = ""

# Search snippets truncate around here. CJK characters count double.
TITLE_MAX, DESC_MAX = 62, 160


def app_store_url(campaign: str) -> str:
    """App Store link, with campaign attribution when the provider token is set.
    The bare /app/id URL redirects each visitor to their own storefront, which is
    right for every language."""
    base = f"https://apps.apple.com/app/id{APP_ID}"
    if PROVIDER_TOKEN:
        return f"{base}?pt={PROVIDER_TOKEN}&ct={campaign}&mt=8"
    return f"{base}?mt=8"


def helpline_block(L: dict) -> str:
    rows = "\n".join(
        f'      <li><span class="hl-region">{r}</span>'
        f'<a href="{u}">{n}</a><span class="hl-note">{d}</span></li>'
        for r, n, u, d in L["helplines"]
    )
    return (
        f'  <aside class="helplines" aria-label="{html.escape(L["help_title"])}">\n'
        f'    <h2>{L["help_title"]}</h2>\n'
        f"    <ul>\n{rows}\n    </ul>\n"
        "  </aside>"
    )


def cta_block(campaign: str, L: dict) -> str:
    """The one CTA component. Honest about review status until the app is live.
    A campaign ending in "_hero" renders as a bare button: at the top of a page the
    headline is already right above it, and the button must clear the phone fold."""
    if campaign.endswith("_hero"):
        return (f'  <p class="cta-hero"><a class="btn" href="{app_store_url(campaign)}">'
                f'{L["cta_btn"]}</a></p>')
    pending = "" if APP_STORE_LIVE else (
        '\n      <p class="cta-pending">Silex is in App Store review. '
        "This link goes live at launch.</p>"
    )
    return (
        f'  <section class="cta">\n    <h2>{L["cta_h"]}</h2>\n'
        f'    <p>{L["cta_p"]}</p>\n'
        f'    <p><a class="btn" href="{app_store_url(campaign)}">{L["cta_btn"]}</a></p>'
        f"{pending}\n  </section>"
    )


# --- template plumbing --------------------------------------------------------

META_RE = re.compile(r"^<!--meta\s*(\{.*?\})\s*-->\s*", re.DOTALL)
SHORTCODE_RE = re.compile(r"\{\{cta:([a-z0-9_]+)\}\}")


def parse_fragment(path: Path, loc: str) -> tuple[dict, str]:
    raw = path.read_text(encoding="utf-8")
    m = META_RE.match(raw)
    if not m:
        raise SystemExit(f"{path}: missing leading <!--meta {{...}} --> block")
    meta = json.loads(m.group(1))
    for key in ("slug", "title", "description", "h1"):
        if key not in meta:
            raise SystemExit(f"{path}: meta is missing '{key}'")
    if loc != "en" and "en" not in meta:
        raise SystemExit(f"{path}: translated page needs an \"en\" key naming its English source")
    meta["loc"] = loc
    if loc == "en":
        meta["path"] = meta["slug"]
    else:  # a translated homepage has slug "" and lives at /<locale>/
        meta["path"] = loc if meta["slug"] == "" else f"{loc}/{meta['slug']}"
    meta["group"] = meta["slug"] if loc == "en" else meta["en"]
    return meta, raw[m.end():]


def canonical_for(path: str) -> str:
    return f"{SITE}/" if path == "" else f"{SITE}/{path}/"


def nav_html(L: dict, active_path: str) -> str:
    items = []
    for href, label in L["nav"]:
        cur = ' aria-current="page"' if href.strip("/") == active_path else ""
        items.append(f'<a href="{href}"{cur}>{label}</a>')
    return "".join(items)


def faq_html(faq: list, L: dict) -> str:
    if not faq:
        return ""
    rows = "\n".join(
        f"    <h3>{html.escape(q)}</h3>\n    <p>{a}</p>" for q, a in faq
    )
    return (
        f'  <section class="faq" id="faq">\n    <h2>{L["faq"]}</h2>\n'
        f"{rows}\n  </section>"
    )


def byline_html(meta: dict, L: dict) -> str:
    if meta.get("type") != "article":
        return ""
    loc = meta["loc"]
    pub, upd = meta["published"], meta.get("updated", meta["published"])
    updated = "" if pub == upd else \
        f' · {L["updated"]} <time datetime="{upd}">{pretty_date(upd, loc)}</time>'
    reviewer = meta.get("reviewer")
    rev = f' · Reviewed by {html.escape(reviewer)}' if reviewer else ""
    return (
        f'  <p class="byline">{L["by"]} <a rel="author" href="/about/">'
        f"{AUTHOR}</a>{rev} · "
        f'<time datetime="{pub}">{pretty_date(pub, loc)}</time>{updated}</p>'
    )


def alternates_html(meta: dict, groups: dict) -> str:
    versions = groups.get(meta["group"], {})
    if len(versions) < 2:
        return ""
    lines = [f'<link rel="alternate" hreflang="{LOCALES[loc]["hreflang"]}" href="{canonical_for(p)}">'
             for loc, p in sorted(versions.items())]
    if "en" in versions:
        lines.append(f'<link rel="alternate" hreflang="x-default" href="{canonical_for(versions["en"])}">')
    return "\n".join(lines) + "\n"


def href_for(path: str) -> str:
    return "/" if path == "" else f"/{path}/"


# Where each language starts: its translated homepage if there is one, otherwise
# its hub (the first nav item). Filled in by main() once all pages are loaded.
ENTRY: dict[str, str] = {}

# The product docs under /docs/, in reading order. Filled in by main().
DOCS: list[dict] = []


def is_doc(meta: dict) -> bool:
    return meta["path"] == "docs" or meta["path"].startswith("docs/")


def llms_href(meta: dict) -> str:
    """The llms.txt an agent should start from: the docs keep their own index."""
    return "/docs/llms.txt" if is_doc(meta) else "/llms.txt"


def docs_toc_html(meta: dict) -> str:
    """Contents list at the end of every docs page."""
    rows = []
    for d in DOCS:
        cur = ' aria-current="page"' if d is meta else ""
        rows.append(f'      <li><a href="/{d["path"]}/"{cur}>{d["h1"]}</a></li>')
    items = "\n".join(rows)
    return (f'  <section class="docs-toc">\n    <h2>Silex documentation</h2>\n'
            f"    <ul>\n{items}\n    </ul>\n  </section>")


def langs_html(meta: dict, groups: dict) -> str:
    order = list(LOCALES)
    if meta["group"] == "":
        # Homepages link every language, not just the ones with a translated
        # homepage — this row is how visitors (and crawlers) find the rest.
        # hreflang stays strict and only lists true equivalents.
        versions = dict(ENTRY)
    else:
        versions = groups.get(meta["group"], {})
        if len(versions) < 2:
            return ""
    links = []
    for loc in sorted(versions, key=order.index):
        cur = ' aria-current="true"' if loc == meta["loc"] else ""
        links.append(f'<a href="{href_for(versions[loc])}" hreflang="{LOCALES[loc]["hreflang"]}" '
                     f'lang="{LOCALES[loc]["html"]}"{cur}>{LOCALES[loc]["label"]}</a>')
    return f'<nav class="langs" aria-label="Language"><div class="wrap">{"".join(links)}</div></nav>\n'


def jsonld_for(meta: dict, L: dict) -> str:
    org = {
        "@type": "Organization",
        "@id": f"{SITE}/#org",
        "name": BRAND_FULL,
        "url": SITE,
        "founder": {"@id": PERSON_ID},
        "email": "support@trysilex.com",
    }
    person = {
        "@type": "Person",
        "@id": PERSON_ID,
        "name": AUTHOR,
        "url": f"{SITE}/about/",
        "jobTitle": "Independent iOS developer",
        "worksFor": {"@id": f"{SITE}/#org"},
        "sameAs": PERSON_SAME_AS,
    }
    graph: list[dict] = [person, org]
    url = canonical_for(meta["path"])

    if meta["path"] == "":
        graph += [
            {
                "@type": "WebSite",
                "@id": f"{SITE}/#website",
                "url": SITE,
                "name": BRAND_FULL,
                "publisher": {"@id": f"{SITE}/#org"},
            },
            {
                "@type": "SoftwareApplication",
                "@id": f"{SITE}/#app",
                "name": "Silex: Stop Gambling",
                "operatingSystem": "iOS 17.0 or later",
                "applicationCategory": "HealthApplication",
                "url": app_store_url("schema"),
                "author": {"@id": f"{SITE}/#org"},
                "offers": [
                    {"@type": "Offer", "price": "4.99", "priceCurrency": "USD",
                     "name": "Weekly"},
                    {"@type": "Offer", "price": "49.99", "priceCurrency": "USD",
                     "name": "Annual, 3-day free trial"},
                ],
            },
        ]

    if meta.get("type") == "article":
        graph.append({
            "@type": "Article",
            "@id": url + "#article",
            "headline": meta["h1"],
            "description": meta["description"],
            "inLanguage": L["hreflang"],
            "datePublished": meta["published"],
            "dateModified": meta.get("updated", meta["published"]),
            "author": {"@id": PERSON_ID},
            "publisher": {"@id": f"{SITE}/#org"},
            "mainEntityOfPage": url,
        })
        home = SITE if meta["loc"] == "en" else SITE + L["nav"][0][0]
        graph.append({
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": L["home"], "item": home},
                {"@type": "ListItem", "position": 2, "name": meta["h1"], "item": url},
            ],
        })

    if meta.get("faq"):
        graph.append({
            "@type": "FAQPage",
            "inLanguage": L["hreflang"],
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}}
                for q, a in meta["faq"]
            ],
        })

    payload = {"@context": "https://schema.org", "@graph": graph}
    return ('<script type="application/ld+json">'
            + json.dumps(payload, separators=(",", ":"), ensure_ascii=False) + "</script>")


def footer_html(L: dict) -> tuple[str, str]:
    nav = "\n      ".join(f'<a href="{h}">{t}</a>' for h, t in L["footer"])
    copy = (f'© 2026 {BRAND} · {L["built_by"]} <a href="/about/">{AUTHOR}</a> '
            f'{L["in_city"]} · <a href="mailto:support@trysilex.com">support@trysilex.com</a>\n'
            f'      · {L["also_by"]}: <a href="https://www.vitalityrize.me/">VitalityRise</a>, {L["vr_desc"]}')
    return nav, copy


def render(meta: dict, body: str, template: str, groups: dict) -> str:
    L = LOCALES[meta["loc"]]
    body = SHORTCODE_RE.sub(lambda m: cta_block(m.group(1), L), body)
    tldr = meta.get("tldr")
    tldr_html = (
        f'  <div class="tldr"><p><strong>{L["short"]}</strong> {tldr}</p></div>\n'
        if tldr else ""
    )
    analytics = (
        f'<script defer src="https://static.cloudflareinsights.com/beacon.min.js" '
        f'data-cf-beacon=\'{{"token": "{ANALYTICS_TOKEN}"}}\'></script>'
        if ANALYTICS_TOKEN else ""
    )
    noindex = bool(meta.get("noindex"))
    footer_nav, copy = footer_html(L)
    subs = {
        "lang": L["html"],
        "og_locale": L["og"],
        "title": html.escape(meta["title"]),
        "description": html.escape(meta["description"]),
        # A noindex page has no canonical URL of its own — point at the root.
        "canonical": SITE + "/" if noindex else canonical_for(meta["path"]),
        "alternates": "" if noindex else alternates_html(meta, groups),
        "head_extra": '<meta name="robots" content="noindex">\n' if noindex else "",
        "og_image": f"{SITE}/assets/og.png",
        "skip": L["skip"],
        "home_href": href_for(ENTRY.get(meta["loc"], "")),
        "nav": nav_html(L, meta["path"]),
        "langs": langs_html(meta, groups),
        "h1": meta["h1"],
        "byline": byline_html(meta, L),
        "tldr": tldr_html,
        "body": body.strip(),
        "faq": faq_html(meta.get("faq", []), L) + (docs_toc_html(meta) if is_doc(meta) else ""),
        "llms_href": llms_href(meta),
        "helplines": helpline_block(L),
        "jsonld": jsonld_for(meta, L),
        "analytics": analytics,
        "app_id": APP_ID,
        "disclaimer": L["disclaimer"],
        "footer_nav": footer_nav,
        "copy": copy,
        "main_class": "article" if meta.get("type") == "article" else "page",
    }
    out = template
    for key, value in subs.items():
        out = out.replace("{{" + key + "}}", value)
    leftover = re.findall(r"\{\{[a-z_]+\}\}", out)
    if leftover:
        raise SystemExit(f"{meta['path'] or 'index'}: unresolved {set(leftover)}")
    return out


def visual_len(s: str) -> int:
    """Length as a search snippet sees it: wide (CJK) characters count double."""
    return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in s)


def load_pages() -> list[tuple[dict, str, Path]]:
    pages = [(*parse_fragment(p, "en"), p)
             for p in sorted(PAGES.glob("*.html")) + sorted((PAGES / "docs").glob("*.html"))]
    for loc in LOCALES:
        if loc == "en":
            continue
        for p in sorted((PAGES / loc).glob("*.html")):
            pages.append((*parse_fragment(p, loc), p))
    return pages


def main() -> None:
    template = (SRC / "_base.html").read_text(encoding="utf-8")
    pages = load_pages()

    # hreflang groups: English slug -> {locale: path}
    groups: dict[str, dict[str, str]] = {}
    for meta, _, path in pages:
        g = groups.setdefault(meta["group"], {})
        if meta["loc"] in g:
            raise SystemExit(f"{path}: duplicate {meta['loc']} page for group '{meta['group']}'")
        g[meta["loc"]] = meta["path"]
    for loc, L in LOCALES.items():
        ENTRY[loc] = groups.get("", {}).get(loc, L["nav"][0][0].strip("/"))
    english = {m["slug"] for m, _, _ in pages if m["loc"] == "en"}
    for key, versions in groups.items():
        if key not in english:
            raise SystemExit(f"translations point at English page '{key}', which does not exist")

    DOCS[:] = sorted((m for m, _, _ in pages if is_doc(m)), key=lambda m: m.get("order", 0))

    warnings = []
    bodies: dict[str, str] = {}
    for meta, body, src in pages:
        bodies[meta["path"]] = body
        out_path = ROOT / "index.html" if meta["path"] == "" else ROOT / meta["path"] / "index.html"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(render(meta, body, template, groups), encoding="utf-8")
        print(f"  {str(src.relative_to(PAGES)):46} -> {out_path.relative_to(ROOT)}")
        if meta["loc"] != "en" and meta.get("slug") != "404":
            if visual_len(meta["title"]) > TITLE_MAX:
                warnings.append(f"{meta['path']}: title {visual_len(meta['title'])} > {TITLE_MAX}")
            if visual_len(meta["description"]) > DESC_MAX:
                warnings.append(f"{meta['path']}: description {visual_len(meta['description'])} > {DESC_MAX}")

    # 404 (GitHub Pages serves /404.html for unknown paths)
    if any(m["path"] == "404" for m, _, _ in pages):
        shutil.copyfile(ROOT / "404" / "index.html", ROOT / "404.html")
        shutil.rmtree(ROOT / "404")
        print("  404/index.html                                 -> 404.html")

    indexable = [m for m, _, _ in pages if m["path"] != "404" and not m.get("noindex")]
    urls = []
    for meta in sorted(indexable, key=lambda m: m["path"]):
        lastmod = meta.get("updated", meta.get("published", "2026-08-10"))
        prio = "1.0" if meta["path"] == "" else "0.8"
        urls.append(
            f"  <url><loc>{canonical_for(meta['path'])}</loc>"
            f"<lastmod>{lastmod}</lastmod><priority>{prio}</priority></url>"
        )
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n",
        encoding="utf-8",
    )

    # The index.md copies are for agents; Google gets the HTML only, so its crawl
    # budget isn't spent on duplicates.
    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n"
        "User-agent: Googlebot\nDisallow: /*.md$\n\n"
        f"Sitemap: {SITE}/sitemap.xml\n",
        encoding="utf-8",
    )

    (ROOT / "CNAME").write_text("trysilex.com\n", encoding="utf-8")
    # No Jekyll: it would turn each index.md into HTML over the real index.html.
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")

    # index.md beside every indexable page: the same content as Markdown, for agents.
    def md_url(path: str) -> str:
        return canonical_for(path) + "index.md"

    for meta in indexable:
        page_dir = ROOT / meta["path"] if meta["path"] else ROOT
        header = (f"> For the complete index of this site, see [llms.txt]({SITE}{llms_href(meta)}). "
                  f"This page on the web: {canonical_for(meta['path'])}")
        md = page_markdown((page_dir / "index.html").read_text(encoding="utf-8"),
                           canonical_for(meta["path"]), header)
        (page_dir / "index.md").write_text(md, encoding="utf-8")

    # Plain-text site summary for answer engines that fetch it.
    summary = ("An iPhone app that blocks gambling across the phone, runs a 90-day "
               "evidence-based quit program, and tracks the money you keep. "
               "No accounts, no ads, and nothing a user writes leaves the phone. Built by "
               f"{AUTHOR}. Weekly $4.99 or annual $49.99 with a 3-day free trial.")
    lines = [f"# {BRAND_FULL}", "", f"> {summary}",
             "", "Each link below is the Markdown version of a page; drop `index.md` for the "
             "web page.",
             "", f"The full text of every page, in one file: {SITE}/llms-full.txt",
             "", f"Product documentation (setup, blocking, subscriptions, privacy): {SITE}/docs/llms.txt",
             "", "## Pages", ""]
    for meta in sorted((m for m in indexable if m["loc"] == "en"), key=lambda m: m["path"]):
        lines.append(f"- [{meta['h1']}]({md_url(meta['path'])}): {meta['description']}")
    lines += ["", "## Other languages", ""]
    for meta in sorted((m for m in indexable if m["loc"] != "en"), key=lambda m: m["path"]):
        lines.append(f"- [{meta['h1']}]({md_url(meta['path'])}) ({LOCALES[meta['loc']]['label']}): "
                     f"{meta['description']}")
    (ROOT / "llms.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # /docs/llms.txt: the product docs on their own, where docs tools look first.
    docs = ["# Silex documentation", "",
            "> How to set up and use Silex, the iPhone app that blocks gambling and runs a "
            "90-day quit program: protection layers, the SOS button, the program, "
            "subscriptions, privacy and troubleshooting.", "",
            "Each link is the Markdown version of a page; drop `index.md` for the web page.",
            "", f"Everything else on the site, including the free guides: {SITE}/llms.txt",
            "", "## Docs", ""]
    for meta in DOCS:
        docs.append(f"- [{meta['h1']}]({md_url(meta['path'])}): {meta['description']}")
    (ROOT / "docs" / "llms.txt").write_text("\n".join(docs) + "\n", encoding="utf-8")

    # llms-full.txt: every indexable page as plain text, for answer engines that
    # fetch the whole site in one request. Shortcodes, scripts and the tools'
    # form UI are stripped; FAQs stay as Q/A pairs. English first, then each
    # locale. Crisis resources are listed once, up front, so a quote from this
    # site in a crisis context carries correct, verified numbers.
    def plain(fragment: str) -> str:
        t = SHORTCODE_RE.sub("", fragment)
        t = re.sub(r"<(script|style|form|noscript|select)\b.*?</\1>", "", t, flags=re.S)
        t = re.sub(r"\s+", " ", t)                   # source line wraps are not breaks
        t = re.sub(r"</(p|li|h[1-6]|tr|div|table|ul|ol)>", "\n", t)
        t = re.sub(r"<li[^>]*>", "- ", t)
        t = re.sub(r"</t[dh]>\s*<t[dh][^>]*>", " | ", t)
        t = re.sub(r"<h2[^>]*>", "\n## ", t)
        t = re.sub(r"<h3[^>]*>", "\n### ", t)
        t = re.sub(r"<br\s*/?>", "\n", t)
        t = re.sub(r"<[^>]+>", "", t)
        t = html.unescape(t)
        t = re.sub(r"[ \t]+", " ", t)
        t = re.sub(r" *\n *", "\n", t)
        return re.sub(r"\n{3,}", "\n\n", t).strip()

    order = list(LOCALES)
    full = [f"# {BRAND_FULL}", "", summary, "",
            "Silex is a wellness app, not medical care, and does not diagnose or treat any condition.",
            "", f"Index: {SITE}/llms.txt", "", "## Crisis resources (verified 2026-10-26)", ""]
    for loc in order:
        for region, name, url, desc in LOCALES[loc]["helplines"]:
            full.append(f"- [{LOCALES[loc]['label']}] {region}: {name} — {html.unescape(desc)}")
    for meta in sorted(indexable, key=lambda m: (order.index(m["loc"]), m["path"])):
        L = LOCALES[meta["loc"]]
        full += ["", "=" * 72, f"# {meta['h1']}",
                 f"URL: {canonical_for(meta['path'])}",
                 f"Language: {L['hreflang']}",
                 f"Description: {meta['description']}"]
        if meta.get("published"):
            full.append(f"Published: {meta['published']} · Updated: "
                        f"{meta.get('updated', meta['published'])}")
        if meta.get("tldr"):
            full += ["", f"{L['short']} {plain(meta['tldr'])}"]
        full += ["", plain(bodies[meta["path"]])]
        if meta.get("faq"):
            full += ["", f"## {L['faq']}"]
            for q, a in meta["faq"]:
                full += ["", f"Q: {q}", f"A: {plain(a)}"]
    (ROOT / "llms-full.txt").write_text("\n".join(full) + "\n", encoding="utf-8")

    n_loc = sum(1 for m in indexable if m["loc"] != "en")
    print(f"\n{len(urls)} pages ({n_loc} translated), sitemap + robots + llms.txt + llms-full.txt + CNAME written.")
    for w in warnings:
        print("  warn:", w)


if __name__ == "__main__":
    main()
