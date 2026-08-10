# trysilex.com

Marketing and content site for **Silex — Stop Gambling** (iOS app, App Store id `6798826038`).

Static HTML, no framework, no build dependencies beyond Python 3. Served by GitHub Pages
directly from the repo root on `main`, exactly like `pixelislands-site`.

## Editing

Page sources live in `src/pages/*.html`. Each one starts with a metadata block:

```html
<!--meta
{
  "slug": "how-to-stop-gambling",
  "type": "article",              // "article" adds byline + Article/Breadcrumb schema
  "published": "2026-08-10",
  "updated": "2026-08-12",        // optional; shows "Updated …" in the byline
  "title": "…",                   // <title> and og:title, ~60 chars
  "description": "…",             // meta description, ~155 chars
  "h1": "…",
  "tldr": "…",                    // optional; renders the Short answer block
  "noindex": true,                // optional
  "faq": [["Question?", "Answer."]]   // renders the FAQ section + FAQPage schema
}
-->
```

`{{cta:campaign_name}}` anywhere in the body renders the App Store call-to-action.
The campaign name becomes the `ct=` attribution token once `PROVIDER_TOKEN` is set.

Then rebuild:

```bash
python3 build.py
```

That regenerates every `<slug>/index.html`, `index.html`, `404.html`, `sitemap.xml`,
`robots.txt`, `llms.txt` and `CNAME`. Commit the generated files — Pages serves them.

## Assets

```bash
python3 make_assets.py
```

Regenerates `assets/` from the app repo at `../StopGamble`: favicon and touch icon from
the app icon, screenshots from `marketing/screenshots/pipeline/raw/`, milestone orb
renders, and the Open Graph card. Only needs re-running when the app's art changes.

## Config, in `build.py`

| Constant | Purpose |
|---|---|
| `APP_STORE_LIVE` | `False` shows "in App Store review" under every CTA. **Flip to `True` the moment 1.0 is approved.** |
| `PROVIDER_TOKEN` | Apple provider token from App Store Connect → Analytics → Campaigns. Until set, App Store links carry no campaign params. |
| `ANALYTICS_TOKEN` | Cloudflare Web Analytics beacon token. Cookieless by design — do not swap in GA4, it would contradict the app's no-tracking claim and require a consent banner. |
| `HELPLINES` | Kept in sync with `App/Services/RegionResources.swift`. Re-verify every publish. |

## Editorial rules

- Competitor prices and claims are cited to the vendor's own page with the date checked.
  Re-verify before touching those pages; roundups in this niche are full of stale figures.
- Screening is never described as diagnosis.
- Every page carries the helpline block and the not-medical-care disclaimer.
- No fabricated statistics, no invented study citations, no effectiveness claims for the
  app — it applies evidence-based material, it has not itself been trialled.
