# Deploy and go-live checklist

The site is live on GitHub Pages from `main` at the repo root. Pushing to `main` deploys;
there is no CI step. Verified serving correctly from GitHub's edge on 2026-08-10.

## 1. DNS at Porkbun — the only thing blocking the domain

`trysilex.com` currently resolves to Porkbun's parking IPs (`207.207.210.36`,
`207.207.210.50`). In the Porkbun DNS panel for `trysilex.com`:

**Delete** the default parking records for the root (`A` or `ALIAS` on the bare domain).

**Add four A records** on the root (host field empty or `@`):

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**Optionally add the AAAA records** too, for IPv6:

```
2606:50c0:8000::153
2606:50c0:8001::153
2606:50c0:8002::153
2606:50c0:8003::153
```

**Add a CNAME** for `www` → `ppingui.github.io`

(Porkbun's `ALIAS` record type on the root pointing at `ppingui.github.io` also works and
is easier to maintain, but the four A records are what GitHub documents.)

Propagation is usually minutes. Check with:

```bash
dig +short A trysilex.com
```

## 2. Then turn on HTTPS

Once DNS resolves to GitHub, Pages issues a Let's Encrypt certificate automatically —
usually within an hour. After the certificate shows as approved, enforce HTTPS:

```bash
gh api -X PUT repos/ppingui/trysilex-site/pages -F https_enforced=true
```

Confirm:

```bash
curl -sI https://trysilex.com/ | head -2
```

## 3. Defensive domain — decided against, for now

`trysilex.app` was deliberately **not** bought (decision, 2026-08-10). The only cost of
skipping it is that if someone else registers it later they can catch traffic from people
who mistype the TLD. Low risk while the brand has no recognition; worth revisiting if the
app gets traction. If you do buy it, point it at a **permanent (301)** to
`https://trysilex.com` and never host content there.

## 4. Indexing — done

- **Google Search Console** — property verified, `sitemap.xml` submitted (2026-08-10).
- **Bing Webmaster Tools** — needed for the query data, and because ChatGPT's live
  retrieval runs on Bing. Bing can import the property straight from Search Console.
- **IndexNow** — live. Key file `2c0401c6323f4aa5bea0ce293dc66e70.txt` is served from the
  root; first submission of all 15 URLs returned `202 Accepted`. After any publish:
  ```bash
  python3 submit_indexnow.py                     # everything in sitemap.xml
  python3 submit_indexnow.py /about/ /support/    # just these
  ```
  Run it only after the push has actually deployed — IndexNow fetches the URLs. The script
  refuses to submit if the hosted key file stops matching.

## 5. Analytics

Cloudflare Web Analytics is free and cookieless and needs no Cloudflare hosting — add the
site, copy the beacon token into `ANALYTICS_TOKEN` in `build.py`, rebuild, push. Do not
use GA4: it contradicts the app's no-tracking claim and would require a consent banner.

## 6. On App Store approval

1. Set `APP_STORE_LIVE = True` in `build.py` — removes the "in App Store review" line
   under every CTA.
2. Fill in `PROVIDER_TOKEN` from App Store Connect → Analytics → Campaigns, so the
   `{{cta:…}}` campaign names become real attribution tokens and you can see which page
   drives installs.
3. Rebuild, commit, push.

## 7. Standing editorial duties

- Re-verify every competitor price and every helpline number before each publish. Prices
  in this niche go stale fast; the helplines are the one place a stale fact could do harm.
- When you edit a page, bump its `"updated"` date in the meta block — visible freshness
  affects both ranking and whether answer engines treat the page as current.

## Current state (2026-08-10)

| Item | State |
|---|---|
| DNS | Porkbun → GitHub's four A records, `www` CNAME. Resolving. |
| HTTPS | Cert approved for apex + `www`, `https_enforced=true`. HTTP and `www` both 301 to the https apex. |
| Pages | 15 URLs, all 200. Custom 404 working. |
| Lighthouse (live) | Performance 99, Accessibility 100, Best practices 100, SEO 100. LCP 0.9s, CLS 0, TBT 0ms. |
| Search Console | Verified, sitemap submitted. |
| IndexNow | Key live, 15 URLs accepted. |
| Bing Webmaster | **Not yet set up.** |
| Analytics | **Not yet set up** — `ANALYTICS_TOKEN` empty. |
| App Store link | **`APP_STORE_LIVE = False`** — CTAs show the "in review" line. |
