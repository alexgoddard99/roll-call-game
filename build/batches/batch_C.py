# Batch C puzzles for Yea or Nay — 110th-116th Congresses, senate.gov XML.
# Vote answers are never written here; fetch.py pulls every vote from the
# official roll-call records.

SENATORS_EXTRA = {
    # key: (bioguide, display name, party, state)
    "corker":     ("C001071", "Bob Corker", "R", "TN"),
    "clevin":     ("L000261", "Carl Levin", "D", "MI"),
    "stabenow":   ("S000770", "Debbie Stabenow", "D", "MI"),
    "demint":     ("D000595", "Jim DeMint", "R", "SC"),
    "graham":     ("G000359", "Lindsey Graham", "R", "SC"),
    "snowe":      ("S000663", "Olympia Snowe", "R", "ME"),
    "landrieu":   ("L000550", "Mary Landrieu", "D", "LA"),
    "franken":    ("F000457", "Al Franken", "D", "MN"),
    "dodd":       ("D000388", "Chris Dodd", "D", "CT"),
    "inhofe":     ("I000024", "Jim Inhofe", "R", "OK"),
    "kyl":        ("K000352", "Jon Kyl", "R", "AZ"),
    "tester":     ("T000464", "Jon Tester", "D", "MT"),
    "mlee":       ("L000577", "Mike Lee", "R", "UT"),
    "gillibrand": ("G000555", "Kirsten Gillibrand", "D", "NY"),
    "ayotte":     ("A000368", "Kelly Ayotte", "R", "NH"),
    "merkley":    ("M001176", "Jeff Merkley", "D", "OR"),
    "portman":    ("P000449", "Rob Portman", "R", "OH"),
    "flake":      ("F000444", "Jeff Flake", "R", "AZ"),
    "pryor":      ("P000590", "Mark Pryor", "D", "AR"),
    "schumer":    ("S000148", "Chuck Schumer", "D", "NY"),
    "reid":       ("R000146", "Harry Reid", "D", "NV"),
    "wyden":      ("W000779", "Ron Wyden", "D", "OR"),
    "donnelly":   ("D000607", "Joe Donnelly", "D", "IN"),
    "harris":     ("H001075", "Kamala Harris", "D", "CA"),
    "king":       ("K000383", "Angus King", "I", "ME"),
}

PUZZLES = [
    {
        "id": "detroit",
        "title": "Detroit on the Brink",
        "era": "110th Congress · 2008",
        "intro": ("The year the American economy comes apart in stages: rebate checks "
                  "in winter, a housing rescue in summer — and by December, the Big "
                  "Three automakers are in Washington begging for survival money."),
        "senators": [
            ("corker",   "A freshman Republican and former Chattanooga mayor who made a fortune "
                         "in construction. Tennessee's auto jobs are at nonunion foreign plants — "
                         "and he has appointed himself lead negotiator on what Detroit must give "
                         "up in exchange for help."),
            ("clevin",   "Michigan's senior senator, three decades in and Detroit's chief defender "
                         "in Washington. The bookish Armed Services chairman rarely raises his "
                         "voice — except when someone suggests letting the auto industry fail."),
            ("mcconnell","The Republican leader, balancing a lame-duck Bush White House's rescue "
                         "requests against a conference in open revolt over bailouts. Kentucky, "
                         "as it happens, assembles Fords in Louisville."),
            ("stabenow", "Michigan's junior senator, a former state legislator who talks about "
                         "manufacturing the way others talk about religion. One in ten Michigan "
                         "jobs traces back to the auto industry, and the state's unemployment "
                         "rate leads the nation."),
            ("demint",   "South Carolina's insurgent conservative, already plotting to fund "
                         "primary challengers against squishy colleagues. His state recruited a "
                         "nonunion BMW plant — and he regards every federal rescue of a failing "
                         "company as a step toward socialism."),
        ],
        "bills": [
            {
                "congress": 110, "session": 2, "vote": 10,
                "name": "The 2008 Stimulus Checks",
                "desc": ("February 7, 2008. With the housing slump curdling into something "
                         "worse, Washington mails money: $600 rebate checks per taxpayer, "
                         "$1,200 for couples, plus business write-offs — a $152 billion package "
                         "agreed between Bush and Pelosi in record time. The Senate adds checks "
                         "for seniors and disabled veterans and hurries it to the President's "
                         "desk."),
            },
            {
                "congress": 110, "session": 2, "vote": 186,
                "name": "The Housing Rescue",
                "desc": ("July 26, 2008. Foreclosures are running at thousands a day. The "
                         "Housing and Economic Recovery Act: a Treasury lifeline for teetering "
                         "mortgage giants Fannie Mae and Freddie Mac, FHA refinancing for "
                         "400,000 underwater borrowers, and a first-time homebuyer credit. "
                         "Treasury Secretary Paulson calls his new Fannie-and-Freddie authority "
                         "a 'bazooka' he hopes never to fire."),
            },
            {
                "congress": 110, "session": 2, "vote": 215,
                "name": "The Auto Bailout",
                "desc": ("December 11, 2008. GM and Chrysler say they are weeks from running "
                         "out of cash. The House has passed $14 billion in bridge loans; in the "
                         "Senate it needs 60 votes. Late-night talks over how fast union wages "
                         "must fall to match Toyota's have just collapsed. If this fails, the "
                         "question goes to the Treasury — or to bankruptcy court."),
            },
        ],
    },
    {
        "id": "change-comes",
        "title": "Change Comes to Washington",
        "era": "111th Congress · 2009",
        "intro": ("A new president sworn in before two million people, a 58-seat "
                  "majority, and an economy in freefall. For the Senate's last "
                  "Republican moderates, every vote is now an identity crisis."),
        "senators": [
            ("specter",  "Twenty-eight years a Republican from purple Pennsylvania: pro-labor, "
                         "pro-science, an appropriator to his bones — now staring at primary "
                         "polling that reads like an obituary. He is doing arithmetic in public "
                         "about where he still belongs."),
            ("snowe",    "Maine's senior Republican, a moderate who sets up shop in the middle "
                         "of every storm. She frets about deficits and process — but she has "
                         "never met a crisis she'd rather filibuster than fix."),
            ("graham",   "South Carolina's genial hawk and John McCain's best friend, back from "
                         "a bruising campaign season. A reliable conservative on economics who "
                         "nonetheless believes elections have consequences — especially for "
                         "judicial nominations."),
            ("sanders",  "Vermont's socialist, delighted the country has finally discovered Wall "
                         "Street's failings but suspicious the cleanup is being written by the "
                         "people who caused the wreck. He wants the new administration bolder, "
                         "faster, and bigger."),
            ("bnelson",  "Nebraska's Democrat, the most conservative member of the caucus. He "
                         "convenes the moderates' back-room meetings, trims every big number he "
                         "sees, and votes his state's Republican lean whenever the spotlight "
                         "allows it."),
        ],
        "bills": [
            {
                "congress": 111, "session": 1, "vote": 64,
                "name": "The Recovery Act",
                "desc": ("February 13, 2009 — three weeks into the new presidency. The $787 "
                         "billion stimulus: infrastructure, aid to states, expanded jobless "
                         "benefits, and tax cuts, trimmed by a tiny band of moderates whose "
                         "votes are the difference between law and nothing. Exactly three "
                         "Republicans are even negotiating. Economists argue over whether it "
                         "is far too big or far too small."),
            },
            {
                "congress": 111, "session": 1, "vote": 154,
                "name": "Obama's First Budget",
                "desc": ("April 2, 2009, 11:30 p.m. The blueprint for the Obama era: a $3.5 "
                         "trillion budget with down payments on health-care reform, clean "
                         "energy, and education — and a deficit north of a trillion dollars. "
                         "Republicans call it the most expansionist plan since the Great "
                         "Society. It needs only 51 votes, which is exactly what makes it a "
                         "free vote for nervous moderates."),
            },
            {
                "congress": 111, "session": 1, "vote": 262,
                "name": "Confirming Sonia Sotomayor",
                "desc": ("August 6, 2009. The first Hispanic nominee to the Supreme Court — a "
                         "Bronx-born federal judge with 17 years on the bench, filling David "
                         "Souter's seat. Conservative groups have spent the summer on her "
                         "'wise Latina' remark; senators doing the math know the seat won't "
                         "shift the Court's balance either way."),
            },
        ],
    },
    {
        "id": "sixty-votes",
        "title": "Sixty Votes",
        "era": "111th Congress · 2009–2010",
        "intro": ("Health-care reform will need every member of the Democratic caucus — "
                  "all sixty — plus anyone else who can be persuaded. A year of "
                  "holdouts, side deals, and 1 a.m. roll calls."),
        "senators": [
            ("landrieu",  "Louisiana's Democrat, a dealmaker from an oil state that gave Obama "
                          "40 percent. She extracts a price for hard votes — critics have just "
                          "branded her Medicaid provision the 'Louisiana Purchase' — and she "
                          "never apologizes for it."),
            ("lieberman", "The independent from Connecticut, who campaigned for McCain last "
                          "fall and keeps his committee chairmanship anyway. Insurance-industry "
                          "country is his home turf, and he relishes being the sixtieth vote "
                          "everyone must court — especially while threatening to withhold it."),
            ("snowe",     "The Republican most likely to cross. She voted the health bill out "
                          "of committee in October — 'when history calls, history calls' — then "
                          "spent two months warning she was being rushed past her comfort."),
            ("franken",   "Minnesota's freshman, seated in July after an eight-month recount — "
                          "the arrival that made sixty possible. A comedy writer turned earnest "
                          "policy student, keeping his head down and his sound bites rare."),
            ("coburn",    "Oklahoma's 'Dr. No,' a practicing physician who calls the health "
                          "bill a government takeover and wields Senate procedure like a "
                          "scalpel — he once forced the clerks to read a 767-page amendment "
                          "aloud."),
        ],
        "bills": [
            {
                "congress": 111, "session": 1, "vote": 385,
                "name": "Breaking the Health-Care Filibuster",
                "desc": ("December 21, 2009, 1:08 a.m., with a blizzard outside. The first of "
                         "three cloture votes on the health-care bill — the one that decides "
                         "everything. The last holdouts have traded their votes for "
                         "concessions; Democrats need all 60 caucus members present and voting "
                         "yes against a unanimous Republican front. There is no margin for "
                         "anyone."),
            },
            {
                "congress": 111, "session": 2, "vote": 105,
                "name": "The Reconciliation Fix",
                "desc": ("March 25, 2010. Obamacare is already law; this companion bill "
                         "patches it through reconciliation — closing the Medicare drug 'donut "
                         "hole,' sweetening subsidies, stripping out the Nebraska deal, and "
                         "overhauling student lending — needing only 51 votes. After a 41-hour "
                         "amendment marathon, Republicans force one last gauntlet before it "
                         "passes."),
            },
            {
                "congress": 111, "session": 2, "vote": 229,
                "name": "Confirming Elena Kagan",
                "desc": ("August 5, 2010. The Solicitor General — a former Harvard Law dean "
                         "who has never been a judge — nominated to succeed John Paul Stevens. "
                         "Republicans press her over military recruiters at Harvard and a thin "
                         "paper trail; Democrats note she would be only the fourth woman ever "
                         "to sit on the Court. A midterm-season referendum on the "
                         "administration as much as the nominee."),
            },
        ],
    },
    {
        "id": "consumer-nation",
        "title": "Consumer Nation",
        "era": "111th Congress · 2009–2010",
        "intro": ("Between the epic fights over health care and Wall Street, the 111th "
                  "Congress quietly rewrites the rules of everyday American life: what "
                  "a credit card can charge, whom a hate-crime law protects, and what "
                  "makes it into the refrigerator."),
        "senators": [
            ("dodd",     "Chairman of the Banking Committee, thirty years in, his reputation "
                         "singed by a sweetheart-mortgage flap and Connecticut polling that has "
                         "him underwater. He is legislating like a man with nothing left to "
                         "protect."),
            ("feingold", "Wisconsin's maverick progressive, who reads every bill for "
                         "civil-liberties fine print and has no fear of voting alone. Consumer "
                         "protection is home turf; expansions of federal power over citizens "
                         "are not."),
            ("coburn",   "The Senate's obstructionist-in-chief, blocking bills by the dozen "
                         "over spending he deems wasteful. An obstetrician who attaches his pet "
                         "amendments — loaded guns in national parks, most famously — to "
                         "anything that moves."),
            ("inhofe",   "Oklahoma's other conservative, a former insurance executive and the "
                         "chamber's loudest climate skeptic. A reliable rule of thumb: if a "
                         "bill grows a federal agency, he is against it."),
            ("collins",  "Maine's methodical moderate and the ranking member overseeing "
                         "food-safety reform. She co-writes half the bipartisan bills in the "
                         "chamber and reads the fine print on the other half."),
        ],
        "bills": [
            {
                "congress": 111, "session": 1, "vote": 194,
                "name": "The Credit CARD Act",
                "desc": ("May 19, 2009. New rules for the credit-card industry: no retroactive "
                         "rate hikes on existing balances, 45 days' notice before raising "
                         "rates, curbs on penalty fees, and limits on marketing to college "
                         "students. Banks warn that free checking will die. Attached along the "
                         "way, to consumer advocates' horror: an amendment allowing loaded "
                         "guns in national parks."),
            },
            {
                "congress": 111, "session": 1, "vote": 327,
                "name": "The Matthew Shepard Hate Crimes Act",
                "desc": ("October 22, 2009. Federal hate-crimes law extended to cover sexual "
                         "orientation and gender identity — eleven years after Matthew Shepard "
                         "was beaten and left to die on a Wyoming fence. Democrats attached it "
                         "to the $680 billion defense authorization, daring opponents to vote "
                         "against troop funding to stop it."),
            },
            {
                "congress": 111, "session": 2, "vote": 257,
                "name": "The Food Safety Modernization Act",
                "desc": ("November 30, 2010. After salmonella in the peanut butter and half a "
                         "billion recalled eggs, the biggest overhaul of food-safety law since "
                         "1938: FDA power to order recalls, more frequent inspections, and "
                         "safety standards for produce. A one-man blockade held it up for "
                         "months over its $1.4 billion price tag."),
            },
        ],
    },
    {
        "id": "lame-duck-miracle",
        "title": "The Lame-Duck Miracle",
        "era": "111th Congress · December 2010",
        "intro": ("After a midterm 'shellacking,' everyone expected the 111th Congress "
                  "to limp home. Instead, three frantic December weeks produce a tax "
                  "deal, a nuclear treaty, and one heartbreak — sometimes in the same "
                  "afternoon."),
        "senators": [
            ("sanders",   "Vermont's socialist, fresh off an eight-and-a-half-hour floor speech "
                          "against the President's tax compromise — instantly dubbed a "
                          "filibuster, instantly a folk legend on the left. Compromise, he "
                          "argues, is how the rich keep winning."),
            ("lugar",     "The Republicans' elder statesman on arms control, co-author of the "
                          "program that dismantled loose Soviet warheads. Increasingly out of "
                          "step with his party's new insurgent wing — and increasingly "
                          "untroubled by it."),
            ("kyl",       "The Republican whip and the man the White House must satisfy on the "
                          "nuclear treaty. He has spent months extracting billions for "
                          "modernizing the weapons labs — and the administration still isn't "
                          "sure it has his vote."),
            ("tester",    "A flat-topped organic farmer from Big Sandy, Montana, facing "
                          "re-election in 2012 in a state swinging hard against his party. "
                          "Every vote this month gets weighed against a general election two "
                          "years out."),
            ("murkowski", "Alaska's Republican, who lost her primary to a Tea Party challenger "
                          "and then won in November anyway on write-in ballots — the first "
                          "senator to manage it since 1954. She now owes the party "
                          "establishment exactly nothing."),
        ],
        "bills": [
            {
                "congress": 111, "session": 2, "vote": 276,
                "name": "The Obama-McConnell Tax Deal",
                "desc": ("December 15, 2010. The grand bargain nobody loves: every Bush tax "
                         "cut extended two years — top earners included — in exchange for 13 "
                         "months of unemployment benefits, a payroll-tax holiday, and an "
                         "estate tax with a $5 million exemption. The left calls it "
                         "capitulation; the White House calls it the only deal on offer."),
            },
            {
                "congress": 111, "session": 2, "vote": 278,
                "name": "The DREAM Act",
                "desc": ("December 18, 2010, a Saturday morning. Cloture on the DREAM Act: "
                         "legal status for young immigrants brought to the country as children "
                         "who finish college or enlist in the military. It has majority "
                         "support and the Pentagon's blessing — what it needs is 60 votes, and "
                         "the outcome turns on a handful of red-state Democrats."),
            },
            {
                "congress": 111, "session": 2, "vote": 298,
                "name": "The New START Treaty",
                "desc": ("December 22, 2010. A U.S.–Russia treaty cutting deployed strategic "
                         "warheads to 1,550 apiece, with inspections restored after a year's "
                         "lapse. Every living Republican former secretary of state endorses "
                         "it; the party's Senate leadership does not. Ratification takes 67 "
                         "votes, and the Vice President is working the cloakroom personally."),
            },
        ],
    },
    {
        "id": "class-of-2010",
        "title": "The Class of 2010",
        "era": "112th Congress · 2011–2013",
        "intro": ("November 2010 sends a wave of new senators to a broken-down "
                  "Washington: Tea Party insurgents, red-state survivors, and an "
                  "appointee proving she belongs. Their first Congress lurches from "
                  "crisis to crisis — and ends at 2 a.m. on New Year's morning."),
        "senators": [
            ("mlee",       "Utah's constitutional originalist, who took down an 18-year "
                           "incumbent at a party convention. A former Supreme Court clerk who "
                           "tests every bill against Article I — and finds most of them "
                           "wanting."),
            ("toomey",     "The former Club for Growth president who chased Arlen Specter out "
                           "of the Republican Party. Pennsylvania expects the occasional "
                           "moderate turn; his donors expect the fiscal discipline he spent a "
                           "decade writing op-eds about."),
            ("manchin",    "West Virginia's former governor, who won Robert Byrd's old seat "
                           "after an ad in which he literally shot the cap-and-trade bill with "
                           "a rifle. He votes his state, not his caucus."),
            ("gillibrand", "Appointed to Hillary Clinton's seat as a Blue Dog from upstate, "
                           "she has sprinted leftward in statewide politics — making the 9/11 "
                           "health bill and the repeal of 'don't ask, don't tell' her calling "
                           "cards."),
            ("ayotte",     "New Hampshire's former attorney general, a Tea Party-year winner "
                           "with an establishment résumé. Hawkish on defense in a state that "
                           "hosts a Navy shipyard, and careful with a swing electorate that "
                           "watches everything."),
        ],
        "bills": [
            {
                "congress": 112, "session": 1, "vote": 230,
                "name": "The NDAA — Indefinite Detention",
                "desc": ("December 15, 2011. The $662 billion defense authorization — with new "
                         "provisions affirming that the military may detain terrorism "
                         "suspects, potentially including Americans, indefinitely and without "
                         "trial. Civil libertarians in both parties call it a betrayal of the "
                         "Bill of Rights; the White House drops its veto threat at the last "
                         "minute."),
            },
            {
                "congress": 112, "session": 2, "vote": 55,
                "name": "The JOBS Act",
                "desc": ("March 22, 2012. A rare election-year lovefest: crowdfunding "
                         "legalized, IPO paperwork slashed for 'emerging growth' companies, "
                         "and startup investing opened to small investors. Silicon Valley and "
                         "the White House are for it; securities regulators and many Democrats "
                         "warn it guts investor protections that date to the Depression."),
            },
            {
                "congress": 112, "session": 2, "vote": 251,
                "name": "The Fiscal Cliff Deal",
                "desc": ("January 1, 2013, 2 a.m. The country went over the fiscal cliff two "
                         "hours ago. The deal, cut by Joe Biden and Mitch McConnell: Bush tax "
                         "cuts made permanent below $400,000 and rates up above it — the first "
                         "income-tax rate increase Republicans have blessed in two decades — "
                         "with the sequester postponed two months."),
            },
        ],
    },
    {
        "id": "nuclear-autumn",
        "title": "The Nuclear Autumn",
        "era": "113th Congress · 2013–2014",
        "intro": ("Years of blockaded nominees come to a head on a November morning "
                  "when the Senate votes to change itself. The fallout — procedural "
                  "and political — lands on everyone, especially a Louisiana Democrat "
                  "running out of time."),
        "senators": [
            ("landrieu",  "Louisiana's three-term Democrat, chair of the Energy Committee and "
                          "the most endangered incumbent in the country. Her survival "
                          "strategy: deliver for oil and gas, loudly, and keep daylight "
                          "between herself and her party's leadership."),
            ("merkley",   "Oregon's methodical progressive and the Senate's leading crusader "
                          "for filibuster reform — he has spent five years writing white "
                          "papers on why the chamber is broken and precisely how to fix it."),
            ("collins",   "The institutionalist's institutionalist: she has never missed a "
                          "roll-call vote and believes the Senate's rules are what separate it "
                          "from the House. Changing them by brute majority strikes her as "
                          "vandalism."),
            ("manchin",   "West Virginia's Democrat, who thinks the Senate's problem is people "
                          "refusing to talk to each other, not the rulebook. Reflexively "
                          "suspicious of anything that concentrates power in either party's "
                          "leadership."),
            ("mcconnell", "The Republican leader and master of the procedural blockade. He "
                          "warns Democrats they will regret weakening the filibuster 'a lot "
                          "sooner than you think' — a prophecy he is unusually well positioned "
                          "to fulfill."),
        ],
        "bills": [
            {
                "congress": 113, "session": 1, "vote": 242,
                "name": "The Nuclear Option",
                "desc": ("November 21, 2013. After Republicans block three D.C. Circuit "
                         "nominees in a row, Harry Reid pulls the trigger. The chair has "
                         "ruled, per decades of precedent, that nominees still need 60 votes; "
                         "Reid appeals the ruling. Voting yea upholds the old 60-vote Senate. "
                         "Voting nay detonates the 'nuclear option' — letting a bare majority "
                         "confirm every nominee short of the Supreme Court."),
            },
            {
                "congress": 113, "session": 1, "vote": 281,
                "name": "The Murray-Ryan Budget",
                "desc": ("December 18, 2013. Two months after the shutdown, the two parties' "
                         "budget chairs — liberal Patty Murray and conservative Paul Ryan — "
                         "produce a modest truce: sequester cuts eased by $63 billion, paid "
                         "for with fees and federal-pension trims, no new taxes, no entitlement "
                         "changes. Its ambition is its lack of ambition: two years without a "
                         "budget crisis."),
            },
            {
                "congress": 113, "session": 2, "vote": 280,
                "name": "The Keystone XL Pipeline",
                "desc": ("November 18, 2014. Mary Landrieu, forced into a December runoff she "
                         "is losing, finally gets the vote she has demanded for years: "
                         "approval of the Keystone XL pipeline from Alberta's oil sands to the "
                         "Gulf, over the President's objections. Every Republican is aboard; "
                         "the question is whether enough Democrats will help her reach 60 and "
                         "save her seat."),
            },
        ],
    },
    {
        "id": "coming-out",
        "title": "The Coming-Out Congress",
        "era": "113th Congress · 2013–2014",
        "intro": ("In March 2013, Rob Portman becomes the first sitting Republican "
                  "senator to endorse same-sex marriage — two years after his son came "
                  "out to him. That autumn, the Senate votes on workplace "
                  "discrimination, and the ground visibly shifts."),
        "senators": [
            ("portman", "Ohio's mild-mannered budget wonk, a former U.S. trade representative "
                        "and OMB director whose announcement that his son is gay — and that he "
                        "now supports same-sex marriage — made him his party's unlikeliest "
                        "social pioneer."),
            ("baldwin", "Wisconsin's freshman and the first openly gay person ever elected to "
                        "the Senate. She has waited a whole career for votes like these — and "
                        "still campaigns as a bread-and-butter economic progressive."),
            ("flake",   "Arizona's new senator, a libertarian-leaning conservative from a "
                        "Mormon family, genial and hard to predict on social questions — he "
                        "backed a version of the gay-rights employment bill as a House member "
                        "in 2007."),
            ("mccain",  "Arizona's senior statesman, busier fighting his party's isolationists "
                        "than its culture warriors. His wife and daughter are outspoken "
                        "marriage-equality advocates; he is not — but he bristles at "
                        "discrimination all the same."),
            ("pryor",   "Arkansas's soft-spoken Democrat, a governor's son and the most "
                        "vulnerable incumbent of 2014 — running in a state Obama just lost by "
                        "24 points, where every social-issue vote is radioactive."),
        ],
        "bills": [
            {
                "congress": 113, "session": 1, "vote": 232,
                "name": "The Employment Non-Discrimination Act",
                "desc": ("November 7, 2013. A federal ban on firing workers over sexual "
                         "orientation or gender identity — first introduced in 1994, never "
                         "before passed by either chamber. Religious organizations are "
                         "exempted. In 29 states it remains legal to fire someone for being "
                         "gay, and about ten Republicans have signaled they might help make "
                         "history."),
            },
            {
                "congress": 113, "session": 2, "vote": 21,
                "name": "The 2014 Farm Bill",
                "desc": ("February 4, 2014. A five-year, $956 billion farm bill, two years "
                         "overdue: crop insurance expanded, direct payments abolished, and an "
                         "$8 billion food-stamp trim that satisfies almost nobody. Rural-state "
                         "senators of both parties call it survival; fiscal hawks call it "
                         "logrolling in its purest form."),
            },
            {
                "congress": 113, "session": 2, "vote": 354,
                "name": "The 'Cromnibus'",
                "desc": ("December 13, 2014, nearing 10 p.m. on a Saturday. A $1.1 trillion "
                         "package funding the government through September — negotiated after "
                         "the midterms, carrying riders that loosen Dodd-Frank's derivatives "
                         "rules and raise campaign-donation caps. Elizabeth Warren is in open "
                         "revolt; party leaders on both sides just want to go home."),
            },
        ],
    },
    {
        "id": "iran-summer",
        "title": "The Iran Deal Summer",
        "era": "114th Congress · 2015",
        "intro": ("A presidential campaign is starting, a nuclear deal is landing, and "
                  "the Senate spends one summer arguing about surveillance, trade, and "
                  "war — with coalitions that scramble every party line."),
        "senators": [
            ("schumer", "Brooklyn's happy warrior and heir apparent to lead Senate Democrats, "
                        "with deep ties to Wall Street and to New York's Jewish community. On "
                        "the nuclear deal, the White House needs him — and is not at all sure "
                        "it has him."),
            ("rpaul",   "Kentucky's libertarian, running for president on dismantling the "
                        "surveillance state. He has just held the floor for ten and a half "
                        "hours against the Patriot Act — and no reform bill is ever quite pure "
                        "enough for him."),
            ("warren",  "Massachusetts's progressive champion, at war with the administration "
                        "over trade — she says fast-track lets corporations write the rules in "
                        "secret — while standing behind it on diplomacy with Iran."),
            ("corker",  "Chairman of Foreign Relations, the dealmaker who wrote the law giving "
                        "Congress this vote on the Iran agreement in the first place. Deeply "
                        "skeptical of the deal; protective of the process that judges it."),
            ("collins", "Maine's moderate, a senior appropriator with a national-security "
                        "bent: wary of the NSA's loudest critics and unpersuaded by the "
                        "administration's Iran diplomacy. She reads every annex before "
                        "deciding anything."),
        ],
        "bills": [
            {
                "congress": 114, "session": 1, "vote": 201,
                "name": "The USA FREEDOM Act",
                "desc": ("June 2, 2015. The NSA's bulk collection of American phone records — "
                         "revealed by Edward Snowden — lapsed at midnight two days ago after "
                         "Rand Paul blocked an extension. The replacement leaves the records "
                         "with phone companies, searchable case-by-case with a court order. "
                         "Civil-liberties absolutists say it changes too little; the NSA's "
                         "defenders say it blinds the watchmen."),
            },
            {
                "congress": 114, "session": 1, "vote": 219,
                "name": "Trade Promotion Authority",
                "desc": ("June 24, 2015. Fast-track: for six years, trade agreements — "
                         "starting with the 12-nation Trans-Pacific Partnership — get an "
                         "up-or-down vote with no amendments and no filibuster. Obama has "
                         "fought his own party for months to get here; organized labor is "
                         "promising primary challenges for any Democrat who helps him."),
            },
            {
                "congress": 114, "session": 1, "vote": 264,
                "name": "Blocking the Iran Nuclear Deal",
                "desc": ("September 10, 2015. A resolution disapproving the Iran nuclear "
                         "agreement — sanctions relief in exchange for a decade of enrichment "
                         "limits and inspections. Voting yea advances the resolution to kill "
                         "the deal; voting nay filibusters it and lets the agreement stand. "
                         "The White House has 42 senators pledged — exactly enough — after "
                         "four Democrats defected. The pressure on both sides is enormous."),
            },
        ],
    },
    {
        "id": "the-leaders",
        "title": "The Leaders",
        "era": "114th Congress · 2015–2016",
        "intro": ("Harry Reid and Mitch McConnell have run the Senate between them for "
                  "a decade — now one is retiring and the other consolidating. Around "
                  "them, the chamber's biggest names pick their last fights of the "
                  "Obama era."),
        "senators": [
            ("reid",      "The Democratic leader, an ex-boxer from Searchlight, Nevada, "
                          "serving his final Congress. Freed from re-election, he fights on "
                          "pure instinct — and his instincts have never once included backing "
                          "down."),
            ("mcconnell", "The majority leader at last, running the chamber with a "
                          "technician's patience. His priorities: confirm judges, protect his "
                          "majority, and never take a vote that divides his conference — "
                          "unless it truly must be taken."),
            ("mlee",      "Utah's constitutional purist, the man the leaders schedule "
                          "around: he reads every bill against the Tenth Amendment and the "
                          "national debt, and no leadership favor has ever changed his "
                          "arithmetic."),
            ("warren",    "The party's self-appointed sheriff of Wall Street, wielding "
                          "hearings and floor speeches like subpoenas. Her latest target: "
                          "drug-industry provisions dressed up, as she sees it, in the "
                          "language of medical progress."),
            ("collins",   "The chamber's most reliable bipartisan and, by the rankings, its "
                          "most moderate member. If a bill gets 90 votes, odds are she helped "
                          "write the compromise that got it there."),
        ],
        "bills": [
            {
                "congress": 114, "session": 1, "vote": 165,
                "name": "Confirming Loretta Lynch",
                "desc": ("April 23, 2015. The Brooklyn federal prosecutor nominated — five "
                         "months ago — to become the first Black woman attorney general. Her "
                         "confirmation sat in limbo while the leaders feuded over an unrelated "
                         "human-trafficking bill, the longest wait for any attorney general "
                         "nominee in three decades. Even senators voting no concede she is "
                         "qualified; the question is who ends the standoff."),
            },
            {
                "congress": 114, "session": 2, "vote": 148,
                "name": "The 9/11 Lawsuits Bill (JASTA)",
                "desc": ("September 28, 2016. JASTA lets the families of 9/11 victims sue "
                         "Saudi Arabia in American courts. Obama vetoed it, warning it will "
                         "expose U.S. troops and diplomats to reciprocal lawsuits abroad — "
                         "and no president has been overridden in his eight years. Six weeks "
                         "before an election, almost no one wants to face the families. "
                         "Overriding takes two-thirds."),
            },
            {
                "congress": 114, "session": 2, "vote": 157,
                "name": "The 21st Century Cures Act",
                "desc": ("December 7, 2016. A $6.3 billion medical-research bill: cancer "
                         "'moonshot' money, opioid-crisis funding, NIH increases, and faster "
                         "FDA approvals for drugs and devices. Patient groups adore it. A "
                         "small band of progressive holdouts calls the approval provisions a "
                         "gift to the pharmaceutical lobbyists — hundreds of whom worked on "
                         "the text."),
            },
        ],
    },
    {
        "id": "the-watchers",
        "title": "The Watchers",
        "era": "114th–116th Congress · 2015–2020",
        "intro": ("Five years of votes on how much the government may see: server "
                  "logs, phone records, browsing histories. The coalitions ignore "
                  "every party label — privacy hawks of the left and right against the "
                  "security establishment of both."),
        "senators": [
            ("wyden",     "Oregon's senior Democrat and the Intelligence Committee's "
                          "designated dissenter. He asks the questions that make NSA "
                          "directors squirm — his cryptic warnings about 'secret law' predate "
                          "the Snowden leaks by years."),
            ("cotton",    "Arkansas's Army veteran and the Senate's most unapologetic "
                          "defender of the surveillance state. He would renew every expiring "
                          "authority permanently, without amendment, and says so at every "
                          "opportunity."),
            ("mlee",      "Utah's constitutional conservative, who reads the Fourth Amendment "
                          "the way he reads the rest of the founding text: literally. A "
                          "persistent negotiator for warrant requirements and reforms of the "
                          "secret surveillance court."),
            ("feinstein", "California's Democrat and longtime Intelligence Committee leader — "
                          "author of the CIA torture report, yet one of the NSA's steadiest "
                          "defenders. Security first is not a contradiction in her book; it is "
                          "the book."),
            ("warren",    "Massachusetts's progressive: no seat on the Intelligence Committee "
                          "and no deference to it either. She votes with the civil-liberties "
                          "bloc — surveillance being, in her telling, one more unaccountable "
                          "concentration of power."),
        ],
        "bills": [
            {
                "congress": 114, "session": 1, "vote": 291,
                "name": "The Cybersecurity Information Sharing Act",
                "desc": ("October 27, 2015. Months after the OPM hack exposed 21 million "
                         "security-clearance files, a bill inviting companies to share 'cyber "
                         "threat indicators' with the government — with liability protection, "
                         "and with the data flowing on to the NSA and FBI. Apple and Twitter "
                         "oppose it; the Chamber of Commerce and the intelligence agencies "
                         "want it badly."),
            },
            {
                "congress": 115, "session": 2, "vote": 12,
                "name": "FISA Section 702 Reauthorization",
                "desc": ("January 18, 2018. Six more years for the NSA's crown-jewel "
                         "authority: warrantless collection of foreigners' communications — "
                         "which also sweeps in the Americans on the other end of the line, "
                         "searchable later by the FBI. An unlikely left-right alliance "
                         "demanded warrants for those searches, and lost. Defenders call the "
                         "program the most valuable intelligence tool America has."),
            },
            {
                "congress": 116, "session": 2, "vote": 92,
                "name": "USA FREEDOM Reauthorization",
                "desc": ("May 14, 2020. Expired FISA authorities meet the post-Carter Page "
                         "moment: an inspector general found 17 errors and omissions in the "
                         "surveillance applications against the former Trump campaign aide, "
                         "scrambling the politics of the entire apparatus. The bill adds legal "
                         "safeguards — an amendment to shield browsing histories from "
                         "warrantless collection has just failed by a single vote."),
            },
        ],
    },
    {
        "id": "new-court",
        "title": "The New Court",
        "era": "115th Congress · 2017–2018",
        "intro": ("Ten Senate Democrats wake up the morning after the 2016 election "
                  "representing states Donald Trump just won. For the next two years, "
                  "every confirmation and every deregulation vote is also a survival "
                  "decision."),
        "senators": [
            ("donnelly",  "Indiana's mild-mannered Democrat, who slipped into the Senate in "
                          "2012 past a self-destructing opponent. Trump carried his state by "
                          "19 points, and Donnelly's strategy is ostentatious moderation: "
                          "pro-gun, anti-abortion, and open to the President's judges."),
            ("tester",    "Montana's flat-topped dirt farmer, missing three fingers to a "
                          "childhood meat-grinder accident and proud of the story. Trump won "
                          "his state by 20; the community banks back home hate Dodd-Frank's "
                          "paperwork, and Tester listens to his bankers."),
            ("warren",    "The resistance's field marshal on economic policy, treating every "
                          "bank-friendly bill and most Trump nominees as five-alarm fires. "
                          "Talk of 2020 follows her everywhere, and she does very little to "
                          "hush it."),
            ("collins",   "The definitive swing vote, suddenly the most powerful moderate in "
                          "Washington. She evaluates judicial nominees on qualifications "
                          "rather than ideology, she insists — and extracts her price on "
                          "everything else."),
            ("murkowski", "Alaska's independent-minded Republican, fresh off helping sink "
                          "Obamacare repeal. She answers to Alaska rather than to any leader — "
                          "on energy, on courts, and on everything in between."),
        ],
        "bills": [
            {
                "congress": 115, "session": 1, "vote": 111,
                "name": "Confirming Neil Gorsuch",
                "desc": ("April 7, 2017. The seat held open for 14 months after Antonin "
                         "Scalia's death — past Merrick Garland's ignored nomination — goes "
                         "to a Colorado appellate judge with impeccable conservative "
                         "credentials. Democrats mounted the first successful partisan "
                         "filibuster of a Court nominee in history; Republicans answered by "
                         "abolishing the filibuster for Supreme Court picks. A simple "
                         "majority now confirms."),
            },
            {
                "congress": 115, "session": 2, "vote": 54,
                "name": "Rolling Back Dodd-Frank",
                "desc": ("March 14, 2018. The biggest loosening of bank rules since the "
                         "financial crisis: the threshold for strictest federal oversight "
                         "raised from $50 billion in assets to $250 billion, with paperwork "
                         "relief for community lenders — written hand-in-hand with a dozen "
                         "red-state Democrats. Elizabeth Warren brands it the 'Bank Lobbyist "
                         "Act'; sponsors call it common sense for Main Street."),
            },
            {
                "congress": 115, "session": 2, "vote": 97,
                "name": "Saving Net Neutrality",
                "desc": ("May 16, 2018. A resolution to overturn the FCC's repeal of "
                         "net-neutrality rules — the Obama-era ban on internet providers "
                         "blocking or throttling traffic. It needs only a bare majority, "
                         "Democrats are unanimous, and the vote is engineered to put "
                         "Republicans on the record before the midterms. The House will never "
                         "take it up; everyone votes anyway."),
            },
        ],
    },
    {
        "id": "daca-day",
        "title": "Four Bills in One Day",
        "era": "115th Congress · February 2018",
        "intro": ("September 2017: the President cancels DACA and gives Congress six "
                  "months to act. February 15, 2018: deadline week arrives, and the "
                  "Senate burns through four rival immigration plans in a single "
                  "afternoon. None will reach 60 — but the roll calls tell the story."),
        "senators": [
            ("harris",  "California's freshman and former state attorney general, a national "
                        "progressive star within a year of arriving. Protecting Dreamers is "
                        "non-negotiable for her — but so is her refusal to pay what she "
                        "considers a $25 billion ransom for a border wall."),
            ("collins", "Maine's dealmaker, hosting the bipartisan 'Common Sense Coalition' "
                        "in her office — complete with a Masai talking stick to keep senators "
                        "from interrupting one another. She still believes the center can "
                        "pass things."),
            ("flake",   "Arizona's lame duck, retiring rather than face a primary he cannot "
                        "win in Trump's party. Freed from the electorate, he has made a "
                        "Dreamer fix his personal parting crusade."),
            ("cotton",  "The President's favorite immigration ally in the chamber, co-author "
                        "of a bill to cut legal immigration in half. He regards 'comprehensive "
                        "reform' as a euphemism for amnesty, and the White House framework as "
                        "the only deal on the table."),
            ("king",    "Maine's independent, a fleece-vested former governor who caucuses "
                        "with Democrats and negotiates with everyone. He co-brokered the "
                        "centrist compromise on today's ballot — the one with money for the "
                        "wall and mercy for the Dreamers."),
        ],
        "bills": [
            {
                "congress": 115, "session": 2, "vote": 33,
                "name": "The McCain-Coons Plan",
                "desc": ("February 15, 2018, 2:33 p.m. The narrowest fix on the menu: a "
                         "path to citizenship for Dreamers plus a study of border-security "
                         "needs — and not a dollar for the wall. Named in part for John "
                         "McCain, absent in Arizona battling cancer. The White House has "
                         "promised a veto of anything arriving without wall money. Cloture "
                         "requires 60 votes."),
            },
            {
                "congress": 115, "session": 2, "vote": 35,
                "name": "The Rounds-King Compromise",
                "desc": ("3:28 p.m. The centrists' grand bargain, hatched in Susan Collins's "
                         "office: citizenship for 1.8 million Dreamers, the President's full "
                         "$25 billion for border security and the wall, and limits on "
                         "sponsoring parents — but no cuts to the diversity lottery. The "
                         "Department of Homeland Security denounces it in a blistering midday "
                         "statement. It is the only plan with a real shot at 60."),
            },
            {
                "congress": 115, "session": 2, "vote": 36,
                "name": "The Grassley Bill — Trump's Four Pillars",
                "desc": ("3:49 p.m. The White House plan, carried by Chuck Grassley: "
                         "citizenship for 1.8 million Dreamers in exchange for the full wall, "
                         "an end to the diversity visa lottery, and family sponsorship cut to "
                         "spouses and minor children — the largest legal-immigration "
                         "reduction in decades. The President endorses only this bill. It "
                         "goes last, and it too needs 60."),
            },
        ],
    },
    {
        "id": "after-the-storm",
        "title": "After the Storm",
        "era": "113th–115th Congress · 2013–2017",
        "intro": ("When catastrophe strikes someone else's state, is disaster aid "
                  "basic duty or a budget-busting grab bag? Watch the storms move "
                  "around the map — from the Jersey Shore to San Juan to Houston — "
                  "and watch the answers move with them."),
        "senators": [
            ("cruz",    "Texas's constitutionalist firebrand, sworn in this month promising "
                        "to fight spending wherever he finds it. Emergency bills, he argues, "
                        "have become Christmas trees for unrelated pork — a principle that "
                        "will be tested repeatedly from here."),
            ("rubio",   "Florida's Republican, a hurricane-state senator with national "
                        "ambitions, caught between Tea Party fiscal doctrine and the "
                        "certainty that his own coastline's turn is always coming."),
            ("schumer", "New York's champion appropriator, whose city just watched the ocean "
                        "pour into its subway tunnels. He keeps a long and precise memory of "
                        "who voted for his state in its emergency — and who did not."),
            ("collins", "Maine's pragmatist, a senior appropriator who treats disaster "
                        "relief as the federal government doing its most basic job. She has "
                        "little patience for turning emergencies into budget seminars."),
            ("rpaul",   "Kentucky's libertarian deficit absolutist: every dollar of "
                        "emergency aid, he insists, should be offset by cuts somewhere else. "
                        "Debt restructuring that costs taxpayers nothing, though — that can "
                        "be a different question."),
        ],
        "bills": [
            {
                "congress": 113, "session": 1, "vote": 4,
                "name": "Superstorm Sandy Relief",
                "desc": ("January 28, 2013 — three months after Sandy drowned the Northeast, "
                         "killing more than 100 Americans and doing roughly $65 billion in "
                         "damage. A $50.5 billion aid package for New York and New Jersey, "
                         "none of it offset, after House conservatives already stalled it "
                         "once. Northeastern Republicans are livid at their own party; fiscal "
                         "hawks call parts of it pork."),
            },
            {
                "congress": 114, "session": 2, "vote": 116,
                "name": "PROMESA — The Puerto Rico Rescue",
                "desc": ("June 29, 2016. Puerto Rico owes $70 billion it cannot pay, and a "
                         "$2 billion default arrives July 1. PROMESA: no taxpayer bailout, "
                         "but a federal oversight board with power to restructure the "
                         "island's debt — and, critics note, to overrule its elected "
                         "government. Bondholders object; so do Puerto Ricans who see a "
                         "colonial junta in all but name."),
            },
            {
                "congress": 115, "session": 1, "vote": 248,
                "name": "Harvey, Irma & Maria — the Disaster Bill",
                "desc": ("October 24, 2017. After a season that flooded Houston, flattened "
                         "the Florida Keys, and left Puerto Rico's grid dark, a $36.5 "
                         "billion package: hurricane and wildfire relief, and debt "
                         "forgiveness for the drowning federal flood-insurance program. "
                         "For two senators who voted no on Sandy aid, the storms now sit "
                         "in their own backyards."),
            },
        ],
    },
    {
        "id": "longest-shutdown",
        "title": "The Longest Shutdown",
        "era": "116th Congress · 2019",
        "intro": ("Thirty-five days, 800,000 unpaid federal workers, and a $5.7 "
                  "billion wall demand nobody will blink on. On day 34, the Senate "
                  "finally votes on both parties' offers, back to back — with a "
                  "brand-new senator from Utah choosing his footing."),
        "senators": [
            ("romney",    "Three weeks into the job, the party's 2012 presidential nominee "
                          "arrived via a Washington Post op-ed scolding the President's "
                          "character. Utah elected a Republican, though — and he insists he "
                          "will vote with Trump whenever the policy warrants it."),
            ("collins",   "Maine's institutionalist, the loudest Republican voice for "
                          "reopening the government first and arguing about the wall second. "
                          "She has been rallying colleagues to sign bipartisan letters; "
                          "letters have not worked."),
            ("manchin",   "West Virginia's Democrat, fresh off surviving 2018 in a state "
                          "Trump carried by 42 points. Federal workers — prison guards, TSA "
                          "screeners — are a bigger constituency for him than either party's "
                          "base, and he has voted for wall money before."),
            ("cruz",      "Texas's border hawk, all-in on the President's demand. He blames "
                          "Democrats for holding paychecks hostage to deny Trump a win — and "
                          "has proposed paying for the wall with El Chapo's seized drug "
                          "fortune."),
            ("murkowski", "Alaska's independent Republican, with thousands of federal workers "
                          "at home and a long list of frozen services. She has said publicly "
                          "that shutting the government down was a mistake; the question is "
                          "what she will do about it."),
        ],
        "bills": [
            {
                "congress": 116, "session": 1, "vote": 9,
                "name": "The President's Offer",
                "desc": ("January 24, 2019 — day 34. The White House package: $5.7 billion "
                         "for the wall, three years of protection for DACA recipients and "
                         "TPS holders, asylum changes — and the government reopened. "
                         "Democrats call the immigration relief a hostage payment that "
                         "recycles protections the President himself canceled. Sixty votes "
                         "needed."),
            },
            {
                "congress": 116, "session": 1, "vote": 10,
                "name": "The Democrats' Offer",
                "desc": ("Minutes later: the Democratic alternative, already passed by the "
                         "House — reopen the government through February 8 with disaster aid "
                         "attached, no wall money, and negotiate border security afterward. "
                         "It is essentially the bill the Senate approved without objection in "
                         "December, before the President changed his mind. Sixty votes "
                         "needed, and all eyes on Republican defectors."),
            },
            {
                "congress": 116, "session": 1, "vote": 26,
                "name": "The Deal That Ended It",
                "desc": ("February 14, 2019. Three weeks after the shutdown ended in a "
                         "temporary truce, the conference committee's verdict: $1.375 billion "
                         "for 55 miles of border fencing — less than the Senate offered the "
                         "President in December — plus full-year funding for nine "
                         "departments. He will sign it, then declare a national emergency to "
                         "build more. Nobody calls it victory."),
            },
        ],
    },
]
