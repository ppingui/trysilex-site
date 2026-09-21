#!/usr/bin/env python3
"""Static site generator for trysilex.com.

Stdlib only. Reads page fragments from src/pages/*.html, wraps them in
src/_base.html, and writes plain HTML to the repo root so GitHub Pages can
serve it with no build step. Run: python3 build.py
"""

from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path

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

NAV = [
    ("/how-to-stop-gambling/", "How to stop"),
    ("/best-gambling-blocker-apps/", "Blockers"),
    ("/gambling-self-check/", "Self-check"),
    ("/about/", "About"),
]


def app_store_url(campaign: str) -> str:
    """App Store link, with campaign attribution when the provider token is set."""
    base = f"https://apps.apple.com/app/id{APP_ID}"
    if PROVIDER_TOKEN:
        return f"{base}?pt={PROVIDER_TOKEN}&ct={campaign}&mt=8"
    return f"{base}?mt=8"


# --- helplines: kept in sync with App/Services/RegionResources.swift -----------
# Verify every number at each publish (product rule).
HELPLINES = [
    ("US", "1-800-GAMBLER", "tel:18004262537",
     "National Problem Gambling Helpline — free, confidential, 24/7"),
    ("US", "988", "tel:988",
     "Suicide &amp; Crisis Lifeline — call or text if it feels like too much"),
    ("UK", "0808 8020 133", "tel:08088020133",
     "National Gambling Helpline (GamCare) — free, confidential, 24/7"),
    ("UK", "116 123", "tel:116123", "Samaritans"),
    ("Elsewhere", "findahelpline.com", "https://findahelpline.com",
     "Crisis lines for your country"),
]


def helpline_block() -> str:
    rows = "\n".join(
        f'      <li><span class="hl-region">{r}</span>'
        f'<a href="{u}">{n}</a><span class="hl-note">{d}</span></li>'
        for r, n, u, d in HELPLINES
    )
    return (
        '  <aside class="helplines" aria-label="Crisis helplines">\n'
        "    <h2>If you need someone right now</h2>\n"
        f"    <ul>\n{rows}\n    </ul>\n"
        "  </aside>"
    )


def cta_block(campaign: str, heading: str, sub: str) -> str:
    """The one CTA component. Honest about review status until the app is live."""
    pending = "" if APP_STORE_LIVE else (
        '\n      <p class="cta-pending">Silex is in App Store review. '
        "This link goes live at launch.</p>"
    )
    return (
        f'  <section class="cta">\n    <h2>{heading}</h2>\n'
        f"    <p>{sub}</p>\n"
        f'    <p><a class="btn" href="{app_store_url(campaign)}">'
        "Get Silex on iPhone</a></p>"
        f"{pending}\n  </section>"
    )


# --- template plumbing --------------------------------------------------------

META_RE = re.compile(r"^<!--meta\s*(\{.*?\})\s*-->\s*", re.DOTALL)
SHORTCODE_RE = re.compile(r"\{\{cta:([a-z0-9_]+)\}\}")


def parse_fragment(path: Path) -> tuple[dict, str]:
    raw = path.read_text(encoding="utf-8")
    m = META_RE.match(raw)
    if not m:
        raise SystemExit(f"{path.name}: missing leading <!--meta {{...}} --> block")
    meta = json.loads(m.group(1))
    for key in ("slug", "title", "description", "h1"):
        if key not in meta:
            raise SystemExit(f"{path.name}: meta is missing '{key}'")
    return meta, raw[m.end():]


def canonical_for(slug: str) -> str:
    return f"{SITE}/" if slug == "" else f"{SITE}/{slug}/"


def nav_html(active_slug: str) -> str:
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href.strip("/") == active_slug else ""
        items.append(f'<a href="{href}"{cur}>{label}</a>')
    return "".join(items)


def faq_html(faq: list) -> str:
    if not faq:
        return ""
    rows = "\n".join(
        f"    <h3>{html.escape(q)}</h3>\n    <p>{a}</p>" for q, a in faq
    )
    return (
        '  <section class="faq" id="faq">\n    <h2>Common questions</h2>\n'
        f"{rows}\n  </section>"
    )


def byline_html(meta: dict) -> str:
    if meta.get("type") != "article":
        return ""
    pub, upd = meta["published"], meta.get("updated", meta["published"])
    same = pub == upd
    updated = "" if same else f' · Updated <time datetime="{upd}">{pretty(upd)}</time>'
    reviewer = meta.get("reviewer")
    rev = f' · Reviewed by {html.escape(reviewer)}' if reviewer else ""
    return (
        '  <p class="byline">By <a rel="author" href="/about/">'
        f"{AUTHOR}</a>{rev} · "
        f'<time datetime="{pub}">{pretty(pub)}</time>{updated}</p>'
    )


MONTHS = ("January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December")


def pretty(iso: str) -> str:
    y, m, d = iso.split("-")
    return f"{MONTHS[int(m) - 1]} {int(d)}, {y}"


def jsonld_for(meta: dict) -> str:
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

    if meta["slug"] == "":
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
            "@id": canonical_for(meta["slug"]) + "#article",
            "headline": meta["h1"],
            "description": meta["description"],
            "datePublished": meta["published"],
            "dateModified": meta.get("updated", meta["published"]),
            "author": {"@id": PERSON_ID},
            "publisher": {"@id": f"{SITE}/#org"},
            "mainEntityOfPage": canonical_for(meta["slug"]),
        })
        graph.append({
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE},
                {"@type": "ListItem", "position": 2, "name": meta["h1"],
                 "item": canonical_for(meta["slug"])},
            ],
        })

    if meta.get("faq"):
        graph.append({
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}}
                for q, a in meta["faq"]
            ],
        })

    payload = {"@context": "https://schema.org", "@graph": graph}
    return ('<script type="application/ld+json">'
            + json.dumps(payload, separators=(",", ":")) + "</script>")


def render(meta: dict, body: str, template: str) -> str:
    body = SHORTCODE_RE.sub(
        lambda m: cta_block(
            m.group(1),
            "Quit for good. Keep the money.",
            "Silex blocks gambling across your iPhone and walks you through 90 days, "
            "one at a time.",
        ),
        body,
    )
    tldr = meta.get("tldr")
    tldr_html = (
        f'  <div class="tldr"><p><strong>Short answer:</strong> {tldr}</p></div>\n'
        if tldr else ""
    )
    analytics = (
        f'<script defer src="https://static.cloudflareinsights.com/beacon.min.js" '
        f'data-cf-beacon=\'{{"token": "{ANALYTICS_TOKEN}"}}\'></script>'
        if ANALYTICS_TOKEN else ""
    )
    noindex = bool(meta.get("noindex"))
    out = template
    subs = {
        "title": html.escape(meta["title"]),
        "description": html.escape(meta["description"]),
        # A noindex page has no canonical URL of its own — point at the root.
        "canonical": SITE + "/" if noindex else canonical_for(meta["slug"]),
        "head_extra": '<meta name="robots" content="noindex">\n' if noindex else "",
        "og_image": f"{SITE}/assets/og.png",
        "nav": nav_html(meta["slug"]),
        "h1": meta["h1"],
        "byline": byline_html(meta),
        "tldr": tldr_html,
        "body": body.strip(),
        "faq": faq_html(meta.get("faq", [])),
        "helplines": helpline_block(),
        "jsonld": jsonld_for(meta),
        "analytics": analytics,
        "app_id": APP_ID,
        "year": "2026",
        "brand": BRAND,
        "main_class": "article" if meta.get("type") == "article" else "page",
    }
    for key, value in subs.items():
        out = out.replace("{{" + key + "}}", value)
    leftover = re.findall(r"\{\{[a-z_]+\}\}", out)
    if leftover:
        raise SystemExit(f"{meta['slug'] or 'index'}: unresolved {set(leftover)}")
    return out


def main() -> None:
    template = (SRC / "_base.html").read_text(encoding="utf-8")
    pages = []

    for path in sorted(PAGES.glob("*.html")):
        meta, body = parse_fragment(path)
        out_path = ROOT / "index.html" if meta["slug"] == "" \
            else ROOT / meta["slug"] / "index.html"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(render(meta, body, template), encoding="utf-8")
        pages.append(meta)
        print(f"  {path.name:38} -> {out_path.relative_to(ROOT)}")

    # 404 (GitHub Pages serves /404.html for unknown paths)
    nf = next((m for m in pages if m["slug"] == "404"), None)
    if nf:
        shutil.copyfile(ROOT / "404" / "index.html", ROOT / "404.html")
        shutil.rmtree(ROOT / "404")
        print("  404/index.html                         -> 404.html")

    urls = []
    for meta in sorted(pages, key=lambda m: m["slug"]):
        if meta["slug"] == "404":
            continue
        lastmod = meta.get("updated", meta.get("published", "2026-08-10"))
        prio = "1.0" if meta["slug"] == "" else "0.8"
        urls.append(
            f"  <url><loc>{canonical_for(meta['slug'])}</loc>"
            f"<lastmod>{lastmod}</lastmod><priority>{prio}</priority></url>"
        )
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n",
        encoding="utf-8",
    )

    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n"
        f"Sitemap: {SITE}/sitemap.xml\n",
        encoding="utf-8",
    )

    (ROOT / "CNAME").write_text("trysilex.com\n", encoding="utf-8")

    # Plain-text site summary for answer engines that fetch it.
    lines = [f"# {BRAND_FULL}", "",
             "An iPhone app that blocks gambling across the phone, runs a 90-day "
             "evidence-based quit program, and tracks the money you keep. "
             "No accounts, no tracking, no ads. Built by "
             f"{AUTHOR}. Weekly $4.99 or annual $49.99 with a 3-day free trial.",
             "", "## Pages", ""]
    for meta in sorted(pages, key=lambda m: m["slug"]):
        if meta["slug"] == "404":
            continue
        lines.append(f"- [{meta['h1']}]({canonical_for(meta['slug'])}): "
                     f"{meta['description']}")
    (ROOT / "llms.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"\n{len(urls)} pages, sitemap + robots + llms.txt + CNAME written.")


if __name__ == "__main__":
    main()
