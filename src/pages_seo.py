"""Search-focused pages: help pages for families, city pages, and a page for companies.

Each page is a dict: path, title, desc, body, crumb, and optional faq (list of question/answer pairs).
In body text, {R} stands for the path back to the site root and is filled in by build.py.
"""

EIN = "41-3146886"

NEED_NOW = '''<div class="card"><h2 class="h3">Need food today?</h2>
<p class="muted">Langar One reviews every request and cannot deliver the same day. If you need food right now, call or text <strong>211</strong>, or visit <a href="https://www.211.org/" target="_blank" rel="noopener">211.org</a>, to find free food near you. You can also <a href="https://www.feedingamerica.org/find-your-local-foodbank" target="_blank" rel="noopener">find your local food bank</a> through Feeding America.</p></div>'''

RECEIVE = '''<div class="grid g3">
<div class="rule"><h3>Real groceries</h3><p class="muted">Fresh produce, proteins, grains and bread, pantry staples, and dairy.</p></div>
<div class="rule"><h3>Chosen around your household</h3><p class="muted">Groceries are selected around your dietary and cultural preferences. Not a pre-packed charity box.</p></div>
<div class="rule"><h3>Three months of support</h3><p class="muted">Approved families receive deliveries for three months, and can renew if they still need help.</p></div>
</div>'''


def request_cta(form, heading="Request free groceries", text="Requests take a few minutes. It costs families $0."):
    return (f'<div class="cta"><div><h2 class="h2s">{heading}</h2><p>{text} Every request is reviewed for eligibility, and approval depends on program capacity.</p></div>'
            f'<a class="btn btn-lg" href="{form}" target="_blank" rel="noopener">Request Help</a></div>')


def hero(h1, lead):
    return f'<section class="page-hero"><div class="wrap"><h1>{h1}</h1>\n<p>{lead}</p></div></section>\n'


def qa_block(pairs):
    return '<div class="faq article" style="padding-top:0">' + "".join(f"<section><h3>{q}</h3><p>{a}</p></section>" for q, a in pairs) + "</div>"


def seo_pages(steps, form):
    pages = []

    # ---- Free groceries
    faq = [
        ("Are the groceries really free?", "Yes. Families pay $0 for the groceries and $0 for delivery. Langar One is a 501(c)(3) charity funded by donations."),
        ("How do I get free groceries delivered?", "Fill out the Langar One request form with your name, phone number, delivery address, household size, and reason for needing help. We review each request, confirm eligibility, and then schedule deliveries to your door."),
        ("How long do the free groceries last?", "Approved families receive grocery deliveries for three months. If your situation has not improved, you can ask to renew."),
        ("Can someone request free groceries for me?", "Yes. A family member, caseworker, or partner agency can submit the request on your behalf."),
    ]
    pages.append(dict(
        path="free-groceries/", crumb="Free Groceries",
        title="Free Groceries Delivered to Your Home | Langar One",
        desc="Get free groceries delivered to your door. Langar One is a charity that delivers free food to families facing food insecurity. Request help online.",
        faq=faq,
        body=hero("Free Groceries, Delivered to Your Home",
                  "Langar One delivers free groceries to families and individuals who are struggling to afford food. There is no cost for the food or the delivery.")
        + f'''<div class="wrap section">
<div class="head"><p class="eyebrow">How to get free groceries</p><h2 class="h2">Four steps from request to doorstep</h2></div>
{steps}
</div>
<section class="white"><div class="wrap section">
<div class="head"><p class="eyebrow">What you receive</p><h2 class="h2">Free food you can cook your own way</h2>
<p class="lead">We deliver real groceries, so you can make the meals your household knows and likes.</p></div>
{RECEIVE}
</div></section>
<div class="wrap section" style="gap:20px">
<div class="head"><h2 class="h2s">Who can get free groceries</h2>
<p class="muted">Langar One serves families and individuals in the United States who are facing food insecurity. You do not need to belong to any faith or community. We review every request, and how many families we can accept depends on the donations we receive. <a href="{{R}}faq/">Read the FAQ</a> or see <a href="{{R}}locations/">where we deliver</a>. Looking for a <a href="{{R}}food-pantry-alternative/">food pantry that delivers</a>? This is how our delivery works.</p></div>
{request_cta(form)}
{NEED_NOW}
</div>
''' + qa_block(faq)))

    # ---- Food pantry delivery (kept at the /food-pantry-alternative/ address)
    faq = [
        ("Is there a food pantry that delivers to my home?", "Some food pantries and food banks run home delivery programs, and whether one covers your address depends on where you live. Call or text 211 to ask about food pantry delivery near you. Langar One is not a food pantry, but we deliver free groceries to the homes of families who cannot get to one."),
        ("How do I get food pantry delivery if I can't drive?", "Ask your local food pantry or 211 whether a delivery program serves your address. You can also send Langar One a request online. A family member, neighbor, caseworker, or meal program can fill out the request for you."),
        ("Is the delivery free?", "Yes. With Langar One, families pay $0 for the groceries and $0 for delivery. Langar One is a 501(c)(3) charity funded by donations."),
        ("How soon will groceries be delivered?", "Not the same day. Langar One reviews every request and confirms eligibility before deliveries begin, and approval depends on program capacity. If you need food today, call or text 211 or contact your local food bank."),
        ("How long do deliveries last?", "Approved families receive grocery deliveries for three months. If your situation has not improved, you can ask to renew."),
        ("Who can get groceries delivered by Langar One?", "Families and individuals in the United States who are facing food insecurity, especially people who cannot easily get to a food pantry because of age, disability, illness, childcare, or transportation. You do not need to belong to any faith or community."),
    ]
    pages.append(dict(
        path="food-pantry-alternative/", crumb="Food Pantry Delivery",
        title="Food Pantry That Delivers? Free Grocery Delivery | Langar One",
        desc="Looking for a food pantry that delivers? Langar One is a charity that brings free groceries to your door if you can't get to a food pantry. Request online.",
        faq=faq,
        body=hero("Looking for a Food Pantry That Delivers?",
                  "Langar One is not a food pantry, but we do what you are looking for. We are a charity that delivers free groceries to your door, for people who cannot easily travel, carry bags home, or wait in line.")
        + f'''<div class="wrap section">
<div class="head"><p class="eyebrow">Food pantry delivery, without the trip</p><h2 class="h2">The groceries come to you</h2>
<p class="lead">Most food pantries ask you to come to them at a set place and time. If getting there is the hard part, home delivery is what you need.</p></div>
<div class="grid g3">
<div class="rule"><h3>Delivered to your door</h3><p class="muted">There is nowhere to drive to and no line to stand in. Groceries arrive at your home.</p></div>
<div class="rule"><h3>Chosen around your household</h3><p class="muted">Fresh produce, proteins, grains, pantry staples, and dairy, selected around your dietary and cultural preferences.</p></div>
<div class="rule"><h3>Ongoing, not one time</h3><p class="muted">Approved families receive deliveries for three months, and can renew if they still need help.</p></div>
</div>
</div>
<section class="white"><div class="wrap section">
<div class="head"><p class="eyebrow">How to get groceries delivered</p><h2 class="h2">Four steps from request to doorstep</h2>
<p class="lead">You can request delivery yourself, or a family member, caseworker, or meal program can <a href="{{R}}partners/">refer you</a>.</p></div>
{steps}
</div></section>
<div class="wrap section">
<div class="head"><h2 class="h2">Who food pantry delivery helps most</h2>
<p class="lead">Delivery is for people who qualify for food help but cannot easily collect it.</p></div>
<div class="grid g3">
<div class="rule"><h3>Older adults</h3><p class="muted">People who no longer drive, or who cannot carry bags of groceries home. See <a href="{{R}}seniors/">free grocery delivery for seniors</a>.</p></div>
<div class="rule"><h3>People with a disability or illness</h3><p class="muted">Anyone for whom travelling to a pantry and waiting in line is not realistic.</p></div>
<div class="rule"><h3>Families without a car or childcare</h3><p class="muted">Parents who cannot get to a pantry during its opening hours.</p></div>
</div>
</div>
<section class="white"><div class="wrap section">
<div class="head"><h2 class="h2">Food pantries and Langar One work together</h2>
<p class="lead">A food pantry or food bank can often help the same day. Langar One takes a little longer to start, then brings regular groceries to your home.</p>
<p class="muted">If you can get to a pantry, use it. Some food banks also run their own home delivery, so it is worth asking 211 what is available where you live. If getting there is the hard part, because of age, disability, illness, childcare, or transportation, ask us for delivery.</p></div>
</div></section>
<div class="wrap section" style="gap:20px">
{request_cta(form, "Ask for free grocery delivery")}
{NEED_NOW}
<div class="head"><h2 class="h2s">Questions about food pantry delivery</h2></div>
</div>
''' + qa_block(faq) + f'''<div class="wrap section" style="gap:20px">
<p class="muted"><a href="{{R}}how-it-works/">See how Langar One works</a> · <a href="{{R}}free-groceries/">Free groceries delivered</a> · <a href="{{R}}seniors/">Free grocery delivery for seniors</a> · <a href="{{R}}locations/">Where we deliver</a></p>
</div>'''))

    # ---- Seniors
    pages.append(dict(
        path="seniors/", crumb="For Seniors",
        title="Free Grocery Delivery for Seniors | Langar One",
        desc="Free grocery delivery for seniors who can't easily shop for food. Request it yourself, or have a family member, caseworker, or meal program refer you.",
        body=hero("Free Grocery Delivery for Seniors",
                  "For older adults who find it hard to get to the store, carry groceries home, or stretch a fixed income, Langar One delivers free groceries to the door.")
        + f'''<div class="wrap section">
<div class="head"><p class="eyebrow">How it works for seniors</p><h2 class="h2">You do not have to do this alone</h2>
<p class="lead">Many of the people we serve are older adults referred by senior meal programs.</p></div>
<div class="grid g3">
<div class="rule"><h3>Request it yourself</h3><p class="muted">Fill out a short request form with your name, phone number, and address.</p></div>
<div class="rule"><h3>Have someone request for you</h3><p class="muted">A son, daughter, neighbor, or caregiver can fill out the form on your behalf.</p></div>
<div class="rule"><h3>Ask your meal program or caseworker</h3><p class="muted">Senior meal programs and agencies can refer the people they serve. <a href="{{R}}partners/">How referrals work</a>.</p></div>
</div>
</div>
<section class="white"><div class="wrap section">
<div class="head"><p class="eyebrow">What you receive</p><h2 class="h2">Groceries that fit how you cook and eat</h2></div>
{RECEIVE}
<div class="head"><h2 class="h2s">Works alongside home-delivered meals</h2>
<p class="muted">Langar One does not replace a meal program. Groceries at home add to the meals you may already receive, and can help while you are on a waiting list. Deliveries are free, and you pay nothing for the food. If you cannot get to a pantry, read about <a href="{{R}}food-pantry-alternative/">food pantry delivery</a>.</p></div>
</div></section>
<div class="wrap section" style="gap:20px">
{request_cta(form, "Request free groceries for yourself or a senior you care for")}
{NEED_NOW}
</div>'''))

    # ---- Locations hub + city pages
    cities = [
        ("los-angeles", "Los Angeles", "Los Angeles, including Hollywood, Venice, and Marina del Rey",
         "We deliver to homes across the Los Angeles area, and work with local agencies that refer the people they serve."),
        ("san-francisco", "San Francisco", "San Francisco",
         "Langar One was founded in the San Francisco Bay Area, and we deliver to homes in San Francisco."),
    ]
    links = "".join(f'<div class="card"><h2 class="h3">{name}</h2><p class="muted">Free grocery delivery in {area}.</p><a class="more" href="{slug}/">Free groceries in {name}</a></div>' for slug, name, area, _ in cities)
    pages.append(dict(
        path="locations/", crumb="Where We Deliver",
        title="Where We Deliver Free Groceries | Langar One",
        desc="See where Langar One delivers free groceries, including Los Angeles and San Francisco, and how to request help in your city.",
        body=hero("Where Langar One Delivers Free Groceries",
                  "Langar One has delivered free groceries in five states and is expanding state by state. These are the cities we deliver to today.")
        + f'''<div class="wrap section">
<div class="head"><p class="eyebrow">Cities we deliver to today</p><h2 class="h2">Free grocery delivery in your city</h2></div>
<div class="grid g3">{links}</div>
<div class="head"><h2 class="h2s">Do not see your city?</h2>
<p class="muted">Send a request anyway. We are expanding state by state, and requests tell us where the need is. We review every request, and how many families we can accept depends on the donations we receive.</p></div>
{request_cta(form)}
{NEED_NOW}
</div>'''))
    for slug, name, area, note in cities:
        pages.append(dict(
            path=f"locations/{slug}/", crumb=name, parent=("Where We Deliver", "locations/"),
            title=f"Free Grocery Delivery in {name} | Langar One",
            desc=f"Free groceries delivered to your home in {name}. Langar One is a charity serving families and seniors facing food insecurity. Request help online.",
            body=hero(f"Free Grocery Delivery in {name}",
                      f"Langar One delivers free groceries to homes in {area}. There is no cost for the food or the delivery.")
            + f'''<div class="wrap section">
<div class="head"><p class="eyebrow">How it works in {name}</p><h2 class="h2">Four steps from request to doorstep</h2>
<p class="lead">{note}</p></div>
{steps}
</div>
<section class="white"><div class="wrap section">
<div class="head"><p class="eyebrow">What you receive</p><h2 class="h2">Real groceries, delivered with dignity</h2></div>
{RECEIVE}
<div class="head"><h2 class="h2s">For agencies and caseworkers in {name}</h2>
<p class="muted">If you serve families or seniors in {name} who need food, you can refer them to Langar One at no cost. <a href="{{R}}partners/">See how referrals work</a>.</p></div>
</div></section>
<div class="wrap section" style="gap:20px">
{request_cta(form, f"Request free groceries in {name}")}
{NEED_NOW}
<p class="muted"><a href="{{R}}locations/">All locations</a> · <a href="{{R}}seniors/">Free grocery delivery for seniors</a> · <a href="{{R}}food-pantry-alternative/">Food pantry delivery</a></p>
</div>'''))

    # ---- Corporate giving
    pages.append(dict(
        path="corporate-giving/", crumb="Corporate Giving",
        title="Corporate Giving: Sponsor Families' Groceries | Langar One",
        desc="Companies can sponsor groceries for families in need, match employee donations, and host workplace food drives with Langar One, a 501(c)(3) charity.",
        body=hero("Corporate Giving: Sponsor Families' Groceries",
                  "Your company can put groceries on families' doorsteps: sponsor families, match employee gifts, or host a workplace drive.")
        + f'''<div class="wrap section">
<div class="head"><p class="eyebrow">Ways companies give</p><h2 class="h2">Simple, tangible, and easy to explain to your team</h2>
<p class="lead">It costs about $170 to deliver groceries to one family for a month, so every gift maps to families fed.</p></div>
<div class="grid g3">
<div class="rule"><h3>Sponsor families</h3><p class="muted">$170 a month sponsors one family. $1,700 a month sponsors ten. A one-time gift of $510 covers one family for a full three-month cycle.</p></div>
<div class="rule"><h3>Match employee gifts</h3><p class="muted">Add Langar One Foundation to your matching-gift program so employee donations go twice as far. Employees can <a href="{{R}}donate/">give online</a> and submit their receipt for a match.</p></div>
<div class="rule"><h3>Host a workplace drive</h3><p class="muted">Run a fundraiser or awareness event with your team. <a href="{{R}}plan-event/">Plan an event</a> and we will help you set it up.</p></div>
</div>
</div>
<section class="white"><div class="wrap section">
<div class="head"><h2 class="h2s">Details for your giving or finance team</h2>
<p class="muted"><strong>Organization:</strong> Langar One Foundation<br><strong>Status:</strong> 501(c)(3) public charity<br><strong>EIN:</strong> {EIN}<br><strong>Mailing address:</strong> 46539 Mission Blvd #1021, Fremont, CA 94539</p>
<p class="muted">Gifts from company foundations and donor-advised funds are welcome. Donations are tax-deductible to the extent allowed by law. <a href="{{R}}founders/">Meet our founders</a> or see <a href="{{R}}how-it-works/">how Langar One works</a>.</p></div>
<div class="cta"><div><h2 class="h2s">Talk to us about a company gift</h2><p>Tell us about your company and what you would like to support.</p></div>
<a class="btn btn-lg" href="mailto:info@langar.one?subject=Corporate%20giving">Email Us</a></div>
</div></section>'''))
    return pages
