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
    "gore":      ("G000321", "Al Gore", "D", "TN"),
    "nunn":      ("N000171", "Sam Nunn", "D", "GA"),
    "dole":      ("D000401", "Bob Dole", "R", "KS"),
    "kerry":     ("K000148", "John Kerry", "D", "MA"),
    "kassebaum": ("K000017", "Nancy Kassebaum", "R", "KS"),
    "moynihan":  ("M001054", "Daniel Patrick Moynihan", "D", "NY"),
    "wellstone": ("W000288", "Paul Wellstone", "D", "MN"),
    "gramm":     ("G000365", "Phil Gramm", "R", "TX"),
    "lugar":     ("L000504", "Richard Lugar", "R", "IN"),
    "boxer":     ("B000711", "Barbara Boxer", "D", "CA"),
    "lieberman": ("L000304", "Joe Lieberman", "D", "CT"),
    "santorum":  ("S000059", "Rick Santorum", "R", "PA"),
    "daschle":   ("D000064", "Tom Daschle", "D", "SD"),
    "specter":   ("S000709", "Arlen Specter", "R", "PA"),
    "zmiller":   ("M001141", "Zell Miller", "D", "GA"),
    "coburn":    ("C000560", "Tom Coburn", "R", "OK"),
    "mcconnell": ("M000355", "Mitch McConnell", "R", "KY"),
    "rubio":     ("R000595", "Marco Rubio", "R", "FL"),
    "sbrown":    ("B001268", "Scott Brown", "R", "MA"),
    "mccaskill": ("M001170", "Claire McCaskill", "D", "MO"),
    "romney":    ("R000615", "Mitt Romney", "R", "UT"),
    "sinema":    ("S001191", "Kyrsten Sinema", "D", "AZ"),
    "warnock":   ("W000790", "Raphael Warnock", "D", "GA"),
    "cotton":    ("C001095", "Tom Cotton", "R", "AR"),
    "baldwin":   ("B001230", "Tammy Baldwin", "D", "WI"),
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
    {
        "id": "line-in-the-sand",
        "title": "Line in the Sand",
        "era": "102nd Congress · 1991",
        "intro": ("Half a million American troops sit in the Saudi desert while Congress "
                  "holds its first real war debate since Vietnam. Nine months later, a "
                  "Supreme Court nomination ends in the most explosive hearings ever held."),
        "senators": [
            ("gore",      "A cerebral Tennessee moderate with presidential ambitions and a "
                          "hawkish streak rare in his party's rising generation. He agonizes "
                          "over big votes — and enjoys telling you so."),
            ("nunn",      "Chairman of Armed Services and the Democrats' most trusted voice on "
                          "the military. A Georgia conservative — but a believer that sanctions "
                          "and patience can win wars cheaper than blood."),
            ("dole",      "The Republican leader: a wounded World War II veteran, sharp-tongued "
                          "dealmaker, and reliable soldier for the Bush White House."),
            ("kerry",     "A decorated Vietnam veteran who came home to protest the war. Two "
                          "decades later, deeply wary of committing American troops before "
                          "every alternative is exhausted."),
            ("kassebaum", "A plainspoken Kansas internationalist, budget-minded and "
                          "independent — one of only two women in the chamber."),
        ],
        "bills": [
            {
                "congress": 102, "session": 1, "vote": 2,
                "name": "Authorizing the Gulf War",
                "desc": ("January 12, 1991. Saddam Hussein has occupied Kuwait for five "
                         "months, and the UN deadline expires in three days. The resolution "
                         "authorizes the President to drive Iraq out by force. The debate is "
                         "somber and the outcome genuinely in doubt — the closest vote to "
                         "authorize war in American history."),
            },
            {
                "congress": 102, "session": 1, "vote": 220,
                "name": "Confirming Clarence Thomas",
                "desc": ("October 15, 1991. Clarence Thomas's Supreme Court nomination "
                         "reaches the floor days after Anita Hill's testimony transfixed the "
                         "country. He would fill Thurgood Marshall's seat — and shift the "
                         "Court for a generation."),
            },
            {
                "congress": 102, "session": 1, "vote": 238,
                "name": "The Civil Rights Act of 1991",
                "desc": ("October 30, 1991. After two years of veto fights over 'quotas,' a "
                         "compromise civil-rights bill restoring workers' power to sue for "
                         "discrimination — finally pre-cleared with the White House."),
            },
        ],
    },
    {
        "id": "republican-revolution",
        "title": "The Republican Revolution",
        "era": "104th Congress · 1996",
        "intro": ("Two years after Gingrich's landslide, a Democratic president runs toward "
                  "the center with an election looming. Welfare, marriage, wages — 1996 is "
                  "one long argument about what the parties are for."),
        "senators": [
            ("moynihan", "The Senate's scholar — a Harvard sociologist who wrote the book on "
                         "poverty policy, literally. Party loyalty means little when he "
                         "believes a bill will hurt the poor."),
            ("lieberman","A moralist Connecticut Democrat comfortable scolding his own party: "
                         "pro-business, hawkish, and outspoken about family values."),
            ("boxer",    "A Marin County liberal and one of the chamber's most reliable "
                         "progressive votes, especially where civil rights are concerned."),
            ("santorum", "The youngest Republican senator: a combative Pennsylvania culture "
                         "warrior who courts blue-collar Catholics with the occasional "
                         "populist economic vote."),
            ("gramm",    "A Texas economics professor turned budget hawk, fresh off a "
                         "presidential run about slashing government. If a bill spends money "
                         "or regulates business, count him out."),
        ],
        "bills": [
            {
                "congress": 104, "session": 2, "vote": 262,
                "name": "Welfare Reform",
                "desc": ("August 1, 1996. 'The end of welfare as we know it': time limits, "
                         "work requirements, and block grants replacing a six-decade federal "
                         "guarantee for poor families. Clinton has vetoed two versions and "
                         "promised to sign this one. Half his party feels betrayed."),
            },
            {
                "congress": 104, "session": 2, "vote": 280,
                "name": "The Defense of Marriage Act",
                "desc": ("September 10, 1996. DOMA: no federal recognition of same-sex "
                         "marriages, and no state required to honor another state's. Clinton "
                         "says he'll sign it. Only a handful of senators are willing to be "
                         "counted against it."),
            },
            {
                "congress": 104, "session": 2, "vote": 186,
                "name": "Minimum Wage Increase",
                "desc": ("July 9, 1996. A 90-cent raise in the minimum wage — $4.25 to $5.15 "
                         "— riding on a package of small-business tax breaks. Election-year "
                         "pressure has cracked the Republican leadership's resistance."),
            },
        ],
    },
    {
        "id": "america-and-the-world",
        "title": "America & the World",
        "era": "105th–106th Congress · 1997–2000",
        "intro": ("With the Cold War won, Washington argues about what comes next: "
                  "disarmament treaties, an expanding NATO, and whether to bet the future "
                  "on trade with China."),
        "senators": [
            ("helms",     "Chairman of Foreign Relations and scourge of the striped-pants "
                          "set. Treaties, foreign aid, the UN — he distrusts them all, and "
                          "buries what he distrusts."),
            ("lugar",     "The Republicans' soft-spoken foreign-policy intellectual, "
                          "co-author of the program dismantling loose Soviet nukes. An "
                          "internationalist to his fingertips."),
            ("moynihan",  "The Senate's contrarian scholar — a former UN ambassador with his "
                          "own theories about secrecy, ethnicity, and international law, "
                          "cheerfully immune to conventional wisdom."),
            ("wellstone", "The happiest warrior of the left: a former wrestling coach and "
                          "campus organizer who votes his conscience on labor and human "
                          "rights, popularity be damned."),
            ("biden",     "The Democrats' garrulous front man on Foreign Relations — an "
                          "institutionalist who believes in American alliances and American "
                          "engagement, almost anywhere."),
        ],
        "bills": [
            {
                "congress": 105, "session": 1, "vote": 51,
                "name": "The Chemical Weapons Treaty",
                "desc": ("April 24, 1997. The Chemical Weapons Convention: a global ban on "
                         "producing and stockpiling chemical arms, signed by the first "
                         "President Bush. Ratification needs 67 votes, and conservatives "
                         "warn it is unverifiable and toothless."),
            },
            {
                "congress": 105, "session": 2, "vote": 117,
                "name": "Expanding NATO Eastward",
                "desc": ("April 30, 1998. Admitting Poland, Hungary, and the Czech Republic "
                         "to NATO — extending America's defense umbrella to Russia's old "
                         "doorstep. Critics ask what the alliance is now for, and whom it "
                         "might provoke. Treaties need 67 votes."),
            },
            {
                "congress": 106, "session": 2, "vote": 251,
                "name": "Permanent Trade with China",
                "desc": ("September 19, 2000. Permanent normal trade relations with China, "
                         "clearing its path into the World Trade Organization. Business is "
                         "euphoric. Labor and human-rights advocates call it a historic "
                         "sellout."),
            },
        ],
    },
    {
        "id": "bush-majority",
        "title": "The Bush Majority",
        "era": "108th Congress · 2003",
        "intro": ("War in Iraq, tax cuts at home, and a Republican Party at high tide. For "
                  "Democrats, every vote is a choice between conviction and survival."),
        "senators": [
            ("mccain",  "The maverick restored: hawkish on the war, but a deficit scold who "
                        "has rediscovered his taste for bucking his own White House on "
                        "spending."),
            ("kennedy", "Forty years in and pugnacious as ever — he calls the Iraq war a "
                        "'fraud cooked up in Texas,' while still cutting domestic deals with "
                        "this White House when it serves his causes."),
            ("daschle", "The Democratic leader: a soft-spoken South Dakotan balancing a "
                        "liberal caucus against a state Bush carried by 22 points — with his "
                        "own re-election looming."),
            ("specter", "Pennsylvania's cranky Republican moderate: pro-choice, pro-labor by "
                        "his party's standards, and facing a bruising primary from his right "
                        "next spring."),
            ("zmiller", "A Georgia Democrat in name only by now: he keynoted for Clinton in "
                        "'92, but has embraced Bush's agenda nearly wholesale — and relishes "
                        "infuriating his own party."),
        ],
        "bills": [
            {
                "congress": 108, "session": 1, "vote": 51,
                "name": "The Partial-Birth Abortion Ban",
                "desc": ("March 13, 2003. A federal ban on the late-term procedure opponents "
                         "call partial-birth abortion — the first federal criminal "
                         "prohibition of an abortion method since Roe, with an exception for "
                         "the mother's life but not her health."),
            },
            {
                "congress": 108, "session": 1, "vote": 400,
                "name": "$87 Billion for Iraq",
                "desc": ("October 17, 2003. Eighty-seven billion dollars for the occupations "
                         "of Iraq and Afghanistan — six months after 'Mission Accomplished,' "
                         "with no weapons found and the insurgency growing. Voting no reads "
                         "as abandoning the troops; voting yes as endorsing the war."),
            },
            {
                "congress": 108, "session": 1, "vote": 459,
                "name": "Medicare Prescription Drugs",
                "desc": ("November 25, 2003. The biggest Medicare expansion in history: a "
                         "prescription-drug benefit delivered through private insurers, with "
                         "the government barred from negotiating prices. Liberals call it a "
                         "giveaway to industry; conservatives call it a budget-buster."),
            },
        ],
    },
    {
        "id": "second-term-blues",
        "title": "Second-Term Blues",
        "era": "109th Congress · 2005–2006",
        "intro": ("A re-elected George W. Bush spends his political capital fast: "
                  "bankruptcy law for the banks, a fence for the border, and military "
                  "tribunals for the age of terror."),
        "senators": [
            ("obama",     "The celebrity freshman, two years from announcing for president: "
                          "a constitutional-law lecturer's instincts inside a cautious "
                          "legislator's record."),
            ("biden",     "Foreign Relations' top Democrat — and Delaware's senator, which "
                          "means the credit-card industry's senator, as his critics never "
                          "tire of noting."),
            ("chafee",    "The chamber's loneliest Republican: anti-war, pro-environment, "
                          "pro-civil-liberties, and fighting for his political life in "
                          "deep-blue Rhode Island this November."),
            ("coburn",    "'Dr. No.' An Oklahoma obstetrician who hunts wasteful spending "
                          "for sport and votes against nearly anything that grows the "
                          "government."),
            ("feinstein", "California's businesslike centrist: tough on crime and terrorism "
                          "by her party's standards, a dealmaker on the Judiciary Committee."),
        ],
        "bills": [
            {
                "congress": 109, "session": 1, "vote": 44,
                "name": "The Bankruptcy Bill",
                "desc": ("March 10, 2005. The credit-card industry's decade-long dream: "
                         "means tests and new hurdles making it far harder for consumers to "
                         "erase debts in bankruptcy. Banks say it targets abuse; consumer "
                         "advocates say it punishes the sick, the divorced, and the broke."),
            },
            {
                "congress": 109, "session": 2, "vote": 262,
                "name": "The Secure Fence Act",
                "desc": ("September 29, 2006. Seven hundred miles of double-layer fencing "
                         "along the Mexican border, voted weeks before the midterms — the "
                         "enforcement-only answer after comprehensive immigration reform "
                         "collapsed."),
            },
            {
                "congress": 109, "session": 2, "vote": 259,
                "name": "The Military Commissions Act",
                "desc": ("September 28, 2006. Military tribunals for Guantánamo detainees, "
                         "stripped of habeas corpus review, with the CIA's interrogation "
                         "program written into law — rushed through in the September dash to "
                         "adjourn and campaign."),
            },
        ],
    },
    {
        "id": "tea-party-senate",
        "title": "The Tea Party Senate",
        "era": "112th Congress · 2011–2012",
        "intro": ("A debt-ceiling standoff brings the country within days of default, and "
                  "the parties' new wings — Tea Party right, progressive left — treat every "
                  "compromise as surrender."),
        "senators": [
            ("rubio",     "The Tea Party's polished new star from Florida, elected over the "
                          "establishment's pick: young, ambitious, and allergic to anything "
                          "that smells like business as usual."),
            ("rpaul",     "The movement's ideologist: an eye doctor who reads deficits as "
                          "theft and most federal programs as unconstitutional. Compromise "
                          "is what he came to Washington to stop."),
            ("sanders",   "Vermont's socialist, now a national voice against austerity — he "
                          "recently held the floor for eight and a half hours against "
                          "extending the Bush tax cuts."),
            ("sbrown",    "The Massachusetts surprise: a Republican in Ted Kennedy's old "
                          "seat, driving a pickup truck and hugging the center line for "
                          "dear life before 2012."),
            ("mccaskill", "A Missouri Democrat with an auditor's temperament, hunting "
                          "earmarks and waste to survive in a state drifting steadily "
                          "redder."),
        ],
        "bills": [
            {
                "congress": 112, "session": 1, "vote": 123,
                "name": "The Debt-Ceiling Deal",
                "desc": ("August 2, 2011 — default is hours away. The Budget Control Act "
                         "raises the debt ceiling in exchange for a decade of spending caps "
                         "and an automatic 'sequester' guillotine. Nobody loves it, and "
                         "leadership is begging for votes from the middle outward."),
            },
            {
                "congress": 112, "session": 2, "vote": 87,
                "name": "Violence Against Women Act",
                "desc": ("April 26, 2012. Reauthorizing the Violence Against Women Act — "
                         "routine for eighteen years, now a fight over newly added "
                         "protections for Native American, immigrant, and LGBT victims."),
            },
            {
                "congress": 112, "session": 2, "vote": 65,
                "name": "The Buffett Rule",
                "desc": ("April 16, 2012. A minimum 30% tax rate on incomes over $1 million, "
                         "named for the billionaire who pays a lower rate than his "
                         "secretary. It needs 60 votes to advance and everyone knows it "
                         "won't get them — this vote is for the campaign ads."),
            },
        ],
    },
    {
        "id": "election-year-fever",
        "title": "Election Year Fever",
        "era": "116th Congress · 2020",
        "intro": ("An impeachment ends, a pandemic begins, and a Supreme Court seat opens "
                  "six weeks before the election. 2020 asks every senator exactly one "
                  "question: how brave are you feeling?"),
        "senators": [
            ("collins", "The last New England Republican, defending a seat in a state Trump "
                        "lost. Her approval has cratered since the Kavanaugh vote, and every "
                        "roll call is scrutinized for daylight from the President."),
            ("romney",  "The party's 2012 nominee, reborn as its most conspicuous internal "
                        "critic — the first senator in history to vote to remove a president "
                        "of his own party."),
            ("sanders", "Running for president again as the progressive standard-bearer, "
                        "against the trade deals and foreign wars of both parties' "
                        "establishments."),
            ("sinema",  "Arizona's unpredictable first-termer: a former Green Party activist "
                        "turned proud centrist who prizes her bipartisan brand above her "
                        "party's agenda."),
            ("cotton",  "An Army veteran of Iraq and Afghanistan and the Senate's most "
                        "disciplined hawk: maximum pressure abroad, maximum loyalty to the "
                        "President at home."),
        ],
        "bills": [
            {
                "congress": 116, "session": 2, "vote": 14,
                "name": "The USMCA Trade Deal",
                "desc": ("January 16, 2020. NAFTA's replacement: modernized rules, tougher "
                         "labor enforcement in Mexico, and the rare blessing of both the "
                         "AFL-CIO and the Chamber of Commerce — the last major bill before "
                         "the impeachment trial consumes the chamber."),
            },
            {
                "congress": 116, "session": 2, "vote": 52,
                "name": "Iran War Powers Resolution",
                "desc": ("February 13, 2020. Weeks after the drone strike killing Qassem "
                         "Soleimani brought the U.S. and Iran to the brink, a resolution "
                         "ordering the President to halt hostilities against Iran absent "
                         "congressional authorization. A veto is certain; the vote is about "
                         "the principle."),
            },
            {
                "congress": 116, "session": 2, "vote": 224,
                "name": "Confirming Amy Coney Barrett",
                "desc": ("October 26, 2020 — eight days before the election, with millions "
                         "of votes already cast. Amy Coney Barrett's confirmation to Ruth "
                         "Bader Ginsburg's seat, four years after the majority held "
                         "Scalia's seat open for ten months on election-year principle."),
            },
        ],
    },
    {
        "id": "fifty-fifty-senate",
        "title": "The Fifty-Fifty Senate",
        "era": "117th Congress · 2021–2022",
        "intro": ("A dead-even chamber where the Vice President breaks ties and any single "
                  "senator holds veto power. Somehow, it becomes the most legislatively "
                  "productive Congress in a generation."),
        "senators": [
            ("mcconnell", "The Republican leader and self-described Grim Reaper of "
                          "Democratic bills — but a master tactician who occasionally deals "
                          "when he judges the party's long-term interest demands it."),
            ("murkowski", "Alaska's write-in survivor, openly estranged from Trump and "
                          "facing his endorsed challenger next year — as independent as a "
                          "Republican can be and still keep the label."),
            ("cruz",      "Still the Senate's happiest warrior of the right, with 2024 on "
                          "his mind and a camera never far away."),
            ("baldwin",   "Wisconsin's workmanlike progressive and the first openly gay "
                          "senator — a patient vote-counter who prefers quietly assembling "
                          "coalitions to cable-news combat."),
            ("sinema",    "Now the Senate's most-watched Democrat alongside Joe Manchin: "
                          "filibuster defender, dealmaker on infrastructure and guns, and "
                          "scourge of her own party's left wing."),
        ],
        "bills": [
            {
                "congress": 117, "session": 1, "vote": 110,
                "name": "The American Rescue Plan",
                "desc": ("March 6, 2021. $1.9 trillion in pandemic relief: $1,400 checks, an "
                         "expanded child tax credit, and vaccine money, pushed through "
                         "budget reconciliation after an all-night vote-a-rama. The new "
                         "President wants it passed before unemployment benefits lapse."),
            },
            {
                "congress": 117, "session": 1, "vote": 314,
                "name": "The Infrastructure Law",
                "desc": ("August 10, 2021. $550 billion in new money for roads, bridges, "
                         "broadband, and transit, negotiated by ten senators from the "
                         "middle. The question isn't whether it passes — it's which "
                         "Republicans dare to touch it."),
            },
            {
                "congress": 117, "session": 2, "vote": 362,
                "name": "The Respect for Marriage Act",
                "desc": ("November 29, 2022. Federal recognition of same-sex and interracial "
                         "marriages, written as insurance after the Dobbs decision shook "
                         "faith in precedent. Twenty-six years after DOMA passed this "
                         "chamber 85–14, the Senate votes on marriage again."),
            },
        ],
    },
]
