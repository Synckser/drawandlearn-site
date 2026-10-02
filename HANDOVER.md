# DRAW & LEARN WEBSITE / DOMAIN / EMAIL — HANDOVER (read this first to resume)

**Last updated:** 2026-10-03 (session 1). Site repo `main` @ 739431a, all pushed. Nothing uncommitted.
**To resume in a new Claude session:** `cd ~/Desktop/DrawAndLearn_Site && claude`, then say:
"Read ~/Desktop/DRAW_AND_LEARN_WEBSITE_HANDOVER.md and carry on."

## What exists (all LIVE)
- **https://drawandlearn.app** — official site, GitHub Pages, HTTPS enforced. `www` redirects to apex.
- **drawandlearn.co.uk** (+www) — 301 redirect to `https://drawandlearn.app{path}` (Cloudflare Redirect Rule, proxied placeholder A 192.0.2.1).
- **Email:** hello@ / support@ / press@ drawandlearn.app (any address, catch-all) forward to piresbobrob@gmail.com via Cloudflare Email Routing. Forward-only (see TODO 1 for sending as the domain).
- **Search Console:** domain property drawandlearn.app VERIFIED (DNS TXT, keep it). Sitemap submitted.
- **App Store Connect:** draft version **1.2** exists with new Support / Marketing / Privacy URLs.
- **Facebook Page:** "Official website" link added.

## Where everything is
- Site repo: `~/Desktop/DrawAndLearn_Site` → GitHub `Synckser/drawandlearn-site` (public, branch `main`).
- Generator: `build.py` (no deps). Copy for every page lives in it as Python strings. Edit → `python3 build.py` → commit → `git pull --rebase origin main` → push. Pages redeploys in ~1 min.
  - GOTCHA: `PUT repos/.../pages cname=` creates a CNAME commit on the remote, so always `pull --rebase` before push.
- Preview: `python3 -m http.server 8765` in the repo, open http://localhost:8765/.
- Styles `assets/style.css`, JS `assets/site.js` (click-to-play videos with sound, hero unmute, scroll reveal; no tracking, no external code).
- Images `assets/img/` (icon, 5 iPhone + 5 iPad screenshots from `~/Desktop/DrawAndLearn_StoreMedia_2026-09-23/screenshots/gb_*`).
- Videos `assets/video/*.mp4` + `.jpg` posters (h264 crf26, aac 96k, faststart, 0.2–2 MB each). Sources from `~/Desktop/DrawAndLearn_Marketing`:
  - `hero_bob` ← `tiktok/ads/01_bob_talks_FIXED.mp4`
  - `preview_1..3` ← `cpp_previews/p1_hook, p2_learn_to_talk, p3_parents`
  - `tracing_wide` ← `tracing_video/DrawAndLearn_tracing_16x9.mp4`
  - `short_quiz_cow/dog`, `short_bob_fox/pumpkin` ← `video_stock/out/`
- Spec: `docs/superpowers/specs/2026-10-02-website-domain-email-design.md`. README has the DNS table.
- Tracked App Store links on the site use `ct=website`, `web_features/bob/parents/support/press`, `footer`, `mobile_bar` (+ ppid of the "Talk with Bob" Custom Product Page). Results: ASC → Analytics → Acquisition → Campaigns.
- Memory note: `~/.claude/projects/-Users-roberto/memory/draw-and-learn-website.md`. Plan log: `~/Desktop/DRAWN AND LEARN RE-SEARCH TEAM/SOCIAL MEDIA PLAN.md` (status log updated).

## Accounts / IDs
- **Cloudflare:** account bob.pires@hotmail.co.uk (signed in via GitHub), account id `0df8ea9a20396b69f6bf6eb56162293f`, zone id drawandlearn.app `52905c4bb000936e26852b2e2068ca9c`. Both domains registered by Roberto (individual registrant; can switch to Ltd later in Domains → Contacts, free).
- **DNS drawandlearn.app:** 4× A → 185.199.108–111.153 (DNS-only), `www` CNAME → synckser.github.io, 3× MX route1-3.mx.cloudflare.net, SPF TXT, DKIM TXT, Google verification TXT `google-site-verification=qJ0LTSGG…` (do not delete).
- **Email Routing:** destination piresbobrob@gmail.com (verified), catch-all rule ACTIVE.
- **Google login in Chrome:** bobbieinvest@gmail.com. It owns the Search Console property. It is NOT the YouTube brand-channel owner.
- **ASC:** app 6777554616, key DQ9PQCAMKL (~/.appstoreconnect). Helper: `~/Desktop/DrawAndLearn_Marketing/cpp_tools/ascapi.py` (`from ascapi import api`). Draft v1.2 id `e7084b50-e941-4fc7-968b-aa901670d3d5` (PREPARE_FOR_SUBMISSION, manual release), new appInfo `a1989b1e-a439-4e98-8e6a-8674c24a3f5c` (privacyPolicyUrl set).
- Legal pages still also live at https://synckser.github.io/draw-and-learn-legal/ (the app binary links there; text identical to the new site's /privacy/ and /terms/).

## TODO — Roberto (cannot be automated)
1. **Gmail "Send mail as" support@drawandlearn.app** (Gmail → Settings → Accounts; SMTP smtp.gmail.com + Gmail app password) so replies show the domain. Send a test mail to support@ first to confirm delivery.
2. **TikTok** website field (phone app; use `?utm_source=tiktok`), **Instagram** website field (phone app; `https://drawandlearn.app/?utm_source=instagram`), **YouTube brand channel** links (Studio → Customisation → Basic info → Links; needs the drawlearnbob account — Chrome here is signed into the wrong Google account).
3. If Play org account uses another Google user: Search Console → Settings → Users → add that user.
4. Optional: 301 vs keep old legal repo — leave as is (the binary points there).

## TODO — Claude / next session
1. **v1.2 submission flow** (existing Halloween plan, `~/Desktop/DrawAndLearn_release_1.2`, spec d34469b): draft ASC version already exists, so attach build 11, write whatsNew, check promo text, submit. Don't re-create the version.
2. When v1.2 ships, optionally switch in-app legal/support links to the new domain (Phase 2 of Halloween work) and verify ASC fields show the new URLs.
3. Site backlog (nice-to-have): Android/Play badge page when the listing exists; Halloween seasonal hero; add a `/press` downloadable ZIP; Lighthouse pass; add `Organization`/`MobileApplication` JSON-LD; GSC check in a week for indexing ("Couldn't fetch" on first sitemap submit is normal).
4. Keep SOCIAL MEDIA PLAN.md START HERE block current (add website to bios row, ratings now 6 / 5.0).

## Gotchas learned
- Claude cannot click Buy/Pay (auto-mode Real-World Transactions guard). Roberto buys, Claude does DNS/email after.
- Cloudflare BIND import (Import → `file_upload` to the hidden file input, untick/tick proxy, Upload) is the fastest way to add records.
- Search Console "Start verification" offers Cloudflare OAuth — do NOT use; pick "Any DNS provider" and add the TXT. The dialog animates; clicking during animation hits the Instagram/TikTok "link account" prompts (cancel them — nothing was linked). Domain-property sitemap needs the FULL URL.
- Live ASC fields (support/marketing/privacy URL) are locked while READY_FOR_SALE; they need a new version.
- Chrome extension disconnects briefly sometimes; retry after `tabs_context_mcp`.
- Facebook: don't click "Post" on the "Create a post?" banner after saving About info.
