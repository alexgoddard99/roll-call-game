# Batch F — TAIL pack: runs Nov 3 (Election Day) -> Nov 14 2026, IN FILE ORDER.
# Concepts F1-F12 from build/batches/CONCEPTS.md. Verified via
#   cd build && python3 fetch.py batches/batch_F.py

SENATORS_EXTRA = {
    # key: (bioguide, display name, party, state) — era-accurate party labels
    "church":     ("C000388", "Frank Church", "D", "ID"),
    "mcgovern":   ("M000452", "George McGovern", "D", "SD"),
    "javits":     ("J000064", "Jacob Javits", "R", "NY"),
    "bayh":       ("B000254", "Birch Bayh", "D", "IN"),
    "ervin":      ("E000211", "Sam Ervin", "D", "NC"),
    "mcsmith":    ("S000590", "Margaret Chase Smith", "R", "ME"),
    "goldwater":  ("G000267", "Barry Goldwater", "R", "AZ"),
    "mlee":       ("L000577", "Mike Lee", "R", "UT"),
    "gillibrand": ("G000555", "Kirsten Gillibrand", "D", "NY"),
    "thurmond":   ("T000254", "Strom Thurmond", "R", "SC"),
    "brooke":     ("B000871", "Edward Brooke", "R", "MA"),
    "rfkennedy":  ("K000114", "Robert F. Kennedy", "D", "NY"),
    "dirksen":    ("D000360", "Everett Dirksen", "R", "IL"),
    "humphrey":   ("H000953", "Hubert Humphrey", "D", "MN"),
    "webb":       ("W000803", "Jim Webb", "D", "VA"),
    "graham":     ("G000359", "Lindsey Graham", "R", "SC"),
    "metzenbaum": ("M000678", "Howard Metzenbaum", "D", "OH"),
    "hatch":      ("H000338", "Orrin Hatch", "R", "UT"),
    "mansfield":  ("M000113", "Mike Mansfield", "D", "MT"),
    "russell":    ("R000536", "Richard Russell", "D", "GA"),
    "hawley":     ("H001089", "Josh Hawley", "R", "MO"),
    "fetterman":  ("F000479", "John Fetterman", "D", "PA"),
}

PUZZLES = [
    {
        "id": "landslides-lame-duck",
        "title": "The Landslide's Lame Duck",
        "era": "96th Congress · November–December 1980",
        "intro": ("Reagan has carried 44 states and the Senate has flipped Republican "
                  "for the first time since 1954. But the old Senate isn't gone yet — "
                  "the defeated return to Washington with six weeks left on the clock."),
        "senators": [
            ("church",   "Chairman of Foreign Relations — for six more weeks. Idaho just "
                         "retired him after four terms, the biggest name on the New Right's "
                         "target list. A conservationist and CIA investigator with unfinished "
                         "business and nothing left to lose."),
            ("mcgovern", "The 1972 presidential nominee, buried by 19 points in South Dakota "
                         "after conservative groups papered the state against him. The "
                         "prairie liberal spends the lame duck voting his conscience one "
                         "last time — it's what got him beaten."),
            ("javits",   "New York's monument of liberal Republicanism, 76 and visibly ill "
                         "with the motor-neuron disease that helped a Long Island unknown "
                         "take his primary. Forty years of civil-rights and social-welfare "
                         "advocacy come down to a final December."),
            ("dole",     "The Kansas wit is one of the winners: come January he chairs the "
                         "Finance Committee in a Republican Senate. He's already thinking "
                         "about the Reagan program — and about not letting the departing "
                         "majority tie his hands on the way out."),
            ("helms",    "The New Right's field marshal, whose fundraising machine helped "
                         "purge the very liberals now serving out the string. He treats the "
                         "lame duck as a holding action: nothing big should pass a Senate "
                         "the voters just repudiated."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 96, "roll": 992,
                "name": "Superfund",
                "question": "On the Stafford Substitute to H.R. 7020", "result": "Agreed to",
                "desc": ("November 24, 1980. Two years after Love Canal, the lame duck's one "
                         "big deal: a $1.6 billion fund — most of it from fees on chemical "
                         "and oil companies — to clean up abandoned toxic-waste dumps, with "
                         "cleanup costs billed to the polluters afterward. This vote on the "
                         "slimmed-down compromise is the decisive roll call; final passage "
                         "follows by voice vote."),
            },
            {
                "source": "voteview", "congress": 96, "roll": 1019,
                "name": "The Fair-Housing Filibuster",
                "question": "On the Cloture Motion (H.R. 5200)", "result": "Cloture Motion Rejected",
                "desc": ("December 9, 1980. The Fair Housing Act of 1968 outlawed housing "
                         "discrimination but gave the government almost no way to enforce "
                         "it; this bill adds administrative judges and real penalties. It is "
                         "Carter's last civil-rights priority, and it is being filibustered. "
                         "A yea ends debate — 60 votes or the bill dies with the Congress."),
            },
            {
                "source": "voteview", "congress": 96, "roll": 1021,
                "name": "Confirming Judge Stephen Breyer",
                "question": "On the Nomination of Stephen G. Breyer", "result": "Nomination Confirmed",
                "desc": ("December 9, 1980. Carter nominates the Senate Judiciary "
                         "Committee's own chief counsel, a 42-year-old Harvard professor "
                         "named Stephen Breyer, to the First Circuit Court of Appeals — "
                         "after the election that threw Carter out. Republicans could "
                         "easily run out the clock and save the seat for Reagan. Do they?"),
            },
        ],
    },
    {
        "id": "nixon-court",
        "title": "The Nixon Court",
        "era": "92nd Congress · 1971–1972",
        "intro": ("Two Supreme Court seats fall vacant in a single September week, and "
                  "Richard Nixon — burned twice by the Senate already — sends up a "
                  "Virginia gentleman and a 47-year-old conservative the liberals "
                  "consider a declaration of war."),
        "senators": [
            ("bayh",     "The Indiana Democrat who led the campaigns that sank Haynsworth "
                         "and Carswell, Nixon's first two failed nominees. Judiciary's "
                         "young constitutional craftsman is deciding whether a third "
                         "confirmation fight in three years is winnable — or wise."),
            ("ervin",    "North Carolina's country-lawyer constitutionalist, a segregationist "
                         "on civil rights who is nonetheless the Senate's fiercest defender "
                         "of the Bill of Rights against wiretaps and databanks. He judges "
                         "nominees by the Constitution as he reads it."),
            ("mcsmith",  "Maine's flinty independent, 74 and facing her last campaign. "
                         "She defied McCarthy in 1950 and votes her own counsel still — "
                         "party labels have never told anyone much about where she'll "
                         "land on a nomination."),
            ("goldwater","Arizona's conservative patriarch, rehabilitated since 1964 and "
                         "delighted that his state's own Bill Rehnquist — a former "
                         "Goldwater campaign lawyer — is up for the Court. On defense "
                         "he wants America second to none, ever."),
            ("javits",   "New York's liberal Republican workhorse, forever crosswise with "
                         "his party's right. He weighs nominees on civil rights and civil "
                         "liberties, and he reads arms-control fine print with a "
                         "lawyer's suspicion of absolutes."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 92, "roll": 408,
                "name": "Confirming Lewis Powell",
                "question": "On the Nomination of Lewis F. Powell Jr.", "result": "Nomination Confirmed",
                "desc": ("December 6, 1971. Lewis Powell of Richmond: past president of the "
                         "American Bar Association, courtly moderate, 64 years old, and so "
                         "broadly respected that even the civil-rights groups hold their "
                         "fire. After the Haynsworth and Carswell debacles, the Senate is "
                         "relieved to be handed a nominee it can live with."),
            },
            {
                "source": "voteview", "congress": 92, "roll": 417,
                "name": "Confirming William Rehnquist",
                "question": "On the Nomination of William H. Rehnquist", "result": "Nomination Confirmed",
                "desc": ("December 10, 1971. The other nominee is a different story: Nixon's "
                         "47-year-old assistant attorney general, the Justice Department's "
                         "house intellectual for wiretapping, surveillance, and preventive "
                         "detention. Civil-rights groups surface a 1964 fight over a Phoenix "
                         "public-accommodations law. Liberals call him an extremist; "
                         "conservatives call him the best mind of his generation."),
            },
            {
                "source": "voteview", "congress": 92, "roll": 824,
                "name": "The Jackson Amendment on SALT",
                "question": "On the Jackson Amendment to S.J. Res. 241", "result": "Amendment Agreed To",
                "desc": ("September 14, 1972. Nixon's SALT interim agreement freezes missile "
                         "launchers — with the Soviets ahead in numbers. Scoop Jackson's "
                         "amendment demands that any future treaty not limit the United "
                         "States to levels inferior to the USSR. Arms-controllers call it a "
                         "poison pill for détente; hawks call it a floor under American "
                         "strength. The White House, needing Jackson, swallows it."),
            },
        ],
    },
    {
        "id": "hundred-days-17",
        "title": "The First Hundred Days of 2017",
        "era": "115th Congress · 2017",
        "intro": ("Donald Trump arrives with unified Republican government and a cabinet "
                  "to confirm, a regulatory rollback moving at repeal-act speed, and a "
                  "treaty that tests what 'America First' actually means."),
        "senators": [
            ("manchin",  "West Virginia's Democrat in a state Trump just carried by 42 "
                         "points. He prides himself on working with any president, breaks "
                         "with his party early and often, and faces re-election next year "
                         "in Trump country."),
            ("warren",   "Massachusetts's progressive champion, days removed from being "
                         "formally silenced on the floor for reading Coretta Scott King's "
                         "letter during a confirmation debate. She has decided the correct "
                         "posture toward this administration is total resistance."),
            ("collins",  "The Maine moderate every whip count starts with. She's already "
                         "opposed one Trump cabinet nominee, guards her independence on "
                         "privacy and consumer issues, and hails from a state that split "
                         "its electoral votes."),
            ("mlee",     "Utah's constitutional originalist, more libertarian than loyalist. "
                         "He reads treaty obligations and federal regulations with the same "
                         "question — where is this written down? — and doesn't mind being "
                         "one of two votes on the losing side."),
            ("mccain",   "The 80-year-old chairman of Armed Services, re-elected just as "
                         "Trump won. He is the Senate's loudest voice for NATO and against "
                         "Vladimir Putin, and his contempt for colleagues who see it "
                         "differently is not private."),
        ],
        "bills": [
            {
                "congress": 115, "session": 1, "vote": 59,
                "name": "Confirming Jeff Sessions",
                "desc": ("February 8, 2017. The Senate votes on one of its own: Jeff "
                         "Sessions of Alabama, Trump's first Senate endorser, to be "
                         "Attorney General. Democrats point to a 1986 judgeship rejection "
                         "over racially charged remarks; Republicans call him a colleague "
                         "of twenty years being smeared. The debate's lasting line comes "
                         "when Elizabeth Warren is cut off mid-letter: 'Nevertheless, she "
                         "persisted.'"),
            },
            {
                "congress": 115, "session": 1, "vote": 94,
                "name": "Repealing the Broadband Privacy Rules",
                "desc": ("March 23, 2017. A Congressional Review Act resolution erasing the "
                         "FCC's brand-new privacy rules, which would have required internet "
                         "providers to get customers' permission before selling their "
                         "browsing histories to advertisers. Repeal also bars the FCC from "
                         "ever writing a substantially similar rule. Providers call the "
                         "rules lopsided; privacy advocates call this a fire sale on your "
                         "web history."),
            },
            {
                "congress": 115, "session": 1, "vote": 98,
                "name": "Montenegro Joins NATO",
                "desc": ("March 28, 2017. Ratifying NATO membership for Montenegro — "
                         "population 620,000, army of about 2,000 — months after an alleged "
                         "Russian-backed coup plot in Podgorica. Supporters call it a "
                         "rebuke to Moscow's sphere; a lonely opposition asks why America "
                         "should extend a war guarantee to a country most voters can't "
                         "find on a map. Two-thirds of senators present required."),
            },
        ],
    },
    {
        "id": "december-rebellion",
        "title": "The December Rebellion",
        "era": "115th Congress · December 2018",
        "intro": ("A lame-duck December with a curious streak of independence: a farm "
                  "bill, a rebuke of a war, and a criminal-justice bill the Senate's "
                  "leadership never wanted on the floor."),
        "senators": [
            ("sanders",  "Vermont's democratic socialist has spent months building an odd-"
                         "couple coalition against American support for the Saudi war in "
                         "Yemen. Fresh off a re-election landslide, he smells a floor "
                         "victory that was unthinkable a year ago."),
            ("gillibrand","New York's Democrat, weeks from launching a presidential "
                         "campaign. Once a Blue Dog House member with an NRA A-rating, she "
                         "has remade herself as a progressive and now votes accordingly — "
                         "her critics say conveniently, her allies say convincingly."),
            ("mlee",     "Utah's constitutional conservative and the Republican co-author "
                         "of the war-powers push — Congress, he insists, never declared "
                         "this war. The same first-principles streak makes him allergic to "
                         "big omnibus spending on general principle."),
            ("cotton",   "The Arkansas hawk and self-appointed guardian against going soft "
                         "on crime. He has spent December warning that the sentencing bill "
                         "frees 'sex offenders and violent felons,' offering amendments to "
                         "gut it, and losing friends in the White House."),
            ("murkowski","Alaska's independent-minded Republican, loyal mostly to Alaska. "
                         "She weighs every December bill against home-state math — "
                         "fisheries in the farm bill, military bases, native communities — "
                         "and is never afraid to be one of a dozen holdouts."),
        ],
        "bills": [
            {
                "congress": 115, "session": 2, "vote": 259,
                "name": "The 2018 Farm Bill",
                "desc": ("December 11, 2018. The $867 billion farm bill conference report: "
                         "five more years of crop supports and food stamps, with the "
                         "House's stricter SNAP work requirements stripped out — and, "
                         "thanks to the Majority Leader himself, the legalization of "
                         "industrial hemp. Farm country, mid-trade-war, wants this signed "
                         "yesterday."),
            },
            {
                "congress": 115, "session": 2, "vote": 266,
                "name": "Yemen War Powers Resolution",
                "desc": ("December 13, 2018 — ten weeks after Jamal Khashoggi's murder. For "
                         "the first time in the War Powers Act's 45 years, a chamber of "
                         "Congress votes to order U.S. forces out of a conflict: American "
                         "refueling and targeting support for the Saudi-led war in Yemen, "
                         "where famine looms. A yea directs the president to withdraw "
                         "that support."),
            },
            {
                "congress": 115, "session": 2, "vote": 271,
                "name": "The First Step Act",
                "desc": ("December 18, 2018. The broadest federal sentencing reform in a "
                         "generation: retroactive relief from the crack-cocaine disparity, "
                         "expanded good-time credits and earned early release, and a wider "
                         "safety valve around mandatory minimums. Jared Kushner lobbied "
                         "for it, Trump endorsed it, and the toughest opposition comes "
                         "from inside the Republican conference."),
            },
        ],
    },
    {
        "id": "mr-justice-marshall",
        "title": "Mr. Justice Marshall",
        "era": "90th Congress · 1967",
        "intro": ("The summer Detroit and Newark burn, Lyndon Johnson sends the Senate a "
                  "nomination he calls 'the right thing to do, the right time to do it, "
                  "the right man and the right place' — and dares it to say no."),
        "senators": [
            ("kennedy",  "The youngest Kennedy brother, 35, already a fluent Senate "
                         "operator with an eye for civil-rights and immigration causes. "
                         "The Judiciary Committee's southern bulls treat him as the "
                         "liberal opposition's floor manager in training."),
            ("ervin",    "The Judiciary Committee's self-styled country lawyer from North "
                         "Carolina, who quizzes nominees on antebellum case law the way "
                         "other men play chess. A segregationist on civil rights who calls "
                         "his objections purely constitutional — 'judicial activism' being "
                         "the charge."),
            ("thurmond", "South Carolina's converted Republican and the record-holder for "
                         "the longest one-man filibuster, set against a civil-rights bill. "
                         "In committee he subjects nominees to hostile pop quizzes; on "
                         "anything touching Moscow he sees appeasement."),
            ("brooke",   "Massachusetts Republican Edward Brooke — the first Black senator "
                         "since Reconstruction, elected statewide by a white electorate. "
                         "A pragmatic moderate on most things, he understands better than "
                         "anyone in the chamber what certain firsts cost and mean."),
            ("byrd",     "West Virginia's tireless workhorse, a New Dealer on economics "
                         "who filibustered the 1964 Civil Rights Act and hasn't warmed "
                         "much since. He is climbing the leadership ladder rung by rung "
                         "and rarely gets caught on the unpopular side of a home-state "
                         "issue."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 90, "roll": 50,
                "name": "The Soviet Consular Treaty",
                "question": "On the Resolution of Ratification (Executive D)", "result": "Convention Ratified",
                "desc": ("March 16, 1967. The first bilateral treaty with the Soviet Union "
                         "ever sent to the Senate: consulates in each other's cities, and a "
                         "guarantee that arrested Americans see a U.S. official within four "
                         "days. The John Birch Society mails a million letters calling "
                         "consulates spy nests; J. Edgar Hoover is quoted on both sides. "
                         "Two-thirds required."),
            },
            {
                "source": "voteview", "congress": 90, "roll": 176,
                "name": "Confirming Thurgood Marshall",
                "question": "On the Nomination of Thurgood Marshall", "result": "Nomination Confirmed",
                "desc": ("August 30, 1967. Thurgood Marshall — the NAACP lawyer who argued "
                         "Brown v. Board and won 29 of 32 cases before the Supreme Court, "
                         "now Solicitor General — is nominated to be the first Black "
                         "justice in the Court's 178 years. Southern senators grill him "
                         "for days on obscure constitutional history, hunting for grounds "
                         "everyone understands are beside the point."),
            },
            {
                "source": "voteview", "congress": 90, "roll": 275,
                "name": "The Social Security Amendments of 1967",
                "question": "On Passage of H.R. 12080", "result": "Bill Passed",
                "desc": ("November 22, 1967. A 13-percent Social Security benefit increase — "
                         "the largest cash raise yet — paired with the Great Society's "
                         "first retrenchment: new limits on Medicaid and controversial "
                         "work requirements and a freeze aimed at welfare rolls. Liberals "
                         "grumble about the strings; conservatives about the price. "
                         "Election year approaches."),
            },
        ],
    },
    {
        "id": "right-to-work-war",
        "title": "The Right-to-Work War",
        "era": "89th Congress · 1965–1966",
        "intro": ("Organized labor delivered for Lyndon Johnson, and now it wants its "
                  "prize: repeal of the law that lets states ban the union shop. Standing "
                  "in the way is the best filibuster general since the Southerners."),
        "senators": [
            ("rfkennedy","New York's freshman senator — attorney general until last year, "
                         "carrying his brother's coalition and his own restless ambition. "
                         "Labor is bedrock for him, and on the war his doubts are still "
                         "private, still forming."),
            ("byrd",     "West Virginia coal country's tireless Democrat, a New Dealer on "
                         "spending who nonetheless keeps his own counsel on labor's "
                         "wish list — the state's mine operators and its miners don't "
                         "always want the same thing. Studying the rulebook, always."),
            ("dirksen",  "The Minority Leader, a baroque orator with a voice like a pipe "
                         "organ. Having delivered Republican votes for civil rights, he "
                         "now leads the other kind of campaign: a filibuster he calls a "
                         "defense of the states, waged with evident relish."),
            ("thurmond", "South Carolina's brand-new Republican, who bolted the Democrats "
                         "to campaign for Goldwater. Right-to-work is practically the "
                         "reason his state's textile belt exists, and he sees no "
                         "contradiction between hawkishness abroad and union-fighting at "
                         "home."),
            ("javits",   "The great outlier: a New York Republican with a labor-liberal "
                         "voting record that shames half the Democratic caucus. He wins "
                         "union endorsements in a state where that's how Republicans "
                         "survive — and his party leadership has stopped being surprised."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 89, "roll": 248,
                "name": "Repealing Right-to-Work — Cloture",
                "question": "On the Cloture Motion (H.R. 77)", "result": "Cloture Motion Rejected",
                "desc": ("October 11, 1965. Section 14(b) of Taft-Hartley lets 19 states "
                         "outlaw the union shop; repealing it is the AFL-CIO's price for a "
                         "decade of loyalty. The House has passed repeal, Johnson has "
                         "endorsed it, and Everett Dirksen has organized a filibuster. A "
                         "yea votes to break it — two-thirds of those voting required, and "
                         "labor is watching every name."),
            },
            {
                "source": "voteview", "congress": 89, "roll": 272,
                "name": "The Vietnam Supplemental",
                "question": "On Passage of S. 2791", "result": "Bill Passed",
                "desc": ("March 1, 1966. An emergency $4.8 billion authorization for the "
                         "war — 215,000 Americans are in Vietnam and more are going. Hours "
                         "earlier the Senate tabled Wayne Morse's amendment to repeal the "
                         "Gulf of Tonkin Resolution itself, 92 to 5. Now comes the money. "
                         "Doubters must decide whether doubt means voting against the "
                         "troops' supplies."),
            },
            {
                "source": "voteview", "congress": 89, "roll": 438,
                "name": "The Minimum Wage Act of 1966",
                "question": "On Passage of H.R. 13712", "result": "Bill Passed",
                "desc": ("August 26, 1966. Raising the minimum wage from $1.25 to $1.60 by "
                         "1968 — and, for the first time ever, extending it to farm "
                         "workers, hotel maids, and hospital orderlies: about eight "
                         "million people the New Deal left out. Business warns of price "
                         "inflation; southern growers warn of ruin; labor calls it "
                         "thirty years overdue."),
            },
        ],
    },
    {
        "id": "watergate-winter",
        "title": "The Watergate Winter",
        "era": "93rd Congress · 1974",
        "intro": ("The year the system reboots itself: campaign money gets rules in "
                  "April, Nixon resigns in August, and by December the Senate is "
                  "confirming a Rockefeller and rewiring world trade in the same week."),
        "senators": [
            ("kennedy",  "The keeper of the Kennedy flame, who took himself out of the "
                         "1976 race in September. He pushes campaign-finance reform as "
                         "the Watergate cure and reads every Republican nomination "
                         "through the lens of accountability."),
            ("humphrey", "The Happy Warrior, back in the Senate since 1971 and at peace "
                         "with it. His own 1968 campaign's fundraising embarrassments "
                         "made him a convert to public financing; on trade and aid he "
                         "remains liberalism's tireless evangelist."),
            ("helms",    "The freshman from North Carolina and the purest voice of the "
                         "New Right: against détente, against big spending, and deeply "
                         "against rewarding the Republican establishment's favorite "
                         "New York liberal with the vice presidency."),
            ("brooke",   "Massachusetts's liberal Republican — the first Black senator "
                         "since Reconstruction — who was also the first Republican "
                         "senator to call for Nixon's resignation. A Rockefeller "
                         "Republican in the most literal sense of the term."),
            ("dole",     "Kansas's sharp-tongued partisan, freshly scarred: he ran the "
                         "RNC during Watergate's early days and just survived a brutal "
                         "re-election because of it. He is recalibrating — loyal to the "
                         "party, wary of anything that smells like the old regime."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 93, "roll": 732,
                "name": "The Campaign Finance Overhaul",
                "question": "On Passage of S. 3044", "result": "Bill Passed",
                "desc": ("April 11, 1974 — as the Watergate hearings' revelations about "
                         "suitcases of cash still hang in the air. The Senate's answer: "
                         "strict contribution and spending limits, an independent Federal "
                         "Election Commission, and public financing of campaigns. "
                         "Opponents call it incumbent protection and a raid on the "
                         "Treasury; supporters call it the minimum Watergate demands."),
            },
            {
                "source": "voteview", "congress": 93, "roll": 1092,
                "name": "Nelson Rockefeller for Vice President",
                "question": "On the Nomination of Nelson A. Rockefeller", "result": "Nomination Confirmed",
                "desc": ("December 10, 1974. The 25th Amendment's second workout: Gerald "
                         "Ford, an unelected president, nominates Nelson Rockefeller, the "
                         "four-term governor of New York, as his unelected vice president. "
                         "Four months of hearings have inventoried the family fortune — "
                         "including a $50,000 gift to Henry Kissinger. Conservatives have "
                         "loathed Rocky since 1964; most everyone else wants the chair "
                         "filled."),
            },
            {
                "source": "voteview", "congress": 93, "roll": 1138,
                "name": "The Trade Act & Jackson-Vanik",
                "question": "On the Conference Report (H.R. 10710)", "result": "Conference Report Agreed To",
                "desc": ("December 20, 1974. The Trade Act creates fast-track authority "
                         "and carries the Jackson-Vanik amendment: no trade privileges "
                         "for communist countries that block emigration — aimed squarely "
                         "at Moscow's exit taxes on Soviet Jews. Kissinger warns it will "
                         "poison détente; Jackson calls linking commerce to human beings "
                         "the whole point."),
            },
        ],
    },
    {
        "id": "home-front-08",
        "title": "The Home Front",
        "era": "110th Congress · 2008",
        "intro": ("Three senators in this chamber are running for president, and two of "
                  "them keep flying back for votes. Between primaries, the Senate takes "
                  "up paychecks, veterans, and the wiretaps nobody wants to own."),
        "senators": [
            ("obama",    "The Democratic front-runner, weeks from clinching. He has "
                         "promised the netroots he'll stand firm on civil liberties — "
                         "including a pledge to filibuster telecom immunity — but the "
                         "general election is coming into view, and with it the center."),
            ("clinton",  "The New York senator fighting to the last primary. With the "
                         "nomination slipping away she has less reason than ever to "
                         "hedge — and a hawkish record she can now afford to complicate "
                         "with some liberal conscience votes."),
            ("webb",     "Virginia's freshman: Reagan's Navy Secretary turned Democrat, "
                         "a novelist with combat boots in his office and a son back from "
                         "Ramadi. He has one obsession this year — veterans' education — "
                         "and the patience of a man who wrote the bill himself."),
            ("graham",   "South Carolina's Republican, John McCain's closest friend and "
                         "campaign surrogate. A JAG colonel in the reserves, he backs the "
                         "administration on surveillance and worries aloud that overly "
                         "generous benefits will tempt sergeants to leave the service."),
            ("mcconnell","The Republican leader, running his conference's defense in a "
                         "brutal cycle. He holds the line for Bush on national security "
                         "and against what he calls trial-lawyer bait — while trying not "
                         "to hand Democrats election-year ammunition."),
        ],
        "bills": [
            {
                "congress": 110, "session": 2, "vote": 110,
                "name": "The Lilly Ledbetter Fair Pay Bill",
                "desc": ("April 23, 2008. The Supreme Court threw out Lilly Ledbetter's "
                         "pay-discrimination case because she sued more than 180 days "
                         "after the first unequal paycheck — decades of smaller ones "
                         "notwithstanding. This bill restarts the clock with each "
                         "paycheck. Both Democratic candidates fly in for the vote; "
                         "business groups warn of endless lawsuits. Sixty votes needed "
                         "to proceed."),
            },
            {
                "congress": 110, "session": 2, "vote": 137,
                "name": "The Post-9/11 GI Bill",
                "desc": ("May 22, 2008. Jim Webb's new GI Bill, attached to the war "
                         "supplemental: full in-state tuition plus a housing stipend for "
                         "anyone with three years' service since 9/11 — restoring the "
                         "World War II-era promise. The Pentagon and President Bush "
                         "object that it's so generous it will hurt retention; Webb "
                         "answers that readjustment is what the country owes."),
            },
            {
                "congress": 110, "session": 2, "vote": 168,
                "name": "The FISA Amendments Act",
                "desc": ("July 9, 2008. The surveillance compromise: court-supervised "
                         "procedures for warrantless monitoring of foreign targets — and "
                         "retroactive immunity for the telecom companies that helped the "
                         "NSA after 9/11, wiping out some forty lawsuits. Civil "
                         "libertarians call immunity a cover-up ratified; the intelligence "
                         "community calls the bill indispensable. Campaign promises "
                         "collide with October."),
            },
        ],
    },
    {
        "id": "judges-trials",
        "title": "The Other Impeachments",
        "era": "99th–101st Congress · 1986–1989",
        "intro": ("For fifty years the Senate's impeachment machinery gathered dust. "
                  "Then, in three years, three federal judges — one drawing his salary "
                  "from a prison cell, one acquitted by a jury, one who refuses to "
                  "resign — put it back to work."),
        "senators": [
            ("kennedy",  "The liberal lion, two decades into his Senate career and a "
                         "senior hand on Judiciary. He helped write the modern rules for "
                         "judging judges and takes the Senate's constitutional court "
                         "duty with unfashionable seriousness."),
            ("moynihan", "New York's scholar-senator, the Senate's resident social "
                         "scientist and its most quotable skeptic of tidy answers. He "
                         "frets in learned footnotes about precedent: what exactly does "
                         "it mean to convict a man a jury has freed?"),
            ("metzenbaum","Ohio's combative liberal millionaire, the chamber's designated "
                         "obstacle to bad bills and worse nominees. A former trial "
                         "lawyer, he holds the government to its burden of proof even "
                         "when the defendant is unsympathetic — especially then."),
            ("specter",  "Pennsylvania's Republican and a former Philadelphia district "
                         "attorney who treats Senate trials like actual trials. He "
                         "cross-examines witnesses himself, follows the evidence wherever "
                         "it goes, and infuriates both parties at predictable intervals."),
            ("hatch",    "Utah's Judiciary Republican, a stickler for process with a "
                         "soft spot for due process. He wants corrupt judges gone — but "
                         "he wants the Senate's shortcuts on the record, and he isn't "
                         "above voting his doubts."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 99, "roll": 716,
                "name": "The Trial of Judge Claiborne",
                "labels": ["GUILTY", "NOT GUILTY"],
                "question": "Article I of the Articles of Impeachment — Guilty or Not Guilty",
                "result": "Guilty",
                "desc": ("October 9, 1986. Harry Claiborne, U.S. district judge for "
                         "Nevada, convicted of tax fraud in 1984 — and still drawing his "
                         "$78,700 judicial salary from a federal prison cell, since only "
                         "impeachment can remove him. Article I charges him with "
                         "falsifying his 1979 return. A vote of GUILTY removes him; "
                         "two-thirds required. It is the Senate's first impeachment "
                         "verdict in 50 years."),
            },
            {
                "congress": 101, "session": 1, "vote": 254,
                "name": "The Trial of Judge Hastings",
                "labels": ["GUILTY", "NOT GUILTY"],
                "desc": ("October 20, 1989. Alcee Hastings of Florida, one of the first "
                         "Black federal judges in the Deep South — acquitted by a jury in "
                         "1983 of conspiring to solicit a $150,000 bribe, then impeached "
                         "413-3 by a House convinced his co-conspirator's silence bought "
                         "the verdict. Article I is the bribery conspiracy. GUILTY "
                         "removes him from the bench; two-thirds required. No one "
                         "acquitted at trial has ever been removed."),
            },
            {
                "congress": 101, "session": 1, "vote": 286,
                "name": "The Trial of Judge Nixon",
                "labels": ["GUILTY", "NOT GUILTY"],
                "desc": ("November 3, 1989. Walter Nixon, chief U.S. district judge in "
                         "Mississippi, imprisoned for lying to a grand jury about "
                         "intervening in the drug prosecution of a business partner's "
                         "son. He has refused to resign, collecting his salary from "
                         "prison and insisting the perjury verdict was wrong. Article I "
                         "charges the false statements. GUILTY removes him; two-thirds "
                         "required."),
            },
        ],
    },
    {
        "id": "last-gift-congress",
        "title": "The Last Gift",
        "era": "118th Congress · December 2024",
        "intro": ("A divided Congress limps to the exits: a defense bill with a culture-"
                  "war rider, a Social Security fix forty years in the making, and a "
                  "shutdown countdown that Elon Musk detonates by tweet."),
        "senators": [
            ("sanders",  "Vermont's 83-year-old independent, just re-elected, planning to "
                         "spend the Trump years on 'oligarchy' tours. He weighs every "
                         "year-end bill against working-class arithmetic — and against "
                         "a Pentagon budget he considers institutionally unauditable."),
            ("warnock",  "Georgia's pastor-senator, keeper of the Ebenezer pulpit and a "
                         "swing-state Democrat with four elections in three years behind "
                         "him. Retired teachers, police officers, and firefighters are "
                         "his kind of constituency, and December is for delivering."),
            ("fetterman","Pennsylvania's hoodie-wearing Democrat, cultivating a post-"
                         "election reputation for contrarian bluntness. He likes bills "
                         "that put money in workers' pockets and has little patience for "
                         "procedural martyrdom on either side."),
            ("cruz",     "Texas's conservative brawler, fresh off re-election and about "
                         "to chair the Commerce Committee. He rails against year-end "
                         "spending blowouts — but incoming chairmen also like planes, "
                         "ships, and bases, and Texas has plenty."),
            ("romney",   "Utah's departing Republican, casting his final votes. The 2012 "
                         "nominee leaves as his party's most unsparing internal critic, "
                         "with a deficit ledger where his heart is and no election left "
                         "to lose."),
        ],
        "bills": [
            {
                "congress": 118, "session": 2, "vote": 325,
                "name": "The FY2025 Defense Bill",
                "desc": ("December 18, 2024. The $895 billion National Defense "
                         "Authorization Act: a 14.5 percent raise for junior enlisted "
                         "troops, submarines, drones — and a rider barring the military "
                         "health plan from covering certain treatments for "
                         "servicemembers' transgender children, which has peeled away "
                         "Democratic votes that the bill's pay raise would normally "
                         "lock down."),
            },
            {
                "congress": 118, "session": 2, "vote": 338,
                "name": "The Social Security Fairness Act",
                "desc": ("December 21, 2024. Repealing two 1980s formulas — the Windfall "
                         "Elimination Provision and Government Pension Offset — that "
                         "reduce Social Security for some 2.8 million retired teachers, "
                         "firefighters, and police with public pensions. Cost: nearly "
                         "$200 billion over a decade, moving the trust fund's insolvency "
                         "date closer. Unions call it justice; budget hawks call it an "
                         "unpaid-for giveaway."),
            },
            {
                "congress": 118, "session": 2, "vote": 339,
                "name": "The Shutdown-Averting Deal",
                "desc": ("December 21, 2024, after midnight. The original bipartisan "
                         "year-end deal was killed in 48 hours by Elon Musk's posts and "
                         "Donald Trump's demand to raise the debt ceiling early. This "
                         "stripped-down replacement funds the government to March 14, "
                         "adds $100 billion for hurricane-battered states and $10 "
                         "billion for farmers — and drops the debt-limit demand "
                         "entirely."),
            },
        ],
    },
    {
        "id": "summer-of-2022",
        "title": "The Summer of 2022",
        "era": "117th Congress · 2022",
        "intro": ("A leaked draft opinion, a fourth-grade classroom in Uvalde, and a "
                  "war on Europe's edge: in four months the 50-50 Senate answers all "
                  "three — each time with a different coalition."),
        "senators": [
            ("manchin",  "West Virginia's Democrat and the chamber's pivot point. A "
                         "gun-owning, coal-state Catholic who says Roe should be codified "
                         "but calls this year's version a bridge too far — and who has "
                         "spent 2022 defining what Democrats can't pass."),
            ("baldwin",  "Wisconsin's progressive Democrat, the first openly gay senator, "
                         "quietly effective at attaching her priorities to moving "
                         "vehicles. On guns she carries Milwaukee's grief; on NATO, a "
                         "border-state Midwesterner's clarity about Russia."),
            ("collins",  "The Maine institutionalist who says Roe is settled law and has "
                         "her own narrower bill to prove it — while calling the "
                         "Democrats' version a vehicle designed to fail. On guns, one "
                         "of the few Republicans negotiators bother calling first."),
            ("murkowski","Alaska's ranked-choice Republican, running this fall against a "
                         "Trump-endorsed challenger. Pro-choice by her own lights but "
                         "particular about statutory language, and independent enough "
                         "that both parties routinely misjudge her."),
            ("hawley",   "Missouri's populist Republican, the man who raised a fist to "
                         "the January 6th crowd. He has concluded that America's real "
                         "adversary is China — and that Europe's defense, gun deals, "
                         "and most bipartisan gangs are distractions from that fight."),
        ],
        "bills": [
            {
                "congress": 117, "session": 2, "vote": 170,
                "name": "The Women's Health Protection Act",
                "desc": ("May 11, 2022 — nine days after the leaked draft of Dobbs. The "
                         "Democrats' bill to write abortion rights into federal statute, "
                         "preempting state bans and restrictions beyond Roe's baseline. "
                         "Republicans call it abortion on demand; two pro-choice "
                         "senators call it overbroad and offer a narrower rival. Sixty "
                         "votes needed even to proceed — this vote is about the message."),
            },
            {
                "congress": 117, "session": 2, "vote": 242,
                "name": "The Bipartisan Safer Communities Act",
                "desc": ("June 23, 2022, a month after Uvalde. The first significant gun "
                         "law in nearly thirty years: enhanced background checks for "
                         "buyers under 21, money for state red-flag laws, closing the "
                         "'boyfriend loophole,' and billions for mental health and school "
                         "security. The NRA is opposed; fifteen Republicans have signed "
                         "on anyway. Careers are on the line."),
            },
            {
                "congress": 117, "session": 2, "vote": 282,
                "name": "Finland & Sweden Join NATO",
                "desc": ("August 3, 2022. Five months into Russia's invasion of Ukraine, "
                         "the Senate votes on admitting Finland and Sweden — ending two "
                         "centuries of Swedish neutrality and doubling NATO's border "
                         "with Russia. Ratification requires two-thirds; the only "
                         "suspense is whether the skeptics of European commitments will "
                         "make anyone take a hard vote."),
            },
        ],
    },
    {
        "id": "new-frontier",
        "title": "The New Frontier",
        "era": "87th Congress · 1962",
        "intro": ("John Kennedy's second year: a United Nations short of cash, a "
                  "communications satellite the liberals call a giveaway, and a trade "
                  "bill the President says will decide whether America leads the new "
                  "Atlantic economy."),
        "senators": [
            ("mansfield","The new Majority Leader, a laconic Montanan running the Senate "
                         "by consent where Johnson ran it by the lapels. He co-sponsors "
                         "the administration's compromises personally and hates making "
                         "any senator walk a plank."),
            ("dirksen",  "The Minority Leader, whose ornate baritone can make a "
                         "procedural motion sound like scripture. He relishes being the "
                         "administration's indispensable Republican partner — at a price, "
                         "publicly negotiated, item by item."),
            ("humphrey", "The Majority Whip, liberalism's happiest warrior, evangelist "
                         "for every internationalist cause from food aid to the UN. His "
                         "job this year: holding restless liberals in line for Kennedy's "
                         "compromises."),
            ("goldwater","Arizona's conservative standard-bearer, whose 'Conscience of a "
                         "Conservative' is outselling most novels. He sees creeping "
                         "socialism in Washington and creeping surrender in Turtle Bay, "
                         "and his no votes are becoming a movement's scorecard."),
            ("russell",  "The courtly Georgian who commands the Southern bloc and the "
                         "Armed Services gavel. A nationalist wary of entangling "
                         "institutions, protective of Senate rules — the filibuster "
                         "above all — and of an older, tariff-minded economy."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 87, "roll": 232,
                "name": "The UN Rescue Loan",
                "question": "On Passage of S. 2768", "result": "Bill Passed",
                "desc": ("April 5, 1962. The United Nations is nearly broke — the Congo "
                         "peacekeeping operation has drained its treasury while the "
                         "Soviet Union and France refuse to pay their share. Kennedy asks "
                         "authority to buy up to $100 million in UN bonds. Supporters "
                         "call it saving the organization America built; critics ask why "
                         "Washington should bankroll deadbeats' wars."),
            },
            {
                "source": "voteview", "congress": 87, "roll": 318,
                "name": "The Comsat Filibuster",
                "question": "On the Cloture Motion (H.R. 11040)", "result": "Cloture Motion Agreed To",
                "desc": ("August 14, 1962. Kennedy's bill puts the world's first "
                         "commercial communications satellites under a private "
                         "corporation, and a band of liberals — crying 'giveaway to "
                         "AT&T' of taxpayer-funded space research — has filibustered it "
                         "for days. A yea ends debate. No cloture motion has succeeded "
                         "since 1927, and the Southerners guard the filibuster like "
                         "scripture."),
            },
            {
                "source": "voteview", "congress": 87, "roll": 392,
                "name": "The Trade Expansion Act",
                "question": "On Passage of H.R. 11970", "result": "Bill Passed",
                "desc": ("September 19, 1962. Kennedy's top legislative priority: "
                         "authority to cut tariffs up to 50 percent — to zero on some "
                         "goods traded with Europe's booming Common Market — plus a new "
                         "idea called trade adjustment assistance for workers displaced "
                         "by imports. Protectionists object; the President calls it the "
                         "most important international measure since the Marshall Plan."),
            },
        ],
    },
]
