# Batch E — tail pack, runs 2026-10-22 -> 2026-11-02 IN FILE ORDER (E1-E12).
# Pre-1989 bills via voteview; 101st Congress onward via senate.gov XML.
# Verified via: python3 fetch.py batches/batch_E.py

SENATORS_EXTRA = {
    # key: (bioguide, display name, party, state) — era-accurate party labels.
    # All but matsunaga reuse tuples already defined in batches A-D.
    "fulbright":  ("F000401", "J. William Fulbright", "D", "AR"),
    "javits":     ("J000064", "Jacob Javits", "R", "NY"),
    "goldwater":  ("G000267", "Barry Goldwater", "R", "AZ"),
    "mansfield":  ("M000113", "Mike Mansfield", "D", "MT"),
    "mcsmith":    ("S000590", "Margaret Chase Smith", "R", "ME"),
    "thurmond":   ("T000254", "Strom Thurmond", "R", "SC"),
    "hbaker":     ("B000063", "Howard Baker", "R", "TN"),
    "hatch":      ("H000338", "Orrin Hatch", "R", "UT"),
    "hayakawa":   ("H000384", "S.I. Hayakawa", "R", "CA"),
    "mitchell":   ("M000811", "George Mitchell", "D", "ME"),
    "matsunaga":  ("M000250", "Spark Matsunaga", "D", "HI"),
    "hawley":     ("H001089", "Josh Hawley", "R", "MO"),
    "sinema_i":   ("S001191", "Kyrsten Sinema", "I", "AZ"),
    "cmurphy":    ("M001169", "Chris Murphy", "D", "CT"),
    "mlee":       ("L000577", "Mike Lee", "R", "UT"),
    "wyden":      ("W000779", "Ron Wyden", "D", "OR"),
    "king":       ("K000383", "Angus King", "I", "ME"),
    "fetterman":  ("F000479", "John Fetterman", "D", "PA"),
}

PUZZLES = [
    {
        "id": "abm-summer",
        "title": "The ABM Summer",
        "era": "91st Congress · 1969",
        "intro": ("Nixon's first year, and the Senate is suddenly full of doubters: about "
                  "an antimissile system half the physicists call a boondoggle, about a "
                  "creaking tax code, and about who gets hired to build federal America."),
        "senators": [
            ("fulbright", "Arkansas's scholarly chairman of Foreign Relations, whose televised "
                          "hearings turned him into the establishment's leading Vietnam heretic. "
                          "He has come to distrust nearly every Pentagon request on principle — "
                          "though at home he votes like a Southerner."),
            ("javits",    "New York's tireless liberal Republican, a Manhattan lawyer who out-works "
                          "the chamber and votes with Democrats on rights and welfare. He is "
                          "deeply skeptical that more missiles make anyone safer."),
            ("goldwater", "Back in the Senate after his 1964 wipeout, an Air Force Reserve major "
                          "general who never met a weapons system he considered sufficient. "
                          "Federal social engineering, on the other hand, starts his engines."),
            ("mansfield", "The Majority Leader, a former history professor who runs the Senate "
                          "with a light hand and regards the arms race — and the war — with "
                          "quiet, mounting dismay."),
            ("mcsmith",   "Maine's flinty senior Republican on Armed Services, who defied Joe "
                          "McCarthy before it was safe. On the ABM she is an absolutist: do the "
                          "thing properly or not at all — half-measures offend her."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 91, "roll": 55,
                "name": "The Cooper-Hart Amendment",
                "question": "On the Cooper-Hart Amendment to S. 2546",
                "result": "Amendment Rejected",
                "desc": ("August 6, 1969, with Vice President Agnew in the chair in case of a "
                         "tie. Cooper-Hart would let research on the Safeguard antiballistic-"
                         "missile system continue but bar actually deploying it around Minuteman "
                         "silos. Scientists have spent the summer testifying the system cannot "
                         "work; Nixon has made the vote a test of his presidency. Minutes "
                         "earlier, a flat-out prohibition died on a 50-50 tie."),
            },
            {
                "source": "voteview", "congress": 91, "roll": 200,
                "name": "The Tax Reform Act of 1969",
                "question": "On Passage of H.R. 13270", "result": "Bill Passed",
                "desc": ("December 11, 1969. Born of outrage that 155 wealthy Americans paid no "
                         "income tax at all, the bill invents a minimum tax, trims the sacred "
                         "27.5% oil-depletion allowance, raises the personal exemption, and "
                         "boosts Social Security benefits 15% — while extending a shrinking "
                         "Vietnam surtax. Treasury warns the Senate's generosity will feed "
                         "inflation."),
            },
            {
                "source": "voteview", "congress": 91, "roll": 231,
                "name": "The Philadelphia Plan Rider",
                "question": "On Retaining the Rider Against the Philadelphia Plan",
                "result": "Rider Retained",
                "desc": ("December 18, 1969. Nixon's Philadelphia Plan orders contractors on "
                         "federal projects to set goals for hiring Black construction workers — "
                         "the first affirmative-action hiring targets. A rider on the "
                         "supplemental spending bill would let the Comptroller General kill it, "
                         "and the White House threatens a veto. A yea keeps the rider and blocks "
                         "the Plan; unions and Southern Democrats want exactly that."),
            },
        ],
    },
    {
        "id": "nineteen-eighty-four",
        "title": "Nineteen Eighty-Four",
        "era": "98th Congress · 1984",
        "intro": ("Reagan cruises toward reelection while his Senate fights over God in the "
                  "classroom, mines in Nicaraguan harbors, and beer in teenagers' hands. "
                  "Everything is a values vote in an election year."),
        "senators": [
            ("dole",      "Kansas's new Finance chairman, a wounded veteran with a dry wit and "
                          "a deal always in his pocket. He carries Reagan's program dutifully — "
                          "but his instincts are more budget ledger than crusade."),
            ("goldwater", "Seventy-five now, chairman of Intelligence, the conservative movement's "
                          "founding father — and its crankiest libertarian. He is fresh from "
                          "writing the CIA director a blistering letter that begins, roughly, "
                          "'I am pissed off.'"),
            ("thurmond",  "South Carolina's 81-year-old Judiciary chairman, the 1948 Dixiecrat "
                          "turned Reagan loyalist. School prayer is his cause of the season, and "
                          "he has little patience for lectures about federalism from either "
                          "direction."),
            ("kennedy",   "The liberal lion, keeper of his brothers' church-and-state scruples "
                          "and scourge of Reagan's Central America policy. He has a talent for "
                          "forcing Republicans to vote on things they'd rather not."),
            ("moynihan",  "New York's professor-senator, vice chairman of Intelligence, a "
                          "Democrat who quotes Burke and drafts indictments of the CIA between "
                          "lectures. He resigned his committee post over the harbor mining — "
                          "briefly, theatrically, effectively."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 98, "roll": 405,
                "name": "The School Prayer Amendment",
                "question": "On Passage of S.J. Res. 73",
                "result": "Rejected (two-thirds required)",
                "desc": ("March 20, 1984. A constitutional amendment declaring that nothing in "
                         "the Constitution prohibits organized, vocal prayer in public schools. "
                         "Reagan has campaigned for it personally; two weeks of debate turn the "
                         "chamber into a seminary. Passage requires 67 votes, and everyone is "
                         "counting — a majority in favor that falls short still makes a fine "
                         "campaign issue."),
            },
            {
                "source": "voteview", "congress": 98, "roll": 430,
                "name": "Condemning the Harbor Mining",
                "question": "On the Kennedy Amendment to H.R. 2163",
                "result": "Amendment Agreed to",
                "desc": ("April 10, 1984, days after Americans learn the CIA secretly mined "
                         "Nicaragua's harbors — and that ships of six nations have struck the "
                         "mines. The nonbinding Kennedy language declares no federal funds shall "
                         "go to planning or executing the mining. The administration calls it "
                         "collective self-defense; even loyal Republicans are running out of "
                         "patience with being briefed after the fact."),
            },
            {
                "source": "voteview", "congress": 98, "roll": 529,
                "name": "The National Drinking Age",
                "question": "On the Lautenberg Amendment to H.R. 4616",
                "result": "Amendment Agreed to",
                "desc": ("June 26, 1984. States that keep a drinking age under 21 would lose a "
                         "slice of their federal highway money. Mothers Against Drunk Driving "
                         "has made 'blood borders' — teenagers driving to the next state's bars "
                         "— a national scandal, and Reagan has swung behind the bill. Purists "
                         "of both parties grumble that Washington is buying obedience from the "
                         "states with their own tax dollars."),
            },
        ],
    },
    {
        "id": "rehnquist-court",
        "title": "The Rehnquist Elevation",
        "era": "99th Congress · 1986",
        "intro": ("Warren Burger retires, and Reagan reaches for the Court's most conservative "
                  "member to lead it. One long September day produces a brawl and a "
                  "coronation — then October delivers the biggest immigration law in decades."),
        "senators": [
            ("biden",     "Delaware's ranking Democrat on Judiciary, 43 and openly weighing a "
                          "presidential run. He must prosecute the case against Rehnquist "
                          "without looking like an obstructionist — a line he walks out loud, "
                          "at length."),
            ("thurmond",  "The Judiciary chairman, 83, moving Reagan's judges with the "
                          "efficiency of a man who has outlasted every enemy. He considers the "
                          "attacks on Rehnquist recycled slander from 1971."),
            ("kennedy",   "Massachusetts's liberal enforcer, who has read the memos on "
                          "restrictive covenants and voter challenges and pronounces the "
                          "nominee 'outside the mainstream.' Immigration, meanwhile, is a "
                          "Kennedy family franchise — which cuts in surprising directions."),
            ("specter",   "Pennsylvania's ex-prosecutor, a Republican who treats confirmation "
                          "hearings as cross-examination and votes wherever the evidence takes "
                          "him — to his party's frequent irritation."),
            ("helms",     "North Carolina's unbending conservative, guardian of the Reagan "
                          "revolution's right flank. Amnesty for illegal aliens, in his view, "
                          "rewards lawbreaking — no matter whose administration proposes it."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 99, "roll": 647,
                "name": "Rehnquist for Chief Justice",
                "question": "On the Nomination of William H. Rehnquist",
                "result": "Nomination Confirmed",
                "desc": ("September 17, 1986. Elevating Associate Justice William Rehnquist — "
                         "the Court's most reliable conservative — to Chief Justice of the "
                         "United States. Democrats resurrect old accusations: memos defending "
                         "school segregation, challenges to Black voters in Phoenix, a "
                         "restrictive covenant on his deed. The 33 votes against will be the "
                         "most ever cast against a confirmed justice."),
            },
            {
                "source": "voteview", "congress": 99, "roll": 648,
                "name": "Confirming Antonin Scalia",
                "question": "On the Nomination of Antonin Scalia",
                "result": "Nomination Confirmed",
                "desc": ("The same day, minutes later. With the chamber's ammunition spent on "
                         "Rehnquist, the nomination of appeals judge Antonin Scalia — 50 years "
                         "old, brilliant, combative, and the first Italian-American nominated "
                         "to the Court — glides through almost unexamined. Some Democrats will "
                         "spend decades regretting the ease of it."),
            },
            {
                "source": "voteview", "congress": 99, "roll": 738,
                "name": "The Immigration Reform and Control Act",
                "question": "On the Conference Report on S. 1200",
                "result": "Conference Report Agreed to",
                "desc": ("October 17, 1986. Simpson-Mazzoli, five years in the making: legal "
                         "status for millions of undocumented immigrants who arrived before "
                         "1982, penalties on employers who knowingly hire illegal workers, and "
                         "a special program for farm labor. Conservatives call it amnesty; "
                         "Hispanic groups fear the sanctions will breed hiring discrimination; "
                         "growers just want their harvest picked."),
            },
        ],
    },
    {
        "id": "the-apology",
        "title": "The Apology",
        "era": "100th Congress · 1988",
        "intro": ("Forty-six years after the internment camps, the Senate decides what the "
                  "country owes — to Japanese-Americans, to seniors facing ruinous medical "
                  "bills, and to factory workers who learn from a padlocked gate."),
        "senators": [
            ("matsunaga", "Hawaii's gentle workhorse, wounded twice in Italy with the storied "
                          "100th Battalion while his government classified families like his as "
                          "enemy aliens. He has personally lobbied all 99 colleagues on the "
                          "redress bill, and everyone knows it."),
            ("byrd",      "The Appropriations baron and former majority leader, a fiddle-playing "
                          "West Virginia institutionalist who measures every cause against the "
                          "Treasury and the Constitution — in that order, some days."),
            ("dole",      "The Republican leader, home from a bruising presidential primary "
                          "loss to George Bush. A Kansas plainsman who left an arm's use on an "
                          "Italian hillside, he has a soldier's regard for the 442nd — and a "
                          "budget hawk's regard for new entitlements."),
            ("gramm",     "Texas's evangelist of spending discipline, a former economics "
                          "professor who converted from the Democrats and brought the zeal of "
                          "the convert. Almost any bill with a price tag finds him unmoved."),
            ("kassebaum", "Kansas's understated moderate, Alf Landon's daughter, allergic to "
                          "grandstanding in both directions. She reads the fine print on "
                          "financing schemes and votes accordingly, party be damned."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 100, "roll": 525,
                "name": "The Civil Liberties Act",
                "question": "On Passage of H.R. 442", "result": "Bill Passed",
                "desc": ("April 20, 1988. A formal apology for the wartime internment of "
                         "120,000 Japanese-Americans, and $20,000 in redress to each surviving "
                         "internee — roughly $1.3 billion in all. The bill is numbered for the "
                         "442nd Regimental Combat Team, the most decorated unit of the war. "
                         "Opponents ask why today's taxpayers should pay for 1942's panic; "
                         "veterans of the 442nd sit in the gallery."),
            },
            {
                "source": "voteview", "congress": 100, "roll": 590,
                "name": "Medicare Catastrophic Coverage",
                "question": "On the Conference Report on H.R. 2470",
                "result": "Conference Report Agreed to",
                "desc": ("June 8, 1988. The largest Medicare expansion since 1965: a cap on "
                         "hospital and doctor bills, and for the first time coverage of "
                         "prescription drugs — financed not by payroll taxes but by a "
                         "supplemental premium on better-off seniors themselves. Reagan, "
                         "remarkably, is ready to sign. The novel financing will prove more "
                         "explosive than anyone in the chamber suspects."),
            },
            {
                "source": "voteview", "congress": 100, "roll": 645,
                "name": "The Plant-Closing Notice Bill",
                "question": "On Passage of S. 2527", "result": "Bill Passed",
                "desc": ("July 6, 1988. Employers with 100 or more workers would owe 60 days' "
                         "written warning before a plant closing or mass layoff. Reagan vetoed "
                         "it once inside the trade bill; Democrats have sent it back alone, "
                         "daring Republicans to defend the padlocked-gate surprise in an "
                         "election year. Business calls it a lawyers' bonanza; Rust Belt "
                         "senators of both parties feel the heat."),
            },
        ],
    },
    {
        "id": "clean-air-congress",
        "title": "The Clean Air Congress",
        "era": "101st Congress · 1989–1990",
        "intro": ("George Mitchell's first Congress as leader takes up unfinished business: "
                  "a minimum wage frozen since 1981, smog and acid rain untouched since "
                  "1977, and a Supreme Court seat nobody saw coming."),
        "senators": [
            ("mitchell",  "The new Majority Leader, a former federal judge from Maine with a "
                          "prosecutor's patience. Clean air is his signature obsession — he has "
                          "spent a decade on acid rain and intends to spend whatever floor time "
                          "it takes."),
            ("byrd",      "Dethroned as leader, enthroned at Appropriations. The senior senator "
                          "from coal fights any acid-rain program that writes off West "
                          "Virginia's miners — and he knows more parliamentary tricks than the "
                          "rest of the chamber combined."),
            ("kennedy",   "Chairman of Labor, custodian of the minimum wage and skeptic-in-chief "
                          "of Republican judicial nominees. He wants to know exactly where a "
                          "'stealth' nominee stands on Roe — and suspects the silence is the "
                          "answer."),
            ("dole",      "The Republican leader, guarding a president who has promised both "
                          "'no new taxes' and a kinder, gentler environmentalism. His job is "
                          "keeping Bush's vetoes sustained — which he does with grim "
                          "efficiency."),
            ("helms",     "The Senate's most reliable no, warring against regulators, wage "
                          "floors, and the entire modern judicial confirmation ritual. When "
                          "ninety colleagues line up one way, he regards it as evidence."),
        ],
        "bills": [
            {
                "congress": 101, "session": 1, "vote": 68,
                "name": "The Minimum Wage Veto Fight",
                "desc": ("May 17, 1989. The conference report raises the minimum wage from "
                         "$3.35 — where it has sat since 1981 — to $4.55 by 1991, with a "
                         "two-month training wage for new hires. Bush has drawn a line at "
                         "$4.25 and promises a veto, his first. Democrats send it to his desk "
                         "anyway, betting that defending $3.35 an hour looks worse than "
                         "breaking a promise."),
            },
            {
                "congress": 101, "session": 2, "vote": 55,
                "name": "The Clean Air Act of 1990",
                "desc": ("April 3, 1990. The first clean-air overhaul in thirteen years: a "
                         "cap-and-trade market to halve acid-rain sulfur emissions, controls "
                         "on 189 toxic air pollutants, and a phase-out of the worst smog in "
                         "dozens of cities. A Byrd amendment to cushion coal miners has just "
                         "died by a single vote. Mitchell has given the floor over to the bill "
                         "for five straight weeks."),
            },
            {
                "congress": 101, "session": 2, "vote": 259,
                "name": "Confirming David Souter",
                "desc": ("October 2, 1990. William Brennan, the Court's liberal architect, is "
                         "gone, and Bush offers a virtually paperless New Hampshire judge — "
                         "the 'stealth nominee.' Souter has charmed the Judiciary Committee "
                         "while declining to say a word about abortion. Most Democrats decide "
                         "he is the best they will get from this president; abortion-rights "
                         "groups beg them not to gamble."),
            },
        ],
    },
    {
        "id": "test-ban-autumn",
        "title": "The Test Ban Autumn",
        "era": "106th Congress · 1999",
        "intro": ("A Senate at war with its president finds three ways to say no: to a "
                  "nuclear treaty, to the trial lawyers, and — some of it — to trade with "
                  "Africa. Nothing is simple the year before a millennium."),
        "senators": [
            ("lugar",     "Indiana's soft-spoken foreign-policy eminence, co-author of the "
                          "program dismantling Soviet warheads. Arms controllers assume his "
                          "vote is theirs on any treaty — an assumption he is about to "
                          "examine."),
            ("specter",   "Pennsylvania's contrarian Republican, a Warren Commission lawyer "
                          "who relishes breaking with his party leadership and explaining why "
                          "at length. Steel country shapes his trade votes; the evidence, he "
                          "says, shapes the rest."),
            ("helms",     "Chairman of Foreign Relations, who kept the treaty locked in his "
                          "committee for two years and calls it 'very low priority.' He "
                          "guards North Carolina textiles as fiercely as American "
                          "sovereignty."),
            ("moynihan",  "New York's scholar-statesman in his valedictory term, a free "
                          "trader and arms-control believer who wrote the book — several "
                          "books — on how governments deceive themselves."),
            ("wellstone", "Minnesota's rumpled progressive, the Senate's most reliable vote "
                          "against corporate liability shields and trade deals alike. He "
                          "measures every bill by what it does to the little guy, allies' "
                          "feelings notwithstanding."),
        ],
        "bills": [
            {
                "congress": 106, "session": 1, "vote": 325,
                "name": "The Comprehensive Test Ban Treaty",
                "desc": ("October 13, 1999. Ratifying the global ban on nuclear test "
                         "explosions — 154 nations have signed, and Clinton signed first. "
                         "Republican leaders suddenly schedule the vote Democrats spent two "
                         "years demanding, then refuse to postpone it when the votes aren't "
                         "there. Rejection would make it the first treaty defeated since "
                         "Versailles in 1920. Ratification needs 67."),
            },
            {
                "congress": 106, "session": 1, "vote": 165,
                "name": "The Y2K Liability Act",
                "desc": ("June 15, 1999. With the millennium bug six months out, the bill "
                         "caps punitive damages and forces a 90-day cooling-off period "
                         "before anyone can sue over Y2K computer failures. Silicon Valley "
                         "says it faces a trillion-dollar litigation lottery; trial lawyers "
                         "and consumer groups call it a permanent corporate shield wearing "
                         "a costume. Clinton is threatening a veto."),
            },
            {
                "congress": 106, "session": 1, "vote": 353,
                "name": "The African Trade Bill",
                "desc": ("November 3, 1999. The African Growth and Opportunity Act opens "
                         "American markets duty-free to sub-Saharan apparel and goods, trading "
                         "tariff preferences for market reforms in 48 countries. Backers call "
                         "it 'trade, not aid.' Textile-state senators of both parties see "
                         "their mills' last customers sailing away, and labor calls it NAFTA "
                         "with a new passport."),
            },
        ],
    },
    {
        "id": "stay-the-course",
        "title": "Stay the Course",
        "era": "97th Congress · 1982",
        "intro": ("Deep in a recession, with deficits exploding and midterms looming, "
                  "Reagan's Senate tries everything at once: raising taxes it just cut, "
                  "extending a voting law the president resisted, and amending the "
                  "Constitution itself."),
        "senators": [
            ("dole",      "The Finance chairman, engineering the unthinkable — a Republican "
                          "tax increase — one loophole at a time. He calls it responsibility; "
                          "a young congressman named Gingrich calls him 'tax collector for "
                          "the welfare state.'"),
            ("hbaker",    "The Majority Leader, Watergate's famous questioner, now Reagan's "
                          "indispensable field marshal. His job is holding a restive majority "
                          "together for whatever the White House needs this week — including "
                          "things it swore off last year."),
            ("helms",     "North Carolina's uncompromising conservative, fresh from "
                          "filibustering the voting-rights extension for weeks. He considers "
                          "the tax bill a betrayal of the Reagan revolution and says so to "
                          "Reagan's face."),
            ("kennedy",   "The liberal standard-bearer, eyeing 1984 and happy to fight "
                          "Reaganomics on every front. Voting rights is sacred ground; "
                          "balanced-budget amendments he calls fiscal quackery in "
                          "constitutional dress."),
            ("byrd",      "The Minority Leader, marshaling a diminished army with a "
                          "parliamentarian's cunning. A courthouse Democrat who loves the "
                          "Constitution too much, he says, to let anyone write a budget "
                          "gimmick into it — most days."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 97, "roll": 687,
                "name": "Extending the Voting Rights Act",
                "question": "On Passage of H.R. 3112", "result": "Bill Passed",
                "desc": ("June 18, 1982. A 25-year extension of the Voting Rights Act — and a "
                         "rebuke to the Supreme Court, restoring the rule that discriminatory "
                         "'results,' not just proven intent, violate the law. Helms held the "
                         "floor for weeks; Reagan resisted, then folded as the margins built. "
                         "By the end, opposing it means standing nearly alone."),
            },
            {
                "source": "voteview", "congress": 97, "roll": 754,
                "name": "The 1982 Tax Increase (TEFRA)",
                "question": "On Passage of H.R. 4961", "result": "Bill Passed",
                "desc": ("July 22, 1982, near midnight. One year after the largest tax cut in "
                         "history, Dole's bill claws back $98 billion — closing loopholes, "
                         "tightening compliance, taxing cigarettes and phone calls — to calm "
                         "markets panicked by 6% deficits. Reagan swallows it as 'tax reform.' "
                         "Supply-siders call it surrender by arithmetic."),
            },
            {
                "source": "voteview", "congress": 97, "roll": 785,
                "name": "The Balanced Budget Amendment",
                "question": "On Passage of S.J. Res. 58",
                "result": "Passed (two-thirds required)",
                "desc": ("August 4, 1982. For the first time in history, the Senate votes on "
                         "sending a balanced-budget constitutional amendment to the states: "
                         "Congress could not spend more than it takes in without a "
                         "three-fifths vote. Reagan campaigns for it even as his own deficits "
                         "set records — a contradiction Democrats note hourly. Two-thirds, "
                         "67 votes, required."),
            },
        ],
    },
    {
        "id": "brady-winter",
        "title": "The Brady Winter",
        "era": "103rd Congress · 1993–1994",
        "intro": ("Unified Democratic government tests its strength: a gun bill named for a "
                  "wounded press secretary, a judge nominated to make history quietly, and "
                  "organized labor calling in a debt that may not get paid."),
        "senators": [
            ("helms",     "North Carolina's implacable conservative, guardian of gun rights "
                          "and sworn enemy of the entire Clinton project. His no votes are "
                          "the closest thing the Senate has to a fixed star."),
            ("dole",      "The Minority Leader, rebuilding Republican power one filibuster at "
                          "a time while measuring the distance to 1996. He fights the Brady "
                          "bill's waiting period to the last procedural ditch — then has to "
                          "decide what to do when the dam breaks."),
            ("specter",   "Pennsylvania's independent-minded Republican, an ex-DA who backs "
                          "some gun controls the NRA hates — and hates some the Democrats "
                          "love. Labor's rank and file back home never let him forget where "
                          "he came from."),
            ("boxer",     "California's freshman firebrand, elected in the Year of the Woman "
                          "on guns, choice, and impatience. She considers the waiting period "
                          "the bare minimum a civilized country owes itself."),
            ("wellstone", "Minnesota's professor-populist, labor's truest believer in the "
                          "chamber. The striker-replacement bill is, to him, the whole point "
                          "of electing Democrats — which makes the arithmetic of 60 votes "
                          "especially bitter."),
        ],
        "bills": [
            {
                "congress": 103, "session": 1, "vote": 232,
                "name": "Confirming Ruth Bader Ginsburg",
                "desc": ("August 3, 1993. Clinton's first Supreme Court pick: the ACLU "
                         "litigator who won five of six sex-discrimination cases before the "
                         "Court she now joins, replacing Byron White. Her 'no hints, no "
                         "forecasts' testimony sets the modern template, and almost nobody "
                         "finds a reason to object out loud."),
            },
            {
                "congress": 103, "session": 1, "vote": 394,
                "name": "The Brady Bill",
                "desc": ("November 20, 1993. Twelve years after Jim Brady was shot in the "
                         "head beside Reagan, the bill requires a five-business-day waiting "
                         "period and a background check to buy a handgun, until an instant "
                         "check system comes online. The NRA has beaten it for seven years "
                         "running; this time the filibusters have finally cracked."),
            },
            {
                "congress": 103, "session": 2, "vote": 189,
                "name": "The Striker Replacement Bill",
                "desc": ("July 13, 1994. Labor's top priority: barring companies from "
                         "permanently replacing workers who strike, a practice booming since "
                         "the Caterpillar and Greyhound wars. With a Democratic president "
                         "waiting to sign, everything rides on breaking a Republican "
                         "filibuster — 60 votes or nothing, and yesterday's try fell seven "
                         "short."),
            },
        ],
    },
    {
        "id": "labors-last-stand",
        "title": "Labor's Last Stand",
        "era": "95th Congress · 1977–1978",
        "intro": ("A Democratic president, 61 Democratic senators, and the AFL-CIO's whole "
                  "agenda on the calendar. What could go wrong meets the filibuster — and a "
                  "new breed of business lobbying that will outlive them all."),
        "senators": [
            ("byrd",      "The new Majority Leader, a onetime coal-town butcher who mastered "
                          "every rule in the book. He counts votes like rosary beads and "
                          "will try any parliamentary device — including six cloture votes "
                          "in a row — before conceding anything."),
            ("hatch",     "Utah's 43-year-old freshman, leading his first great crusade: an "
                          "around-the-clock filibuster against the labor bill, armed with "
                          "index cards and bottomless stamina. Winning it would make him; he "
                          "knows it."),
            ("javits",    "New York's veteran liberal Republican, ranking member on Labor, "
                          "co-author of half the workplace laws on the books. Big business's "
                          "new militancy alarms him almost as much as it delights his "
                          "party's young conservatives."),
            ("hayakawa",  "California's celebrity semanticist, the tam-o'-shanter-wearing "
                          "college president who faced down student strikers at San "
                          "Francisco State. He naps through some debates and torpedoes "
                          "liberal bills in his sleep."),
            ("biden",     "Delaware's young second-termer, a scrappy blue-collar Democrat "
                          "with a commuter's Amtrak schedule and an economist's anxiety "
                          "about inflation. Labor counts him a friend — mostly."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 95, "roll": 549,
                "name": "The Minimum Wage Act of 1977",
                "question": "On Passage of H.R. 3744", "result": "Bill Passed",
                "desc": ("October 7, 1977. Raising the minimum wage from $2.30 to $3.35 by "
                         "1981 in four annual steps — and, for the first time, indexing "
                         "debate to inflation running near 7%. Carter and the AFL-CIO settled "
                         "for steps instead of indexing; business warns every dime costs "
                         "teenagers their jobs."),
            },
            {
                "source": "voteview", "congress": 95, "roll": 802,
                "name": "Labor Law Reform — the Fifth Cloture",
                "question": "On the Cloture Motion (H.R. 8410)",
                "result": "Cloture Rejected",
                "desc": ("June 14, 1978. Labor's bill to speed union elections and punish "
                         "employers who fire organizers has already passed the House. Hatch "
                         "and Lugar have filibustered for weeks while business groups bury "
                         "the Senate in eight million pieces of mail. This is the fifth "
                         "cloture vote — the high-water mark. Sixty votes ends the "
                         "filibuster; labor will never come closer."),
            },
            {
                "source": "voteview", "congress": 95, "roll": 1131,
                "name": "Humphrey-Hawkins Full Employment",
                "question": "On Passage of H.R. 50", "result": "Bill Passed",
                "desc": ("October 13, 1978. The Full Employment Act that Hubert Humphrey "
                         "did not live to see: national goals of 4% unemployment within five "
                         "years, with the government as employer of last resort long since "
                         "bargained away. Critics call what remains a press release with a "
                         "preamble; to liberals it is a promise worth writing down, and a "
                         "memorial besides."),
            },
        ],
    },
    {
        "id": "tiktok-ultimatum",
        "title": "The TikTok Ultimatum",
        "era": "118th Congress · 2024",
        "intro": ("An election-year Senate ties a war chest to an app store: Ukraine aid "
                  "rides with a TikTok ultimatum, a tax deal dies of the calendar, and a "
                  "border compromise returns as a ghost to haunt its own authors."),
        "senators": [
            ("hawley",    "Missouri's combative populist, done with 'blank checks' for "
                          "Ukraine but delighted to break up Big Tech and to court union "
                          "voters with a child tax credit his party leadership scorns. He "
                          "relishes scrambling the old lines."),
            ("collins",   "The Appropriations ranking member and dean of the dwindling "
                          "moderates, a Ukraine hawk who reads every bill and occasionally "
                          "votes against her own side's theater on both flanks."),
            ("murkowski", "Alaska's write-in survivor, unbossed by leadership or primary "
                          "voters. She backs the border deal when her party bolts, and "
                          "votes her own read of Alaska's interest on everything else."),
            ("sinema_i",  "Arizona's independent, retiring rather than face the voters, "
                          "co-author of the border compromise her former parties took turns "
                          "killing. Her remaining months are one long exercise in telling "
                          "everyone exactly what she thinks of them."),
            ("cmurphy",   "Connecticut's earnest dealmaker, the Democrat who spent four "
                          "months negotiating the border package and watched it die in a "
                          "morning. He keeps voting for his own handiwork, on principle and "
                          "on the record."),
        ],
        "bills": [
            {
                "congress": 118, "session": 2, "vote": 154,
                "name": "Foreign Aid Plus the TikTok Ban",
                "desc": ("April 23, 2024, 9 p.m. The $95 billion package — Ukraine artillery "
                         "and air defense, Israel, Taiwan — that hardliners stalled for six "
                         "months, now welded to a sweetener the House added: TikTok's Chinese "
                         "owner must sell within a year or the app goes dark in America, "
                         "plus seized Russian assets steered to Kyiv. One vote, take it or "
                         "leave it all."),
            },
            {
                "congress": 118, "session": 2, "vote": 230,
                "name": "The Wyden-Smith Tax Deal",
                "desc": ("August 1, 2024, the last day before recess. The bipartisan bargain "
                         "that passed the House 357-70 in January: a bigger child tax credit "
                         "for low-income families traded for restored business write-offs on "
                         "research and equipment. Republican leaders would rather write next "
                         "year's tax bill with a President Trump; Democrats force the vote to "
                         "make them say so. Sixty needed."),
            },
            {
                "congress": 118, "session": 2, "vote": 182,
                "name": "The Border Deal, Take Two",
                "desc": ("May 23, 2024. Schumer revives the Lankford-Murphy-Sinema border "
                         "compromise — asylum overhaul, emergency shutdown authority, more "
                         "agents — that Republicans killed in February on Trump's word. "
                         "Everyone knows this rerun is about the campaign, not the law; the "
                         "only question is who votes for their own deal the second time, "
                         "and who calls the whole thing a stunt."),
            },
        ],
    },
    {
        "id": "quiet-congress",
        "title": "The Quiet Congress",
        "era": "114th Congress · 2015–2016",
        "intro": ("Between government shutdowns and a circus of a presidential campaign, an "
                  "unfashionably productive Senate rewrites the school law, takes on the "
                  "opioid crisis, and passes a trillion-dollar deal almost nobody reads "
                  "twice."),
        "senators": [
            ("mlee",      "Utah's constitutional purist, who runs every bill through a "
                          "founding-era filter most legislation fails. Compromise omnibuses "
                          "and federal programs, however popular, rarely survive the test."),
            ("rpaul",     "Kentucky's libertarian gadfly, running for president on "
                          "spending restraint and criminal-justice heresy. He votes no on "
                          "autopilot — except where addiction and prison reform meet his "
                          "own unusual map of liberty."),
            ("wyden",     "Oregon's wonkish Finance Democrat, godfather of half the tax "
                          "provisions in any year-end deal — which never guarantees he can "
                          "stomach the whole package once leadership finishes trading."),
            ("collins",   "Maine's institutionalist, ranked the Senate's most bipartisan "
                          "member so often it reads like a job title. If a bill has 70 "
                          "votes, she probably helped build the coalition."),
            ("king",      "Maine's independent former governor, a pragmatist who caucuses "
                          "with Democrats and shops issue by issue. He judges bills like "
                          "budgets he once signed: does the thing actually work?"),
        ],
        "bills": [
            {
                "congress": 114, "session": 1, "vote": 334,
                "name": "The Every Student Succeeds Act",
                "desc": ("December 9, 2015. The overdue replacement for No Child Left "
                         "Behind: annual testing stays, but Washington's judgments about "
                         "failing schools — and its power to order fixes — go back to the "
                         "states. Teachers' unions and most governors are relieved; "
                         "conservatives who wanted the Education Department dismantled "
                         "call it a missed shot."),
            },
            {
                "congress": 114, "session": 1, "vote": 339,
                "name": "The Trillion-Dollar Year-End Deal",
                "desc": ("December 18, 2015. A $1.1 trillion omnibus funding the government "
                         "through September, fused to $680 billion in tax cuts: the R&D "
                         "credit made permanent, working-family credits locked in, and — "
                         "the quiet blockbuster — the 40-year-old ban on exporting American "
                         "crude oil repealed. Everyone's priorities, nobody's principles, "
                         "one vote before Christmas."),
            },
            {
                "congress": 114, "session": 2, "vote": 129,
                "name": "The Opioid Treatment Act (CARA)",
                "desc": ("July 13, 2016. With overdoses killing 78 Americans a day, the "
                         "first major federal addiction law in decades: naloxone for first "
                         "responders, prescription-monitoring grants, treatment instead of "
                         "jail for nonviolent users. Democrats fume that it authorizes "
                         "programs without appropriating real money — then face the vote "
                         "on an election-year lifeline."),
            },
        ],
    },
    {
        "id": "year-two",
        "title": "Year Two",
        "era": "119th Congress · 2025",
        "intro": ("Trump's second-term Senate writes rules for crypto, debates a war it "
                  "wasn't consulted on, and finally reopens a government shuttered for a "
                  "record 43 days. Every vote is a loyalty test somebody fails."),
        "senators": [
            ("rpaul",     "Kentucky's libertarian institution, chairing Homeland Security "
                          "while voting against most of what it oversees. War powers "
                          "belong to Congress and spending bills should shrink — he has "
                          "said so for fifteen years and is not stopping now."),
            ("collins",   "The Appropriations chair at last, writing the bills a shutdown "
                          "leaves stranded, with a 2026 reelection race looming in a state "
                          "that didn't vote for Trump. Ending the standoff runs through "
                          "her office."),
            ("fetterman", "Pennsylvania's hoodie-wearing contrarian Democrat, pro-crypto, "
                          "staunchly pro-Israel, and loudly done with shutdown politics — "
                          "his party's strategy included. He votes to keep the lights on "
                          "every single time, and says so on television."),
            ("king",      "Maine's independent, a Jefferson-quoting institutionalist who "
                          "voted to reopen the government early and often. On executive "
                          "war-making and financial guardrails he reads the fine print "
                          "first."),
            ("warren",    "Massachusetts's banking-committee scourge, who sees the "
                          "stablecoin bill as a gift wrapped for the president's own "
                          "crypto ventures — and holding out on the shutdown as the only "
                          "leverage her party has left."),
        ],
        "bills": [
            {
                "congress": 119, "session": 1, "vote": 318,
                "name": "The GENIUS Act",
                "desc": ("June 17, 2025. The first federal law for stablecoins — "
                         "dollar-pegged crypto tokens — requiring full reserves, audits, and "
                         "federal or state oversight of issuers. The industry spent a "
                         "fortune electing this Congress; critics note the Trump family's "
                         "own stablecoin stands to profit from the legitimacy. Eighteen "
                         "Democrats cross over anyway."),
            },
            {
                "congress": 119, "session": 1, "vote": 328,
                "name": "Iran War Powers",
                "desc": ("June 27, 2025, six days after B-2s struck Iran's nuclear sites at "
                         "Fordow and Natanz without a word to Congress. The Kaine resolution "
                         "would require congressional authorization for further hostilities "
                         "against Iran. A fragile ceasefire holds; the question is whether "
                         "the Senate insists on being asked before the next strike."),
            },
            {
                "congress": 119, "session": 1, "vote": 618,
                "name": "Reopening the Government",
                "desc": ("November 10, 2025 — day 41 of the longest shutdown in history. "
                         "Flights canceled by the thousand, food aid in the courts, 42 days "
                         "of missed paychecks. The deal funds the government into January "
                         "and promises a mere future vote on the expiring Obamacare "
                         "subsidies Democrats shut it down over. Eight members of their "
                         "caucus decide a promise is enough."),
            },
        ],
    },
]
