# Batch B puzzles for Yea or Nay — 102nd through 110th Congress (senate.gov XML).
# Vote answers are NOT written here; fetch.py pulls every vote from official roll-call
# records. Keys already in puzzles_source.py SENATORS are reused, not redefined.

SENATORS_EXTRA = {
    # key: (bioguide, display name, party, state) — era-accurate party labels
    "mitchell":    ("M000811", "George Mitchell", "D", "ME"),
    "wofford":     ("W000665", "Harris Wofford", "D", "PA"),
    "bkerrey":     ("K000146", "Bob Kerrey", "D", "NE"),
    "hatch":       ("H000338", "Orrin Hatch", "R", "UT"),
    "mikulski":    ("M000702", "Barbara Mikulski", "D", "MD"),
    "hatfield":    ("H000343", "Mark Hatfield", "R", "OR"),
    "snowe":       ("S000663", "Olympia Snowe", "R", "ME"),
    "lott":        ("L000447", "Trent Lott", "R", "MS"),
    "ashcroft":    ("A000356", "John Ashcroft", "R", "MO"),
    "schumer":     ("S000148", "Chuck Schumer", "D", "NY"),
    "jeffords":    ("J000072", "Jim Jeffords", "R", "VT"),   # R until June 2001
    "leahy":       ("L000174", "Patrick Leahy", "D", "VT"),
    "stevens":     ("S000888", "Ted Stevens", "R", "AK"),
    "frist":       ("F000439", "Bill Frist", "R", "TN"),
    "sessions":    ("S001141", "Jeff Sessions", "R", "AL"),
    "sununu":      ("S001078", "John Sununu", "R", "NH"),
    "jwarner":     ("W000154", "John Warner", "R", "VA"),
    "hagel":       ("H001028", "Chuck Hagel", "R", "NE"),
    "webb":        ("W000803", "Jim Webb", "D", "VA"),
    "lieberman_i": ("L000304", "Joe Lieberman", "I", "CT"),  # Independent from 2007
}

PUZZLES = [
    {
        "id": "peace-dividend",
        "title": "The Peace Dividend",
        "era": "102nd Congress · 1992",
        "intro": ("The Cold War is over, the economy is sour, and George Bush is behind "
                  "in the polls. A Democratic Senate spends the autumn sending him "
                  "popular bills — and daring him to keep vetoing them."),
        "senators": [
            ("mitchell", "The Majority Leader: a former federal judge from Maine with a "
                         "prosecutor's patience and a genius for making the President veto "
                         "popular things. He has scheduled the fall's override votes for "
                         "maximum election-season discomfort."),
            ("dole",     "The Republican leader, fighting a rearguard action to keep Bush's "
                         "veto record perfect — 35 vetoes, 35 sustained. With his troops "
                         "drifting home to campaign, every override attempt is a fresh "
                         "headcount."),
            ("specter",  "Pennsylvania's cranky moderate, five weeks from facing voters "
                         "still angry over his grilling of Anita Hill. Labor-friendly by "
                         "Republican standards, he has little appetite for defending "
                         "unpopular vetoes just now."),
            ("wofford",  "The accidental senator: a former college president and "
                         "civil-rights veteran who won a shock 1991 special election on "
                         "national health insurance. His upset is the reason half of "
                         "Washington thinks Bush can lose."),
            ("kassebaum","A plainspoken Kansas Republican — internationalist abroad, "
                         "skeptical of mandates on business at home. She makes up her own "
                         "mind and announces it without drama."),
        ],
        "bills": [
            {
                "congress": 102, "session": 2, "vote": 232,
                "name": "The Family Leave Veto Fight",
                "desc": ("September 24, 1992. Bush has vetoed the family-leave bill — "
                         "twelve weeks of unpaid leave for a new baby or a sick relative "
                         "at companies of fifty or more — calling it a costly mandate on "
                         "business. Democrats schedule the override six weeks before the "
                         "election. Two-thirds needed."),
            },
            {
                "congress": 102, "session": 2, "vote": 253,
                "name": "The START Treaty",
                "desc": ("October 1, 1992. The Strategic Arms Reduction Treaty, signed by "
                         "Bush and Gorbachev before the country Gorbachev led ceased to "
                         "exist. It cuts deployed strategic warheads by roughly a third — "
                         "the first treaty to shrink the arsenals rather than cap them — "
                         "with Russia, Ukraine, Belarus, and Kazakhstan now inheriting "
                         "the Soviet side."),
            },
            {
                "congress": 102, "session": 2, "vote": 264,
                "name": "The Cable TV Act",
                "desc": ("October 5, 1992. Cable rates have roughly tripled since "
                         "deregulation, and this bill lets the FCC cap them. Bush vetoed "
                         "it as re-regulation; the cable and broadcast lobbies are at war "
                         "in the corridors. No Bush veto has ever been overridden — and "
                         "the election is four weeks away."),
            },
        ],
    },
    {
        "id": "hundred-days-93",
        "title": "The Hundred Days of 1993",
        "era": "103rd Congress · 1993",
        "intro": ("Bill Clinton arrives with a Democratic Congress and a to-do list "
                  "Bush's vetoes kept frozen for years. By August, the honeymoon is "
                  "down to a single vote."),
        "senators": [
            ("bkerrey", "Nebraska's Medal of Honor recipient, who ran against Clinton in "
                        "the '92 primaries and hasn't warmed to him since. A deficit hawk "
                        "with a philosopher's temperament, he treats every big vote as a "
                        "crisis of conscience — and lets everyone watch."),
            ("dole",    "The Republican leader, freshly demoted to the minority and "
                        "plotting the road back. With Bush gone, discipline is his "
                        "product: make Clinton's majority carry every hard vote alone."),
            ("boxer",   "A Marin County liberal swept in with the Year of the Woman "
                        "class. She campaigned on exactly this agenda and sees no reason "
                        "to hesitate now."),
            ("nunn",    "Armed Services' Georgia conservative, openly at odds with the "
                        "new White House over gays in the military. Fiscally orthodox, "
                        "socially cautious, and unimpressed by the young administration."),
            ("specter", "Pennsylvania's Republican moderate, back from a bruising "
                        "re-election. Labor-friendly enough to cross the aisle on "
                        "workplace bills — and orthodox enough to hold the line where "
                        "taxes are concerned."),
        ],
        "bills": [
            {
                "congress": 103, "session": 1, "vote": 11,
                "name": "The Family and Medical Leave Act",
                "desc": ("February 4, 1993 — week two of the new administration. The same "
                         "twelve weeks of unpaid leave Bush vetoed twice, back for a "
                         "president who has promised to make it the first bill he signs. "
                         "For Republicans, the question is whether to keep fighting a "
                         "war that's already lost."),
            },
            {
                "congress": 103, "session": 1, "vote": 118,
                "name": "The Motor Voter Act",
                "desc": ("May 11, 1993. Register to vote at the DMV and the welfare "
                         "office. Democrats call it democracy's plumbing; Republicans "
                         "call it an invitation to fraud and a thumb on the partisan "
                         "scale. Bush vetoed it last year — this time the conference "
                         "report is headed to a signature."),
            },
            {
                "congress": 103, "session": 1, "vote": 247,
                "name": "Clinton's First Budget",
                "desc": ("August 6, 1993, nearly 10 p.m. The deficit plan: a 39.6% top "
                         "rate, a 4.3-cent gas tax, an expanded credit for the working "
                         "poor — $496 billion in deficit reduction with not one "
                         "Republican vote for it, anywhere. The chamber is so tightly "
                         "deadlocked that the Vice President waits in the chair to "
                         "break a tie."),
            },
        ],
    },
    {
        "id": "crime-and-trade",
        "title": "Crime & Punishment",
        "era": "103rd Congress · 1994",
        "intro": ("A midterm year with crime atop every poll. Judiciary sends a justice "
                  "to the Court and a crime bill to the floor — then a lame-duck Senate "
                  "takes up the biggest trade deal in history."),
        "senators": [
            ("biden",    "Judiciary's chairman and the crime bill's proud author — a "
                         "Delaware dealmaker who has spent years positioning Democrats "
                         "as the party of cops, prisons, and prevention money alike."),
            ("hatch",    "Utah's courtly conservative, Judiciary's ranking Republican. "
                         "He'll bless a qualified nominee of either party — but he has "
                         "been savaging the crime bill's prevention spending as social "
                         "work wearing a badge."),
            ("feingold", "A first-term Wisconsin reformer with a contrarian streak: "
                         "deficit-minded, suspicious of Washington consensus, and "
                         "unbothered by votes that leave both parties squinting."),
            ("helms",    "'Senator No.' Law-and-order to his boots, protectionist where "
                         "tobacco and textiles are concerned, and reflexively against "
                         "anything blessed by the editorial pages."),
            ("mikulski", "Baltimore's four-foot-eleven force of nature, a former social "
                         "worker who climbed from the city council to the Appropriations "
                         "Committee. Practical, blunt, and loyal to the party's "
                         "working-class base."),
        ],
        "bills": [
            {
                "congress": 103, "session": 2, "vote": 242,
                "name": "Confirming Stephen Breyer",
                "desc": ("July 29, 1994. Clinton's second Supreme Court pick in two "
                         "years: a Harvard professor and appeals judge, an antitrust "
                         "technician praised by both parties' legal establishments. "
                         "After the Bork and Thomas wars, the hearings were almost "
                         "soothing."),
            },
            {
                "congress": 103, "session": 2, "vote": 295,
                "name": "The 1994 Crime Bill",
                "desc": ("August 25, 1994. The conference report: $30 billion for "
                         "100,000 new police officers, new federal death penalties, "
                         "three-strikes sentencing, and the assault-weapons ban — plus "
                         "prevention programs Republicans mock as 'midnight basketball.' "
                         "After the package nearly died in the House, most of the GOP "
                         "has turned against a bill many of them helped shape."),
            },
            {
                "congress": 103, "session": 2, "vote": 329,
                "name": "The GATT World Trade Deal",
                "desc": ("December 1, 1994 — a lame-duck session weeks after the "
                         "Republican landslide. The Uruguay Round: tariff cuts across "
                         "123 nations and a new World Trade Organization to referee "
                         "them. Business is united in favor; an odd alliance of labor "
                         "Democrats, sovereignty conservatives, and Perot voters is "
                         "not."),
            },
        ],
    },
    {
        "id": "one-vote-short",
        "title": "One Vote Short",
        "era": "104th Congress · 1995–1996",
        "intro": ("The Gingrich Congress means to rewire the government itself: a "
                  "balanced-budget amendment that died by a single vote in 1995, a "
                  "line-item veto — and, mid-revolution, a president sending troops "
                  "to the Balkans."),
        "senators": [
            ("hatfield", "Oregon's gentle Republican heretic: a World War II veteran who "
                         "walked the ruins of Hiroshima, an appropriator who believes in "
                         "government, a pacifist in the party of peace through strength. "
                         "Conservatives tried to strip his chairmanship after he defied "
                         "them on the budget amendment last year."),
            ("dole",     "The Leader and nominee-in-waiting, trying to run for president "
                         "from the majority leader's desk. He needs accomplishments to "
                         "campaign on — and his restless right flank takes his "
                         "measurements daily."),
            ("byrd",     "The Senate's constitutional conscience, armored in Article I. "
                         "To Byrd, the appropriations power is the people's leash on "
                         "presidents, and anyone proposing to lend it out is proposing "
                         "vandalism."),
            ("boxer",    "California's unapologetic liberal: she calls the "
                         "balanced-budget craze a slow-motion raid on Social Security "
                         "and the line-item veto a power grab. Her loyalty runs to the "
                         "Democratic White House, not to Senate custom."),
            ("nunn",     "Georgia's defense eminence, headed for retirement and freer by "
                         "the month. A deficit hawk from the party's vanishing "
                         "conservative wing — but on troops and treaties, the chamber "
                         "waits to hear him first."),
        ],
        "bills": [
            {
                "congress": 104, "session": 1, "vote": 603,
                "name": "Troops to Bosnia",
                "desc": ("December 13, 1995. The Dayton accords are signed, and Clinton "
                         "is sending 20,000 Americans to enforce the peace in Bosnia — "
                         "with or without Congress. The resolution backs the troops and "
                         "their mission while registering deep reservations about the "
                         "policy. Somalia's ghosts hang over the debate."),
            },
            {
                "congress": 104, "session": 2, "vote": 56,
                "name": "The Line-Item Veto",
                "desc": ("March 27, 1996. A Contract with America plank handing "
                         "presidents the power to strike individual spending items from "
                         "bills they sign — a power governors have long held and "
                         "presidents have coveted since Grant. Its loudest opponent has "
                         "delivered fourteen floor speeches on the Roman Republic to "
                         "explain what happens next."),
            },
            {
                "congress": 104, "session": 2, "vote": 158,
                "name": "The Balanced Budget Amendment, Again",
                "desc": ("June 6, 1996. Fifteen months after the constitutional "
                         "amendment to balance the budget died a single vote short, "
                         "Dole brings it back for an encore — five days before he "
                         "leaves the Senate for good to run full-time. Two-thirds "
                         "required, and nobody's arithmetic has changed."),
            },
        ],
    },
    {
        "id": "doles-last-year",
        "title": "Dole's Last Year",
        "era": "104th Congress · 1996",
        "intro": ("Bob Dole tries to run for president without leaving the majority "
                  "leader's office. While he juggles, the 104th rewires the phone "
                  "lines, upends sixty years of farm policy, and answers MiGs over "
                  "the Florida Straits."),
        "senators": [
            ("dole",     "The Leader as candidate: 72 years old, wickedly funny in "
                         "private, stiff on camera, trying to legislate his way to the "
                         "nomination. Every floor result is now a campaign story."),
            ("moynihan", "Finance's ranking sage, armed with more history than the "
                         "Congressional Research Service. He judges bills by their "
                         "consequences for the poor and the Republic; party messaging "
                         "concerns him not at all."),
            ("bkerrey",  "Nebraska's restless Vietnam hero, running the Democrats' "
                         "campaign committee while representing a farm state that eyes "
                         "the Republicans' 'Freedom to Farm' revolution warily. "
                         "Contrarian enough to surprise anyone."),
            ("helms",    "Foreign Relations' chairman, at the peak of his powers. Cuban "
                         "MiGs have just shot down two exile aircraft off Havana, and "
                         "Helms means to make the embargo permanent — and personal."),
            ("snowe",    "Maine's freshman Republican, sixteen years in the House behind "
                         "her: pro-choice, pragmatic, attentive to mill towns and dairy "
                         "farms that don't love either party's orthodoxies."),
        ],
        "bills": [
            {
                "congress": 104, "session": 2, "vote": 8,
                "name": "The Telecommunications Act",
                "desc": ("February 1, 1996. The first rewrite of communications law "
                         "since 1934: local phone companies, long-distance carriers, and "
                         "cable systems freed to invade one another's markets, ownership "
                         "caps loosened, and an online 'decency' provision bolted on. "
                         "Nearly everyone is for it; the dissenters warn of merger mania "
                         "and censorship."),
            },
            {
                "congress": 104, "session": 2, "vote": 19,
                "name": "Freedom to Farm",
                "desc": ("February 7, 1996. The end of New Deal agriculture: price "
                         "supports and planting controls replaced by seven years of "
                         "fixed, declining payments and the freedom — or the risk — of "
                         "the open market. Grain prices are high today, which makes the "
                         "deal look better than skeptics think it will feel in a bust."),
            },
            {
                "congress": 104, "session": 2, "vote": 22,
                "name": "The Helms-Burton Act",
                "desc": ("March 5, 1996. Ten days after Cuban jets shot down two "
                         "unarmed exile planes, killing four, the embargo is codified "
                         "into law: no president can lift it alone, and foreign "
                         "companies 'trafficking' in confiscated American property can "
                         "be sued in U.S. courts. Canada and Europe are furious."),
            },
        ],
    },
    {
        "id": "scandal-season",
        "title": "Scandal Season",
        "era": "105th Congress · 1997–1998",
        "intro": ("Peace, prosperity, and a scandal consuming the other end of "
                  "Pennsylvania Avenue. While the country argues about the President's "
                  "conduct, the Senate balances a budget, fights Big Tobacco, and "
                  "spanks the IRS."),
        "senators": [
            ("mccain",    "Commerce's chairman, waging a crusade to make cigarettes "
                          "ruinously expensive — to the horror of much of his own party. "
                          "The maverick brand is polishing itself nicely ahead of 2000."),
            ("lott",      "The Majority Leader: a Mississippi conservative with a whip's "
                          "instinct for counting and a scheduler's power to kill. He "
                          "decides what reaches the floor — and what quietly dies "
                          "waiting."),
            ("kennedy",   "The liberal lion, and a shrewder inside player than the "
                          "oratory suggests: he attached children's health insurance to "
                          "the budget deal and considers tobacco money the way to pay "
                          "for more."),
            ("ashcroft",  "Missouri's religious conservative, testing a presidential run "
                          "on the party's right. He reads most bipartisan deals as "
                          "surrender documents — taxes too high, spending too generous, "
                          "Washington too pleased with itself."),
            ("wellstone", "The happiest warrior of the left, plotting his own quixotic "
                          "presidential tour. He votes his conscience on labor, health, "
                          "and the little guy — and against anything he smells as a "
                          "corporate favor."),
        ],
        "bills": [
            {
                "congress": 105, "session": 1, "vote": 209,
                "name": "The Balanced Budget Act",
                "desc": ("July 31, 1997. A deal to balance the budget by 2002: $115 "
                         "billion in Medicare savings, a new children's health program, "
                         "and a companion bill of tax cuts. After a generation of red "
                         "ink both parties want the credit — and each party's purists "
                         "want no part of it."),
            },
            {
                "congress": 105, "session": 2, "vote": 161,
                "name": "The McCain Tobacco Bill",
                "desc": ("June 17, 1998. $516 billion from the industry over 25 years, "
                         "$1.10 more a pack, FDA authority over nicotine, curbs on "
                         "marketing to kids. The industry has answered with a $40 "
                         "million ad blitz about big taxes and big government. Sixty "
                         "votes to keep the bill alive — and leadership isn't "
                         "helping."),
            },
            {
                "congress": 105, "session": 2, "vote": 189,
                "name": "IRS Restructuring and Reform",
                "desc": ("July 9, 1998. After Finance Committee hearings filled with "
                         "horror stories of abusive collections, a rebuilt IRS: an "
                         "independent oversight board, a taxpayer advocate, and the "
                         "burden of proof shifted to the government in tax court. An "
                         "election-year vote almost nobody wants to explain opposing."),
            },
        ],
    },
    {
        "id": "the-trial",
        "title": "The Trial of the President",
        "era": "106th Congress · 1999",
        "intro": ("For the first time in 131 years, the Senate convenes as a court of "
                  "impeachment: one hundred senators sworn to impartial justice, the "
                  "Chief Justice presiding, sixty-seven votes needed to remove a "
                  "president."),
        "senators": [
            ("collins",  "Maine's junior senator, two years in: methodical, moderate, "
                         "and visibly uncomfortable with both the President's conduct "
                         "and the House managers' case. She spent the trial drafting "
                         "compromise 'findings of fact' that went nowhere."),
            ("mccain",   "Arizona's hawk, weeks from announcing a presidential run built "
                         "on candor and character. He has kept his counsel through the "
                         "trial while his party splinters between constitutional duty "
                         "and political survival."),
            ("byrd",     "The Senate's institutional memory, treating the trial with "
                         "liturgical seriousness. He moved to dismiss the case in "
                         "January — while pronouncing the President's conduct "
                         "indefensible. Both sides claim him; neither is sure."),
            ("feingold", "Wisconsin's civil-libertarian contrarian — the only Democrat "
                         "to vote against dismissing the charges, on the theory that "
                         "the Constitution was owed a full trial. Where the verdict is "
                         "concerned, the theory guarantees nothing."),
            ("specter",  "The former Philadelphia district attorney, a juror with his "
                         "own jurisprudence: unimpressed by the House managers' "
                         "evidence, unwilling to bless the White House's conduct, and "
                         "muttering about verdicts American law doesn't offer."),
        ],
        "bills": [
            {
                "congress": 106, "session": 1, "vote": 17,
                "name": "Article I: Perjury",
                "labels": ["GUILTY", "NOT GUILTY"],
                "question": "Article I of the Articles of Impeachment — Guilty or Not Guilty",
                "result": "Acquitted",
                "desc": ("February 12, 1999. The first article charges President "
                         "Clinton with lying to a federal grand jury about his "
                         "relationship with Monica Lewinsky. A vote of GUILTY is a vote "
                         "to convict and remove the 42nd President; two-thirds — 67 "
                         "senators — are required. The public's verdict is already in: "
                         "his approval sits near 65 percent."),
            },
            {
                "congress": 106, "session": 1, "vote": 18,
                "name": "Article II: Obstruction of Justice",
                "labels": ["GUILTY", "NOT GUILTY"],
                "question": "Article II of the Articles of Impeachment — Guilty or Not Guilty",
                "result": "Acquitted",
                "desc": ("The second article charges a scheme to conceal the affair: "
                         "coaching witnesses, hiding gifts under subpoena, job-hunting "
                         "for a grand-jury witness. It drew more votes in the House "
                         "than perjury and is considered the managers' stronger case. "
                         "GUILTY convicts and removes; sixty-seven still required."),
            },
            {
                "congress": 106, "session": 1, "vote": 57,
                "name": "Air War Over Kosovo",
                "desc": ("March 23, 1999 — six weeks after the trial ends. Slobodan "
                         "Milosevic's forces are purging Kosovo's Albanians, and NATO's "
                         "bombers are hours from launching. The resolution authorizes "
                         "air and missile operations against Yugoslavia: the same "
                         "senators who just judged this president now decide whether "
                         "to follow him to war."),
            },
        ],
    },
    {
        "id": "millennium",
        "title": "The Millennium Senate",
        "era": "106th Congress · 1999–2000",
        "intro": ("Surpluses, dot-com champagne, and a country a month past Columbine. "
                  "On the way to the recount, the Senate decides who checks gun "
                  "buyers, what banks may own, and who pays taxes at death."),
        "senators": [
            ("gramm",     "Banking's chairman, a free-market economics professor who has "
                          "waited a career to bury Depression-era financial law. He "
                          "calls the wall between banking and Wall Street a relic; the "
                          "repeal will carry his name."),
            ("wellstone", "Minnesota's professor-organizer, the surest no in the chamber "
                          "on anything Wall Street wants. He keeps warning that "
                          "memories of 1929 are shorter than the statutes written "
                          "after it."),
            ("schumer",   "Brooklyn's new senator, fresh from toppling Al D'Amato: "
                          "author of the House's Brady Bill and a ferocious gun-control "
                          "advocate — who also represents the financial capital of the "
                          "world and knows who signs his state's paychecks."),
            ("snowe",     "Maine's centrist Republican, a charter member of the "
                          "chamber's shrinking middle. Leadership needs her on close "
                          "votes and never quite knows which way New England "
                          "pragmatism will break."),
            ("helms",     "The old lion of the right, voting as he has since 1973: "
                          "against gun control and death taxes alike, and against "
                          "most things with 'modernization' in the title."),
        ],
        "bills": [
            {
                "congress": 106, "session": 1, "vote": 134,
                "name": "Gun-Show Background Checks",
                "desc": ("May 20, 1999 — one month after two students murdered "
                         "thirteen people at Columbine High School. The Lautenberg "
                         "amendment requires background checks for every gun-show "
                         "sale, closing the private-sale loophole. The chamber has "
                         "spent a week seesawing between rival versions — and this one "
                         "lands in a dead tie, the Vice President waiting in the "
                         "chair."),
            },
            {
                "congress": 106, "session": 1, "vote": 354,
                "name": "Repealing Glass-Steagall",
                "desc": ("November 4, 1999. Gramm-Leach-Bliley tears down the "
                         "Depression-era walls separating banks, brokerages, and "
                         "insurers — ratifying, in effect, the Citicorp-Travelers "
                         "merger that jumped the gun last year. Most of the chamber "
                         "sees modernization; a few dissenters see the next crash "
                         "being chartered."),
            },
            {
                "congress": 106, "session": 2, "vote": 197,
                "name": "Repealing the Estate Tax",
                "desc": ("July 14, 2000. A phased repeal of the estate tax — the "
                         "'death tax,' in messaging that has turned a levy paid by two "
                         "percent of estates into a kitchen-table grievance. Clinton "
                         "has promised a veto, so the vote is really about November. "
                         "Surpluses make everything look affordable."),
            },
        ],
    },
    {
        "id": "jeffords-spring",
        "title": "Jeffords Spring",
        "era": "107th Congress · 2001",
        "intro": ("A president who lost the popular vote meets a Senate split exactly "
                  "50-50, with Dick Cheney breaking ties and committees shared like a "
                  "divorced couple's kitchen. Every senator matters — and one mild "
                  "Vermonter is about to matter most."),
        "senators": [
            ("jeffords", "Vermont's soft-spoken Republican, a moderate the party's "
                         "Texas ascendancy keeps forgetting to consult. He wants full "
                         "funding for special education and a smaller tax cut — "
                         "grievances piling up faster than leadership has noticed."),
            ("zmiller",  "Georgia's new Democrat, an old-school Southern populist who "
                         "keynoted for Clinton in '92 — and signed on as an original "
                         "cosponsor of Bush's tax cut before the ink on his own oath "
                         "was dry."),
            ("mccain",   "The maverick, months past a bitter primary loss to Bush. He "
                         "came back with scores to settle and a signature cause: "
                         "driving unregulated 'soft money' out of American politics."),
            ("feingold", "McCain's Democratic partner in the campaign-finance crusade "
                         "and the chamber's resident purist — he polices his own "
                         "side's loopholes too, and votes against Democratic comforts "
                         "as readily as Republican ones."),
            ("clinton",  "The freshman from New York by way of the White House: "
                         "studiously humble, diligently briefed, voting with her "
                         "caucus while an entire press corps waits for her to do "
                         "something interesting."),
        ],
        "bills": [
            {
                "congress": 107, "session": 1, "vote": 36,
                "name": "The Bankruptcy Bill",
                "desc": ("March 15, 2001. The credit-card industry's bill is back: "
                         "means tests to push filers from Chapter 7 into repayment "
                         "plans, new paperwork, fewer exits. Clinton pocket-vetoed the "
                         "last version in December; the new President is eager to "
                         "sign. Consumer advocates call it a collections agency with "
                         "a gavel."),
            },
            {
                "congress": 107, "session": 1, "vote": 64,
                "name": "McCain-Feingold",
                "desc": ("April 2, 2001. After six years of filibusters, campaign "
                         "finance reform finally passes something: a ban on unlimited "
                         "'soft money' donations to the parties and limits on sham "
                         "'issue ads' before elections. Opponents call it an assault "
                         "on the First Amendment; supporters call it plumbing repair "
                         "for democracy."),
            },
            {
                "congress": 107, "session": 1, "vote": 170,
                "name": "The Bush Tax Cut",
                "desc": ("May 26, 2001. $1.35 trillion over eleven years: lower rates "
                         "in every bracket, rebate checks this summer, the estate tax "
                         "phased toward zero — all sunsetting in 2010 to squeeze under "
                         "budget rules. Two days earlier, Jim Jeffords announced he "
                         "was leaving the Republican Party, handing Democrats the "
                         "Senate; this is the old majority's parting gift to itself."),
            },
        ],
    },
    {
        "id": "homeland",
        "title": "Homeland",
        "era": "107th Congress · 2002",
        "intro": ("One year after the attacks: Enron's shredders, WorldCom's "
                  "restatements, a war debate warming up, and a midterm fought over a "
                  "new Department of Homeland Security. The Senate spends 2002 "
                  "deciding how much to trust this president."),
        "senators": [
            ("byrd",      "The octogenarian keeper of Senate prerogative, pocket "
                          "Constitution at the ready. Speed is the thing he distrusts "
                          "most in government, and 2002 is a year of nothing but "
                          "speed."),
            ("lieberman", "Connecticut's hawkish moralist — Gore's former running mate, "
                          "scourge of corporate misbehavior, and the original author of "
                          "the homeland-security department the White House opposed for "
                          "months before embracing it as its own idea."),
            ("clinton",   "New York's senator, building a national-security résumé "
                          "stone by stone. Her state took the attack; she votes like a "
                          "senator who intends never to be called soft."),
            ("gramm",     "The free-market economist in his final months before "
                          "retirement: dismissive of regulatory stampedes, protective "
                          "of business, and largely past caring what anyone thinks."),
            ("chafee",    "The Senate's loneliest Republican: anti-war, "
                          "pro-environment, wary of executive power. He votes his New "
                          "England conscience and lets the party fume."),
        ],
        "bills": [
            {
                "congress": 107, "session": 2, "vote": 192,
                "name": "Sarbanes-Oxley",
                "desc": ("July 25, 2002. Enron evaporated in December; WorldCom "
                         "confessed to the largest accounting fraud in history three "
                         "weeks ago. The response: a new audit-oversight board, CEOs "
                         "personally certifying their books, and prison time for "
                         "shredding. On final passage, opposition has simply ceased "
                         "to exist."),
            },
            {
                "congress": 107, "session": 2, "vote": 207,
                "name": "Trade Promotion Authority",
                "desc": ("August 1, 2002. Fast-track returns after an eight-year "
                         "lapse: Congress binds itself to yes-or-no votes on whatever "
                         "trade deals the President negotiates. Business calls it "
                         "essential; labor calls it the NAFTA machine restarted. For "
                         "Democrats, it's a loyalty test with no comfortable answer."),
            },
            {
                "congress": 107, "session": 2, "vote": 249,
                "name": "The Homeland Security Act",
                "desc": ("November 19, 2002 — two weeks after a midterm fought "
                         "largely over this bill. Twenty-two agencies and 170,000 "
                         "employees fused into the largest new department since the "
                         "Pentagon, with workforce rules the unions hate and Democrats "
                         "spent months resisting. The election has settled the "
                         "argument for most of them."),
            },
        ],
    },
    {
        "id": "values-election",
        "title": "The Values Election",
        "era": "108th Congress · 2004",
        "intro": ("San Francisco is issuing marriage licenses, Massachusetts courts "
                  "have legalized same-sex marriage, and the assault-weapons ban is "
                  "expiring — all in a presidential year. Karl Rove has done the "
                  "math; the Senate does the voting."),
        "senators": [
            ("santorum", "The Senate's third-ranking Republican and its most fervent "
                         "culture warrior, floor general for the marriage amendment. "
                         "Pennsylvania is purple, but Santorum has never trimmed a "
                         "conviction to fit a state."),
            ("mccain",   "A conservative with a constitutionalist's allergy to amending "
                         "the founding document for politics — and a westerner's "
                         "suspicion of gun laws. In a wedge-issue year, he is nobody's "
                         "reliable wedge."),
            ("collins",  "Maine's moderate: pro-choice, supportive of gay rights by her "
                         "party's standards, and no friend of the gun lobby's "
                         "scorecard. Election-year social policy is exactly the "
                         "terrain she least enjoys."),
            ("boxer",    "California's liberal warhorse, happy to lose culture-war "
                         "votes loudly if losing sharpens the contrast for November."),
            ("byrd",     "West Virginia's patriarch: a traditionalist on marriage and "
                         "faith, a skeptic of constitutional tinkering, and harder to "
                         "handicap on guns than the scorecards assume. He answers to "
                         "the Constitution and to West Virginia, in that order."),
        ],
        "bills": [
            {
                "congress": 108, "session": 2, "vote": 24,
                "name": "Renewing the Assault Weapons Ban",
                "desc": ("March 2, 2004. Feinstein's amendment extends the 1994 "
                         "assault-weapons ban for ten more years, ahead of its "
                         "September expiration — attached to a bill shielding "
                         "gunmakers from lawsuits. The NRA has already passed word "
                         "that if the amendment sticks, the whole bill should die."),
            },
            {
                "congress": 108, "session": 2, "vote": 63,
                "name": "The Unborn Victims of Violence Act",
                "desc": ("March 25, 2004. Laci Peterson's name is on the news and on "
                         "this bill: harming a fetus during a federal crime becomes a "
                         "separate offense, with 'child in utero' defined in federal "
                         "law for the first time. Abortion-rights groups see a "
                         "foundation stone being laid; supporters say it simply names "
                         "a second victim."),
            },
            {
                "congress": 108, "session": 2, "vote": 155,
                "name": "The Federal Marriage Amendment",
                "desc": ("July 14, 2004. A constitutional amendment defining marriage "
                         "as the union of one man and one woman, scheduled four months "
                         "before the election. Sixty votes are needed just to take it "
                         "up, and nobody pretends the count is close — the roll call "
                         "itself is the point. A yea advances the amendment."),
            },
        ],
    },
    {
        "id": "roberts-court",
        "title": "The Roberts Court",
        "era": "109th Congress · 2005–2006",
        "intro": ("William Rehnquist is dead, Sandra Day O'Connor is retiring, and "
                  "George W. Bush gets to redraw the Supreme Court in a single term — "
                  "while the PATRIOT Act, born in six weeks of fear, comes due for "
                  "permanent renewal."),
        "senators": [
            ("obama",    "The freshman phenomenon and former constitutional-law "
                         "lecturer, already swatting away presidential questions. "
                         "Every judicial vote he casts is read as a signal of what he "
                         "might become."),
            ("leahy",    "Judiciary's top Democrat, a Vermont institutionalist who "
                         "still believes qualified nominees deserve respect across "
                         "party lines — even as his base demands total war over the "
                         "Court."),
            ("byrd",     "Eighty-eight now, the Senate's living constitution. He "
                         "judges nominees on deference to Congress and respect for "
                         "the institution — categories that cut across party in ways "
                         "that regularly embarrass the whip counts."),
            ("chafee",   "Rhode Island's endangered Republican moderate, facing a "
                         "brutal 2006 in a deep-blue state. Every high-profile vote "
                         "is a choice between his primary and his general."),
            ("feingold", "The civil libertarian who cast the Senate's only vote "
                         "against the PATRIOT Act in 2001 — and who insists on "
                         "judging judges by their records, not by his party's talking "
                         "points."),
        ],
        "bills": [
            {
                "congress": 109, "session": 1, "vote": 245,
                "name": "Confirming John Roberts",
                "desc": ("September 29, 2005. Rehnquist's former clerk succeeds him "
                         "as Chief Justice: fifty years old, the ABA's highest rating, "
                         "and hearings so polished they left barely a scratch. "
                         "Democrats must decide whether 'brilliant but conservative' "
                         "is a reason to vote no — and they are genuinely split."),
            },
            {
                "congress": 109, "session": 2, "vote": 2,
                "name": "Confirming Samuel Alito",
                "desc": ("January 31, 2006. The stakes double: Alito would replace "
                         "O'Connor, the Court's swing vote, not merely one "
                         "conservative with another. A last-minute filibuster attempt "
                         "has fizzled; now a simple majority decides the seat that "
                         "decides abortion, affirmative action, and executive power."),
            },
            {
                "congress": 109, "session": 2, "vote": 29,
                "name": "Renewing the PATRIOT Act",
                "desc": ("March 2, 2006. The 2001 law's expiring powers made "
                         "permanent, with four-year sunsets on roving wiretaps and "
                         "library-records demands and a handful of negotiated "
                         "safeguards. After a winter standoff — and revelations of "
                         "warrantless NSA wiretapping — most senators have decided "
                         "the fixes are enough. A stubborn few have not."),
            },
        ],
    },
    {
        "id": "pork-and-torture",
        "title": "Pork, Torture & PATRIOT",
        "era": "109th Congress · 2005",
        "intro": ("Autumn 2005: Katrina's bills arriving, Abu Ghraib's photographs "
                  "unforgotten, the PATRIOT Act expiring at New Year's. Three fights "
                  "over what the government may spend — and what it may do."),
        "senators": [
            ("coburn",   "'Dr. No.' The Oklahoma obstetrician hunts earmarks for "
                         "sport, reads appropriations bills for pleasure, and has "
                         "decided a $220 million bridge to an island of fifty people "
                         "is the perfect specimen."),
            ("stevens",  "Alaska's Appropriations titan — thirty-seven years of "
                         "steering federal concrete north. He wears an Incredible "
                         "Hulk necktie on days of battle, and touching Alaska's "
                         "earmarks summons exactly that mood."),
            ("sununu",   "New Hampshire's engineer-Republican, the chamber's youngest "
                         "member and one of its few genuine civil libertarians. He "
                         "has spent months demanding rewrites of the surveillance law "
                         "his party wants renewed untouched."),
            ("feingold", "The PATRIOT Act's original lone dissenter, still insisting "
                         "the question was never whether to fight terrorism but how "
                         "much liberty to charge for it."),
            ("obama",    "The freshman celebrity, picking his shots carefully: "
                         "reformist instincts, a cautious record, and a wary eye on "
                         "how every vote will read in five years."),
        ],
        "bills": [
            {
                "congress": 109, "session": 1, "vote": 249,
                "name": "The McCain Torture Amendment",
                "desc": ("October 5, 2005. John McCain's amendment: no cruel, inhuman, "
                         "or degrading treatment of anyone in U.S. custody, and the "
                         "Army Field Manual as the single interrogation standard. The "
                         "White House threatens a veto; Vice President Cheney lobbies "
                         "for a CIA exemption. McCain, who was tortured in Hanoi, is "
                         "not negotiating."),
            },
            {
                "congress": 109, "session": 1, "vote": 262,
                "name": "The Bridge to Nowhere",
                "desc": ("October 20, 2005. Coburn's amendment would redirect $220 "
                         "million from Alaska's Gravina Island bridge — serving an "
                         "airport and about fifty residents — to rebuild a "
                         "Katrina-shattered Interstate 10 bridge outside New Orleans. "
                         "Stevens threatens to resign on the spot if it passes, and "
                         "the appropriators of both parties close ranks."),
            },
            {
                "congress": 109, "session": 1, "vote": 358,
                "name": "Filibustering the PATRIOT Act",
                "desc": ("December 16, 2005. The PATRIOT reauthorization needs sixty "
                         "votes to advance — and this very morning the New York Times "
                         "revealed that the NSA has been wiretapping Americans "
                         "without warrants. A yea pushes the renewal through as "
                         "written; a nay joins a filibuster demanding stronger "
                         "safeguards first."),
            },
        ],
    },
    {
        "id": "mccain-kennedy",
        "title": "The McCain-Kennedy Moment",
        "era": "109th Congress · 2006",
        "intro": ("Millions march for immigrants in the spring; the flag amendment "
                  "falls one vote short in June; Bush casts the first veto of his "
                  "presidency in July. The 109th's last summer tries a little of "
                  "everything."),
        "senators": [
            ("kennedy",  "Forty-four years in, the liberal lion has found his latest "
                         "unlikely partner: John McCain, on immigration. He wants a "
                         "law, not an issue — and he has traded with harder men than "
                         "this White House."),
            ("mccain",   "The maverick with 2008 in plain view, co-authoring 'amnesty' "
                         "— his enemies' word — with Ted Kennedy while courting the "
                         "conservatives who distrust him. The tightrope act of the "
                         "decade."),
            ("frist",    "The Majority Leader, a Nashville transplant surgeon retiring "
                         "to run for president. He schedules the culture-war votes "
                         "his base demands — and has broken with Bush on the one "
                         "issue where the doctor outranks the politician."),
            ("obama",    "The freshman superstar, notionally focused on Illinois: "
                         "pro-reform on immigration, deliberate everywhere else, "
                         "drafting the persona a national run will require."),
            ("sessions", "Alabama's former federal prosecutor and the floor's most "
                         "relentless immigration hardliner: to Sessions, the "
                         "guest-worker bill is amnesty with paperwork, and no fence "
                         "provision changes that."),
        ],
        "bills": [
            {
                "congress": 109, "session": 2, "vote": 157,
                "name": "Comprehensive Immigration Reform",
                "desc": ("May 25, 2006. The McCain-Kennedy framework: a path to "
                         "citizenship tiered by years in the country, a guest-worker "
                         "program, 370 miles of new fencing, and English declared the "
                         "'national language.' Weeks after millions marched in the "
                         "streets, the Senate attempts what the House has sworn to "
                         "bury."),
            },
            {
                "congress": 109, "session": 2, "vote": 189,
                "name": "The Flag Desecration Amendment",
                "desc": ("June 27, 2006. A constitutional amendment letting Congress "
                         "ban desecration of the American flag, timed for the Fourth "
                         "of July and the fall campaign. Every count says it will "
                         "come within a single vote of the 67 needed — close enough "
                         "that no senator can hide."),
            },
            {
                "congress": 109, "session": 2, "vote": 206,
                "name": "The Stem Cell Research Act",
                "desc": ("July 18, 2006. Federal funding for research on embryonic "
                         "stem-cell lines from IVF embryos already slated for "
                         "disposal. Nancy Reagan is for it; the White House has "
                         "promised the first veto of Bush's presidency; and the "
                         "science-versus-sanctity argument splits both parties along "
                         "unfamiliar seams."),
            },
        ],
    },
    {
        "id": "surge",
        "title": "The Surge Debates",
        "era": "110th Congress · 2007",
        "intro": ("Voters have just handed Congress to the Democrats to end the Iraq "
                  "war; Bush answers with 21,500 more troops. Every few months the "
                  "Senate takes up the same question — can sixty votes stop a war? — "
                  "and the arithmetic never quite works."),
        "senators": [
            ("jwarner",     "Virginia's courtly elder statesman: five terms, a former "
                            "Navy Secretary, the Republican whose doubts about the "
                            "surge carry the most weight. He wrote a resolution "
                            "against it — and hates handing Democrats procedural "
                            "victories almost as much."),
            ("hagel",       "A Vietnam infantry sergeant with two Purple Hearts, now "
                            "the Republicans' fiercest Iraq apostate — he has called "
                            "the surge the most dangerous foreign-policy blunder "
                            "since Vietnam, out loud, in committee."),
            ("lieberman_i", "Re-elected as an independent after Democrats primaried "
                            "him over the war, and freer than ever: the surge's most "
                            "devoted Senate defender, caucusing with a party that can "
                            "barely look at him."),
            ("clinton",     "The Democratic frontrunner, whose 2002 war vote shadows "
                            "every primary event. She is walking backward out of Iraq "
                            "— deliberately, vote by vote, without ever quite saying "
                            "the word 'mistake.'"),
            ("webb",        "Virginia's freshman: decorated Marine, novelist, "
                            "Reagan's Navy Secretary, elected on opposition to the "
                            "war his son is fighting as a lance corporal. Subtle as "
                            "an ambush, and about as friendly to the White House."),
        ],
        "bills": [
            {
                "congress": 110, "session": 1, "vote": 51,
                "name": "Debating the Surge",
                "desc": ("February 17, 2007 — a rare Saturday session. The House has "
                         "passed a resolution disapproving the 21,500-troop "
                         "escalation; this cloture vote decides whether the Senate "
                         "may even take it up. Sixty votes needed. A yea advances "
                         "the rebuke of the surge; a nay keeps it off the floor."),
            },
            {
                "congress": 110, "session": 1, "vote": 252,
                "name": "The Levin-Reed Withdrawal Plan",
                "desc": ("July 18, 2007, after an all-night session complete with "
                         "cots in the cloakrooms. Levin-Reed would order withdrawal "
                         "to begin within 120 days, with most troops out by April "
                         "2008. Sixty votes to advance — and 'wait for General "
                         "Petraeus's September report' has become the Republican "
                         "refrain."),
            },
            {
                "congress": 110, "session": 1, "vote": 349,
                "name": "The Kyl-Lieberman Iran Amendment",
                "desc": ("September 26, 2007. A sense-of-the-Senate measure urging "
                         "that Iran's Revolutionary Guard be designated a terrorist "
                         "organization for arming Shiite militias in Iraq. Supporters "
                         "call it pressure; opponents hear the opening argument for "
                         "the next war. For the candidates in the room, this vote "
                         "will be quoted back for years."),
            },
        ],
    },
]
