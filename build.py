#!/usr/bin/env python3
"""Static site generator for drawandlearn.app. Run: python3 build.py  → writes HTML next to this file."""
import os, pathlib

ROOT = pathlib.Path(__file__).parent
DOMAIN = "https://drawandlearn.app"
APP_ID = "6777554616"
PPID = "d7351bd0-9993-4b03-9648-612a49a9a093"
def store(ct): return f"https://apps.apple.com/app/apple-store/id{APP_ID}?pt=955046&ct={ct}&mt=8&ppid={PPID}"
STORE = store("website")
SUPPORT_EMAIL = "support@drawandlearn.app"
PRESS_EMAIL = "press@drawandlearn.app"
HELLO_EMAIL = "hello@drawandlearn.app"
SOCIAL = {
    "TikTok": "https://www.tiktok.com/@drawandlearnbob",
    "Instagram": "https://www.instagram.com/drawandlearnbob",
    "Facebook": "https://www.facebook.com/profile.php?id=61594829610568",
    "YouTube": "https://www.youtube.com/@DrawLearnwithBob",
}
NAV = [("Features", "/features/"), ("Meet Bob", "/bob/"), ("For parents", "/parents/"), ("Support", "/support/"), ("Press", "/press/")]

def layout(path, title, desc, body, *, ct="website", og_image="/assets/img/icon-512.png"):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == path else ""}>{t}</a>' for t, h in NAV)
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}{path}">
<link rel="icon" href="/assets/img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<meta name="apple-itunes-app" content="app-id={APP_ID}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Draw &amp; Learn">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{DOMAIN}{path}">
<meta property="og:image" content="{DOMAIN}{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#2F8BFF">
<link rel="stylesheet" href="/assets/style.css">
<script defer src="/assets/site.js"></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site">
  <div class="wrap">
    <a class="brand" href="/"><img src="/assets/img/favicon.png" alt="" width="36" height="36">Draw &amp; Learn</a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav" onclick="var n=document.getElementById('nav');n.classList.toggle('open');this.setAttribute('aria-expanded',n.classList.contains('open'))">Menu</button>
    <nav class="main" id="nav" aria-label="Main">{nav}<a class="cta" href="{store(ct)}">Get the app</a></nav>
  </div>
</header>
<main id="main">
{body}
</main>
<a class="mobile-cta" href="{store('mobile_bar')}"><span style="display:flex;align-items:center;gap:10px"><img src="/assets/img/favicon.png" alt="">Free on the App Store</span><span>Get it →</span></a>
<footer class="site">
  <div class="wrap">
    <div class="cols">
      <div>
        <h4>Draw &amp; Learn to Talk with Bob</h4>
        <p style="margin:0 0 8px">A free drawing, colouring and first-words app for children aged 5 and under. No ads, no tracking, works offline.</p>
        <a href="{store('footer')}">Download on the App Store →</a>
      </div>
      <div><h4>App</h4><a href="/features/">Features</a><a href="/bob/">Meet Bob</a><a href="/parents/">For parents</a><a href="/press/">Press kit</a></div>
      <div><h4>Help</h4><a href="/support/">Support &amp; FAQ</a><a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a><a href="/privacy/">Privacy policy</a><a href="/terms/">Terms of use</a></div>
      <div><h4>Follow</h4>{''.join(f'<a href="{u}" rel="me noopener">{n}</a>' for n, u in SOCIAL.items())}</div>
    </div>
    <div class="legal"><span>© 2026 Roberto Pires Almeida. Draw &amp; Learn and Bob are made in the UK.</span><span>Apple, the Apple logo, iPhone and iPad are trademarks of Apple Inc. App Store is a service mark of Apple Inc.</span></div>
  </div>
</footer>
</body>
</html>
"""

def write(path, html):
    out = ROOT / path.strip("/") / "index.html" if path != "/" else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print("wrote", out.relative_to(ROOT))

STORE_BTN = f'<a class="btn primary" href="{STORE}"><span aria-hidden="true" style="font-size:20px"></span> Download on the App Store</a>'

# ---------------- HOME ----------------
home = f"""
<section class="hero">
  <div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div><div class="blob b4"></div>
  <div class="wrap">
    <div>
      <img class="icon" src="/assets/img/icon-512.png" alt="Draw &amp; Learn app icon: Bob the robot with a pencil and paintbrush" width="112" height="112">
      <h1>Draw, colour and <span>learn to talk</span> with Bob</h1>
      <p class="lead">A free iPhone and iPad app for children aged 5 and under. Trace 500+ friendly pictures, hear every word and letter sound, and build first words while you play.</p>
      <div class="actions">{STORE_BTN}<a class="btn secondary" href="#watch">▶ Watch Bob in action</a></div>
      <p class="rating">★★★★★ Rated 5.0 on the App Store (UK) · Free · Made for Kids</p>
      <div class="pills"><span class="pill">🚫 No ads</span><span class="pill">🔒 No tracking</span><span class="pill">✈️ Works offline</span><span class="pill">🌍 18 languages</span></div>
    </div>
    <div>
      <div class="phone hero-phone" data-hero>
        <video autoplay muted loop playsinline preload="metadata" poster="/assets/video/hero_bob.jpg" aria-label="Draw &amp; Learn app demo: Bob talks while a child colours a dolphin and a dinosaur">
          <source src="/assets/video/hero_bob.mp4" type="video/mp4">
        </video>
        <button class="sound" type="button">🔊 Hear Bob</button>
      </div>
      <p class="hero-note">Real app footage. Tap the phone for sound.</p>
    </div>
  </div>
</section>

<section id="watch" class="alt">
  <div class="wrap">
    <h2 class="reveal">See it in action</h2>
    <p class="sub reveal">Three short videos, with sound. Tap any phone to play.</p>
    <div class="vgrid">
      <figure class="reveal">
        <div class="phone player" data-player>
          <span class="badge">0:29</span>
          <video playsinline preload="metadata" poster="/assets/video/preview_1.jpg"><source src="/assets/video/preview_1.mp4" type="video/mp4"></video>
          <button class="play" type="button" aria-label="Play: Draw and colour with Bob"></button>
        </div>
        <figcaption>Draw &amp; colour<small>The only screen time I say yes to</small></figcaption>
      </figure>
      <figure class="reveal">
        <div class="phone player" data-player>
          <span class="badge">0:29</span>
          <video playsinline preload="metadata" poster="/assets/video/preview_2.jpg"><source src="/assets/video/preview_2.mp4" type="video/mp4"></video>
          <button class="play" type="button" aria-label="Play: Learn to talk with Bob"></button>
        </div>
        <figcaption>Learn to talk<small>Bob says the word, your child repeats it</small></figcaption>
      </figure>
      <figure class="reveal">
        <div class="phone player" data-player>
          <span class="badge">0:29</span>
          <video playsinline preload="metadata" poster="/assets/video/preview_3.jpg"><source src="/assets/video/preview_3.mp4" type="video/mp4"></video>
          <button class="play" type="button" aria-label="Play: For parents"></button>
        </div>
        <figcaption>For parents<small>No ads. No data collected. Works offline.</small></figcaption>
      </figure>
    </div>
    <div class="stats reveal">
      <div class="stat"><b>500+</b><span>pictures to trace</span></div>
      <div class="stat"><b>18</b><span>languages</span></div>
      <div class="stat"><b>0</b><span>ads, ever</span></div>
      <div class="stat"><b>5.0★</b><span>App Store rating</span></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 class="reveal">Everything a little artist needs</h2>
    <p class="sub">Simple enough for toddlers, rich enough to grow with them.</p>
    <div class="grid">
      <div class="card tint-blue"><div class="em">✏️</div><h3>500+ pictures to trace</h3><p>Animals, dinosaurs, ocean, space, vehicles, fruit and more, with clear friendly guides at Easy, Medium or Hard.</p></div>
      <div class="card tint-red"><div class="em">🗣️</div><h3>Bob says every word</h3><p>Bob greets your child from the first screen and says every word out loud, with audio built in for offline use.</p></div>
      <div class="card tint-yellow"><div class="em">🔤</div><h3>Phonics &amp; first words</h3><p>Tap the letters above each picture to hear their sounds, then learn ABC, 123 and shapes.</p></div>
      <div class="card tint-green"><div class="em">🎨</div><h3>Brushes, stamps &amp; bucket fill</h3><p>Colour in with a full palette, add stickers and stamps, or fill a whole area with one tap.</p></div>
      <div class="card tint-purple"><div class="em">🌍</div><h3>18 languages</h3><p>Switch the words Bob says to French, Spanish, Portuguese, Hindi, Japanese and more.</p></div>
      <div class="card tint-blue"><div class="em">📸</div><h3>Keep every picture</h3><p>Finished artwork is saved in the in-app gallery, and can be added to Photos or printed.</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2>Take a look</h2>
    <p class="sub">Designed for small hands on iPhone and iPad.</p>
    <div class="strip">
      <img src="/assets/img/iphone_1.png" alt="Tracing a dolphin" loading="lazy" width="430" height="932">
      <img src="/assets/img/iphone_2.png" alt="Letter sounds while colouring a dinosaur" loading="lazy" width="430" height="932">
      <img src="/assets/img/iphone_3.png" alt="Home screen with drawing categories" loading="lazy" width="430" height="932">
      <img src="/assets/img/iphone_4.png" alt="Choosing an ocean picture to draw" loading="lazy" width="430" height="932">
      <img src="/assets/img/iphone_5.png" alt="Letters category: learn ABC" loading="lazy" width="430" height="932">
    </div>
    <div class="ipad">
      <img src="/assets/img/ipad_1.png" alt="Draw &amp; Learn on iPad" loading="lazy">
      <img src="/assets/img/ipad_3.png" alt="Draw &amp; Learn categories on iPad" loading="lazy">
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 class="reveal">How kids learn to draw</h2>
    <p class="sub reveal">Trace the sample, colour it in, then try without the guide. Watch a full picture on iPad, with sound.</p>
    <div class="tablet player reveal" data-player>
      <span class="badge">0:47 · iPad</span>
      <video playsinline preload="metadata" poster="/assets/video/tracing_wide.jpg"><source src="/assets/video/tracing_wide.mp4" type="video/mp4"></video>
      <button class="play" type="button" aria-label="Play: how kids learn to draw an apple"></button>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2 class="reveal">Bob says… 🗣️</h2>
    <p class="sub reveal">Ten-second clips straight from the app. Can your toddler guess the animal before Bob says it?</p>
    <div class="shorts">
      <div class="player reveal" data-player><video playsinline preload="metadata" poster="/assets/video/short_quiz_cow.jpg"><source src="/assets/video/short_quiz_cow.mp4" type="video/mp4"></video><button class="play" type="button" aria-label="Play: guess the animal, cow"></button></div>
      <div class="player reveal" data-player><video playsinline preload="metadata" poster="/assets/video/short_quiz_dog.jpg"><source src="/assets/video/short_quiz_dog.mp4" type="video/mp4"></video><button class="play" type="button" aria-label="Play: guess the animal, dog"></button></div>
      <div class="player reveal" data-player><video playsinline preload="metadata" poster="/assets/video/short_bob_fox.jpg"><source src="/assets/video/short_bob_fox.mp4" type="video/mp4"></video><button class="play" type="button" aria-label="Play: Bob says fox"></button></div>
      <div class="player reveal" data-player><video playsinline preload="metadata" poster="/assets/video/short_bob_pumpkin.jpg"><source src="/assets/video/short_bob_pumpkin.mp4" type="video/mp4"></video><button class="play" type="button" aria-label="Play: Bob says pumpkin"></button></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <img class="reveal" src="/assets/img/icon-512.png" alt="Bob the robot" loading="lazy" width="340" height="340">
    <div class="reveal">
      <h2>Meet Bob 🤖</h2>
      <p class="sub" style="margin-bottom:16px">Bob is the friendly robot who lives in the app. He cheers on every picture, names what your child draws, and never runs out of patience.</p>
      <ul class="check">
        <li>Says every word and letter sound clearly</li>
        <li>Celebrates finished drawings ("You drew a dolphin! Brilliant work!")</li>
        <li>Sets a fun "Today's challenge" picture each day</li>
        <li>Speaks 18 languages</li>
      </ul>
      <p style="margin-top:18px"><a class="btn secondary" href="/bob/">More about Bob</a></p>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap split">
    <div>
      <h2>Made for families, built by a dad</h2>
      <p class="sub" style="margin-bottom:16px">Draw &amp; Learn was made by a parent who wanted a drawing app that was safe, calm and genuinely useful. So it is.</p>
      <ul class="check">
        <li>Made for Kids on the App Store, ages 5 and under</li>
        <li>No ads, no tracking, no account and no third-party code</li>
        <li>Works fully offline: car journeys, flights, waiting rooms</li>
        <li>Adjustable difficulty that grows with your child</li>
        <li>Grown-up settings behind a parental gate</li>
      </ul>
      <p style="margin-top:18px"><a class="btn secondary" href="/parents/">Read the parents' guide</a></p>
    </div>
    <img src="/assets/img/iphone_5.png" alt="Learn ABC and 123 screen" loading="lazy" width="340" height="737">
  </div>
</section>

<section class="cta-band">
  <div class="wrap">
    <h2>Free on the App Store</h2>
    <p>Every picture, word and sound included. iPhone and iPad, iOS 16.6 or later.</p>
    {STORE_BTN}
  </div>
</section>
"""
write("/", layout("/", "Draw & Learn to Talk with Bob – Free drawing & first-words app for kids", "Free iPhone and iPad app for children aged 5 and under. Trace 500+ pictures, hear every word and letter sound with Bob the robot. No ads, no tracking, works offline.", home))

# ---------------- FEATURES ----------------
features = f"""
<section class="page"><div class="wrap">
  <h1>Features</h1>
  <p class="meta">Everything in the app, free, with nothing locked away.</p>
  <div class="grid">
    <div class="card tint-blue"><div class="em">✏️</div><h3>500+ guided pictures</h3><p>Farm, wild animals, pets, Arctic, ocean, birds, bugs, reptiles, dinosaurs, vehicles, space, fruit, shapes, letters and numbers.</p></div>
    <div class="card tint-green"><div class="em">🎚️</div><h3>Easy · Medium · Hard</h3><p>Guides get lighter as skills grow. Start with thick outlines, finish with free drawing.</p></div>
    <div class="card tint-red"><div class="em">🗣️</div><h3>Every word spoken</h3><p>Bob says the name of every picture and letter. Audio is bundled in the app, so it works with no internet.</p></div>
    <div class="card tint-yellow"><div class="em">🔤</div><h3>Phonics letters</h3><p>Letter tiles above each picture: tap to hear each sound, then hear the whole word.</p></div>
    <div class="card tint-purple"><div class="em">🌍</div><h3>18 languages</h3><p>English, French, Spanish, Portuguese, German, Italian, Dutch, Hindi, Japanese, Korean, Chinese, Thai, Turkish, Vietnamese, Malay and more.</p></div>
    <div class="card tint-blue"><div class="em">🪣</div><h3>Bucket fill, brushes &amp; stamps</h3><p>Big colour palette, glitter, stamps and one-tap fill. Undo and rubber always one tap away.</p></div>
    <div class="card tint-green"><div class="em">🖼️</div><h3>Blank canvas</h3><p>Free drawing with all the same tools for when imagination takes over.</p></div>
    <div class="card tint-red"><div class="em">⭐</div><h3>Today's challenge</h3><p>A new picture to try every day, with Bob cheering at the end.</p></div>
    <div class="card tint-yellow"><div class="em">📸</div><h3>Gallery, Photos &amp; print</h3><p>Every finished picture is kept in "My Art", and can be added to Photos or printed from the app.</p></div>
    <div class="card tint-purple"><div class="em">🔒</div><h3>Parental gate</h3><p>Settings, links and the App Store rating prompt sit behind a grown-ups-only gate.</p></div>
    <div class="card tint-blue"><div class="em">✈️</div><h3>100% offline</h3><p>No internet needed, ever. Nothing is uploaded; drawings stay on the device.</p></div>
    <div class="card tint-green"><div class="em">📱</div><h3>iPhone &amp; iPad</h3><p>Universal app, iOS and iPadOS 16.6 or later. One download, every device in the family.</p></div>
  </div>
  <p style="margin-top:32px">{STORE_BTN}</p>
</div></section>
"""
write("/features/", layout("/features/", "Features – Draw & Learn to Talk with Bob", "500+ guided pictures, phonics letter sounds, 18 languages, bucket fill, blank canvas, parental gate, fully offline. All free.", features, ct="web_features"))

# ---------------- BOB ----------------
bob = f"""
<section class="page"><div class="wrap">
  <div class="split">
    <img src="/assets/img/icon-512.png" alt="Bob the robot" width="340" height="340">
    <div>
      <h1>Meet Bob</h1>
      <p class="meta">The friendly robot who helps children draw, colour and learn to talk.</p>
      <div class="prose">
        <p>Bob is the heart of Draw &amp; Learn. He says hello when the app opens, names every picture your child picks, sounds out the letters, and cheers when a drawing is done. He never rushes, never scolds and never runs out of encouragement.</p>
        <p>Bob's voice is recorded and bundled with the app, so he works in the car, on the plane and anywhere else without internet. In other languages, Bob uses the on-device voice built into iPhone and iPad.</p>
        <h2>What Bob does</h2>
        <ul class="check">
          <li>Greets your child and reads out the name of each picture</li>
          <li>Says each letter sound when its tile is tapped</li>
          <li>Celebrates finished pictures by name ("You drew a DOLPHIN! Brilliant work!")</li>
          <li>Suggests Today's challenge, a new picture each day</li>
          <li>Speaks 18 languages</li>
        </ul>
        <h2>Why a robot?</h2>
        <p>Toddlers love repeating things. Bob happily says "dolphin" for the fiftieth time with the same big smile. He gives children a reason to talk back, and parents a calm helper for the moments when little hands want to draw and little voices want to practise words.</p>
        <p style="margin-top:22px">{STORE_BTN}</p>
      </div>
    </div>
  </div>
</div></section>
"""
write("/bob/", layout("/bob/", "Meet Bob – Draw & Learn", "Bob is the friendly robot in Draw & Learn who names every picture, sounds out letters and cheers on every drawing. Speaks 18 languages, works offline.", bob, ct="web_bob"))

# ---------------- PARENTS ----------------
parents = f"""
<section class="page"><div class="wrap">
  <h1>For parents</h1>
  <p class="meta">The honest version: what the app does, what it doesn't, and how it protects your child.</p>
  <div class="prose">
    <p class="summary"><strong>Short version:</strong> Draw &amp; Learn is free, has no ads, collects no data, needs no account and works offline. It is listed in the App Store's Made for Kids section for ages 5 and under.</p>
    <h2>Who it's for</h2>
    <p>Children from roughly 18 months to 5 years. Toddlers start with Easy guides and bucket fill; older children move to Medium and Hard outlines, then free drawing on a blank canvas. Many parents use it alongside first words and phonics practice.</p>
    <h2>Privacy, in plain words</h2>
    <ul class="check">
      <li>No personal data is collected, ever. App Store privacy label: <strong>Data Not Collected</strong>.</li>
      <li>No advertising, no analytics, no tracking and no third-party code inside the app.</li>
      <li>No account, no sign-in, no email needed.</li>
      <li>No microphone or camera. The only permission it may ask for is to <em>add</em> a finished drawing to Photos.</li>
      <li>Works fully offline. Drawings and progress stay on the device.</li>
    </ul>
    <p>Full details in our <a href="/privacy/">Privacy Policy</a>.</p>
    <h2>Parental gate</h2>
    <p>Settings, language, the rating prompt and any link that leaves the app are behind a grown-ups gate, so a child can't wander out of the drawing area.</p>
    <h2>Learning goals</h2>
    <ul class="check">
      <li><strong>Fine motor skills:</strong> tracing, colouring inside the lines, pinch-to-zoom for detail.</li>
      <li><strong>Vocabulary:</strong> every picture is named out loud, in up to 18 languages.</li>
      <li><strong>Phonics:</strong> letter tiles play individual sounds, then the whole word.</li>
      <li><strong>Letters, numbers and shapes:</strong> dedicated categories to trace.</li>
      <li><strong>Confidence:</strong> Bob celebrates every finished picture.</li>
    </ul>
    <p>Draw &amp; Learn is a learning aid, not a therapy or a replacement for professional advice.</p>
    <h2>Price</h2>
    <p>The app is free and every category is unlocked. There are no subscriptions and no in-app purchases in the current version.</p>
    <h2>Devices</h2>
    <p>iPhone and iPad running iOS or iPadOS 16.6 or later. The app is about 200 MB because all the audio and pictures are included for offline use.</p>
    <p style="margin-top:22px">{STORE_BTN}</p>
  </div>
</div></section>
"""
write("/parents/", layout("/parents/", "For parents – Draw & Learn", "Free, no ads, no data collected, no account, works offline. Made for Kids, ages 5 and under. What Draw & Learn does and how it protects your child.", parents, ct="web_parents"))

# ---------------- SUPPORT ----------------
support = f"""
<section class="page"><div class="wrap">
  <h1>Support</h1>
  <p class="meta">Need help? Email <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>. We aim to reply within 48 hours.</p>
  <div class="prose faq">
    <h2>Frequently asked questions</h2>
    <details open><summary>Is the app free?</summary><p>Yes. All drawing categories and learning activities are available without a subscription or in-app purchase.</p></details>
    <details><summary>Is my child's data safe?</summary><p>Draw &amp; Learn does not collect personal data, show advertising or track children. Drawings remain on the device unless you choose to export them. See our <a href="/privacy/">Privacy Policy</a>.</p></details>
    <details><summary>What ages is it designed for?</summary><p>Children aged 5 and under, with guided drawing, tracing, colouring, first words, phonics, shapes and numbers. Parent settings and links sit behind a parental gate.</p></details>
    <details><summary>Does the app use the internet, microphone or camera?</summary><p>No. Everything children use works fully offline. Bob's voice is either audio bundled with the app or Apple's on-device text-to-speech. The app never asks for microphone or camera access. The only permission it may request is to add a finished drawing to Photos when you choose to save it.</p></details>
    <details><summary>How do I change the language?</summary><p>Tap the flag on the home screen (behind the parental gate) and choose from 18 languages. Bob's words and letter sounds switch immediately.</p></details>
    <details><summary>How do I save or print a drawing?</summary><p>Tap the tick when a picture is done. It is kept in "My Art". From there use the Photos or print buttons at the top of the screen.</p></details>
    <details><summary>The app is not working correctly</summary><p>1. Confirm the device runs iOS or iPadOS 16.6 or later.<br>2. Close and reopen the app.<br>3. Restart the device.<br>If the issue continues, email us with the device model and a description.</p></details>
    <details><summary>Can I request a new picture or category?</summary><p>Yes please! Email <a href="mailto:{HELLO_EMAIL}">{HELLO_EMAIL}</a>. Seasonal packs are added regularly.</p></details>
    <h2>Contact</h2>
    <p>Support: <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a><br>General: <a href="mailto:{HELLO_EMAIL}">{HELLO_EMAIL}</a><br>Press: <a href="mailto:{PRESS_EMAIL}">{PRESS_EMAIL}</a></p>
    <p>Developer: Roberto Pires Almeida, United Kingdom.</p>
  </div>
</div></section>
"""
write("/support/", layout("/support/", "Support – Draw & Learn", "Help and FAQ for the Draw & Learn to Talk with Bob app. Contact support@drawandlearn.app.", support, ct="web_support"))

# ---------------- PRESS ----------------
press = f"""
<section class="page"><div class="wrap">
  <h1>Press kit</h1>
  <p class="meta">Facts, images and boilerplate for writers and creators. Contact <a href="mailto:{PRESS_EMAIL}">{PRESS_EMAIL}</a>.</p>
  <div class="prose">
    <h2>Boilerplate</h2>
    <p class="summary">Draw &amp; Learn to Talk with Bob is a free iPhone and iPad app that helps children aged 5 and under draw, colour and learn first words. Bob, a friendly robot, names every one of the 500+ pictures, sounds out letters and cheers on every finished drawing, in 18 languages. The app has no ads, no tracking and no account, and works fully offline. It was built in the UK by a dad for his own child.</p>
    <h2>Fast facts</h2>
    <table class="facts">
      <tr><th>Name</th><td>Draw &amp; Learn to Talk with Bob</td></tr>
      <tr><th>Platform</th><td>iPhone &amp; iPad, iOS 16.6+</td></tr>
      <tr><th>Price</th><td>Free, no in-app purchases</td></tr>
      <tr><th>Age</th><td>Made for Kids, 5 and under</td></tr>
      <tr><th>Category</th><td>Education</td></tr>
      <tr><th>Content</th><td>500+ pictures, 20+ categories, letters, numbers, shapes, blank canvas</td></tr>
      <tr><th>Languages</th><td>18</td></tr>
      <tr><th>Privacy</th><td>Data Not Collected. No ads, no analytics, no third-party SDKs.</td></tr>
      <tr><th>Developer</th><td>Roberto Pires Almeida, United Kingdom</td></tr>
      <tr><th>Released</th><td>September 2026</td></tr>
      <tr><th>App Store</th><td><a href="https://apps.apple.com/app/id{APP_ID}">apps.apple.com/app/id{APP_ID}</a></td></tr>
    </table>
    <h2>Images</h2>
    <p>Right-click to save. Free to use in coverage of the app.</p>
    <div class="dl">
      <a href="/assets/img/icon.png" download><img src="/assets/img/icon-512.png" alt="App icon"></a>
      <a href="/assets/img/iphone_1.png" download><img src="/assets/img/iphone_1.png" alt="Screenshot 1"></a>
      <a href="/assets/img/iphone_2.png" download><img src="/assets/img/iphone_2.png" alt="Screenshot 2"></a>
      <a href="/assets/img/iphone_3.png" download><img src="/assets/img/iphone_3.png" alt="Screenshot 3"></a>
      <a href="/assets/img/iphone_4.png" download><img src="/assets/img/iphone_4.png" alt="Screenshot 4"></a>
      <a href="/assets/img/iphone_5.png" download><img src="/assets/img/iphone_5.png" alt="Screenshot 5"></a>
    </div>
    <h2>Social</h2>
    <p>{' · '.join(f'<a href="{u}">{n}</a>' for n, u in SOCIAL.items())}</p>
    <h2>Story angles</h2>
    <ul>
      <li>A dad built a toddler app with zero data collection, and Apple approved it for the Made for Kids section.</li>
      <li>Why Bob is a robot: toddlers want the same word said fifty times, patiently.</li>
      <li>An offline-first kids app in a world of subscriptions and ads.</li>
    </ul>
  </div>
</div></section>
"""
write("/press/", layout("/press/", "Press kit – Draw & Learn", "Press kit for Draw & Learn to Talk with Bob: boilerplate, fast facts, icon and screenshots. Contact press@drawandlearn.app.", press, ct="web_press"))

# ---------------- PRIVACY ----------------
privacy = f"""
<section class="page"><div class="wrap"><div class="prose">
  <h1>Privacy Policy</h1>
  <p class="meta">Effective: 28 September 2026</p>
  <p class="summary"><strong>Parent summary:</strong> Draw &amp; Learn does not collect, store, sell, or share personal information about children. It has no accounts, advertising, analytics, or tracking, and contains no third-party SDKs. Drawings and progress stay on the device.</p>
  <h2>Who we are</h2>
  <p>Draw &amp; Learn (listed on the App Store as "Draw &amp; Learn to Talk with Bob") is developed by Roberto Pires Almeida. It is made for children aged 5 and under. This policy explains the privacy practices of the iPhone and iPad app.</p>
  <h2>Information we collect</h2>
  <p>We do not collect personal information, contact information, identifiers, location, usage analytics, advertising data, diagnostics, drawings, voice recordings, or other user content. We do not use tracking technologies or third-party advertising or analytics SDKs. The app contains no third-party code at all, does not access the advertising identifier, and does not send any information to us or to any third party.</p>
  <h2>Offline use</h2>
  <p>Everything children use in the app works offline. The only online content is these legal and support pages and Apple's App Store rating and review screens, which a parent can reach only after passing the parental gate.</p>
  <h2>On-device information</h2>
  <p>The app stores preferences, progress, and drawings locally on the device so its features work. This information is not sent to us. Removing the app may remove locally stored information, subject to Apple's device and backup behaviour.</p>
  <h2>Photos permission</h2>
  <p>If a user explicitly chooses to export artwork, the app may request permission to add that drawing to the device's photo library. It does not read the photo library. Apple controls the permission prompt, and permission can be changed in device Settings.</p>
  <h2>Audio and speech</h2>
  <p>Learning audio is bundled with the app or produced by Apple's on-device system services. The app does not request microphone, camera, or speech-recognition access, does not record audio, and does not send children's speech to us.</p>
  <h2>Children's privacy</h2>
  <p>The app is designed for children and follows a data-minimising approach consistent with applicable children's privacy requirements, including COPPA and the UK Children's Code. Because we do not collect personal information, we do not knowingly collect personal information from children under 13 or any other age.</p>
  <h2>External links and parental gate</h2>
  <p>Parent-facing settings and links to legal and support pages are protected by a parental gate. Those websites are hosted by GitHub Pages and are outside the child-directed activity area. As with any website, GitHub may process standard technical information (such as IP address) when a page is visited, under GitHub's own privacy statement; the app itself sends no information. This website uses no cookies, analytics or third-party scripts. Apple's App Store rating prompt and review page are also reachable only after the parental gate.</p>
  <h2>Data sharing, sale, and retention</h2>
  <p>We do not sell or share personal information. Because we do not receive personal information from the app, we have no server-side personal information to retain or delete.</p>
  <h2>Security</h2>
  <p>We minimise risk by keeping app content and user-created drawings on the device and by avoiding accounts, advertising, analytics, and remote databases.</p>
  <h2>Changes</h2>
  <p>Material changes will be posted on this page with a new effective date. If future app functionality changes its data practices, this policy and the App Store privacy disclosures will be updated before that functionality is released.</p>
  <h2>Contact</h2>
  <p>Privacy questions: <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>.</p>
</div></div></section>
"""
write("/privacy/", layout("/privacy/", "Privacy Policy – Draw & Learn", "Draw & Learn collects no personal data, has no ads, analytics or tracking, and works offline. Full privacy policy.", privacy))

# ---------------- TERMS ----------------
terms = f"""
<section class="page"><div class="wrap"><div class="prose">
  <h1>Terms of Use</h1>
  <p class="meta">Effective: 28 September 2026</p>
  <p class="summary"><strong>Summary:</strong> Draw &amp; Learn (listed on the App Store as "Draw &amp; Learn to Talk with Bob") is a free educational app made for children aged 5 and under. It has no subscription or in-app purchase in this release. A parent or legal guardian should review these terms for a child.</p>
  <h2>1. Agreement</h2><p>By downloading or using Draw &amp; Learn, you agree to these Terms and Apple's applicable App Store and Apple Media Services terms. If you permit a child to use the app, you accept these Terms on the child's behalf and remain responsible for supervising use.</p>
  <h2>2. Educational purpose</h2><p>The app provides creative drawing, tracing, vocabulary, phonics, shape, and number activities. It is a learning aid and does not replace professional educational, medical, developmental, or therapeutic advice.</p>
  <h2>3. Free access</h2><p>The current version of the app provides all included categories and activities free of charge. No subscription, trial, advertising, or in-app purchase is required. Apple may apply its own connectivity or device-service terms.</p>
  <h2>4. Licence</h2><p>We grant you a limited, personal, non-exclusive, non-transferable, revocable licence to use the app on Apple-branded products you own or control, as permitted by Apple's Usage Rules. You may not copy, resell, reverse engineer except where law permits, interfere with, or use the app unlawfully.</p>
  <h2>5. User-created artwork</h2><p>You retain rights in artwork created with the app. Artwork is stored locally and is not uploaded to us. You are responsible for exported or shared artwork and for ensuring it does not infringe another person's rights.</p>
  <h2>6. Intellectual property</h2><p>The app, bundled learning materials, artwork, audio, design, and software are protected by applicable intellectual-property laws. These Terms do not transfer ownership of those materials.</p>
  <h2>7. Privacy and children</h2><p>Our <a href="/privacy/">Privacy Policy</a> explains the app's data practices. Parent-facing external links are placed behind a parental gate. Parents and guardians remain responsible for device settings, backups, exports, and supervision.</p>
  <h2>8. Availability and updates</h2><p>We may update, improve, suspend, or discontinue features. Some functions depend on a compatible device and operating system. We do not guarantee uninterrupted or error-free operation.</p>
  <h2>9. Disclaimer</h2><p>To the maximum extent permitted by law, the app is provided "as is" and "as available," without warranties beyond those that cannot legally be excluded. Nothing in these Terms limits statutory consumer rights.</p>
  <h2>10. Liability</h2><p>To the maximum extent permitted by law, we are not liable for indirect, incidental, special, or consequential loss arising from use of the app. Where liability cannot be excluded, it is limited to the greater of the amount paid for the app and the minimum amount required by applicable law. The app is free in this release.</p>
  <h2>11. Apple terms</h2><p>These Terms are between you and the developer, not Apple. Apple has no obligation to provide maintenance or support. Apple and its subsidiaries are third-party beneficiaries of these Terms and may enforce the Apple-related provisions. Claims relating to the app remain the developer's responsibility to the extent required by law and Apple's standard licensed application terms.</p>
  <h2>12. Governing law</h2><p>These Terms are governed by the laws applicable to the developer, without removing mandatory consumer protections or rights available in your country of residence.</p>
  <h2>13. Changes and contact</h2><p>Changes will be posted here with a new effective date. Questions may be sent to <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>.</p>
</div></div></section>
"""
write("/terms/", layout("/terms/", "Terms of Use – Draw & Learn", "Terms of use for the Draw & Learn to Talk with Bob app.", terms))

# ---------------- 404 ----------------
(ROOT / "404.html").write_text(layout("/404", "Page not found – Draw & Learn", "Page not found.", f"""
<section class="page"><div class="wrap"><h1>Oops, Bob can't find that page</h1><p class="meta">The link may be old. Try the <a href="/">home page</a> or <a href="/support/">support</a>.</p></div></section>
"""))
print("wrote 404.html")

# robots + sitemap
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
pages = ["/", "/features/", "/bob/", "/parents/", "/support/", "/press/", "/privacy/", "/terms/"]
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{DOMAIN}{p}</loc></url>\n" for p in pages) + "</urlset>\n")
(ROOT / "CNAME").write_text("drawandlearn.app\n")
(ROOT / ".nojekyll").write_text("")
print("wrote robots.txt sitemap.xml CNAME .nojekyll")
