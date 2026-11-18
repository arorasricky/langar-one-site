#!/usr/bin/env python3
"""Builds the Langar One static site into ../docs. Run: python3 build.py"""
import datetime, json, os, pathlib, re, shutil

SRC = pathlib.Path(__file__).parent
PREVIEW = bool(os.environ.get("PREVIEW"))
DIST = SRC.parent / ("preview" if PREVIEW else "docs")
SITE = "https://www.langar.one"
REQUEST_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdpoP7_V4gVnkZWpGE3dDRKkj0TAPt26lUG5-_h-JF7MszP4w/viewform"
FONTS = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700;12..96,800&family=Figtree:wght@400;500;600;700&display=swap"

BASKET = '<path d="M17 30a15 15 0 0 1 30 0" fill="none" stroke="#F2A81D" stroke-width="7" stroke-linecap="round"/><path d="M6 30h52l-5 24a5 5 0 0 1-5 4H16a5 5 0 0 1-5-4z" fill="{body}"/>'


def mark(size, body="#F3F6F1"):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" aria-hidden="true">{BASKET.format(body=body)}</svg>'


def icon(paths, color="#2F6B4F", size=32):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>')


HEART = '<path d="M12 20s-7-4.3-7-10a4 4 0 0 1 7-2.600A4 4 0 0 1 19 10c0 5.700-7 10-7 10z"/>'
PEOPLE = '<circle cx="8" cy="9" r="3"/><circle cx="17" cy="10" r="2.5"/><path d="M2.5 19a5.500 5.500 0 0 1 11 0"/><path d="M15 19a4 4 0 0 1 6.500-3"/>'
GLOBE = '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c3 3.200 3 14.800 0 18"/><path d="M12 3c-3 3.200-3 14.800 0 18"/>'
BOLT = '<path d="M13 3L5 13.500h6L10 21l9-11h-6z"/>'
BASKET_ICON = '<path d="M7 11a5 5 0 0 1 10 0"/><path d="M3 11h18l-1.800 8a2 2 0 0 1-2 1.500H6.800a2 2 0 0 1-2-1.500z"/>'
SPEAKER = '<path d="M4 10v4h3l6 4V6l-6 4z"/><path d="M16.500 9.500a4 4 0 0 1 0 5"/><path d="M19 7a7.500 7.500 0 0 1 0 10"/>'
ARROW = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5"/><path d="M11 6l-6 6 6 6"/></svg>'


def header(root, home):
    brand = (f'<a class="brand" href="{root}" aria-label="Langar One home">{mark(40)}'
             f'<span class="brand-text"><span class="brand-name">Langar <b>One</b></span>'
             + ('<span class="brand-tag">A 501(c)(3) charity</span>' if home else '') + '</span></a>')
    if home:
        right = ('<nav class="nav" aria-label="Main"><a href="how-it-works/">How It Works</a><a href="#mission">Mission</a><a href="#origin">Origin Story</a>'
                 '<a href="#impact">Impact</a><a href="faq/">FAQ</a><a href="#involved">Get Involved</a></nav>')
    else:
        right = f'<a class="back" href="{root}">{ARROW}Back to Home</a>'
    return f'<header class="site-header"><div class="wrap">{brand}{right}</div></header>'


def footer(root):
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div class="foot-brand"><a class="brand" href="{root}">{mark(34)}<span class="brand-name">Langar <b>One</b></span></a>
<p>Ending hunger, one delivery at a time.</p><p style="font-size:15px">A 501(c)(3) charity</p></div>
<nav class="foot-col" aria-label="About"><strong>About</strong><a href="{root}#mission">Our Mission</a><a href="{root}#impact">Our Impact</a><a href="{root}#origin">Our Story</a><a href="{root}how-it-works/">How It Works</a><a href="{root}faq/">FAQ</a></nav>
<nav class="foot-col" aria-label="Get involved"><strong>Get Involved</strong><a href="{root}volunteer/">Volunteer</a><a href="{root}#involved">Donate</a><a href="{root}plan-event/">Host an Event</a></nav>
<div class="foot-col"><strong>Contact</strong><a href="mailto:info@langar.one">info@langar.one</a><address>46539 Mission Blvd #1021<br>Fremont, CA 94539<br>United States</address></div>
</div>
<div class="foot-base"><span>© 2026 Langar One. All rights reserved.</span>
<span><a href="{root}terms/">Terms &amp; Conditions</a><span aria-hidden="true">·</span><a href="{root}privacy/">Privacy Policy</a></span>
<span>Made with <svg width="16" height="16" viewBox="0 0 24 24" fill="#F2A81D" role="img" aria-label="love">{HEART}</svg> for communities everywhere</span></div>
</div></footer>'''


def page(path, title, desc, body, home=False, script=False, crumb=None, extra=None):
    root = "./" if path == "" else ("/" if path == "404" else "../")
    canonical = f"{SITE}/{path}"
    noindex = path == "404"
    data = [ORG, WEBSITE] if home else []
    if crumb:
        data.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": crumb.replace("&amp;", "&"), "item": canonical}]})
    if extra:
        data.append(extra)
    jsonld = "".join(f'<script type="application/ld+json">{json.dumps(d, ensure_ascii=False)}</script>\n' for d in data)
    robots = '<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
{'' if noindex else '<link rel="canonical" href="' + canonical + '">'}
<meta property="og:type" content="website">
<meta property="og:locale" content="en_US">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Langar One: Ending Hunger, One Delivery at a Time">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/assets/og.png">
<meta property="og:site_name" content="Langar One">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta name="theme-color" content="#12392B">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{root}assets/site.css">
{jsonld}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{header(root, home)}
<main id="main">
{body}
</main>
{footer(root)}
{'<script src="' + root + 'assets/site.js"></script>' if script else ''}
</body>
</html>
'''
    if PREVIEW:  # explicit index.html links so pages open without a web server's directory index
        html = re.sub(r'href="((?:\.\.?/)(?:[a-z-]+/)?|[a-z-]+/)(#[a-z]+)?"', lambda m: f'href="{m.group(1)}index.html{m.group(2) or ""}"', html)
    out = DIST / path / "index.html" if path != "404" else DIST / "404.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


DESC = "Langar One is a 501(c)(3) charity delivering free groceries to families facing food insecurity across the United States. Request help or get involved."
ORG = {"@context": "https://schema.org", "@type": "NGO", "@id": f"{SITE}/#organization", "name": "Langar One", "url": f"{SITE}/",
       "logo": f"{SITE}/assets/logo.png", "image": f"{SITE}/assets/og.png", "slogan": "Ending Hunger, One Delivery at a Time",
       "description": DESC, "foundingDate": "2022", "email": "info@langar.one", "nonprofitStatus": "https://schema.org/Nonprofit501c3",
       "areaServed": {"@type": "Country", "name": "United States"},
       "knowsAbout": ["Food insecurity", "Hunger relief", "Free grocery delivery", "Langar"],
       "address": {"@type": "PostalAddress", "streetAddress": "46539 Mission Blvd #1021", "addressLocality": "Fremont",
                   "addressRegion": "CA", "postalCode": "94539", "addressCountry": "US"}}
WEBSITE = {"@context": "https://schema.org", "@type": "WebSite", "@id": f"{SITE}/#website", "name": "Langar One", "url": f"{SITE}/",
           "publisher": {"@id": f"{SITE}/#organization"}}


def card(ic, title, text):
    return f'<div class="card">{icon(ic)}<h3 class="h3">{title}</h3><p class="muted">{text}</p></div>'


STEPS = '''<ol class="steps">
<li><span class="num">1</span><h3 class="h3">Request assistance</h3><p>A family asks for help through our request form — or a partner agency submits a request on their behalf.</p></li>
<li><span class="num">2</span><h3 class="h3">Eligibility confirmed</h3><p>We review each request and confirm the family qualifies for the program.</p></li>
<li><span class="num">3</span><h3 class="h3">Groceries delivered</h3><p>A real grocery shop arrives at their door, at no cost to the family.</p></li>
<li class="last"><span class="num">4</span><h3 class="h3">3-month support cycle</h3><p>Delivery runs for 3 months. If a family's situation hasn't improved, the program renews — continued support for as long as it's truly needed.</p></li>
</ol>'''

HOME = f'''<section class="hero" id="top"><div class="wrap">
<div class="hero-copy"><h1>Ending Hunger,<br>One Delivery at a Time</h1>
<p>Our mission is to solve hunger and food insecurity by delivering groceries to families in need across the United States.</p>
<a class="btn btn-gold btn-lg" href="{REQUEST_FORM}" target="_blank" rel="noopener">Request Help</a></div>
<div class="hero-art"><svg viewBox="0 0 460 440" aria-hidden="true"><path d="M110 250a120 120 0 0 1 240 0" fill="none" stroke="#F2A81D" stroke-width="46" stroke-linecap="round"/><path d="M20 250h420l-34 190H54z" fill="#F3F6F1"/><path d="M31 313h398" fill="none" stroke="#C9D8CD" stroke-width="4"/><path d="M43 376h374" fill="none" stroke="#C9D8CD" stroke-width="4"/></svg></div>
</div></section>

<section class="band" aria-labelledby="challenge"><div class="wrap">
<h2 id="challenge">The challenge we're facing</h2>
<div class="grid">
<div class="stat"><b>42 million</b><span>Americans face food insecurity, including 13 million children</span></div>
<div class="stat"><b>1 in 8</b><span>Households in the US struggle to put food on the table</span></div>
<div class="stat"><b>$0</b><span>That's what families pay for our groceries — everyone deserves access to food</span></div>
</div></div></section>

<section id="how" class="white"><div class="wrap section">
<div class="head"><p class="eyebrow">How it works</p><h2 class="h2">Four steps from request to doorstep</h2></div>
{STEPS}
<p><a class="more" href="how-it-works/">See how Langar One works and what families receive</a> · <a class="more" href="faq/">Read the FAQ</a></p>
</div></section>

<section id="mission"><div class="wrap section">
<div class="head"><p class="eyebrow">What we stand for</p><h2 class="h2">Our Mission</h2>
<p class="lead">At Langar One, we're transforming the fight against hunger by bringing the grocery store directly to families in need.</p></div>
<div class="grid g4">
{card(HEART, "Dignity First", "We deliver groceries to needy families across the US, so they can cook it maintaining their autonomy and cultural food preferences.")}
{card(PEOPLE, "Community Connection", "Every delivery strengthens bonds. We're not just feeding families — we're building a network of care across America.")}
{card(GLOBE, "Start Local, Think Global", "We're tackling hunger state by state, with a vision to create a model that can be replicated worldwide.")}
{card(BOLT, "Technology Forward", "Using technology as an enabler to drive broad change faster.")}
</div></div></section>

<section id="origin" class="white"><div class="wrap section" style="gap:60px">
<div class="head"><p class="eyebrow">Our journey</p><h2 class="h2">Origin Story</h2>
<p class="lead">From a simple act of service to a movement fighting hunger across America</p></div>
<div class="quote">{mark(84)}<blockquote>“The Langar tradition teaches us that everyone, regardless of their background, deserves to be fed with dignity and respect.”</blockquote></div>
<div class="grid g3 wide">
<div class="rule"><h3>The Langar Tradition</h3><p class="muted">For 500+ years, Sikh Temples have operated "Langar" — free community kitchens serving meals to all people, embodying equality and service.</p></div>
<div class="rule"><h3>A Modern Adaptation</h3><p class="muted">Langar One brings this tradition to the 21st century by delivering groceries directly to families facing food insecurity.</p></div>
<div class="rule"><h3>Our Vision</h3><p class="muted">Eliminate hunger across America, one grocery delivery at a time.</p></div>
</div>
<div class="journey"><h3>Our Journey So Far</h3><ol>
<li><span class="year">2022</span><span class="bar"></span><h4>The Beginning</h4><p class="muted">Langar One was founded with a vision to solve hunger through grocery deliveries during COVID</p></li>
<li><span class="year">2024</span><span class="bar"></span><h4>Expanded Reach</h4><p class="muted">Reached 1,000+ deliveries with 20+ supporters helping us make a difference</p></li>
<li><span class="year">2025</span><span class="bar"></span><h4>Scaling Impact</h4><p class="muted">Reached 2,000+ deliveries with massive expansion plans</p></li>
</ol></div>
</div></section>

<section id="impact" class="dark"><div class="wrap section" style="gap:56px">
<div class="head"><h2 class="h2">Our Impact</h2><p class="lead">Together, we're making a real difference in the fight against hunger. Here's what we've accomplished so far.</p></div>
<div class="grid g-impact">
<div class="impact"><b>2,000+</b><h3>Grocery Deliveries</h3><p>Packages of nutritious food delivered to families</p></div>
<div class="impact"><b>5</b><h3>States</h3><p>Delivering hope and groceries across the US</p></div>
<div class="impact"><b>100+</b><h3>Supporters</h3><p>Dedicated individuals making a difference</p></div>
<div class="impact"><b>100%</b><h3>Commitment</h3><p>To ending hunger in our lifetime</p></div>
</div></div></section>

<section id="involved"><div class="wrap section">
<div class="head"><h2 class="h2">Get Involved</h2><p class="lead">Join us in the fight against hunger. There are many ways you can help make a difference in our communities.</p></div>
<div class="grid g4">
<div class="act"><h3>Volunteer</h3><p>Help us pack and deliver groceries to families in need. Every hour counts.</p><a class="btn" href="volunteer/">Sign Up to Volunteer</a></div>
<div class="act gold"><h3>Donate</h3><p>Your financial support helps us purchase and deliver groceries to more families.</p><span class="pill">Coming Soon</span></div>
<div class="act"><h3>Host an Event</h3><p>Organize a food drive, fundraiser, or awareness event in your community.</p><a class="btn" href="plan-event/">Plan an Event</a></div>
<div class="act"><h3>Contact Us</h3><p>Have questions or want to learn more? We'd love to hear from you.</p><a class="btn" href="mailto:info@langar.one">Send Message</a></div>
</div></div></section>'''


HOW = f'''<section class="page-hero"><div class="wrap"><h1>How Langar One Works</h1>
<p>Bringing the grocery store directly to families in need — with dignity, choice, and community. Four steps from request to doorstep.</p></div></section>
<div class="wrap section">
{STEPS}
</div>
<section class="white"><div class="wrap receive">
<div class="receive-copy"><p class="eyebrow">What families receive</p>
<h2 class="h2">Real groceries. Real choice. Delivered with dignity.</h2>
<p class="lead">Families receive a curated basket of staple groceries — fresh produce, proteins, grains, and pantry essentials — selected around their dietary and cultural preferences.</p>
<p class="punch">Not a pre-packed charity box. A real grocery shop.</p></div>
<ul class="groceries"><li><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#2F6B4F" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 19c0-8 5-13 14-14 0 9-5 14-14 14z"/><path d="M5 19l8-8"/></svg><span>Fresh produce</span></li><li><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#2F6B4F" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3c3.500 0 6.500 5.500 6.500 10a6.500 6.500 0 0 1-13 0C5.500 8.500 8.500 3 12 3z"/></svg><span>Protein</span></li><li><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#2F6B4F" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 11a4 4 0 0 1 4-4h8a4 4 0 0 1 2 7.500V19H6v-4.500A4 4 0 0 1 4 11z"/><path d="M10 11v3"/><path d="M14 11v3"/></svg><span>Grains &amp; bread</span></li><li><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#2F6B4F" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="6" y="8" width="12" height="13" rx="2.500"/><path d="M8 4h8v4H8z"/><path d="M6 13h12"/></svg><span>Pantry staples</span></li><li><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#2F6B4F" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 3h6v3l2.500 4V19a2 2 0 0 1-2 2h-7a2 2 0 0 1-2-2v-9L9 6z"/><path d="M6.500 13h11"/></svg><span>Dairy &amp; milk</span></li></ul>
</div></section>
<div class="wrap section" style="gap:20px">
<div class="grid g3" style="grid-template-columns:repeat(auto-fit,minmax(min(340px,100%),1fr))">
<div class="card"><h2 class="h3">Renewable support</h2><p class="muted">Delivery runs for 3 months. If a family's situation hasn't improved, the program renews — continued support for as long as it's truly needed.</p></div>
<div class="card"><h2 class="h3">Agency submissions welcome</h2><p class="muted">Partner agencies can submit requests on behalf of families — connecting clients to food support without adding burden to them.</p></div>
</div>
<div class="cta"><div><h2 class="h2s">Need groceries, or know a family who does?</h2><p>Requests take a few minutes. It costs families $0.</p></div>
<a class="btn btn-lg" href="{REQUEST_FORM}" target="_blank" rel="noopener">Request Help</a></div>
</div>'''

FAQS = [
    ("What is Langar One?", "Langar One is a 501(c)(3) charity that delivers free groceries to families facing food insecurity across the United States. Our mission is to solve hunger and food insecurity by bringing the grocery store directly to families in need."),
    ("Who can get help from Langar One?", "Families in the United States who are facing food insecurity can request help. Every request goes through an eligibility review, and approval also depends on program capacity."),
    ("How much does it cost?", "Nothing. Families pay $0 for the groceries and for delivery."),
    ("How do I request groceries?", f'Fill out the <a href="{REQUEST_FORM}" target="_blank" rel="noopener">Langar One grocery delivery request form</a>. It should be completed by an adult on behalf of the household, and asks for your name, phone number, delivery address, the number of dependents in your household, and your reason for needing food assistance.'),
    ("What groceries will I receive?", "A basket of staple groceries — fresh produce, proteins, grains and bread, pantry staples, and dairy — selected around your household's dietary and cultural preferences. Specific items can't be guaranteed and may be substituted based on supply, so please check ingredient labels for allergens."),
    ("How long does support last?", "Approved families receive grocery deliveries for up to three months. If your situation hasn't improved, you can request a renewal, which is reviewed based on continued need and program capacity."),
    ("Can an agency or caseworker request help for a client?", "Yes. Partner agencies can submit requests on behalf of the families they serve, connecting clients to food support without adding burden to them."),
    ("Where does Langar One deliver?", "We have delivered groceries in 5 states so far and are expanding state by state, with the goal of serving families across the United States."),
    ("What does \"Langar\" mean? Do I need to be Sikh to get help?", "Langar is a 500-year-old Sikh tradition of free community kitchens that serve meals to all people, embodying equality and service. Langar One brings that tradition to grocery delivery. Help is for everyone, regardless of background."),
    ("How is my personal information used?", 'We use your information only to run the program: to verify eligibility, coordinate and deliver your groceries, and contact you about your delivery. We do not sell, rent, or trade it. See our <a href="../privacy/">Privacy Policy</a> for details.'),
    ("How can I help?", 'You can <a href="../volunteer/">volunteer</a> to help with grocery deliveries, or <a href="../plan-event/">host a food drive, fundraiser, or awareness event</a>. Online donations are coming soon. Questions? Email <a href="mailto:info@langar.one">info@langar.one</a>.'),
]
FAQ = ('<section class="page-hero"><div class="wrap"><h1>Frequently Asked Questions</h1>'
       '<p>How free grocery delivery from Langar One works, who qualifies, and how to get involved.</p></div></section>'
       '<div class="faq">' + "".join(f"<section><h2>{q}</h2><p>{a}</p></section>" for q, a in FAQS) + "</div>")
FAQ_LD = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in FAQS]}


def field(name, label, type_="text", required=False, placeholder="", auto=""):
    star = " *" if required else ""
    attrs = f'type="{type_}" name="{name}" data-label="{label}"'
    if required:
        attrs += " required"
    if placeholder:
        attrs += f' placeholder="{placeholder}"'
    if auto:
        attrs += f' autocomplete="{auto}"'
    return f'<label>{label}{star}<input {attrs}></label>'


VOLUNTEER = f'''<section class="page-hero"><div class="wrap"><h1>Volunteer With Us</h1>
<p>Join our community of volunteers making a real difference in the fight against hunger. Whether you can spare a few hours a week or a full day, your time matters.</p></div></section>
<div class="wrap split">
<div class="why"><h2 class="h2s">Why Volunteer?</h2><div>
<div class="rule"><h3>Make a Direct Impact</h3><p class="muted">Every grocery delivery you help with directly supports a family in need</p></div>
<div class="rule"><h3>Flexible Schedule</h3><p class="muted">Choose volunteer shifts that work with your availability</p></div>
<div class="rule"><h3>Serve Your Community</h3><p class="muted">Connect with and support families in your local area</p></div>
</div></div>
<form class="form" data-form="volunteer">
<div class="form-head"><h2>Volunteer Application</h2><p class="muted">Fill out the form below and we'll get in touch with volunteer opportunities</p></div>
<div class="row">{field("firstName", "First Name", required=True, auto="given-name")}{field("lastName", "Last Name", required=True, auto="family-name")}</div>
{field("email", "Email", "email", True, auto="email")}
{field("phone", "Phone Number", "tel", auto="tel")}
{field("cityState", "City/State", placeholder="e.g., San Francisco, CA")}
<button class="btn btn-gold" type="submit">Submit Application</button>
<p class="form-msg" role="status" tabindex="-1" hidden></p>
</form></div>'''

EVENT = f'''<section class="page-hero"><div class="wrap"><h1>Plan an Event</h1>
<p>Host a food drive, fundraiser, or awareness event in your community. Together, we can make a bigger impact in the fight against hunger.</p></div></section>
<div class="wrap ideas"><h2 class="h2s">Event Ideas</h2><div class="grid g3">
{card(BASKET_ICON, "Food Drive", "Organize a collection event at your workplace, school, or community center to gather non-perishable food items")}
{card(HEART, "Fundraiser", "Host a benefit dinner, bake sale, or virtual fundraising campaign to raise money for grocery deliveries")}
{card(SPEAKER, "Awareness Event", "Organize a community presentation, panel discussion, or social media campaign to raise awareness about food insecurity")}
</div></div>
<div class="narrow"><form class="form" data-form="event">
<div class="form-head"><h2>Event Proposal</h2><p class="muted">Tell us about your event idea and we'll help bring it to life</p></div>
{field("name", "Your Name", required=True, auto="name")}
<div class="row">{field("email", "Email", "email", True, auto="email")}{field("phone", "Phone Number", "tel", auto="tel")}</div>
{field("organization", "Organization (Optional)", placeholder="School, workplace, community group, etc.", auto="organization")}
<label>Event Type *<select name="eventType" data-label="Event Type" required><option value="">Select event type</option><option>Food Drive</option><option>Fundraiser</option><option>Awareness Event</option><option>Volunteer Rally</option><option>Other</option></select></label>
{field("location", "Location", placeholder="City, State or venue address")}
<button class="btn btn-gold" type="submit">Submit Event Proposal</button>
<p class="form-msg" role="status" tabindex="-1" hidden></p>
</form></div>'''


def legal(title, intro, sections):
    body = "".join(f"<section><h2>{h}</h2>{c}</section>" for h, c in sections)
    return (f'<div class="legal"><div class="legal-head"><h1>{title}</h1><p class="date">Langar One · Effective April 5, 2026</p>'
            f'<p class="intro">{intro}</p></div>{body}<p class="sig">Langar One · langar.one · hello@langar.one</p></div>')


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


HELLO = '<a href="mailto:hello@langar.one">hello@langar.one</a>'

TERMS = legal("Terms &amp; Conditions",
    "By submitting the Langar One Grocery Delivery request form, you agree to the following terms. Please read them carefully before submitting.", [
    ("1. Program Description", "<p>Langar One provides free grocery delivery to families facing food insecurity across the United States. Approved applicants receive grocery deliveries for up to three (3) months, with an option to renew based on continued need.</p>"),
    ("2. Eligibility", "<p>Participation is subject to eligibility review. Langar One reserves the right to approve, deny, or discontinue service at its sole discretion, including if demand exceeds available capacity or if information provided is found to be inaccurate.</p>"),
    ("3. Accuracy of Information", "<p>You agree that all information submitted — including your name, address, household size, and reason for needing assistance — is truthful and accurate. Providing false or misleading information may result in immediate removal from the program.</p>"),
    ("4. No Liability for Groceries Delivered", '<p class="caps">LANGAR ONE MAKES NO WARRANTIES, EXPRESS OR IMPLIED, REGARDING THE GROCERIES DELIVERED, INCLUDING BUT NOT LIMITED TO THEIR FITNESS FOR A PARTICULAR PURPOSE, FRESHNESS, NUTRITIONAL CONTENT, OR SUITABILITY FOR ANY DIETARY NEED.</p><p>You acknowledge and agree that:</p>' + ul(
        "Langar One is not liable for any allergic reactions, illness, injury, or harm resulting from consumption of delivered groceries.",
        "It is your sole responsibility to review all items received and verify they are safe for you and your household members, including checking ingredient labels for allergens.",
        "Langar One does not guarantee the availability of specific items and reserves the right to substitute products based on supply.",
        "Langar One is not responsible for any damage, loss, or theft occurring after delivery has been made to the address provided.")),
    ("5. Renewal &amp; Program Continuation", "<p>Grocery delivery is provided for up to three (3) months per approved application. Continuation requires a renewal request and is subject to re-evaluation of need and program capacity. Langar One reserves the right to modify, suspend, or discontinue the program at any time.</p>"),
    ("6. Limitation of Liability", '<p class="caps">TO THE FULLEST EXTENT PERMITTED BY APPLICABLE LAW, LANGAR ONE, ITS OFFICERS, VOLUNTEERS, PARTNERS, AND AFFILIATES SHALL NOT BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES ARISING FROM YOUR PARTICIPATION IN THE PROGRAM OR YOUR USE OF GROCERIES DELIVERED. IN NO EVENT SHALL LANGAR ONE\'S TOTAL LIABILITY EXCEED THE VALUE OF THE GROCERIES DELIVERED TO YOU.</p>'),
    ("7. Changes to These Terms", "<p>Langar One may update these Terms at any time. Continued participation in the program following any update constitutes acceptance of the revised Terms.</p>"),
    ("8. Governing Law", "<p>These Terms are governed by the laws of the United States and the state in which you reside, without regard to conflict of law principles.</p>"),
    ("9. Contact", f"<p>Questions about these Terms? Reach us at {HELLO}.</p>"),
])

PRIVACY = legal("Privacy Policy",
    "Langar One is committed to protecting the privacy of every family we serve. This Privacy Policy explains what information we collect through our Grocery Delivery request form, how we use it, and your rights.", [
    ("1. Information We Collect", "<p>When you submit the Langar One Grocery Delivery request form, we collect:</p>" + ul("Full name", "Phone number", "Delivery address (street, city, state)", "Number of dependents in your household", "Reason for needing food assistance")),
    ("2. How We Use Your Information", "<p>We use your information solely to operate the Langar One program:</p>" + ul("Verify your eligibility for the program", "Coordinate and deliver groceries to your address", "Contact you regarding your delivery or program status", "Evaluate overall program impact in aggregate, anonymized form")),
    ("3. How We Share Your Information", "<p>Langar One does not sell, rent, or trade your personal information. We share it only in these limited circumstances:</p>" + ul("With grocery suppliers and delivery partners — solely to fulfill your delivery", "With partner agencies assisting in program administration", "As required by law or in response to a valid legal process") + "<p>All third parties who receive your information are required to handle it confidentially and use it only to fulfill your delivery.</p>"),
    ("4. Data Retention", "<p>We retain your information for as long as you are an active participant and for a reasonable period thereafter for recordkeeping purposes. You may request deletion at any time (see Section 6).</p>"),
    ("5. Data Security", "<p>We take reasonable measures to protect your personal information from unauthorized access, loss, or misuse. No electronic system is completely secure, and we cannot guarantee absolute security.</p>"),
    ("6. Your Rights", "<p>You have the right to:</p>" + ul("Access the personal information we hold about you", "Request correction of inaccurate information", "Request deletion of your information", "Withdraw from the program at any time") + f"<p>To exercise any of these rights, contact us at {HELLO}.</p>"),
    ("7. Children's Privacy", "<p>Our form is intended to be completed by adults on behalf of their households. We do not knowingly collect personal information directly from children under 13.</p>"),
    ("8. Changes to This Policy", "<p>We may update this Privacy Policy from time to time. Any changes will be reflected with a new effective date. Continued participation constitutes acceptance of the updated Policy.</p>"),
    ("9. Contact", f"<p>Questions or concerns? Contact us at {HELLO} or visit langar.one.</p>"),
])

NOTFOUND = '<div class="wrap notfound"><h1 class="h2">Page not found</h1><p class="lead">That page doesn\'t exist. The homepage has everything.</p><a class="btn btn-gold btn-lg" href="/">Back to Home</a></div>'

FAVICON = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#12392B"/><g transform="translate(9 7) scale(.72)">{BASKET.format(body="#F3F6F1")}</g></svg>'
LOGO = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">{BASKET.format(body="#12392B")}</svg>'


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / "assets").mkdir(parents=True)
    for f in ("site.css", "site.js"):
        shutil.copy(SRC / f, DIST / "assets" / f)
    for f in (SRC / "static").iterdir():
        shutil.copy(f, DIST / "assets" / f.name)
    (DIST / "assets" / "favicon.svg").write_text(FAVICON)
    (DIST / "assets" / "logo.svg").write_text(LOGO)
    (DIST / ".nojekyll").write_text("")
    if not PREVIEW:
        (DIST / "CNAME").write_text("www.langar.one\n")  # GitHub Pages custom domain
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    paths = ["", "how-it-works/", "faq/", "volunteer/", "plan-event/", "terms/", "privacy/"]
    (DIST / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"<url><loc>{SITE}/{p}</loc><lastmod>{datetime.date.today().isoformat()}</lastmod></url>\n" for p in paths) + "</urlset>\n")
    page("", "Langar One | Free Grocery Delivery for Families in Need", DESC, HOME, home=True)
    page("how-it-works/", "How Free Grocery Delivery Works | Langar One",
         "How Langar One delivers free groceries to families in need: request help, eligibility review, doorstep delivery, and three months of renewable support.", HOW, crumb="How It Works")
    page("faq/", "FAQ: Free Grocery Delivery for Families | Langar One",
         "Answers about Langar One's free grocery delivery: who qualifies, what it costs, what groceries you receive, how long support lasts, and how to help.", FAQ, crumb="FAQ", extra=FAQ_LD)
    page("volunteer/", "Volunteer With Langar One | Help Deliver Free Groceries",
         "Volunteer with Langar One to help deliver free groceries to families in need. Flexible shifts and direct impact in your community. Apply online.", VOLUNTEER, script=True, crumb="Volunteer")
    page("plan-event/", "Host a Food Drive or Fundraiser | Langar One",
         "Plan a food drive, fundraiser, or awareness event with Langar One and help fight hunger in your community. Send us your event proposal.", EVENT, script=True, crumb="Plan an Event")
    page("terms/", "Terms &amp; Conditions - Langar One", "Terms and conditions for the Langar One free grocery delivery program.", TERMS, crumb="Terms &amp; Conditions")
    page("privacy/", "Privacy Policy - Langar One", "How Langar One collects, uses and protects the information families share through its grocery delivery request form.", PRIVACY, crumb="Privacy Policy")
    page("404", "Page not found - Langar One", "Page not found.", NOTFOUND)
    print("built", sorted(str(p.relative_to(DIST)) for p in DIST.rglob("*") if p.is_file()))


if __name__ == "__main__":
    main()
