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

## 3. trysilex.app redirect

Point `trysilex.app` at a 301 to `https://trysilex.com`. Porkbun's URL-forwarding does
this in one field — set it to a **permanent (301)** redirect, not a frame or a 302. Never
host content on the `.app` domain; it exists only to stop a near-miss squat.

## 4. Submit for indexing

- **Google Search Console** — add `trysilex.com` as a domain property, verify by DNS TXT
  record at Porkbun, then submit `https://trysilex.com/sitemap.xml`.
- **Bing Webmaster Tools** — non-negotiable, not optional: ChatGPT's live retrieval runs
  on Bing, so a site missing from Bing's index cannot be cited there. Add the site, verify,
  submit the same sitemap. Bing can import the property straight from Search Console.
- **IndexNow** (optional, after Bing verification): generate a key in Bing Webmaster
  Tools, commit it as `<key>.txt` at the repo root, then ping on publish:
  ```bash
  curl "https://api.indexnow.org/indexnow?url=https://trysilex.com/&key=YOUR_KEY"
  ```

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

## 7. Content owner's to-do

- `src/pages/about.html` has a `TODO(Kyrylo)` placeholder — one paragraph in your own
  words about why you built this. It is the highest-value paragraph on the site for both
  trust and AI citation, and it has to be yours.
- Re-verify every competitor price and every helpline number before each publish. Prices
  in this niche go stale fast; the helplines are the one place a stale fact could do harm.
