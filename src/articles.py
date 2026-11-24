"""Stories and updates: short articles, listed at /stories/.

Each article is a dict: slug, title (H1), seo (title tag), desc, date (ISO), lead, summary (for the index card), body.
In body text, {R} is the path back to the site root and {FORM} is the grocery request form.
Bodies are a list of (heading, html) sections.
"""
import datetime, os

SITE = "https://www.langar.one"

_ALL = [
    dict(
        slug="langar-vs-food-pantry",
        title="Langar vs. Food Pantry: What's the Difference?",
        seo="Langar vs. Food Pantry: What's the Difference? | Langar One",
        desc="A langar serves a free meal to anyone who walks in. A food pantry gives out groceries to take home. Here is how they differ, and where Langar One fits.",
        date="2026-11-28",
        lead="Both feed people for free. A langar serves a cooked meal to anyone who walks in. A food pantry gives out groceries to take home. Here is how they compare, and where Langar One fits.",
        summary="A langar serves a free meal to everyone. A food pantry gives out groceries. How the two compare, and where Langar One fits.",
        body=[
            ("What a langar is",
             "<p>A langar is the free community kitchen found in every gurdwara, the Sikh place of worship. Volunteers cook a vegetarian meal and serve it to whoever comes. People of every faith, background, and income sit together and eat the same food.</p>"
             "<p>There is no sign-up, no proof of need, and no cost. A langar does not ask whether you are hungry enough to qualify. It simply feeds you. <a href=\"{R}what-is-langar/\">Read more about what langar is</a>.</p>"),
            ("What a food pantry is",
             "<p>A food pantry gives groceries directly to people who need them, usually at a set place and time. Most pantries are supplied by a regional food bank, which collects and stores food in bulk and distributes it to pantries, shelters, and meal programs.</p>"
             "<p>Rules vary from pantry to pantry. Some ask for an ID or proof of address, some limit how often you can visit, and many are open only on certain days. What you take home depends on what was donated that week.</p>"),
            ("The main differences",
             "<p><strong>Meal or groceries.</strong> A langar serves a hot meal you eat there. A pantry gives you food to cook at home.</p>"
             "<p><strong>Who it is for.</strong> A langar is open to everyone, whether or not they are in need. A pantry is set up for people who are short on food.</p>"
             "<p><strong>How you get it.</strong> For both, you have to get there. That is easy for some people and very hard for others.</p>"),
            ("Where Langar One fits",
             "<p>Langar One takes the spirit of langar, feeding people with dignity and without distinction, and applies it to groceries. We are not a food pantry and we do not run a kitchen. We deliver free groceries to the homes of families facing food insecurity.</p>"
             "<p>That matters most for people who cannot easily get to a pantry or a shared meal: older adults, people with a disability or illness, parents without childcare, and families without a car. Groceries are selected around each family's dietary and cultural preferences, and approved families receive deliveries for three months, which can be renewed.</p>"
             "<p>If you can reach a food pantry, use it. Pantries can often help the same day. If getting there is the hard part, <a href=\"{R}food-pantry-alternative/\">ask us about delivery</a>.</p>"),
        ],
    ),
    dict(
        slug="how-to-get-free-groceries-delivered",
        title="How to Get Free Groceries Delivered to Your Home",
        seo="How to Get Free Groceries Delivered to Your Home | Langar One",
        desc="Five ways to get free or low-cost groceries delivered: charity grocery delivery, food banks, 211, home-delivered meals for seniors, and SNAP online ordering.",
        date="2026-11-21",
        lead="If you cannot get to a store or a food pantry, there are still ways to get food to your door. Here are five places to start.",
        summary="Five places to start if you need food and cannot get to a store or a food pantry.",
        body=[
            ("1. Request free grocery delivery from Langar One",
             "<p>Langar One is a charity that delivers free groceries to families and individuals facing food insecurity. You pay nothing for the food or the delivery.</p>"
             "<p>To ask for help, <a href=\"{FORM}\" target=\"_blank\" rel=\"noopener\">fill out the request form</a> with your name, phone number, delivery address, household size, and the reason you need help. We review every request. Approved families receive groceries for three months and can ask to renew. How many families we can accept depends on the donations we receive, so apply even if you are also trying the options below. <a href=\"{R}how-it-works/\">See how it works</a>.</p>"),
            ("2. Call or text 211",
             "<p>211 is a free, confidential service that connects people to local help, including food. Call or text <strong>211</strong>, or visit <a href=\"https://www.211.org/\" target=\"_blank\" rel=\"noopener\">211.org</a>, and ask which food programs near you deliver. This is the fastest way to find out what exists in your area.</p>"),
            ("3. Ask your local food bank about delivery",
             "<p>Food banks supply the pantries in your area, and some pantries deliver to people who are homebound. Use Feeding America's <a href=\"https://www.feedingamerica.org/find-your-local-foodbank\" target=\"_blank\" rel=\"noopener\">food bank finder</a>, then call and ask two questions: do you deliver, and can someone pick up food on my behalf? Many pantries allow a friend or relative to collect food for you. More on this: <a href=\"{R}food-pantry-alternative/\">looking for a food pantry that delivers</a>.</p>"),
            ("4. If you are an older adult, look into home-delivered meals",
             "<p>Programs such as Meals on Wheels bring prepared meals to older adults at home. The Eldercare Locator, a public service of the U.S. Administration for Community Living, can point you to the meal programs and aging services near you. Call <strong>1-800-677-1116</strong> or visit <a href=\"https://eldercare.acl.gov/\" target=\"_blank\" rel=\"noopener\">eldercare.acl.gov</a>.</p>"
             "<p>Meals and groceries work well together. See <a href=\"{R}seniors/\">free grocery delivery for seniors</a>.</p>"),
            ("5. If you receive SNAP, order groceries online",
             "<p>SNAP benefits can be used to buy groceries online from participating stores in all 50 states and Washington, D.C. The USDA keeps a <a href=\"https://www.fns.usda.gov/snap/online\" target=\"_blank\" rel=\"noopener\">list of stores by state</a>.</p>"
             "<p>One thing to know: SNAP pays for the food only. It cannot be used for delivery or service fees, so you will need another way to pay those. Some stores waive the delivery fee above a minimum order or offer free pickup.</p>"),
            ("If you need food today",
             "<p>Langar One cannot deliver the same day. If you need food right now, start with 211 or your local food bank, then send us a request so that regular groceries can follow.</p>"),
        ],
    ),
    dict(
        slug="free-groceries-for-an-aging-parent",
        title="How to Get Free Groceries for an Aging Parent or Neighbor",
        seo="How to Get Free Groceries for an Aging Parent or Neighbor | Langar One",
        desc="You can request free grocery delivery on behalf of a parent, relative, or neighbor. Here is what to have ready, what to expect, and other help for older adults.",
        date="2026-12-05",
        lead="Many older adults will not ask for help with food, even when the fridge is close to empty. You can ask for them. Here is how.",
        summary="You can request free grocery delivery on someone else's behalf. What to have ready and what to expect.",
        body=[
            ("You can request groceries on someone's behalf",
             "<p>Langar One's request form can be filled out by a son, daughter, relative, neighbor, caregiver, or caseworker. The form asks whether you are requesting for yourself or for someone else. Groceries go to their home, and they pay nothing for the food or the delivery.</p>"),
            ("Talk to them first",
             "<p>Ask before you apply. People are more comfortable accepting help they agreed to, and we will need to reach them to arrange deliveries. It can help to explain that this is not a handout line: groceries come quietly to the door, and they cook what they like.</p>"),
            ("What to have ready",
             "<p>The form takes a few minutes. Have these on hand:</p>"
             "<p>Their name and the best phone number to reach them.<br>The delivery address.<br>How many people live in the home.<br>Why they need help with food.<br>Any allergies or dietary restrictions.<br>Delivery instructions, such as a gate code or which door to use.</p>"
             "<p><a href=\"{FORM}\" target=\"_blank\" rel=\"noopener\">Open the request form</a>.</p>"),
            ("What happens next",
             "<p>We review every request and confirm eligibility. Approval depends on program capacity, which is set by the donations we receive. Approved families receive grocery deliveries for three months, and can ask to renew if the need continues. <a href=\"{R}how-it-works/\">See the four steps</a>.</p>"),
            ("Other help worth knowing about",
             "<p><strong>Home-delivered meals.</strong> Programs such as Meals on Wheels bring prepared meals to older adults. Groceries from Langar One can add to those meals, and can help during a waiting list.</p>"
             "<p><strong>The Eldercare Locator.</strong> This public service of the U.S. Administration for Community Living connects older adults and caregivers to local meals, transportation, and home care. Call <strong>1-800-677-1116</strong> or visit <a href=\"https://eldercare.acl.gov/\" target=\"_blank\" rel=\"noopener\">eldercare.acl.gov</a>.</p>"
             "<p><strong>211.</strong> Call or text 211 for food available today near their home.</p>"
             "<p>If you work for an agency that serves older adults, you can refer the people you serve at no cost. <a href=\"{R}partners/\">See how referrals work</a>, or read more about <a href=\"{R}seniors/\">free grocery delivery for seniors</a>.</p>"),
        ],
    ),
    dict(
        slug="why-we-deliver-groceries-not-meals",
        title="Why We Deliver Groceries, Not Meals",
        seo="Why We Deliver Groceries, Not Meals | Langar One",
        desc="Langar One is inspired by a tradition of shared meals, yet we deliver groceries. Here is why: choice, dignity, food that fits each family, and reach.",
        date="2026-12-19",
        lead="Langar One is named for a tradition built around a shared, cooked meal. So why do we deliver bags of groceries instead?",
        summary="Langar is a tradition of shared meals. Here is why Langar One delivers groceries to the door instead.",
        body=[
            ("Families know what they need",
             "<p>A prepared meal is one dinner, decided by someone else. A bag of groceries is a week of decisions made by the family: what to cook, when to eat, and what the children will actually finish. We would rather hand over the ingredients and trust the person in their own kitchen.</p>"),
            ("Food is personal",
             "<p>What counts as a proper meal depends on where you grew up, what you believe, and what your body can handle. Groceries let us fit each family. We select them around dietary and cultural preferences, so a family receives food it recognizes and will use, not a standard box.</p>"),
            ("The doorstep reaches people a kitchen cannot",
             "<p>A community meal works for people who can get to it. Many of the people we serve cannot: older adults, people managing an illness or disability, parents without childcare, and families without a car. Delivery removes the trip, the line, and the need to carry bags home.</p>"),
            ("It works alongside meal programs",
             "<p>We are not a replacement for home-delivered meals or food pantries. Groceries add to the meals someone may already receive, and several of the agencies that refer people to us run meal programs themselves. <a href=\"{R}partners/\">See who we work with</a>.</p>"),
            ("It is easy to see where a gift goes",
             "<p>It costs about $170 to deliver groceries to one family for a month, which is under $6 a day. Donors can see what their gift becomes: food in a family's kitchen. <a href=\"{R}donate/\">Sponsor a family's groceries</a>.</p>"),
            ("The same idea, carried to the door",
             "<p>In a langar, everyone is welcome and everyone eats the same food, side by side. We cannot seat families together across the country. We can keep the part that matters most: nobody has to prove they deserve to eat, and everyone is served with dignity. <a href=\"{R}what-is-langar/\">Learn what langar is</a>.</p>"),
        ],
    ),
    dict(
        slug="history-of-langar",
        title="The History of Langar: 500 Years of Feeding Everyone",
        seo="The History of Langar: 500 Years of Free Community Kitchens | Langar One",
        desc="The history of langar, the Sikh free community kitchen: from Guru Nanak in the 1500s to gurdwaras that serve free meals to everyone around the world today.",
        date="2026-12-12",
        lead="Langar, the Sikh free community kitchen, has served free meals to anyone who comes for more than five centuries. This is a short history of how it began and why it has lasted.",
        summary="How the Sikh free community kitchen began with Guru Nanak and grew into a tradition practiced around the world.",
        body=[
            ("It began with Guru Nanak",
             "<p>Langar goes back to Guru Nanak (1469 to 1539), the founder of Sikhism. He taught that all people are equal, and that honest work and sharing what you earn are part of a good life. A shared meal, open to all, put that teaching into practice.</p>"
             "<p>In the society of his time, who you could eat with was decided by caste and religion. Asking everyone to sit together and eat the same food was a quiet and radical act.</p>"),
            ("Mata Khivi and the early kitchen",
             "<p>Under the second Guru, Guru Angad, the langar was run by his wife, Mata Khivi. She is remembered for her generosity and for the quality of the food she served, and she is praised by name in the Guru Granth Sahib, the Sikh scripture.</p>"),
            ("First eat together, then meet together",
             "<p>The third Guru, Guru Amar Das, made langar a lasting institution. He is associated with the rule <em>pehle pangat, pichhe sangat</em>: first sit and eat together, then join the congregation. Anyone who wished to see him ate in the langar first.</p>"
             "<p>Sikh tradition holds that this applied even to the Mughal emperor Akbar, who sat on the floor and ate alongside everyone else before meeting the Guru.</p>"),
            ("How a langar works",
             "<p>Three ideas shape every langar. <em>Seva</em> means selfless service: the cooking, serving, and washing up are done by volunteers. <em>Pangat</em> means sitting in rows, side by side, with no one placed above anyone else. And the meal is vegetarian, so that people of nearly any faith or diet can eat it.</p>"
             "<p>The food is paid for by donations from the community, and it is always free.</p>"),
            ("Langar today",
             "<p>Today, gurdwaras around the world serve langar. The kitchen at the Golden Temple in Amritsar, India, is often described as one of the largest free kitchens in the world, feeding tens of thousands of people every day.</p>"
             "<p>Sikh communities have also carried langar outside the gurdwara, serving free meals after natural disasters and to people in need in their own cities.</p>"),
            ("Where Langar One comes in",
             "<p>Langar One was founded in 2021, during COVID, to carry the same idea to the doorstep. We deliver free groceries to families facing food insecurity, whatever their faith or background. <a href=\"{R}what-is-langar/\">Read our short guide to langar</a>, <a href=\"{R}how-it-works/\">see how Langar One works</a>, or <a href=\"{R}donate/\">sponsor a family's groceries</a>.</p>"),
        ],
    ),
]


def _nice(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.strftime('%B')} {d.day}, {d.year}"


def story_pages(form):
    """Return page dicts (same shape as pages_seo) for the index and each article.

    An article goes live on its date: the build skips any dated in the future, newest first on the index.
    Set PUBLISH_ALL=1 to preview everything.
    """
    today = datetime.date.today().isoformat()
    ARTICLES = sorted((a for a in _ALL if os.environ.get("PUBLISH_ALL") or a["date"] <= today), key=lambda a: a["date"], reverse=True)
    pages = []
    cards = "".join(
        f'<div class="card"><p class="eyebrow">{_nice(a["date"])}</p><h2 class="h3"><a href="{a["slug"]}/">{a["title"]}</a></h2>'
        f'<p class="muted">{a["summary"]}</p><a class="more" href="{a["slug"]}/" aria-label="Read: {a["title"]}">Read the article</a></div>'
        for a in ARTICLES)
    pages.append(dict(
        path="stories/", crumb="Stories",
        title="Stories &amp; Updates: Langar, Free Groceries, and Food Help | Langar One",
        desc="Articles from Langar One on the langar tradition, how to get free groceries delivered, helping older adults find food, and why we deliver groceries.",
        body='<section class="page-hero"><div class="wrap"><h1>Stories &amp; Updates</h1>\n'
             '<p>Short reads on langar, getting free groceries, and how Langar One works.</p></div></section>\n'
             f'<div class="wrap section"><div class="grid g3">{cards}</div></div>',
        ld={"@context": "https://schema.org", "@type": "Blog", "name": "Langar One Stories & Updates", "url": f"{SITE}/stories/",
            "publisher": {"@type": "NGO", "name": "Langar One", "url": f"{SITE}/"},
            "blogPost": [{"@type": "BlogPosting", "headline": a["title"], "url": f"{SITE}/stories/{a['slug']}/", "datePublished": a["date"]} for a in ARTICLES]}))
    for i, a in enumerate(ARTICLES):
        sections = "".join(f"<section><h2>{h}</h2>{html}</section>" for h, html in a["body"]).replace("{FORM}", form)
        others = [o for o in ARTICLES if o is not a]
        more = "".join(f'<a href="../{o["slug"]}/">{o["title"]}</a><br>' for o in others[:3])
        path = f"stories/{a['slug']}/"
        pages.append(dict(
            path=path, crumb=a["title"], parent=("Stories", "stories/"),
            title=a["seo"], desc=a["desc"], date=a["date"],
            body=f'<section class="page-hero"><div class="wrap"><p class="post-date">{_nice(a["date"])} · Langar One</p><h1 class="post-title">{a["title"]}</h1>\n'
                 f'<p>{a["lead"]}</p></div></section>\n'
                 f'<article class="faq article post">{sections}'
                 f'<section><h3>Keep reading</h3><p>{more}<a href="../">All stories and updates</a></p></section></article>\n'
                 '<div class="wrap section" style="gap:20px;padding-top:0">'
                 f'<div class="cta"><div><h2 class="h2s">Need groceries, or know someone who does?</h2><p>Requests take a few minutes and cost families $0. Every request is reviewed, and approval depends on program capacity.</p></div>'
                 f'<a class="btn btn-lg" href="{form}" target="_blank" rel="noopener">Request Help</a></div></div>',
            ld={"@context": "https://schema.org", "@type": "BlogPosting", "headline": a["title"], "description": a["desc"],
                "datePublished": a["date"], "dateModified": a["date"], "inLanguage": "en-US",
                "mainEntityOfPage": f"{SITE}/{path}", "image": f"{SITE}/assets/og.png",
                "author": {"@type": "Organization", "name": "Langar One", "url": f"{SITE}/"},
                "publisher": {"@type": "NGO", "name": "Langar One", "url": f"{SITE}/",
                              "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/logo.png"}}}))
    return pages
