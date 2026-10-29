> For the complete index of this site, see [llms.txt](https://trysilex.com/llms.txt). This page on the web: https://trysilex.com/block-gambling-sites-iphone/

# How to block gambling sites and apps on iPhone

By [Kyrylo Lozovyi](https://trysilex.com/about/) · August 10, 2026

**Short answer:** Screen Time alone won't do it. The combination that holds is: a **system-wide DNS profile** (covers every app and browser), **Screen Time restrictions with the passcode held by someone else** (stops reinstalling), and the two layers you cannot undo in a craving — **operator self-exclusion** and a **bank gambling block**. Setting up all four takes about 30 minutes.

On Android instead? [Here's the Android setup](https://trysilex.com/block-gambling-apps-android/) — the free built-in option there is genuinely better.

There are five distinct ways to block gambling on an iPhone, and they cover different things. Most guides list one, that one has a hole in it, and the hole is where the relapse goes. Here is all of it, with the honest limitations of each.

## Start here: what each method actually covers

| Method | Covers | How fast can you undo it? | Cost |
|---|---|---|---|
| Screen Time restrictions | App installs, named websites in Safari, app hiding | Seconds — unless someone else holds the passcode | Free |
| System-wide DNS profile | **Every app and every browser**, on Wi-Fi and cellular | About a minute, in Settings | Free options exist |
| Safari content blocker | Safari only | Seconds | Free or bundled with an app |
| Bank gambling block | Card payments to gambling merchants | Often a 48-hour cooling-off before it lifts | Free |
| Operator self-exclusion | Your accounts, at the source | **You can't** — months to years | Free |

Read that table as a stack, not a menu. The first three make gambling inconvenient; the last two make it genuinely hard. People who only do the first three tend to relapse through a browser or a payment method they forgot about.

## 1. Screen Time: block installs and named sites

Screen Time is free, built in, and more useful for what it *prevents* than for what it filters.

**Stop new gambling apps appearing:** Settings → Screen Time → Content & Privacy Restrictions → turn on → iTunes & App Store Purchases → Installing Apps → **Don't Allow**. This is the highest-value switch on the whole phone. Delete the sportsbook apps first, then flip it — now reinstalling requires the Screen Time passcode.

**Block gambling websites in Safari:** Content & Privacy Restrictions → Content Restrictions → Web Content → **Limit Adult Websites**, then add each operator under **Never Allow**. Turning on Limit Adult Websites also disables Private Browsing in Safari, which is a genuine bonus.

**The catch nobody mentions:** iOS has no gambling category. "Limit Adult Websites" is an adult-content filter; it catches some gambling sites incidentally and misses most sportsbooks. If you rely on it alone you will be blocked from nothing you actually use. The Never Allow list works, but you are maintaining it by hand against an industry with thousands of mirror domains.

**Do this bit properly:** set a Screen Time passcode you don't know. Have your partner, a friend, or a family member type it in and keep it. Everything above is a five-second undo for whoever holds that code — so make sure that isn't you at 1am.

## 2. A system-wide DNS profile: the one that covers everything

This is the method most guides skip, and it is the strongest thing that lives on the phone itself. Every app and browser has to look up a domain name before it can connect. If the lookup fails, the app fails — no extension needed, no per-browser setup, and it works on cellular data as well as Wi-Fi.

iOS lets an app or a configuration profile install an encrypted-DNS (DoH) setting that applies device-wide. Point it at a resolver that filters gambling and every sportsbook, casino and slots site stops resolving.

Free and paid options that filter gambling:

- **Mullvad's public DoH resolvers** — a free "family" resolver that blocks gambling among other categories, run under a published no-logging policy.
- **NextDNS** — free tier for moderate query volumes, with a gambling blocklist you switch on plus a large catalogue of community lists.
- **Control D** — similar idea, category filtering, free tier available.
- **A blocker app that installs the profile for you** — including [Silex](https://trysilex.com/), which sets up an encrypted-DNS shield and merges public gambling-domain lists so you never maintain one by hand.

Verify it after setup: Settings → General → VPN, DNS & Device Management → DNS should show your chosen configuration as selected, and a known gambling site should fail to load in a browser you don't normally use.

**Its limitation, stated plainly:** you can turn it off in Settings in under a minute. DNS filtering is a speed bump against a determined craving, not a wall. It is an excellent speed bump — most relapses are impulsive, and one minute of friction is often enough — but do not treat it as the last line.

## 3. Safari content blockers

A content blocker extension can refuse to load a list of domains inside Safari. Enable one at Settings → Apps → Safari → Extensions, then switch the blocker on. Silex ships one; so do most dedicated blocker apps.

Useful, and narrow: it covers Safari and nothing else. Chrome, Firefox, Edge, the in-app browser inside a social app and the sportsbook's own native app are all untouched. Treat a Safari blocker as a supplement to DNS filtering, never a replacement.

## 4. Make your bank decline the payment

Blocking access is only half of it — the other half is making the money hard to move. Most UK banks and a growing number of US and Canadian ones offer a gambling-merchant block that declines transactions to gambling operators outright, and many enforce a cooling-off period (often 48 hours) before they will lift it.

That cooling-off is the point: it makes the block outlast the urge. [Here's how to turn it on, bank by bank.](https://trysilex.com/block-gambling-transactions-bank/)

## 5. Self-exclude at the source

The strongest layer isn't on your phone at all. Self-exclusion means telling the operator, or a national scheme, to close your accounts and refuse you service for a fixed period. In the UK, **GAMSTOP** covers every UK-licensed online operator with one free registration. In the US, most states run self-exclusion programmes, and every licensed sportsbook has its own.

You cannot undo this in a craving — that is precisely why it works. [The full self-exclusion guide is here.](https://trysilex.com/self-exclusion-guide/)

## What doesn't work

- **Just deleting the apps.** Reinstalling takes fifteen seconds, and the mobile website works fine without any app at all.
- **Router-level blocking on its own.** Home Wi-Fi filtering, including a Pi-hole or a router-level DNS change, evaporates the moment the phone switches to cellular. Do it as well, never instead.
- **A general VPN.** It relocates your traffic; it doesn't filter it. Some privacy VPNs offer a content-filtering DNS mode, which does work — the plain VPN does nothing for you here.
- **An app whose only feature is a streak counter.** Tracking is a motivator, not a barrier. You need both, and the barrier goes in first.
- **Anything that promises to be unremovable on iOS.** The sandbox does not permit it. Claims like that are marketing, and believing them is how people end up with one layer instead of four.

## The 30-minute setup, in order

1. Delete every gambling app. Sign out of any operator accounts still logged in on the browser.
2. Turn on a filtering DNS profile, and confirm a gambling site fails to load.
3. Screen Time → Installing Apps → Don't Allow, plus Never Allow entries for the sites you actually used. Hand the passcode to someone else.
4. Enable a Safari content blocker.
5. Call or message your bank and ask for the gambling block.
6. Self-exclude with every operator you have an account with — and with GAMSTOP if you are in the UK.

Steps 5 and 6 are the ones people postpone, and they are the ones that hold. Do them first if you only have ten minutes.

## Blocking is the floor, not the plan

Every layer above buys you time in the ninety seconds when an urge peaks. What you do with that time decides whether it works twice. [Urges rise, crest and fall on a fairly predictable curve](https://trysilex.com/how-long-do-gambling-urges-last/), and learning to wait one out is a skill that improves with repetition. That is what the [90-day side of this](https://trysilex.com/how-to-stop-gambling/) is for.

## Quit for good. Keep the money.

Silex blocks gambling across your iPhone and walks you through 90 days, one at a time.

[Get Silex on iPhone](https://apps.apple.com/app/id6798826038?mt=8)

## Common questions

### Can I block gambling apps on iPhone without an app?

Yes. Screen Time can block the App Store and specific websites, and iOS can install a DNS configuration that makes gambling domains fail to resolve in every app. Both are free and built in. What iOS cannot do on its own is maintain the list of hundreds of thousands of gambling domains — that is what a blocker app or a filtering DNS service adds.

### Does Screen Time block gambling apps?

Partly. Screen Time can stop new apps being installed, hide apps you have, and block specific websites in Safari. It has no gambling category, so 'Limit Adult Websites' is not a gambling filter — you have to add domains to Never Allow yourself, or use a filtering DNS resolver that keeps the list for you.

### Can gambling apps be blocked permanently on iPhone?

No, and any app claiming otherwise is overselling. On iOS you can always remove a profile or delete an app. Permanence has to come from outside the phone: self-exclusion with the operator, and a block at your bank. Those two you genuinely cannot reverse in the ninety seconds a craving lasts.

### Will a VPN block gambling sites?

A general-purpose VPN will not — it changes where your traffic exits, not what it can reach. A filtering DNS service or DNS-based blocker is what you want. Some privacy VPNs bundle a content-filtering DNS option, which does work.

### Does blocking work on cellular data as well as Wi-Fi?

A DNS configuration installed on the iPhone does, because it belongs to the device. Router-level blocking does not — it stops at your front door, and the phone falls straight back to gambling as soon as it switches to 5G. This is the single most common reason home blocking fails.

## If you need someone right now

- US: [1-800-GAMBLER](tel:18004262537) — National Problem Gambling Helpline — free, confidential, 24/7
- US: [988](tel:988) — Suicide & Crisis Lifeline — call or text if it feels like too much
- UK: [0808 8020 133](tel:08088020133) — National Gambling Helpline (GamCare) — free, confidential, 24/7
- UK: [116 123](tel:116123) — Samaritans
- Elsewhere: [findahelpline.com](https://findahelpline.com) — Crisis lines for your country
