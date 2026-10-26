#!/usr/bin/env python3
"""Ask Google, per URL, whether it is actually indexed — and if not, why.

Reuses gsc_report.py's OAuth. Slow (a few seconds per URL), so run it in the
background and read the output file.

    python3 gsc_inspect.py            # every URL in sitemap.xml
"""
import json, re, sys, urllib.request, pathlib
from gsc_report import oauth_token, SITE

INSPECT = "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect"


def inspect(token: str, url: str) -> dict:
    body = json.dumps({"inspectionUrl": url, "siteUrl": SITE}).encode()
    req = urllib.request.Request(
        INSPECT, data=body,
        headers={"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def main() -> int:
    sitemap = (pathlib.Path(__file__).parent / "sitemap.xml").read_text()
    urls = re.findall(r"<loc>([^<]+)</loc>", sitemap)
    token = oauth_token()
    print(f"{'page':44} {'coverage':38} last crawl")
    indexed = 0
    for u in urls:
        try:
            res = inspect(token, u)["inspectionResult"]["indexStatusResult"]
        except Exception as exc:
            print(f"{u.replace('https://trysilex.com','') or '/':44} ERROR {exc}")
            continue
        cov = res.get("coverageState", "?")
        crawl = (res.get("lastCrawlTime") or "never")[:10]
        if "Submitted and indexed" in cov or cov == "Indexed, not submitted in sitemap":
            indexed += 1
        print(f"{u.replace('https://trysilex.com','') or '/':44} {cov:38} {crawl}")
        sys.stdout.flush()
    print(f"\n{indexed}/{len(urls)} indexed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
