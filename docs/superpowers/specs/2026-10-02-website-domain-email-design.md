# Draw & Learn — Website, Domain & Email (design spec)

Date: 2026-10-02. Approved in chat by Roberto (4 decisions below).

## Goal
Official-looking public home for the app "Draw & Learn to Talk with Bob" (iOS, App Store id 6777554616), used in ads, social bios, press, App Store marketing/support URLs, and later for Google Play organisation-account verification (Search Console + D-U-N-S).

## Decisions (Roberto, 2026-10-02)
1. Domains: **drawandlearn.app** (primary) + **drawandlearn.co.uk** (redirect → .app). Registrar: Cloudflare (at-cost). drawandlearn.com is a parked squat — ignore.
2. Email: **Cloudflare Email Routing** (free forwarding). Aliases `hello@`, `support@`, `press@` → piresbobrob@gmail.com. Gmail "Send mail as" configured later if replies must show the domain.
3. Site scope: **full marketing site**, static HTML/CSS, no JS frameworks, no tracking/analytics (Kids app — stay privacy-clean).
4. Purchase: driven together in Chrome; Roberto clicks Pay.

## Hosting
GitHub Pages from new public repo `Synckser/drawandlearn-site` (branch `main`, root). Custom domain `drawandlearn.app` with HTTPS enforced. `www.` → apex. Legal repo (`Synckser/draw-and-learn-legal`) stays as-is; site hosts its own copies of Privacy/Terms with identical wording and the old GitHub URLs keep working.

## Pages (all one shared header/footer, mobile-first)
- `/` Home: hero (icon, title, subtitle "Colouring, First Words & ABC", tracked App Store badge), 3 trust pills (No ads · No tracking · Works offline), feature grid, screenshot strip, Meet Bob block, parents block, footer.
- `/features/` Full feature list (from live App Store description; 500+ pictures, 18 languages, phonics, bucket fill, blank canvas, save to Photos, parental gate).
- `/bob/` Meet Bob: who he is, the voice, what he says.
- `/parents/` For Parents: age 5 and under, Made for Kids, privacy summary, offline, difficulty, parental gate, FAQ.
- `/support/` Contact + FAQ. Mailto `support@drawandlearn.app`. This URL becomes App Store Support URL.
- `/press/` Press kit: one-paragraph boilerplate, icon + screenshots download, facts, contact `press@`.
- `/privacy/` and `/terms/` — copied from legal repo (source of truth GitHub repo text, 2026-09-28 revision).
- `404.html`.

## Content sources
- Live listing text via iTunes lookup (name, description, 5★ / 6 ratings on 2026-10-02).
- Icon: `~/Desktop/DrawAndLearn_Marketing/icon_options/icon.png`.
- Screenshots: `~/Desktop/DrawAndLearn_StoreMedia_2026-09-23/screenshots/gb_iphone67_*.png`, `gb_ipad_*.png` (resize to ≤1200px, WebP + PNG fallback).
- Links: tracked App Store link format from `TRACKING LINKS.md` with `ct=website`; socials @drawandlearnbob (TikTok, IG), FB Page, YouTube @DrawLearnwithBob.

## Rules
- No child faces, no therapy claims, no "free this week" urgency, no "glow mode" claim.
- British English (en-GB primary); mention US "coloring" only in meta keywords.
- Lighthouse ≥ 95 on mobile; total page weight < 1.5 MB on home.
- No external scripts/fonts at all (system font stack) → no cookie banner needed.

## DNS (Cloudflare, after purchase)
- `A @` → 185.199.108.153 / .109 / .110 / .111 (GitHub Pages), DNS-only (grey cloud) so GitHub can issue the cert.
- `CNAME www` → `synckser.github.io`.
- `.co.uk`: Cloudflare Redirect Rule 301 → `https://drawandlearn.app$1` (proxied placeholder A record 192.0.2.1).
- Email Routing enables its own MX/TXT automatically; add `TXT @ "v=spf1 include:_spf.mx.cloudflare.net ~all"` (routing adds it).

## Verification
- `curl -I https://drawandlearn.app` → 200, valid cert.
- `curl -I https://drawandlearn.co.uk` → 301 to .app.
- Send test mail to hello@/support@/press@ → arrives in Gmail.
- Google Search Console property added (needed for Play org account) — DNS TXT verification.
- Update App Store Connect: marketing URL + support URL (next version metadata), social bios, SOCIAL MEDIA PLAN.md START HERE + Status log.

## Out of scope (v1)
Blog, newsletter, analytics, Android page (add when Play listing exists), trademark filing.
