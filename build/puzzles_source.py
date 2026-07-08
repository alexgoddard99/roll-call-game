# Source-of-truth puzzle definitions for Roll Call.
# Vote answers are NOT written here — they are fetched from senate.gov roll-call XML
# by fetch.py, so every answer in the game is a verified real vote.

SENATORS = {
    # key: (bioguide, display name, party, state)
    "collins":   ("C001035", "Susan Collins", "R", "ME"),
    "bnelson":   ("N000180", "Ben Nelson", "D", "NE"),
    "sanders":   ("S000033", "Bernie Sanders", "I", "VT"),
    "mccain":    ("M000303", "John McCain", "R", "AZ"),
    "feingold":  ("F000061", "Russ Feingold", "D", "WI"),
    "clinton":   ("C001041", "Hillary Clinton", "D", "NY"),
    "chafee":    ("C001040", "Lincoln Chafee", "R", "RI"),
    "byrd":      ("B001210", "Robert Byrd", "D", "WV"),
    "kennedy":   ("K000105", "Ted Kennedy", "D", "MA"),
    "obama":     ("O000167", "Barack Obama", "D", "IL"),
    "biden":     ("B000444", "Joe Biden", "D", "DE"),
    "manchin":   ("M001183", "Joe Manchin", "D", "WV"),
    "toomey":    ("T000461", "Pat Toomey", "R", "PA"),
    "cruz":      ("C001098", "Ted Cruz", "R", "TX"),
    "warren":    ("W000817", "Elizabeth Warren", "D", "MA"),
    "kirk":      ("K000360", "Mark Kirk", "R", "IL"),
    "murkowski": ("M001153", "Lisa Murkowski", "R", "AK"),
    "rpaul":     ("P000603", "Rand Paul", "R", "KY"),
    "heitkamp":  ("H001069", "Heidi Heitkamp", "D", "ND"),
    "feinstein": ("F000062", "Dianne Feinstein", "D", "CA"),
    "helms":     ("H000463", "Jesse Helms", "R", "NC"),
}

PUZZLES = [
    {
        "id": "obama-wave",
        "title": "The Obama Wave",
        "era": "111th Congress · 2009–2010",
        "intro": ("Barack Obama arrives with a filibuster-proof majority, a financial "
                  "crisis on every desk, and an agenda the size of the New Deal. Every "
                  "big vote comes down to a handful of independent minds."),
        "senators": [
            ("collins", "A Maine moderate and one of the last New England Republicans. "
                        "She prides herself on bipartisan deal-making — she helped write "
                        "down the 2009 stimulus — but guards her independence on social issues."),
            ("bnelson", "Perhaps the most conservative Democrat in the chamber, from deep-red "
                        "Nebraska. He haggles for home-state concessions and agonizes publicly "
                        "before every big vote."),
            ("sanders", "The Senate's democratic socialist, caucusing with Democrats under his own "
                        "flag. He wants Medicare-for-all and blames Wall Street for most of America's "
                        "ills — the question is whether half-measures earn his vote."),
            ("mccain",  "Fresh off losing the presidency to Obama, the old maverick has turned "
                        "partisan brawler, opposing most of the new administration's agenda while "
                        "keeping his hawkish, reform-minded reputation."),
            ("feingold","A civil-libertarian progressive from Wisconsin who treats principle as "
                        "non-negotiable. He'll vote against his own party when a bill doesn't go "
                        "far enough, and he's famous for casting lonely no votes."),
        ],
        "bills": [
            {
                "congress": 111, "session": 1, "vote": 396,
                "name": "The Affordable Care Act",
                "desc": ("December 24, 2009, 7 a.m. — the Senate's first Christmas Eve vote in "
                         "114 years. Obama's health-care overhaul: an individual mandate to buy "
                         "insurance, subsidized exchanges, a Medicaid expansion, and a ban on "
                         "denying coverage for pre-existing conditions. After a year of town-hall "
                         "fury, Democrats need all 60 caucus votes to break the filibuster."),
            },
            {
                "congress": 111, "session": 2, "vote": 208,
                "name": "Dodd-Frank Wall Street Reform",
                "desc": ("July 2010. The answer to the financial crisis: a new consumer-protection "
                         "bureau, derivatives regulation, and authority to wind down 'too big to "
                         "fail' banks. Wall Street hates it — and some progressives say it's still "
                         "far too soft on the megabanks."),
            },
            {
                "congress": 111, "session": 2, "vote": 281,
                "name": "Repeal of Don't Ask, Don't Tell",
                "desc": ("December 2010, the lame-duck session. A standalone bill to end the "
                         "17-year ban on gay and lesbian troops serving openly, after a Pentagon "
                         "study found repeal would not harm military readiness."),
            },
        ],
    },
    {
        "id": "after-september",
        "title": "After September 11",
        "era": "107th Congress · 2001–2002",
        "intro": ("Anthrax in the mailroom, troops mobilizing, flags on every lapel. "
                  "A Senate under pressure to move fast — on surveillance, on schools, "
                  "and finally on war."),
        "senators": [
            ("feingold", "Wisconsin's civil-libertarian conscience — deeply skeptical of government "
                         "surveillance and of blank-check war powers, even when the whole country "
                         "is demanding action."),
            ("clinton",  "The former First Lady, ten months into her Senate career, representing "
                         "the state that was attacked. She is building a hawkish, centrist "
                         "national-security profile — with an eye, everyone assumes, on bigger things."),
            ("chafee",   "The Senate's most liberal Republican, an heir to Yankee moderation. He "
                         "regularly opposes his own party on taxes, the environment, and the use "
                         "of force."),
            ("byrd",     "The Senate's octogenarian institutionalist, a copy of the Constitution "
                         "in his breast pocket. He defends Congress's war powers against any "
                         "president, of either party."),
            ("kennedy",  "The liberal lion. A master legislator happy to partner with George W. "
                         "Bush on domestic causes he cares about — education above all — while "
                         "fighting him on nearly everything else."),
        ],
        "bills": [
            {
                "congress": 107, "session": 1, "vote": 313,
                "name": "The USA PATRIOT Act",
                "desc": ("October 25, 2001 — six weeks after the attacks. Sweeping new surveillance "
                         "powers: roving wiretaps, expanded FISA authority, 'sneak and peek' "
                         "searches, and government access to business records. It is moving so "
                         "fast that most senators admit they haven't read it."),
            },
            {
                "congress": 107, "session": 1, "vote": 371,
                "name": "No Child Left Behind",
                "desc": ("December 2001. Bush's signature education law: annual testing, public "
                         "school report cards, and consequences for failing schools — negotiated "
                         "hand-in-hand with leading Democrats and paired with a big increase in "
                         "federal education spending."),
            },
            {
                "congress": 107, "session": 2, "vote": 237,
                "name": "Authorization for War in Iraq",
                "desc": ("October 11, 2002, three weeks before the midterms. The resolution "
                         "authorizes the President to use the Armed Forces against Saddam "
                         "Hussein's Iraq at a time of his choosing. Intelligence about weapons "
                         "of mass destruction is everywhere. So are doubts."),
            },
        ],
    },
    {
        "id": "class-of-2008",
        "title": "The Class of 2008",
        "era": "110th Congress · 2007–2008",
        "intro": ("Five senators — four of whom want the same promotion. Watch how a "
                  "presidential campaign, and then a financial collapse, shapes a "
                  "voting record."),
        "senators": [
            ("obama",   "The freshman phenomenon, running on his early opposition to the Iraq war. "
                        "Cautious and consensus-minded on most everything else — he can't afford "
                        "a vote that reads as radical."),
            ("clinton", "The frontrunner, defending the hawkish national-security record she built "
                        "after 9/11 while a primary electorate pulls her left."),
            ("mccain",  "The Republican nominee-in-waiting: a national-security hawk and deficit "
                        "scold with a history of party apostasy he's currently trying to live down."),
            ("biden",   "Chairman of Foreign Relations, blue-collar Democrat from Delaware, "
                        "long-shot candidate running on judgment and experience."),
            ("sanders", "The freshman socialist, not running for anything — yet. Economics first, "
                        "and no patience for rescuing the people he blames for the mess."),
        ],
        "bills": [
            {
                "congress": 110, "session": 1, "vote": 42,
                "name": "Minimum Wage Increase",
                "desc": ("February 2007. The new Democratic majority's first order of business: "
                         "raising the federal minimum wage from $5.15 to $7.25 over two years, "
                         "sweetened with small-business tax breaks to bring Republicans along."),
            },
            {
                "congress": 110, "session": 1, "vote": 181,
                "name": "Iraq War Funding — No Timeline",
                "desc": ("May 24, 2007. Bush has just vetoed a war-funding bill because it "
                         "included a withdrawal timeline. This is the replacement: $95 billion "
                         "for the troops with the timeline stripped out. Anti-war groups call "
                         "voting yes a capitulation; opponents of the bill are accused of "
                         "defunding troops in the field."),
            },
            {
                "congress": 110, "session": 2, "vote": 213,
                "name": "The $700B Bank Bailout (TARP)",
                "desc": ("October 1, 2008. Lehman is dead, credit is frozen, and the Treasury "
                         "Secretary wants $700 billion to rescue the banking system. Both "
                         "presidential nominees fly back to Washington for the vote. Main Street "
                         "is furious."),
            },
        ],
    },
    {
        "id": "guns-and-borders",
        "title": "Guns & Borders",
        "era": "113th Congress · 2013",
        "intro": ("After Sandy Hook, and after an election Republicans lost badly with "
                  "Hispanic voters, the Senate attempts guns and immigration in one year — "
                  "then shuts the government down arguing about health care."),
        "senators": [
            ("manchin", "A gun-owning, coal-country Democrat from a state Obama just lost by 27 "
                        "points. He holds an NRA 'A' rating and protects his centrist brand "
                        "fiercely — but Sandy Hook shook him."),
            ("toomey",  "A former Club for Growth president — about as fiscally conservative as "
                        "they come — now representing purple Pennsylvania, which expects the "
                        "occasional pragmatic turn."),
            ("cruz",    "Three months into his first term and already the Senate's chief "
                        "insurgent. He came to Washington to fight the establishments of both "
                        "parties, not to make deals."),
            ("warren",  "The consumer-protection professor turned senator — the new "
                        "standard-bearer of the party's progressive wing."),
            ("kirk",    "A moderate, socially liberal Republican from deep-blue Illinois, "
                        "recently back from a stroke, facing voters who just backed Obama twice."),
        ],
        "bills": [
            {
                "congress": 113, "session": 1, "vote": 97,
                "name": "Manchin-Toomey Background Checks",
                "desc": ("April 17, 2013 — four months after Sandy Hook. A bipartisan compromise "
                         "extending background checks to gun shows and internet sales, far short "
                         "of an assault-weapons ban, polling near 90% support. Under the deal in "
                         "force, it needs 60 votes."),
            },
            {
                "congress": 113, "session": 1, "vote": 168,
                "name": "The Gang of Eight Immigration Bill",
                "desc": ("June 2013. Comprehensive immigration reform: a 13-year path to "
                         "citizenship for 11 million undocumented immigrants, a doubling of the "
                         "Border Patrol, 700 miles of fencing, and mandatory E-Verify."),
            },
            {
                "congress": 113, "session": 1, "vote": 219,
                "name": "Reopening the Government",
                "desc": ("October 16, 2013 — day 16 of the shutdown, hours from a debt default. "
                         "The deal reopens the government and raises the debt ceiling with "
                         "essentially nothing given to the defund-Obamacare campaign that "
                         "started it."),
            },
        ],
    },
    {
        "id": "fifty-one-forty-nine",
        "title": "Three Votes to Lose",
        "era": "115th Congress · 2017–2018",
        "intro": ("Unified Republican government and a razor-thin Senate. With almost no "
                  "margin for error, every landmark vote hangs on a handful of senators "
                  "who answer to no one."),
        "senators": [
            ("collins",   "Twenty years in, the chamber's definitive swing vote: pro-choice, "
                          "deficit-conscious, protective of Maine's rural hospitals, and "
                          "increasingly willing to buck her party's new president."),
            ("murkowski", "Alaska's senator owes her seat to a write-in campaign, not the party — "
                          "she once lost her own primary and won anyway. Energy development and "
                          "Alaska's native healthcare systems outrank party loyalty."),
            ("manchin",   "Still the reddest-state Democrat, now facing re-election in a state "
                          "Trump carried by 42 points. He votes with the President more than any "
                          "other Democrat — when he thinks West Virginia wants it."),
            ("rpaul",     "The libertarian: wants government out of health care, taxes near zero, "
                          "and deficits actually shrinking. Happily votes against Republican "
                          "bills for being insufficiently conservative."),
            ("heitkamp",  "A North Dakota Democrat holding the Senate's most endangered seat, "
                          "balancing her party's base against a state Trump won by 36. Every "
                          "vote is a re-election calculation."),
        ],
        "bills": [
            {
                "congress": 115, "session": 1, "vote": 179,
                "name": "'Skinny' Obamacare Repeal",
                "desc": ("July 28, 2017, 1:30 a.m. After full repeal has already failed, "
                         "Republicans try 'skinny repeal' — killing the individual mandate and a "
                         "few taxes — as a vehicle to keep the repeal effort alive in conference. "
                         "Leadership swears it will never become law as written. Fifty votes "
                         "will do it, and the floor is thick with rumors."),
            },
            {
                "congress": 115, "session": 1, "vote": 303,
                "name": "The Trump Tax Cuts",
                "desc": ("December 2, 2017, nearly 2 a.m. The Tax Cuts and Jobs Act: the "
                         "corporate rate slashed from 35% to 20%, individual cuts that expire "
                         "after 2025, the ACA's mandate penalty zeroed out, and roughly $1.4 "
                         "trillion added to the deficit. Handwritten amendments are still being "
                         "scribbled in the margins."),
            },
            {
                "congress": 115, "session": 2, "vote": 223,
                "name": "Confirming Brett Kavanaugh",
                "desc": ("October 6, 2018. After Christine Blasey Ford's testimony and a "
                         "supplemental FBI investigation, the Supreme Court confirmation comes "
                         "to the floor with the chamber — and the country — at a boil. A simple "
                         "majority confirms."),
                "overrides": {
                    "murkowski": ["nay",
                        "Murkowski's declared vote was No. She withdrew it and voted 'present' "
                        "as a courtesy 'live pair' with Steve Daines (R-MT), a Kavanaugh "
                        "supporter away at his daughter's wedding — old Senate custom, same "
                        "effect as a Nay."],
                },
            },
        ],
    },
    {
        "id": "clinton-years",
        "title": "November 1993",
        "era": "103rd Congress · 1993",
        "intro": ("A young President Clinton, a Democratic Congress full of Southern "
                  "conservatives, and one extraordinary week in November: trade, guns, "
                  "and crime, back to back."),
        "senators": [
            ("biden",     "Two decades in, chairman of the Judiciary Committee: a deal-making "
                          "Delaware Democrat, tough-on-crime by design and trade-friendly by "
                          "instinct."),
            ("byrd",      "The Appropriations king and guardian of West Virginia's mines and "
                          "mills. Suspicious of anything that might ship jobs overseas; devoted "
                          "to the working man as he defines him."),
            ("mccain",    "An Arizona conservative with a westerner's view of government: "
                          "pro-trade, pro-military, and as skeptical of gun laws as his voters are."),
            ("feinstein", "San Francisco's former mayor, in the Senate less than a year. She "
                          "became mayor the day a colleague was assassinated at City Hall — gun "
                          "violence is personal, and she has chosen it as her first great fight."),
            ("helms",     "'Senator No.' The hard-right anchor of the chamber: anti-communist, "
                          "protectionist where tobacco and textiles are concerned, and against "
                          "nearly anything with 'new' in the name."),
        ],
        "bills": [
            {
                "congress": 103, "session": 1, "vote": 375,
                "name": "The Assault Weapons Ban",
                "desc": ("November 17, 1993. An amendment to the crime bill banning the "
                         "manufacture of 19 named semiautomatic 'assault weapons' and "
                         "high-capacity magazines for ten years. Even many Democrats from "
                         "rural states are queasy."),
            },
            {
                "congress": 103, "session": 1, "vote": 394,
                "name": "The Brady Bill",
                "desc": ("November 20, 1993. A five-day waiting period and background check for "
                         "handgun purchases, named for Reagan's press secretary, shot and "
                         "paralyzed in 1981. The NRA has fought it for seven years straight."),
            },
            {
                "congress": 103, "session": 1, "vote": 395,
                "name": "NAFTA",
                "desc": ("Also November 20, 1993. The North American Free Trade Agreement — "
                         "negotiated by Bush, embraced by Clinton over his own party's "
                         "objections and organized labor's fury. Ross Perot says you can "
                         "already hear a 'giant sucking sound' of jobs going south."),
            },
        ],
    },
]
