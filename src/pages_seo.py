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

    # ---- Donor pages
    give_cta = lambda heading, text, label="Sponsor a Family": (
        f'<div class="cta"><div><h2 class="h2s">{heading}</h2><p>{text}</p></div>'
        f'<a class="btn btn-lg" href="{{R}}donate/#give">{label}</a></div>')
    tiles = """<div class="grid g-impact">
<div class="impact give"><b>$40</b><h3>A month</h3><p>Covers about one week of groceries for a family, every month.</p></div>
<div class="impact give"><b>$85</b><h3>A month</h3><p>Covers half of one family's groceries, every month.</p></div>
<div class="impact give"><b>$170</b><h3>A month</h3><p>Sponsors one family's grocery deliveries in full, every month.</p></div>
<div class="impact give"><b>$510</b><h3>One time</h3><p>Sponsors one family through a complete 3-month support cycle.</p></div>
</div>"""
    help_card = (f'<div class="card"><h2 class="h3">Looking for help for your own family?</h2>'
                 f'<p class="muted">Langar One delivers free groceries to families facing food insecurity. <a href="{form}" target="_blank" rel="noopener">Send us a request</a>. '
                 'We review every request, approval depends on program capacity, and we cannot deliver the same day. If you need food now, call or text <strong>211</strong>.</p></div>')

    # Sponsor a family
    faq = [
        ("How much does it cost to sponsor a family?", "It costs about $170 to deliver groceries to one family for a month. A one-time gift of $510 sponsors one family through a full three-month support cycle. Monthly gifts start at $40."),
        ("What does my sponsorship pay for?", "Groceries, delivered to a family's door: fresh produce, proteins, grains, pantry staples, and dairy, chosen around what that family eats. The family pays nothing."),
        ("Can I adopt a family for more than one month?", "Yes. A monthly gift of $170 keeps groceries arriving for one family month after month, and you can sponsor more than one family."),
        ("Will I meet the family I sponsor?", "No. To protect families' privacy, we do not share their names or details with sponsors. Your gift is used to buy and deliver groceries to families in the program."),
        ("Is my gift tax-deductible?", "Langar One Foundation is a 501(c)(3) charity, EIN 41-3146886. Donations are tax-deductible to the extent allowed by law."),
        ("Can my company or group sponsor families?", "Yes. Companies, congregations, schools, and groups of friends can sponsor one family or many. See our corporate giving page, or email info@langar.one."),
    ]
    pages.append(dict(
        path="sponsor-a-family/", crumb="Sponsor a Family",
        title="Sponsor a Family: Adopt a Family's Groceries | Langar One",
        desc="Sponsor a family in need for $170 a month. Your gift buys and delivers a family's groceries to their door. Adopt a family for a month or a full season.",
        faq=faq,
        body=hero("Sponsor a Family",
                  "Adopt a family's groceries. $170 feeds one family for a month, delivered to their door, with food they choose and know how to cook.")
        + f'''<div class="wrap section">
<div class="head"><p class="eyebrow">What it costs to feed a family</p><h2 class="h2">Pick the sponsorship that fits you</h2>
<p class="lead">Every amount maps to groceries on a real family's doorstep. Give once, or sponsor a family every month.</p></div>
{tiles}
</div>
<section class="white"><div class="wrap section">
<div class="head"><p class="eyebrow">How sponsoring a family works</p><h2 class="h2">From your gift to their kitchen</h2></div>
<div class="grid g3">
<div class="rule"><h3>1. You sponsor</h3><p class="muted">Choose an amount and give online, once or monthly. It takes about two minutes.</p></div>
<div class="rule"><h3>2. We shop and deliver</h3><p class="muted">We buy groceries selected around a family's dietary and cultural preferences and have them delivered to the family's home.</p></div>
<div class="rule"><h3>3. The family is supported for three months</h3><p class="muted">Approved families receive deliveries for three months, and can renew if the need continues. <a href="{{R}}how-it-works/">See how Langar One works</a>.</p></div>
</div>
</div></section>
<div class="wrap section">
<div class="head"><h2 class="h2">Who you are sponsoring</h2>
<p class="lead">Families and individuals who qualify for food help but cannot easily get to a store or a food pantry: older adults, people with a disability or illness, and parents without a car or childcare.</p>
<p class="muted">Many are referred to us by agencies that already care for them, such as <a href="{{R}}partners/">Meals on Wheels</a>. Langar One has made more than 2,000 grocery deliveries in five states since 2021. The idea comes from <a href="{{R}}what-is-langar/">langar</a>, the Sikh tradition of a free kitchen open to everyone.</p></div>
</div>
<div class="wrap section" style="gap:20px">
{give_cta("Sponsor a family today", "$170 feeds one family for a month. Langar One Foundation is a 501(c)(3) charity, EIN " + EIN + ".")}
<div class="head"><h2 class="h2s">Questions about sponsoring a family</h2></div>
</div>
''' + qa_block(faq) + f'''<div class="wrap section" style="gap:20px">
{help_card}
<p class="muted"><a href="{{R}}adopt-a-family-for-christmas/">Adopt a family for Christmas</a> · <a href="{{R}}donor-advised-fund/">Give through a donor-advised fund</a> · <a href="{{R}}corporate-giving/">Corporate giving</a> · <a href="{{R}}donate/">All ways to give</a></p>
</div>'''))

    # Adopt a family for Christmas
    faq = [
        ("How do I adopt a family for Christmas?", "With Langar One, you adopt a family by sponsoring their groceries. Give $170 to cover a family's groceries for a month, or $510 to cover the full three-month season, and we buy and deliver the food to their door."),
        ("Do I buy and wrap gifts?", "No. Langar One does not run a wish-list or gift program. Your gift is groceries, delivered to a family's home so they can cook their own holiday meals."),
        ("How much does it cost to sponsor a family for Christmas?", "$170 sponsors one family's groceries for a month. $510 sponsors one family for three months, through the holidays and into the new year."),
        ("Can I adopt more than one family?", "Yes. Families, workplaces, congregations, and groups of friends can sponsor several families. Email info@langar.one if you would like help planning a group gift."),
        ("How can my family get adopted for Christmas?", "Langar One does not match families with gift sponsors. If your family needs food, you can send us a request for free grocery delivery. We review every request, approval depends on program capacity, and we cannot deliver the same day. For help right now, including holiday programs near you, call or text 211."),
    ]
    pages.append(dict(
        path="adopt-a-family-for-christmas/", crumb="Adopt a Family for Christmas",
        title="Adopt a Family for Christmas: Sponsor Their Groceries | Langar One",
        desc="Adopt a family for Christmas by sponsoring their groceries. $170 fills a family's kitchen for a month, delivered to their door. No shopping or wrapping.",
        faq=faq,
        body=hero("Adopt a Family for Christmas",
                  "Sponsor a family for Christmas with the gift they will use every day: a kitchen full of groceries, delivered to their door.")
        + f'''<div class="wrap section">
<div class="head"><p class="eyebrow">A different kind of adopt-a-family</p><h2 class="h2">Give a family their holiday meals</h2>
<p class="lead">Most adopt-a-family programs ask you to shop from a wish list. Here, your gift is food: real groceries a family chooses and cooks in their own kitchen.</p></div>
<div class="grid g3">
<div class="rule"><h3>$170 covers the holiday month</h3><p class="muted">One family's groceries for a month, delivered to their home.</p></div>
<div class="rule"><h3>$510 covers the season</h3><p class="muted">Three months of groceries, through the holidays and into the new year, when help is often hardest to find.</p></div>
<div class="rule"><h3>Nothing to shop for or wrap</h3><p class="muted">Give online in about two minutes. We buy the groceries and arrange delivery.</p></div>
</div>
</div>
<section class="white"><div class="wrap section">
<div class="head"><h2 class="h2">Who your Christmas gift reaches</h2>
<p class="lead">Older adults, people with a disability or illness, and families without a car or childcare, who cannot easily get to a store or a food pantry.</p>
<p class="muted">Groceries are selected around each family's dietary and cultural preferences, so the food on the table is food they know. To protect their privacy, we do not share families' names or details with sponsors. <a href="{{R}}how-it-works/">See how Langar One works</a>.</p></div>
</div></section>
<div class="wrap section">
<div class="head"><h2 class="h2">Adopt a family as a group</h2>
<p class="lead">Offices, congregations, classrooms, and families often sponsor together. Ten people giving $17 each feed a family for a month.</p>
<p class="muted">Giving on behalf of a company? See <a href="{{R}}corporate-giving/">corporate giving</a>. Planning a fundraiser? <a href="{{R}}plan-event/">Host an event</a>.</p></div>
</div>
<div class="wrap section" style="gap:20px">
{give_cta("Adopt a family this Christmas", "$170 feeds one family for a month. Langar One Foundation is a 501(c)(3) charity, EIN " + EIN + ".", "Sponsor a Family")}
<div class="head"><h2 class="h2s">Questions about adopting a family for Christmas</h2></div>
</div>
''' + qa_block(faq) + f'''<div class="wrap section" style="gap:20px">
{help_card}
<p class="muted"><a href="{{R}}sponsor-a-family/">Sponsor a family all year</a> · <a href="{{R}}donor-advised-fund/">Give through a donor-advised fund</a> · <a href="{{R}}donate/">All ways to give</a></p>
</div>'''))

    # Donor-advised fund giving
    faq = [
        ("Can I give to Langar One from a donor-advised fund?", "Yes. Langar One Foundation is a 501(c)(3) public charity and can receive grants from donor-advised funds. Recommend a grant through your fund's sponsor using our legal name and EIN, 41-3146886."),
        ("What information does my DAF sponsor need?", "Our legal name, Langar One Foundation; our EIN, 41-3146886; and our mailing address, 46539 Mission Blvd #1021, Fremont, CA 94539."),
        ("Is there a minimum DAF grant?", "Langar One has no minimum. Your fund's sponsor may set its own minimum grant size."),
        ("Can I recommend a recurring grant?", "Many DAF sponsors let you schedule a recurring grant. $170 a month sponsors one family's groceries on an ongoing basis."),
        ("Will I get a tax receipt for a DAF grant?", "No. You received your tax deduction when you contributed to your donor-advised fund, so a grant from it is not deductible again. We will still acknowledge the grant if your sponsor shares your name with us."),
    ]
    pages.append(dict(
        path="donor-advised-fund/", crumb="Donor-Advised Fund Giving",
        title="DAF Giving: Donor-Advised Fund Grants | Langar One",
        desc="Recommend a grant to Langar One Foundation from your donor-advised fund. EIN 41-3146886. $170 feeds one family for a month; $2,040 feeds a family for a year.",
        faq=faq,
        body=hero("Give Through Your Donor-Advised Fund",
                  "A DAF grant to Langar One becomes groceries at a family's door. Here is everything your fund's sponsor will ask for.")
        + f'''<div class="wrap section">
<div class="head"><p class="eyebrow">DAF giving details</p><h2 class="h2">What to enter when you recommend a grant</h2></div>
<div class="card"><p class="muted"><strong>Organization:</strong> Langar One Foundation<br><strong>Status:</strong> 501(c)(3) public charity<br><strong>EIN:</strong> {EIN}<br><strong>Mailing address:</strong> 46539 Mission Blvd #1021, Fremont, CA 94539<br><strong>Contact:</strong> <a href="mailto:info@langar.one?subject=Donor-advised%20fund%20grant">info@langar.one</a></p></div>
</div>
<section class="white"><div class="wrap section">
<div class="head"><p class="eyebrow">How to recommend a grant</p><h2 class="h2">Three steps</h2></div>
<div class="grid g3">
<div class="rule"><h3>1. Log in to your fund</h3><p class="muted">Sign in with your DAF sponsor, such as Fidelity Charitable, DAFgiving360, Vanguard Charitable, or a community foundation.</p></div>
<div class="rule"><h3>2. Search for us</h3><p class="muted">Search for "Langar One Foundation" or EIN {EIN}, and enter the grant amount.</p></div>
<div class="rule"><h3>3. Let us know</h3><p class="muted">Sponsors do not always pass on donor names. <a href="mailto:info@langar.one?subject=Donor-advised%20fund%20grant">Email us</a> so we can thank you and tell you what your grant did.</p></div>
</div>
</div></section>
<div class="wrap section">
<div class="head"><p class="eyebrow">What a grant does</p><h2 class="h2">Every grant maps to families fed</h2>
<p class="lead">It costs about $170 to deliver groceries to one family for a month.</p></div>
<div class="grid g3">
<div class="rule"><h3>$510</h3><p class="muted">One family through a complete three-month support cycle.</p></div>
<div class="rule"><h3>$2,040</h3><p class="muted">One family's groceries for a full year.</p></div>
<div class="rule"><h3>$20,400</h3><p class="muted">Ten families' groceries for a full year.</p></div>
</div>
<p class="muted">Langar One has made more than 2,000 grocery deliveries in five states since 2021. <a href="{{R}}founders/">Meet our founders</a>, see <a href="{{R}}how-it-works/">how the program works</a>, or view our nonprofit profile on <a href="https://app.candid.org/profile/16525490/langar-one-foundation-41-3146886" target="_blank" rel="noopener">Candid</a>, where we hold a Seal of Transparency.</p>
</div>
<div class="wrap section" style="gap:20px">
<div class="cta"><div><h2 class="h2s">Talk to us about a grant</h2><p>We are glad to answer questions from donors, advisors, and foundation staff.</p></div>
<a class="btn btn-lg" href="mailto:info@langar.one?subject=Donor-advised%20fund%20grant">Email Us</a></div>
<div class="head"><h2 class="h2s">Questions about DAF giving</h2></div>
</div>
''' + qa_block(faq) + f'''<div class="wrap section" style="gap:20px">
<p class="muted"><a href="{{R}}sponsor-a-family/">Sponsor a family</a> · <a href="{{R}}corporate-giving/">Corporate giving</a> · <a href="{{R}}donate/">Give online</a></p>
</div>'''))

    # ---- Corporate giving
    corp_faq = [
        ("How can a company support Langar One?", "Companies sponsor families' groceries with a company gift, match employee donations, or host a workplace fundraiser. It costs about $170 to deliver groceries to one family for a month."),
        ("Is Langar One eligible for corporate matching gifts?", "Langar One Foundation is a 501(c)(3) public charity, EIN 41-3146886, which is what most matching-gift programs require. We are listed on Blackbaud YourCause, so employees at companies that use it can find us in their giving portal. Check your company's program for its own rules."),
        ("Can we give through our company foundation or donor-advised fund?", "Yes. Grants from company foundations and donor-advised funds are welcome. Use our legal name, Langar One Foundation, and EIN 41-3146886."),
        ("Will we get a report on what our gift did?", "Yes. Email info@langar.one and we will tell you how many families your gift fed and for how long."),
    ]
    pages.append(dict(
        path="corporate-giving/", crumb="Corporate Giving",
        title="Corporate Giving Programs: Sponsor Families' Groceries | Langar One",
        desc="Add hunger relief to your corporate giving program: sponsor families' groceries, match employee giving, or host a workplace drive with Langar One, a 501(c)(3).",
        faq=corp_faq,
        body=hero("Corporate Giving: Sponsor Families' Groceries",
                  "Your company can put groceries on families' doorsteps: sponsor families, match employee gifts, or host a workplace drive.")
        + f'''<div class="wrap section">
<div class="head"><p class="eyebrow">Ways companies give</p><h2 class="h2">Simple, tangible, and easy to explain to your team</h2>
<p class="lead">It costs about $170 to deliver groceries to one family for a month, so every gift maps to families fed.</p></div>
<div class="grid g3">
<div class="rule"><h3>Sponsor families</h3><p class="muted">$170 a month sponsors one family. $1,700 a month sponsors ten. A one-time gift of $510 covers one family for a full three-month cycle.</p></div>
<div class="rule"><h3>Match employee gifts</h3><p class="muted">Add Langar One Foundation to your matching-gift program so employee donations go twice as far. Employees can <a href="{{R}}donate/">give online</a> and submit their receipt for a match, or give through <a href="https://host.nxt.blackbaud.com/npp/nonprofits/nonprofit-public-profile/16480622?svcid=bbvn" target="_blank" rel="noopener">Blackbaud YourCause</a> where their company uses it.</p></div>
<div class="rule"><h3>Host a workplace drive</h3><p class="muted">Run a fundraiser or awareness event with your team. <a href="{{R}}plan-event/">Plan an event</a> and we will help you set it up.</p></div>
</div>
</div>
<div class="wrap section">
<div class="head"><p class="eyebrow">For your corporate giving program</p><h2 class="h2">Where Langar One fits</h2>
<p class="lead">Most corporate giving programs combine company gifts, employee giving, and volunteering. We can be part of each.</p></div>
<div class="grid g3">
<div class="rule"><h3>Company gifts and sponsorships</h3><p class="muted">A gift with a clear unit of impact: $170 feeds one family for a month, which is easy to report to leadership and staff.</p></div>
<div class="rule"><h3>Employee giving and matching gifts</h3><p class="muted">Employees give through payroll or workplace giving platforms, and your match doubles it. Langar One Foundation is listed on <a href="https://host.nxt.blackbaud.com/npp/nonprofits/nonprofit-public-profile/16480622?svcid=bbvn" target="_blank" rel="noopener">Blackbaud YourCause</a> and is eligible for giving through the Blackbaud Giving Fund. Tell us if your company uses a different platform.</p></div>
<div class="rule"><h3>Team volunteering</h3><p class="muted">Remote and skills-based roles suit distributed teams. <a href="{{R}}volunteer/">See volunteer options</a>.</p></div>
</div>
</div>
<section class="white"><div class="wrap section">
<div class="head"><h2 class="h2s">Details for your giving or finance team</h2>
<p class="muted"><strong>Organization:</strong> Langar One Foundation<br><strong>Status:</strong> 501(c)(3) public charity<br><strong>EIN:</strong> {EIN}<br><strong>Mailing address:</strong> 46539 Mission Blvd #1021, Fremont, CA 94539</p>
<p class="muted">Gifts from company foundations and donor-advised funds are welcome. Donations are tax-deductible to the extent allowed by law. <a href="{{R}}founders/">Meet our founders</a> or see <a href="{{R}}how-it-works/">how Langar One works</a>.</p></div>
<div class="cta"><div><h2 class="h2s">Talk to us about a company gift</h2><p>Tell us about your company and what you would like to support.</p></div>
<a class="btn btn-lg" href="mailto:info@langar.one?subject=Corporate%20giving">Email Us</a></div>
</div></section>
<div class="wrap section" style="gap:20px"><div class="head"><h2 class="h2s">Questions about corporate giving</h2></div></div>
''' + qa_block(corp_faq) + f'''<div class="wrap section" style="gap:20px">
<p class="muted"><a href="{{R}}sponsor-a-family/">Sponsor a family</a> · <a href="{{R}}donor-advised-fund/">Donor-advised fund giving</a> · <a href="{{R}}donate/">Give online</a></p>
</div>'''))
    return pages
