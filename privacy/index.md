> For the complete index of this site, see [llms.txt](https://trysilex.com/llms.txt). This page on the web: https://trysilex.com/privacy/

# Privacy Policy

Last updated: 30 October 2026. Canonical version of this notice; it replaces the Notion-hosted copy linked from older builds of the app.

Silex is built on one principle: **your recovery is nobody's dataset.**

*We* store nothing about you on any server, hold no accounts, and have no way to read anything you write in this app. (The one piece of code we run on a server is the optional Notion connector in §14, which keeps nothing.) One third party does run a server that receives something: an analytics service is sent the *names* of the screens you reach, and there is a switch in Settings that stops it. This page explains exactly what that means — including the few places where data does leave your phone, because a privacy policy that only lists the reassuring parts is not a privacy policy.

This notice is written to meet the EU General Data Protection Regulation (GDPR) and the UK GDPR. If you are in the EEA or the UK, the sections on legal bases, transfers and your rights apply to you in full.

## 1. What you enter stays on your device

Everything you record — quiz answers, check-ins, journal reflections, program answers, urge logs, lapse entries, streak dates, money figures, your signature and your orb collection — is stored in two places, both of which belong to you:

- **On your iPhone**, in the app's local database.
- **In your private iCloud**, via Apple CloudKit's private database, so your history survives a lost or replaced device.

Your private iCloud database is accessible only to your Apple ID. We are not a party to it and cannot read it. If iCloud is unavailable or disabled, the app stores data only on your device.

**We never receive this content.** There is no API call that sends it, no backup on our side, and no key that would let us decrypt it. Because we have no access to it and no ability to use it, we do not consider ourselves the controller of what you write in the app — you are. We describe it here for transparency, not because we process it.

## 2. What actually reaches anyone else

Five narrow cases, all optional or technically unavoidable.

### Purchases — Apple, and RevenueCat

Subscriptions are processed by Apple. We use RevenueCat to verify and manage subscription status. It acts as our processor and receives:

- device type and operating system,
- last-seen time, and Apple receipt files,
- optionally, a user identifier and attribution metadata.

It never receives your journal, answers, streak or any recovery content. See [Apple's privacy policy](https://www.apple.com/legal/privacy/) and [RevenueCat's privacy policy](https://www.revenuecat.com/privacy/).

### The DNS shield — only if you turn it on

This installs an encrypted-DNS (DoH) configuration so gambling domains fail to resolve across your apps and browsers. While it is on, your device's DNS lookups are answered by [Mullvad's public resolver](https://mullvad.net/en/help/dns-over-https-and-dns-over-tls) under their [no-logging policy](https://mullvad.net/en/help/no-logging-data-policy/). Advanced users may point it at their own NextDNS configuration instead. Mullvad or NextDNS act as independent controllers for those lookups under their own policies — we are not in that path and never see your browsing. Turning the shield off in iOS Settings ends this immediately.

### Blocklist updates

The app periodically downloads public gambling-domain lists from jsDelivr and GitHub. As with any file download, those servers can see the request and your IP address. The request carries no identifier and nothing about you or your recovery.

### Usage counts — the tally on your device

The app keeps a first-party tally of *how the app is used* (for example, how many times a screen was opened on a given day), stored as counts by day in a single file in the app's own storage. It contains no identifiers and no content you wrote, and **that file never leaves your phone**. Deleting the app deletes it. The same event *names* are separately sent to TelemetryDeck unless you turn that off — which is the next section, and the honest reason this one no longer says "reach no one".

### Usage analytics — TelemetryDeck, unless you switch it off

To see where people abandon onboarding — the difference between fixing a screen and guessing at it — the app sends the *names* of the steps it reaches to **TelemetryDeck GmbH**, Von-der-Tann-Str. 54, 86159 Augsburg, Germany. What is sent:

- the **name** of each onboarding step reached and its position in the sequence (`funnel.question_04`, `funnel.paywall`), each one at most once per install;
- the **names** of other in-app events — a program day completed, the panic button opened — and nothing about them beyond the name;
- TelemetryDeck's own default payload: operating-system version, device model, locale, region, app version and similar;
- a random identifier minted by the app for this install.

What is never sent: your quiz answers, your PGSI score, your weekly spend, your journal text, your lapse records — anything you wrote or chose. The signal is that a screen was reached, never what was on it and never what you put into it.

**About that identifier.** It is a random UUID the app generates on first run. It is deliberately *not* `identifierForVendor`, the identifier iOS would otherwise have used, because that one survives deleting and reinstalling the app and is shared with every other app from the same developer. Ours is shared with nothing and dies when you delete the app. Before it leaves your phone it is hashed with a salt on the device; when it arrives, TelemetryDeck adds its own salt and hashes it again, so neither we nor they can work back from the stored value to the original. A single hash would only be pseudonymisation, which is why they do the second one.

We also switch off two things TelemetryDeck would otherwise collect: the session-began signal, and session statistics.

**The switch.** Settings → Your data → **Share anonymous usage**. It is **on by default**, and the reason is not a good look dressed up: an opt-in funnel measures the wrong population, because the people who quit on the first screen are exactly the people who never reach a consent prompt, so the drop-off being measured would be the thing biasing the sample. The price of that default is saying plainly what is sent, which is what this section is for. Turning it off stops new signals immediately, removes the sink from the app, and deletes the batch of unsent signals waiting on disk. What has already gone cannot be recalled — and nothing in it points back to you.

In the App Store's own vocabulary, the app declares **no tracking** (`NSPrivacyTracking` false, no tracking domains) and two collected data types — Product Interaction and Device ID — both marked *not linked to your identity* and *not used for tracking*, for the single purpose of analytics. See [TelemetryDeck's privacy policy](https://telemetrydeck.com/privacy/).

**Nothing else.** Those four network paths are the only ones the app has. There are no advertising identifiers, no cross-app tracking, and no profiling or automated decision-making that produces legal or similarly significant effects.

## 3. Legal bases (GDPR Art. 6 and Art. 9)

| What | Purpose | Legal basis |
|---|---|---|
| Purchase & subscription status (via Apple / RevenueCat) | Provide and restore the subscription you bought; prevent fraudulent entitlement | **Art. 6(1)(b)** — performance of a contract with you |
| IP address visible to the blocklist CDN when the app downloads a list | Deliver the blocking feature the app exists to provide | **Art. 6(1)(f)** — legitimate interests (keeping protection lists current). Our assessment: minimal data, no profiling, no linkage to you |
| Event names, a hashed install-scoped identifier and TelemetryDeck's default device payload, while "Share anonymous usage" is on | See where people abandon onboarding, so the screens that lose them can be fixed | **Art. 6(1)(f)** — legitimate interests (making the app work for the people it is meant for). Our assessment: no content, no advertising identifier, an identifier that cannot follow you between apps or survive deleting the app, and a switch in Settings that ends it. The switch is what carries the balancing test — an interest you can refuse in one tap is not one being asserted over you |
| DNS lookups, while the shield is enabled | Block gambling domains device-wide | **Art. 6(1)(a)** — your consent, given by enabling the shield and approving the iOS dialog; withdrawable at any time by turning it off |
| What you write in the app | Deliver the recovery programme to you on your own device | We do not receive it, so we carry out no processing to justify. To the extent it is processed at all, it is on your device under your control |

**Special-category (health) data.** What you record here reveals information about health and about a possible behavioural addiction, which is special-category data under **Art. 9**. That is exactly why the app is designed the way it is: that data never reaches us, so we never rely on an Art. 9 condition for it.

The harder question is the analytics, and we would rather work through it than wave it away. A signal reading `funnel.question_04` carries no content — but Silex is a gambling-recovery app, and the Court of Justice has held that data which only *indirectly* reveals a special category is caught all the same (Case C-184/20, *OT*). So we do not claim these signals are innocuous by subject matter: "this install walked into Silex's onboarding" says something adjacent to health about whoever was holding the phone. What we rely on is the other half of Art. 9, which bites on data concerning an **identified or identifiable** natural person. The identifier attached to these signals is random, minted for a single install, salted and hashed on your device, then salted again with TelemetryDeck's own salt and rehashed on arrival — so no party to it, us included, can work back to a person or match it against anything else. On that basis we treat what reaches TelemetryDeck as outside Art. 9, while still treating it as pseudonymous personal data under Art. 6 and giving it a lawful basis and a working opt-out, because the more cautious of the two readings is the one worth being wrong in. A subscription receipt is unchanged: it does not reveal a health condition beyond the fact that you bought an app.

This is the one paragraph here where competent lawyers can reasonably land in different places, and we would rather say so than let it read as settled.

## 4. International transfers

**RevenueCat** is a US company (Brandon, Florida) storing data on Amazon Web Services in the United States. Transfers are covered by its data processing agreement, which incorporates the European Commission's **Standard Contractual Clauses** (Implementing Decision (EU) 2021/914), **Module Two — controller to processor**. For the UK it additionally applies the ICO's **International Data Transfer Addendum** of 21 March 2022, and for Switzerland the SCCs adapted to the Swiss FADP. RevenueCat is **not** certified under the EU–US Data Privacy Framework; the SCCs are the mechanism. *Verified against RevenueCat's published DPA on 6 August 2026.*

**TelemetryDeck** is a German company (TelemetryDeck GmbH, Augsburg). It states that usage data is stored **exclusively within the European Union**, on Hetzner infrastructure in Nuremberg, with parts of the pipeline still running on Azure in Amsterdam and AWS in Frankfurt and a stated plan to consolidate onto Hetzner during 2026. Its corporate privacy policy names those counterparties as Hetzner Online GmbH (Germany), Microsoft Ireland Operations Ltd (Ireland) and Amazon Web Services, Inc. (Seattle, United States) — the AWS entity is American, but the region it stores in is Frankfurt. On TelemetryDeck's own account, then, no analytics data of ours leaves the EEA and **no Chapter V transfer mechanism is engaged**, because there is no third-country transfer to cover. We have not independently verified those storage regions and cannot; we are reporting what TelemetryDeck publishes.

One thing we cannot give you, and it is why this entry is longer than RevenueCat's. **TelemetryDeck offers no Art. 28 processor agreement.** Its data processing terms are automatically part of its Terms of Service, so there is nothing to sign — but they state that it acts "neither as a processor within the meaning of Article 4(8) of the GDPR nor as a joint controller", and that Articles 26 and 28 do not apply, on the ground that what it receives is anonymous rather than personal data. We have not adopted that position: we treat the hashed install identifier as pseudonymous personal data, give it an Art. 6 basis and an opt-out regardless (§3), and describe TelemetryDeck as a processor in substance because that is what it is doing. The consequence you should know about is that the guarantees an Art. 28 contract would carry — documented instructions, audit rights, a contractual deletion obligation — are not available to us from this vendor, because it declines the role that creates them. *Verified against TelemetryDeck's published privacy policy, data processing agreement and architecture & security pages on 17 August 2026.*

**Apple** — see Apple's privacy policy for its own transfer safeguards. Your private iCloud data is governed by Apple's terms and is not transferred by us, because we never hold it.

**Us.** We are established in Ukraine, which is outside the EEA and has no European Commission adequacy decision. Where you give data to us directly, that is a direct collection rather than a Chapter V transfer (per EDPB Guidelines 05/2021 on the interplay of Art. 3 and Chapter V). In practice there is almost nothing to collect: there is no account, and the only personal data we can see is the pseudonymous subscription record in RevenueCat's dashboard and the aggregate counts in TelemetryDeck's.

## 5. How long anything is kept

- **On your device and in your private iCloud:** until you delete it. We cannot delete it for you, and we cannot stop you deleting it.
- **On our systems:** nothing, because we operate none. The only third-party server holding anything of ours is TelemetryDeck's — see below.
- **Purchase records:** retained by Apple and RevenueCat under their own retention schedules, and as required by tax and accounting law.
- **Usage counts on your device:** removed when the app is deleted.
- **Event names held by TelemetryDeck:** **it publishes no deletion schedule for them.** Its plans quote a retention figure — 90 days on the free tier, longer on paid ones — but that is a *query* window: how far back its dashboards can look. Data older than the window is moved to cold storage rather than deleted, and can be loaded back. TelemetryDeck says deletion, one-off or on a schedule, can be arranged on request; we have not arranged one, so assume these signals persist indefinitely. Since they are counts carrying no identifier that reaches back to you, that is a smaller statement than it sounds — but it is the accurate one, and we would rather print it than a number we made up.

## 6. Who is responsible

**Controller:** Kyrylo Lozovyi
**Address:** Vidpochinku 12, Kyiv, Ukraine
**Privacy contact:** [support@trysilex.com](mailto:support@trysilex.com) (also reachable at [stopgamblesupport@gmail.com](mailto:stopgamblesupport@gmail.com), the address shown inside current builds of the app)

We have not appointed a Data Protection Officer; we are not required to, because we carry out no large-scale monitoring and hold no special-category data on our systems (see §3).

## 7. Your rights

If you are in the EEA or UK you have the right to **access** your data, to **rectification**, to **erasure**, to **restriction** of processing, to **data portability**, to **object** to processing based on legitimate interests, and to **withdraw consent** at any time where consent is the basis (the DNS shield — withdraw by turning it off; this does not affect processing already carried out).

**An honest limitation.** For almost everything this app touches, we hold no identifiable data about you and no account that could link a request to a person. Under **GDPR Art. 11** we are not required to obtain extra information purely to identify you, and we will not ask you for identity documents to service a request we have no data to answer. In practice:

- **Content you wrote** — exercise these rights directly: it is on your device and in your iCloud, and deleting the app (plus the iCloud copy) erases it completely.
- **Purchase data** — contact Apple, or contact us and we will pass the request to RevenueCat, which acts as our processor.
- **Usage analytics** — your **Art. 21 right to object** to our legitimate interests has a switch rather than a support queue: Settings → Your data → **Share anonymous usage**, off. It stops new signals immediately, removes the sink and deletes the batch waiting on disk. You do not have to write to us and you do not have to give a reason. What was already sent cannot be pulled back, and cannot be found again either, because nothing in it identifies you.

Write to [support@trysilex.com](mailto:support@trysilex.com) and we will respond within one month, as required by Art. 12(3).

**Right to complain.** You may lodge a complaint with your national data protection authority. The list is at [edpb.europa.eu](https://edpb.europa.eu/about-edpb/board/members_en); in the UK it is the [ICO](https://ico.org.uk/make-a-complaint/). You do not have to contact us first, though we would rather you did.

## 8. Deleting everything

- Delete the app from your iPhone.
- Remove the iCloud copy: Settings → your name → iCloud → Manage Account Storage → Silex.
- Cancel a subscription: Settings → your name → Subscriptions, or the Manage Subscription link in the app.

## 9. Sensitive information, and why the design is the policy

What you record here concerns your health and your finances, and we treat it that way. No accounts to breach, no servers of ours to subpoena, and nothing held by any vendor that could be read back as *your* recovery. The strongest protection we can offer is not holding your data at all — and that part is structural rather than a promise: there is no key, no backup and no copy, so there is nothing to quietly reverse a decision about.

**What changed.** Until August 2026 this section also said there was no analytics vendor holding a copy. That is no longer true: TelemetryDeck holds a count of how many installs reached each screen. It is a real reduction in the guarantee and we are not going to call it anything else. What survives is the part doing the work — the content stays on your phone, the identifier attached to those counts cannot be tied to you or followed between apps, and the whole thing has a switch. What we gave up is the ability to say the word *none*.

## 10. Children

Silex is intended for adults and is not directed at children. We do not knowingly collect information from anyone under 18. The App Store listing is rated accordingly.

## 11. Changes

If this policy changes, the date at the top changes and the current version is always published at this address.

Adding TelemetryDeck is a material change, and the previous version of this section promised that material changes would be surfaced in the app. **We have amended that promise rather than claim we kept it.** The app has no mechanism that shows a notice on update, and we are not going to describe one that does not exist. What this release actually does is put the switch in Settings with a plain description of what is sent beside it — visible to anyone who looks, not pushed at anyone who does not. That is less than the old sentence promised, which is exactly why the sentence had to change rather than the account of what happened.

So the promise now reads: material changes are named in this section and in the App Store release notes of the version that makes them, and any change that widens what leaves your device ships with the control for it in the same release.

## 12. Contact

[support@trysilex.com](mailto:support@trysilex.com)

## 13. The free browser extension

This notice also covers **Silex — Free Gambling Blocker**, the browser extension for Chrome, Microsoft Edge and Firefox. It is simpler than the app, and so is this section:

- **It collects nothing.** No account, no analytics, no identifiers, and it makes no network requests of its own. Nothing about you or your browsing is sent to us or to anyone else.
- **How it blocks.** The extension carries a list of gambling domains inside it. Your browser compares the pages you open against that list locally, using its built-in `declarativeNetRequest` feature. The browser does not report back to the extension, or to us, which sites you visit or which were blocked.
- **Why it asks for access to all sites.** Browsers only let an extension replace a blocked page with its own help page — instead of showing an error — if it holds access to the sites involved. That access is used for nothing else: the extension does not read, change or collect the content of any page.
- **The help page** shows crisis lines and links to this website. Following a link is an ordinary visit to trysilex.com, covered by the rest of this notice.
- **Reporting a missed site** opens your own email app. What you send is up to you; we use it only to update the list and reply.
- **Removing the extension** removes it and everything in it.

The domain list is derived from The Blocklist Project (public domain) and the UT1 lists of Université Toulouse Capitole (CC BY-SA 4.0).

## 14. The Notion recovery tracker

**Silex Recovery Tracker for Notion** is an optional, free connector that sets up a recovery tracker page in your own Notion workspace. It has nothing to do with the app: using one does not touch the other.

- **What runs, and where.** A small function we wrote, hosted by Cloudflare. It runs only for the few seconds after you click Connect and approve access in Notion.
- **What it receives.** Notion sends it a one-time code, which it swaps for an access token to your workspace. Notion's reply also includes your workspace name and your Notion profile (name, and possibly email and avatar). The function reads only the token and ignores the rest.
- **What it does with the token.** It creates one page, two tables and two example rows in your workspace, then sends you to that page. It does not read or search your existing pages, except — only if Notion refuses a top-level page — to find the one page you chose to share, so the tracker can go inside it.
- **What it keeps.** Nothing. The token exists only in memory for that one request; there is no database, no file and no copy of anything you write in the tracker. We cannot open your tracker afterwards, and if Notion returns an error, only Notion's error code is logged, never workspace content.
- **Removing it.** In Notion, go to Settings → Connections and remove Silex. The tracker stays: it's an ordinary page that belongs to you. Delete it like any other page.

Legal basis: the request you make by clicking Connect (GDPR Art. 6(1)(b)). Cloudflare processes the connection itself (your IP address and request headers) as our processor; see [Cloudflare's privacy policy](https://www.cloudflare.com/privacypolicy/). What you write in the tracker is between you and Notion, under [Notion's privacy policy](https://www.notion.com/trust/privacy-policy).

## 15. Silex Help in ChatGPT and other AI assistants

**Silex Help** is a free, read-only service that AI assistants such as ChatGPT can call to answer questions about stopping gambling: helplines for a country, self-exclusion schemes, whether a website is on our gambling-domain list, the PGSI self-check, and blocking guides. It has nothing to do with the app, and it has no accounts.

- **What it receives.** Only what the assistant sends when it uses a tool: a country, the web addresses to check, or your nine self-check answers. Your conversation, your name and your assistant account are not sent to us.
- **What it does.** It looks the answer up in data bundled with the service and sends it back. It makes no requests to anyone else.
- **What it keeps.** Nothing. Each request is handled in memory and forgotten; there is no database and no log of what was asked.
- **The assistant itself.** What you type to ChatGPT or another assistant is covered by that provider's own privacy policy, not this one.

Legal basis: the request your assistant makes on your behalf (GDPR Art. 6(1)(b)). Cloudflare runs the service and processes each connection (IP address and request headers) as our processor; see [Cloudflare's privacy policy](https://www.cloudflare.com/privacypolicy/).

## If you need someone right now

- US: [1-800-MY-RESET](tel:18006973738) — National Problem Gambling Helpline — free, confidential, 24/7
- US: [988](tel:988) — Suicide & Crisis Lifeline — call or text if it feels like too much
- UK: [0808 8020 133](tel:08088020133) — National Gambling Helpline (GamCare) — free, confidential, 24/7
- UK: [116 123](tel:116123) — Samaritans
- Elsewhere: [findahelpline.com](https://findahelpline.com) — Crisis lines for your country
