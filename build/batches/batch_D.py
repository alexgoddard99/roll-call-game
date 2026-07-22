# Batch D puzzles for Yea or Nay — 116th-119th Congress plus cross-era specials.
# Vote answers are NOT written here; fetch.py verifies every roll call against
# senate.gov XML. See batches/BRIEF.md.

SENATORS_EXTRA = {
    # key: (bioguide, display name, party, state)
    "mlee":      ("L000577", "Mike Lee", "R", "UT"),
    "tester":    ("T000464", "Jon Tester", "D", "MT"),
    "hawley":    ("H001089", "Josh Hawley", "R", "MO"),
    "graham":    ("G000359", "Lindsey Graham", "R", "SC"),
    "burr":      ("B001135", "Richard Burr", "R", "NC"),
    "cassidy":   ("C001075", "Bill Cassidy", "R", "LA"),
    "merkley":   ("M001176", "Jeff Merkley", "D", "OR"),
    "fetterman": ("F000479", "John Fetterman", "D", "PA"),
    "vance":     ("V000137", "J.D. Vance", "R", "OH"),
    "lankford":  ("L000575", "James Lankford", "R", "OK"),
    "cmurphy":   ("M001169", "Chris Murphy", "D", "CT"),
    "pmurray":   ("M001111", "Patty Murray", "D", "WA"),
    "schumer":   ("S000148", "Chuck Schumer", "D", "NY"),
    "inhofe":    ("I000024", "Jim Inhofe", "R", "OK"),
    "jwarner":   ("W000154", "John Warner", "R", "VA"),
    "cantwell":  ("C000127", "Maria Cantwell", "D", "WA"),
    "wyden":     ("W000779", "Ron Wyden", "D", "OR"),
    "tillis":    ("T000476", "Thom Tillis", "R", "NC"),
    "curtis":    ("C001114", "John Curtis", "R", "UT"),
    "voinovich": ("V000126", "George Voinovich", "R", "OH"),
    # Sinema left the Democratic Party in December 2022; use this key for
    # votes cast after that date. Same person, same photo, era-accurate label.
    "sinema_i":  ("S001191", "Kyrsten Sinema", "I", "AZ"),
}

PUZZLES = [
    {
        "id": "first-trial",
        "title": "The First Trial",
        "era": "116th Congress · 2019–2020",
        "intro": ("A president stands trial in the Senate for the third time in American "
                  "history. For the senators who might break ranks, every vote — on his "
                  "war powers, on his removal — is a test of how much defiance costs."),
        "senators": [
            ("romney",    "Utah's freshman is also the party's 2012 presidential nominee — "
                          "a devout institutionalist who announced his Senate run with an "
                          "essay condemning Trump's character. He talks about his oath, his "
                          "conscience, and his father's example. Constantly."),
            ("collins",   "The Maine moderate faces the toughest re-election of her life in "
                          "a state Trump lost. She voted to force witness testimony at the "
                          "trial, and says the President has learned 'a pretty big lesson' "
                          "from impeachment itself."),
            ("murkowski", "Alaska's write-in survivor answers to no party machine. She "
                          "called the House process rushed and the Senate trial 'shameful' "
                          "on all sides — while leaving everyone guessing where that "
                          "leaves her."),
            ("manchin",   "A West Virginia Democrat in a state Trump carried by 42 points, "
                          "personally friendly with the President and publicly agonized. "
                          "He spends the trial's final week floating a censure resolution "
                          "instead."),
            ("mcconnell", "The majority leader, who has said plainly he is 'not an "
                          "impartial juror' and is coordinating trial strategy with the "
                          "White House. His priority is protecting his majority — and "
                          "ending this quickly."),
        ],
        "bills": [
            {
                "congress": 116, "session": 1, "vote": 94,
                "name": "Yemen War Powers — Veto Override",
                "desc": ("May 2, 2019. Congress passed a resolution ordering an end to "
                         "U.S. military support for the Saudi-led war in Yemen — the "
                         "first war-powers resolution ever to reach a president's desk — "
                         "and Trump vetoed it. Now the override vote: a two-thirds "
                         "majority to reclaim Congress's war power over the President's "
                         "objection, with the humanitarian toll in Yemen mounting."),
            },
            {
                "congress": 116, "session": 2, "vote": 33,
                "name": "Article I: Abuse of Power",
                "labels": ["GUILTY", "NOT GUILTY"],
                "desc": ("February 5, 2020. The first article of impeachment charges the "
                         "President with pressuring Ukraine to investigate the Bidens "
                         "while withholding $391 million in military aid. Each senator "
                         "stands at their desk to pronounce him guilty or not guilty; "
                         "a two-thirds vote convicts and removes him from office. No "
                         "senator has ever voted to remove a president of his own party."),
            },
            {
                "congress": 116, "session": 2, "vote": 34,
                "name": "Article II: Obstruction of Congress",
                "labels": ["GUILTY", "NOT GUILTY"],
                "desc": ("Minutes later, the second article: obstruction of Congress, for "
                         "the White House's blanket refusal to provide witnesses or "
                         "documents to the House inquiry. Some senators see a categorical "
                         "stonewall without precedent; others see a legitimate assertion "
                         "of executive privilege that the House never tested in court. "
                         "Again, two-thirds to convict."),
            },
        ],
    },
    {
        "id": "divided-2019",
        "title": "Divided Government",
        "era": "116th Congress · 2019",
        "intro": ("A record 35-day shutdown ends, a national emergency begins, and an "
                  "odd-couple coalition tries to end a war. In 2019 the interesting "
                  "line isn't between the parties — it's inside them."),
        "senators": [
            ("mlee",    "Utah's constitutional obsessive: a Federalist Society "
                        "conservative who backs Trump on judges and taxes but treats "
                        "executive overreach as original sin — whichever president is "
                        "doing the reaching. He co-sponsors the Yemen resolution with "
                        "Bernie Sanders."),
            ("sanders", "The Vermont socialist, weeks into his second presidential "
                        "campaign, using the Senate floor to force votes on ending "
                        "American support for the Saudi war in Yemen."),
            ("collins", "Twenty-two years in and staring down a brutal 2020 race, the "
                        "Maine moderate is the first name on every whip list — praised "
                        "as an institutionalist at home, pilloried as a fence-sitter "
                        "everywhere else."),
            ("rubio",   "Florida's hawk: a believer in American power abroad and the "
                        "Saudi alliance, but also a Cuban-American with long memories "
                        "about presidents who rule by decree."),
            ("tester",  "A flat-topped dirt farmer from Big Sandy, Montana — a "
                        "seven-fingered Democrat who won three times in Trump country "
                        "by voting like Montana and sounding like it too."),
        ],
        "bills": [
            {
                "congress": 116, "session": 1, "vote": 26,
                "name": "Ending the Shutdown Fight",
                "desc": ("February 14, 2019. After the longest government shutdown in "
                         "history — 35 days over border-wall money — the conference "
                         "deal funds the government through September with $1.375 "
                         "billion for 55 miles of fencing, a fraction of the $5.7 "
                         "billion the President demanded. Trump will sign it the "
                         "next day — and, the same morning, declare a national "
                         "emergency to get the rest."),
            },
            {
                "congress": 116, "session": 1, "vote": 48,
                "name": "Yemen War Powers Resolution",
                "desc": ("March 13, 2019. The Sanders-Lee resolution directs the "
                         "removal of U.S. forces from hostilities in Yemen's civil "
                         "war — the refueling, targeting help, and intelligence "
                         "sustaining the Saudi bombing campaign — invoking the 1973 "
                         "War Powers Act against a sitting president for the first "
                         "time. The White House promises a veto."),
            },
            {
                "congress": 116, "session": 1, "vote": 49,
                "name": "Terminating the Border Emergency",
                "desc": ("March 14, 2019. One day later: a resolution terminating the "
                         "national emergency Trump declared to move military "
                         "construction money to the border wall after Congress refused "
                         "to appropriate it. The question splits constitutional "
                         "conservatives from the White House: can a president spend "
                         "what Congress declined to give him?"),
            },
        ],
    },
    {
        "id": "jan-six",
        "title": "January 6th, After Midnight",
        "era": "117th Congress · 2021",
        "intro": ("A mob has just been cleared from the Capitol. Senators return to a "
                  "building of broken glass to finish counting the electoral votes — "
                  "and five months later, to decide whether anyone should "
                  "investigate what happened."),
        "senators": [
            ("hawley",    "Missouri's 41-year-old Yale Law populist was the first "
                          "senator to announce he'd object to the count — the raised "
                          "fist to the crowd outside is already the photo of his "
                          "career, for better or worse."),
            ("cruz",      "The Texan leads a bloc demanding a ten-day 'election audit' "
                          "commission, modeled on 1877. Runner-up to Trump in 2016, "
                          "he has no intention of ceding the Trump lane in 2024."),
            ("graham",    "Trump's golf partner and most quotable ally — but a "
                          "30-year institutionalist who spent January 6 in the chamber "
                          "he loves, hearing the mob outside. 'Count me out,' he says "
                          "that night. How far out?"),
            ("romney",    "The party's sharpest internal critic, who marched to the "
                          "Capitol that morning past heckling crowds and voted to "
                          "convict Trump once already. His fury on the floor tonight "
                          "is not performed."),
            ("murkowski", "Alaska's independent-minded survivor, first Republican "
                          "senator to call on Trump to resign after the attack — and "
                          "the only one of the objectors' colleagues facing his "
                          "endorsed challenger next year."),
        ],
        "bills": [
            {
                "congress": 117, "session": 1, "vote": 1,
                "name": "The Arizona Objection",
                "desc": ("January 6, 2021, 9:58 p.m. The objection to counting "
                         "Arizona's electoral votes — filed by Rep. Gosar and Sen. "
                         "Cruz — was being debated when rioters stormed the Capitol. "
                         "Now the Senate, back in its chamber, votes on it. A Yea "
                         "sustains the objection and throws out Arizona's eleven "
                         "electoral votes for Biden; a Nay counts them as certified."),
            },
            {
                "congress": 117, "session": 1, "vote": 2,
                "name": "The Pennsylvania Objection",
                "desc": ("12:30 a.m., January 7. The second and final objection to "
                         "survive to a Senate vote: Pennsylvania's twenty electoral "
                         "votes, challenged by Rep. Perry and Sen. Hawley over the "
                         "state's expanded mail voting. Again, Yea sustains the "
                         "objection and rejects the state's certified electors. Some "
                         "who planned to object hours ago have had second thoughts."),
            },
            {
                "congress": 117, "session": 1, "vote": 218,
                "name": "A January 6th Commission",
                "desc": ("May 28, 2021. A bill creating an independent, 9/11-style "
                         "commission on the attack: ten commissioners, evenly split "
                         "between the parties, with bipartisan subpoena power. The "
                         "House passed it with 35 Republican votes. McConnell calls "
                         "it 'a purely political exercise'; it needs 60 to advance."),
            },
        ],
    },
    {
        "id": "institutionalists",
        "title": "The Institutionalists",
        "era": "117th Congress · 2021–2022",
        "intro": ("After January 6th, a handful of Republicans stop worrying about "
                  "primaries — several by leaving politics altogether. Freed from the "
                  "base, what do they actually vote for?"),
        "senators": [
            ("toomey",    "Pennsylvania's flinty fiscal conservative, retiring rather "
                          "than run again in a Trump party. A Club for Growth alumnus "
                          "to the end: he'll defy Trump on principle and still vote "
                          "against almost anything that spends money."),
            ("burr",      "North Carolina's laconic three-termer, also retiring. As "
                          "Intelligence chairman he ran the Senate's Russia "
                          "investigation straight down the middle and shrugged off "
                          "the censure his own state party passed against him."),
            ("cassidy",   "A Baton Rouge liver doctor who worked charity hospitals for "
                          "25 years. He reads bills like charts — wonkish, blunt, and "
                          "newly re-elected, which buys him six years of not caring "
                          "what Louisiana's party committees think."),
            ("murkowski", "Alaska's write-in survivor, the only Republican in this "
                          "group actually facing voters in 2022 — with a Trump-endorsed "
                          "challenger already in the race and a new ranked-choice "
                          "system that just might save her."),
            ("warnock",   "The pastor of Ebenezer Baptist, months into the seat he won "
                          "in a runoff that flipped the Senate — and already running "
                          "again in purple Georgia, preaching bipartisanship while "
                          "voting mostly with his party."),
        ],
        "bills": [
            {
                "congress": 117, "session": 1, "vote": 59,
                "name": "The Second Impeachment Trial",
                "labels": ["GUILTY", "NOT GUILTY"],
                "desc": ("February 13, 2021. Donald Trump's second impeachment trial — "
                         "the first ever of a former president — ends with a verdict "
                         "on a single article: incitement of insurrection for January "
                         "6th. He is out of office; conviction would clear the way to "
                         "disqualify him from ever holding office again. Two-thirds "
                         "to convict, and every Republican Yea is a career risk."),
            },
            {
                "congress": 117, "session": 2, "vote": 261,
                "name": "Advancing the CHIPS Act",
                "desc": ("July 19, 2022. The make-or-break test vote on $52 billion "
                         "in subsidies for domestic semiconductor manufacturing, plus "
                         "a 25% investment tax credit — industrial policy on a scale "
                         "unseen in decades, sold as keeping chip fabs out of China's "
                         "shadow. Free-market conservatives call it corporate "
                         "welfare; the Commerce Department calls it national "
                         "security."),
            },
            {
                "congress": 117, "session": 2, "vote": 280,
                "name": "The PACT Act",
                "desc": ("August 2, 2022. Health care and disability benefits for "
                         "veterans exposed to toxic burn pits in Iraq and "
                         "Afghanistan — roughly $280 billion over a decade, the "
                         "largest expansion of veterans' benefits in a generation. "
                         "A procedural blockade days earlier left veterans' groups "
                         "camped on the Capitol steps with Jon Stewart. Now the "
                         "final vote."),
            },
        ],
    },
    {
        "id": "manchin-sinema",
        "title": "The Manchin-Sinema Show",
        "era": "117th Congress · 2021–2022",
        "intro": ("In a 50-50 Senate, two Democrats hold the pen on everything — and "
                  "three Republican moderates decide what else gets through. Five "
                  "people, one chamber, and every camera in Washington."),
        "senators": [
            ("manchin",   "West Virginia's last statewide Democrat, who killed Build "
                          "Back Better on Fox News Sunday and then spent months "
                          "secretly negotiating something leaner with Schumer. Coal "
                          "state, coal portfolio, deciding vote on a climate bill."),
            ("sinema",    "The Arizonan who curtsied thumbs-down on the minimum wage: "
                          "a former Green Party activist turned business-friendly "
                          "enigma who guards the filibuster, loves a bipartisan gang, "
                          "and negotiates by press blackout."),
            ("collins",   "The dean of Senate moderates, fresh off a nine-point "
                          "re-election no pollster predicted. With nothing left to "
                          "prove, she brokers deals on infrastructure, guns, and "
                          "marriage — but taxes and spending are another matter."),
            ("murkowski", "Alaska's write-in survivor, censured by her state party and "
                          "running for re-election anyway. Persuadable on nominees, "
                          "process, and anything that helps Alaska — immovable when "
                          "she thinks the base is bluffing."),
            ("romney",    "Utah's institutionalist, the only Republican who voted to "
                          "convict Trump twice. He'll join any gang of ten — and "
                          "still votes like a Chamber of Commerce Republican on the "
                          "big-ticket spending."),
        ],
        "bills": [
            {
                "congress": 117, "session": 1, "vote": 489,
                "name": "Repealing the Vaccine Mandate",
                "desc": ("December 8, 2021. A Congressional Review Act resolution to "
                         "nullify OSHA's emergency rule requiring vaccination or "
                         "weekly testing at every employer with 100 or more workers — "
                         "84 million people. Under the CRA it needs only a simple "
                         "majority, which means one or two Democrats decide whether "
                         "the Senate rebukes the administration's pandemic "
                         "centerpiece."),
            },
            {
                "congress": 117, "session": 2, "vote": 134,
                "name": "Confirming Ketanji Brown Jackson",
                "desc": ("April 7, 2022. The first Black woman nominated to the "
                         "Supreme Court: a Harvard-trained appellate judge and former "
                         "federal public defender, replacing the retiring Stephen "
                         "Breyer. The hearings turned combative over sentencing "
                         "records, but the outcome hinges on a simple question — "
                         "which, if any, Republicans vote yes?"),
            },
            {
                "congress": 117, "session": 2, "vote": 325,
                "name": "The Inflation Reduction Act",
                "desc": ("August 7, 2022, 3 p.m., after a 27-hour vote-a-rama. The "
                         "bill nobody saw coming: $369 billion in climate and energy "
                         "tax credits, Medicare drug-price negotiation, a 15% "
                         "corporate minimum tax. Built by Manchin and Schumer in "
                         "secret, rescued when Sinema extracted her final edits — "
                         "and passed, if it passes, with zero votes to spare."),
            },
        ],
    },
    {
        "id": "filibuster-winter",
        "title": "The Filibuster Winter",
        "era": "117th Congress · 2021–2022",
        "intro": ("Democrats hold the House, the Senate, and the White House — and "
                  "watch their voting-rights agenda die at sixty votes, three times. "
                  "Then they try to change the number itself."),
        "senators": [
            ("manchin",   "West Virginia's Democrat calls the filibuster the soul of "
                          "the Senate and refuses to gut it — while insisting he "
                          "wants a voting-rights deal, and writing his own compromise "
                          "bill to prove it."),
            ("sinema",    "Arizona's first-term enigma delivers a floor speech "
                          "defending the 60-vote threshold on the very day the "
                          "President comes to the Hill to lobby against it. She "
                          "backs the bills; the rules are another question."),
            ("mcconnell", "The minority leader with a floor-length view of Senate "
                          "rules: he calls the elections bill a federal takeover and "
                          "promises a 'scorched earth' chamber if Democrats touch "
                          "the filibuster."),
            ("merkley",   "Oregon's methodical progressive has spent a decade drafting "
                          "filibuster-reform plans and is the elections bill's chief "
                          "author — this is the moment he's been organizing toward "
                          "his entire Senate career."),
            ("warnock",   "The freshman pastor from Ebenezer Baptist frames voting "
                          "rights as 'a moral issue' in the tradition of the church "
                          "he leads — and argues democracy shouldn't die to preserve "
                          "a Senate custom."),
        ],
        "bills": [
            {
                "congress": 117, "session": 1, "vote": 246,
                "name": "The For the People Act",
                "desc": ("June 22, 2021. Cloture on the Democrats' 800-page "
                         "democracy overhaul: national automatic and same-day "
                         "registration, independent redistricting commissions, "
                         "small-donor matching, dark-money disclosure. Every "
                         "Republican calls it a power grab; the only suspense is "
                         "whether all fifty Democrats will even agree to open "
                         "debate. Sixty votes to advance."),
            },
            {
                "congress": 117, "session": 1, "vote": 459,
                "name": "The John Lewis Voting Rights Act",
                "desc": ("November 3, 2021. A narrower bill restoring the Voting "
                         "Rights Act's preclearance formula, struck down by the "
                         "Supreme Court in 2013 — requiring states with recent "
                         "violations to clear election changes with Washington "
                         "again. Named for the late congressman who bled at Selma. "
                         "Again sixty votes, and this time exactly one Republican "
                         "is willing."),
            },
            {
                "congress": 117, "session": 2, "vote": 10,
                "name": "The Filibuster Carve-Out",
                "desc": ("January 19, 2022, 10:21 p.m. With the voting bill blocked "
                         "again, Schumer moves to change the rules: a 'talking "
                         "filibuster' exception letting elections legislation pass "
                         "by simple majority. The chair rules the 60-vote threshold "
                         "stands; this vote is the appeal. A Yea upholds the ruling "
                         "and keeps the filibuster intact — a Nay blows the hole "
                         "open. Fifty-two senators will settle it."),
            },
        ],
    },
    {
        "id": "railroad",
        "title": "Working on the Railroad",
        "era": "117th Congress · 2022",
        "intro": ("A national rail strike is nine days away, and Congress reaches for "
                  "a 1926 law to impose a contract on 115,000 workers. Suddenly "
                  "nobody's party label predicts anything."),
        "senators": [
            ("sanders",  "The Vermont socialist and self-appointed shop steward of the "
                         "Senate. He's spent months hammering the railroads' record "
                         "profits and stock buybacks — and a contract without sick "
                         "days is exactly his kind of fight."),
            ("rubio",    "Florida's senator has been rebranding as a 'common-good' "
                         "conservative — pro-worker, anti-woke-capital. He announced "
                         "he won't vote to impose a deal the rail workers themselves "
                         "rejected. The AFL-CIO is watching with one eyebrow raised."),
            ("hawley",   "Missouri's populist, courting the union rank-and-file for a "
                         "post-Trump GOP. He relishes votes where he can side with "
                         "workers against management and his own party's donor class "
                         "in a single afternoon."),
            ("baldwin",  "Wisconsin's workmanlike progressive, from a state built on "
                         "railroads and factory floors. A reliable labor vote — but "
                         "also a Democrat weighing what a freight shutdown would do "
                         "to dairy farms and drinking-water plants."),
            ("romney",   "Utah's businessman-senator, who ran Bain Capital and "
                         "believes in negotiated settlements — and in not letting a "
                         "strike subtract two billion dollars a day from the economy "
                         "three weeks before Christmas."),
        ],
        "bills": [
            {
                "congress": 117, "session": 2, "vote": 372,
                "name": "Imposing the Rail Agreement",
                "desc": ("December 1, 2022. Under the Railway Labor Act, Congress "
                         "forces the White House-brokered contract on the freight "
                         "railroads and their unions: a 24% raise over five years, "
                         "but just one added personal day — the deal four of twelve "
                         "unions voted down. A strike would halt 30% of U.S. freight "
                         "within days. Labor calls the vote a betrayal; shippers "
                         "call it a rescue."),
            },
            {
                "congress": 117, "session": 2, "vote": 371,
                "name": "Seven Days of Paid Sick Leave",
                "desc": ("The companion vote, moments earlier: adding seven paid "
                         "sick days to the imposed contract. Rail workers currently "
                         "get zero — scheduling systems penalize them for doctor's "
                         "appointments. The House passed it separately so the rescue "
                         "could survive without it. It needs 60 votes here, and the "
                         "whip count is genuinely strange."),
            },
            {
                "congress": 117, "session": 2, "vote": 421,
                "name": "The Year-End Omnibus",
                "desc": ("December 22, 2022. The $1.7 trillion everything bill, "
                         "racing a Christmas blizzard out of town: full-year funding "
                         "for the government, $45 billion for Ukraine, an overhaul "
                         "of the Electoral Count Act, and 7,200 earmarks. "
                         "Retiring appropriators call it Congress doing its job; "
                         "conservatives call it 4,155 pages nobody has read."),
            },
        ],
    },
    {
        "id": "debt-rerun",
        "title": "The Debt-Ceiling Rerun",
        "era": "118th Congress · 2023",
        "intro": ("Divided government returns, and with it the sequels: a debt-limit "
                  "standoff, a shutdown countdown, and a Pentagon budget. A freshman "
                  "class of populists gets its first taste of governing by deadline."),
        "senators": [
            ("fetterman", "Pennsylvania's 6-foot-8 freshman in gym shorts, back at "
                          "work after treatment for depression he discussed with "
                          "unusual candor. A blue-collar populist who measures every "
                          "deal by what it does to the little guy — and hates being "
                          "told something is 'the only option.'"),
            ("vance",     "Ohio's freshman wrote Hillbilly Elegy, then remade himself "
                          "as a Trump-endorsed scourge of the foreign-policy and "
                          "spending establishments. He didn't come to Washington to "
                          "vote for grand bargains."),
            ("sinema_i",  "Now officially an independent, having left the Democratic "
                          "Party weeks after the midterms. Still caucusing for "
                          "committee purposes, still the Senate's most relentless "
                          "dealmaker — and still keeping Arizona guessing about "
                          "2024."),
            ("murkowski", "Alaska's senior senator, fresh off beating a Trump-backed "
                          "challenger under ranked-choice voting. More insulated from "
                          "the base than any Republican in the chamber, and she "
                          "votes like it."),
            ("rpaul",     "Kentucky's libertarian: he has voted against every debt- "
                          "ceiling increase, most spending bills, and any Pentagon "
                          "budget he deems bloated. Deadlines, in his view, are "
                          "leverage everyone else keeps wasting."),
        ],
        "bills": [
            {
                "congress": 118, "session": 1, "vote": 146,
                "name": "The Fiscal Responsibility Act",
                "desc": ("June 1, 2023, 10:37 p.m. — default is projected in four "
                         "days. The Biden-McCarthy deal suspends the debt ceiling "
                         "into 2025 in exchange for two years of spending caps, "
                         "clawed-back COVID and IRS money, expanded work "
                         "requirements, and approval of the Mountain Valley "
                         "Pipeline. Hardliners in both parties hate it — which is "
                         "usually how these pass."),
            },
            {
                "congress": 118, "session": 1, "vote": 212,
                "name": "The FY2024 Defense Bill",
                "desc": ("July 27, 2023. An $886 billion defense authorization: a "
                         "5.2% pay raise for the troops — the largest in two decades "
                         "— new submarines and hypersonics money, and another round "
                         "of aid authorities for Ukraine and Taiwan. The perennial "
                         "must-pass bill, opposed each year by an odd chorus of "
                         "doves and deficit hawks."),
            },
            {
                "congress": 118, "session": 1, "vote": 247,
                "name": "The 45-Day Stopgap",
                "desc": ("September 30, 2023, 8:10 p.m. — four hours to a shutdown. "
                         "A bare-bones continuing resolution keeping the government "
                         "open 45 days, with disaster relief but no Ukraine aid, "
                         "jammed through after Speaker McCarthy abandoned his right "
                         "flank to pass it. Three days later, the House will fire "
                         "him for it."),
            },
        ],
    },
    {
        "id": "border-winter",
        "title": "The Border Winter",
        "era": "118th Congress · 2024",
        "intro": ("Three senators spend four months negotiating the toughest border "
                  "deal in a generation. It dies in 48 hours. What's left — foreign "
                  "aid, surveillance law — passes at five in the morning."),
        "senators": [
            ("lankford",  "Oklahoma's Baptist conservative drew the assignment of a "
                          "lifetime: negotiate the border deal his party demanded. "
                          "Then Trump came out against it, the party bolted, and his "
                          "state GOP censured him. He says he read the bill; he "
                          "wrote it."),
            ("cmurphy",   "Connecticut's Democratic negotiator, who came up through "
                          "the gun-safety wars and believes deals with Republicans "
                          "are still possible — he traded four months of asylum "
                          "concessions on that theory."),
            ("sinema_i",  "The Senate's independent broker completed the negotiating "
                          "trio. Facing an unwinnable three-way race at home, she'll "
                          "announce her retirement in March — freer than ever, and "
                          "twice as blunt about it."),
            ("rpaul",     "Kentucky's libertarian objector-in-chief: against the "
                          "border bill's spending, against foreign aid on principle, "
                          "and willing to hold the floor all night to slow any of "
                          "it down."),
            ("fetterman", "Pennsylvania's hoodie-clad Democrat has been drifting from "
                          "the left flank — blunt about a border 'crisis,' loudly "
                          "pro-Israel and pro-Ukraine, and openly contemptuous of "
                          "purity tests from either direction."),
        ],
        "bills": [
            {
                "congress": 118, "session": 2, "vote": 39,
                "name": "The Border Deal",
                "desc": ("February 7, 2024. Cloture on the $118 billion national "
                         "security package built around the Lankford-Murphy-Sinema "
                         "border compromise: a tougher asylum standard, faster "
                         "removals, and an emergency authority to shut the border "
                         "when crossings surge — paired with Ukraine and Israel "
                         "aid. Trump has denounced it; the Border Patrol union "
                         "endorsed it. Sixty votes to advance the deal."),
            },
            {
                "congress": 118, "session": 2, "vote": 48,
                "name": "The Foreign-Aid Supplemental",
                "desc": ("February 13, 2024, 5:14 a.m. With the border provisions "
                         "stripped out, the remainder: $60 billion for Ukraine's "
                         "third year of war, $14 billion for Israel, humanitarian "
                         "aid for Gaza, and Indo-Pacific deterrence money — passed "
                         "at dawn after opponents forced the Senate through a week "
                         "of all-night sessions."),
            },
            {
                "congress": 118, "session": 2, "vote": 150,
                "name": "FISA Section 702 Renewal",
                "desc": ("April 19, 2024, 11:45 p.m. — fifteen minutes before the "
                         "government's warrantless-surveillance authority expires. "
                         "A two-year reauthorization of Section 702, which sweeps "
                         "up foreigners' communications abroad — and, incidentally, "
                         "Americans' messages with them. Civil libertarians in both "
                         "parties demand a warrant requirement; the "
                         "intelligence agencies call that unilateral disarmament."),
            },
        ],
    },
    {
        "id": "advice-dissent",
        "title": "Advice & Dissent",
        "era": "107th–115th Congress · 2001–2017",
        "intro": ("Three cabinet fights, sixteen years apart: an attorney general, a "
                  "defense secretary, an education secretary. The same five senators "
                  "sit in judgment each time — watch what loyalty does."),
        "senators": [
            ("collins",  "The Maine Republican holds an old-fashioned doctrine: "
                         "presidents of either party deserve their cabinet absent "
                         "disqualifying flaws. The interesting question is what she "
                         "counts as disqualifying — and whether sixteen years of "
                         "polarization moves her line."),
            ("pmurray",  "Washington's 'mom in tennis shoes,' risen from school-board "
                         "revolt to the Democratic leadership. Education is her home "
                         "turf, abortion rights her bright line, and she has little "
                         "patience for nominees on the wrong side of either."),
            ("mccain",   "The maverick across three eras: a partisan when the wound "
                         "is fresh, a dealmaker when the institution needs it, and "
                         "famously personal about who has — and hasn't — earned his "
                         "respect. One of these nominees is an old friend who "
                         "crossed him."),
            ("schumer",  "Brooklyn's happiest warrior, climbing from freshman to "
                         "Democratic leader across these years. He reads every "
                         "confirmation as a power question first — and by 2017 he's "
                         "whipping his caucus to fight nearly everything."),
            ("inhofe",   "Oklahoma's flinty conservative, an Army veteran and "
                         "commercial pilot who backs Republican presidents' picks "
                         "as a matter of course — and treats Democratic outrage as "
                         "a reason to dig in."),
        ],
        "bills": [
            {
                "congress": 107, "session": 1, "vote": 8,
                "name": "Confirming John Ashcroft",
                "desc": ("February 1, 2001. George W. Bush's attorney general: a "
                         "former Missouri senator and governor, a devout Pentecostal "
                         "beloved by religious conservatives — who just lost his "
                         "Senate seat to a dead man. Civil-rights groups mobilize "
                         "over his record on desegregation and abortion; colleagues "
                         "weigh how hard to fight a man they served beside."),
            },
            {
                "congress": 113, "session": 1, "vote": 24,
                "name": "Confirming Chuck Hagel",
                "desc": ("February 26, 2013. Obama crosses the aisle for his defense "
                         "secretary: Chuck Hagel, twice-wounded Vietnam sergeant and "
                         "former Republican senator — who broke with his party over "
                         "the Iraq surge. His old GOP colleagues filibustered him "
                         "for two weeks and savaged his 'Jewish lobby' remark and "
                         "shaky hearing. Nothing tests old friendships like "
                         "apostasy."),
            },
            {
                "congress": 115, "session": 1, "vote": 54,
                "name": "Confirming Betsy DeVos",
                "desc": ("February 7, 2017. Trump's education secretary: a Michigan "
                         "billionaire philanthropist and school-choice crusader with "
                         "no experience in public schools, whose hearing produced "
                         "the 'grizzly bears' answer on guns in classrooms. "
                         "Teachers' unions flood the phone lines. The tally stands "
                         "at 50-50 — meaning the Vice President waits in the "
                         "chair."),
            },
        ],
    },
    {
        "id": "sending-troops",
        "title": "Sending the Troops",
        "era": "103rd–104th Congress · 1993–1995",
        "intro": ("After the Cold War, the question turns strange: when does America "
                  "send soldiers into other people's wars? Somalia sours everyone; "
                  "then Bosnia asks the question twice."),
        "senators": [
            ("dole",      "The Republican leader and wounded veteran of the Italian "
                          "campaign, eyeing the 1996 nomination. He hammers Clinton's "
                          "foreign policy weekly — but believes a president's "
                          "soldiers, once committed, must not be undercut. Bosnia's "
                          "besieged Muslims have no louder American champion."),
            ("mccain",    "Vietnam's most famous POW, burned by Beirut and Mogadishu "
                          "into a hard rule: no troops without a mission, no mission "
                          "without an exit. He is the Senate's sharpest critic of "
                          "peacekeeping-by-good-intentions."),
            ("byrd",      "The Constitution-pocket institutionalist, Appropriations' "
                          "master, and the loudest voice demanding Congress — not "
                          "presidents — decide where Americans fight. Nation-building "
                          "in the Balkans strikes him as folly on stilts."),
            ("wellstone", "Minnesota's happy-warrior progressive: a dove by instinct "
                          "who marched against Vietnam, yet haunted by Bosnia's "
                          "camps and massacres. Human rights and anti-war principle "
                          "point in opposite directions here."),
            ("jwarner",   "Virginia's courtly former Navy secretary, the uniformed "
                          "services' best friend in the chamber. He weighs every "
                          "deployment like the Pentagon planner he once was — "
                          "supportive of soldiers, skeptical of open-ended missions."),
        ],
        "bills": [
            {
                "congress": 103, "session": 1, "vote": 314,
                "name": "The Somalia Deadline",
                "desc": ("October 15, 1993, after midnight. Twelve days after "
                         "eighteen Army Rangers died in Mogadishu, the Byrd "
                         "amendment cuts off funding for the Somalia mission after "
                         "March 31, 1994, forcing a withdrawal date on the Clinton "
                         "White House. Some hawks want out even sooner — this is "
                         "the compromise between retreat now and staying the "
                         "course."),
            },
            {
                "congress": 104, "session": 1, "vote": 331,
                "name": "Lifting the Bosnia Arms Embargo",
                "desc": ("July 26, 1995 — two weeks after Srebrenica, where Serb "
                         "forces murdered thousands under UN protection. The "
                         "Dole-Lieberman bill ends U.S. enforcement of the arms "
                         "embargo so Bosnia's Muslims can arm themselves. Clinton "
                         "warns it will Americanize the war and promises a veto; "
                         "supporters answer that the embargo only disarms the "
                         "victims."),
            },
            {
                "congress": 104, "session": 1, "vote": 603,
                "name": "Backing the Troops to Bosnia",
                "desc": ("December 13, 1995, 10:44 p.m. The Dayton peace accords "
                         "are signed, and 20,000 American troops are going to "
                         "Bosnia to enforce them — with or without Congress. The "
                         "Dole-McCain resolution swallows 'reservations' about "
                         "Clinton's policy but declares support for the soldiers "
                         "and lets the deployment proceed. Voting no means voting "
                         "to leave the president's commitment naked."),
            },
        ],
    },
    {
        "id": "climate-wars",
        "title": "The Climate Wars",
        "era": "108th–114th Congress · 2003–2015",
        "intro": ("Twelve years of the Senate arguing with a thermometer: a "
                  "cap-and-trade bill ahead of its time, a fight over Alaska's "
                  "refuge, and a pipeline that becomes a national symbol."),
        "senators": [
            ("mccain",    "The Republican who believes the science and says so: he "
                          "co-authors the first real climate bill and holds hearings "
                          "with glaciologists. But he's also a westerner who loves "
                          "energy independence — the pipeline era will test which "
                          "instinct runs deeper."),
            ("murkowski", "Alaska's senator, later chairman of Energy. Oil fills a "
                          "third of her state's payroll, and opening ANWR's coastal "
                          "plain has been the family cause since her father held "
                          "the seat. Climate talk, in her Senate, must coexist "
                          "with drilling."),
            ("cantwell",  "Washington's former tech executive, who treats the Arctic "
                          "National Wildlife Refuge fight as her signature stand — "
                          "she leads the floor defense against drilling and never "
                          "misses an oil-market manipulation hearing."),
            ("inhofe",    "Oklahoma's implacable skeptic, who calls man-made global "
                          "warming 'the greatest hoax ever perpetrated on the "
                          "American people' from the chairmanship of the "
                          "Environment Committee. Oil and gas built his state; he "
                          "intends to return the favor."),
            ("wyden",     "Oregon's cerebral progressive: salmon streams, wind "
                          "farms, and a tax-code approach to everything. A reliable "
                          "environmental vote who'd rather rewrite energy "
                          "incentives than posture about them."),
        ],
        "bills": [
            {
                "congress": 108, "session": 1, "vote": 420,
                "name": "The Climate Stewardship Act",
                "desc": ("October 30, 2003. McCain-Lieberman: the Senate's first "
                         "real vote on capping greenhouse gases — emissions held to "
                         "2000 levels by 2010, with tradable allowances for power "
                         "plants and factories. Opponents brandish studies on "
                         "electricity prices; supporters just want it on the "
                         "record that a bipartisan climate bill can exist."),
            },
            {
                "congress": 109, "session": 1, "vote": 52,
                "name": "Blocking Arctic Refuge Drilling",
                "desc": ("March 16, 2005. Drilling advocates have tucked ANWR's "
                         "coastal plain into the budget resolution, where no "
                         "filibuster can reach it. The Cantwell amendment strikes "
                         "the provision — a Yea protects the refuge, a Nay keeps "
                         "drilling on track. After three decades of stalemate over "
                         "10 billion barrels and a caribou calving ground, the "
                         "margin is razor thin."),
            },
            {
                "congress": 114, "session": 1, "vote": 49,
                "name": "The Keystone XL Pipeline",
                "desc": ("January 29, 2015. The new Republican majority's Bill "
                         "Number One: approving the 1,179-mile pipeline carrying "
                         "Canadian oil-sands crude to Gulf refineries, six years "
                         "into an environmental review Obama refuses to shortcut. "
                         "Unions want the construction jobs; climate activists have "
                         "made the route a line in the tar sand. A veto is "
                         "promised."),
            },
        ],
    },
    {
        "id": "loyalty-tests",
        "title": "The Loyalty Tests",
        "era": "119th Congress · 2025",
        "intro": ("A re-elected Donald Trump sends the Senate his most "
                  "unconventional cabinet yet, daring Republicans to object. For "
                  "three weeks, every confirmation is a loyalty test with a "
                  "two-vote margin."),
        "senators": [
            ("collins",   "Five terms in and chairing Appropriations at last, the "
                          "Maine moderate is one of the few Republicans left who "
                          "publicly weighs nominees one by one — knowing every 'no' "
                          "now invites a primary threat from Mar-a-Lago."),
            ("murkowski", "Alaska's independent-minded survivor, re-elected under "
                          "ranked-choice voting and openly unafraid of Trump. She "
                          "scrutinizes qualifications the old-fashioned way and "
                          "shrugs at the consequences."),
            ("mcconnell", "The longest-serving Senate leader in history is a leader "
                          "no more — a backbencher at 82, a polio survivor with "
                          "hawkish convictions and, suddenly, nothing left to "
                          "protect but his own judgment."),
            ("fetterman", "Pennsylvania's hoodie-wearing Democrat, who flew to "
                          "Mar-a-Lago to meet the president-elect and says some "
                          "nominees deserve a fair look. His party's activists are "
                          "furious; he appears to enjoy that."),
            ("curtis",    "Utah's freshman, who won Mitt Romney's old seat promising "
                          "civility and climate conservatism. A former Provo mayor "
                          "with an institutional streak — but a Republican freshman "
                          "still, with a base watching his first big votes."),
        ],
        "bills": [
            {
                "congress": 119, "session": 1, "vote": 15,
                "name": "Confirming Pete Hegseth",
                "desc": ("January 24, 2025. Secretary of Defense: a decorated Army "
                         "National Guard veteran and Fox News weekend host who has "
                         "never run anything close to a three-million-person "
                         "department. The hearings churn through allegations about "
                         "his drinking and personal conduct — all denied — and his "
                         "past opposition to women in combat. The tally hangs at "
                         "50-50, and the Vice President is standing by."),
            },
            {
                "congress": 119, "session": 1, "vote": 52,
                "name": "Confirming Robert F. Kennedy Jr.",
                "desc": ("February 13, 2025. Health and Human Services: America's "
                         "most famous vaccine skeptic, bearer of its most famous "
                         "Democratic name, atop a $1.7 trillion health apparatus. "
                         "He promises senators he won't touch the childhood vaccine "
                         "schedule and pitches a war on chronic disease. The "
                         "chamber's doctors face the hardest choice of the "
                         "season."),
            },
            {
                "congress": 119, "session": 1, "vote": 61,
                "name": "Confirming Kash Patel",
                "desc": ("February 20, 2025. FBI director: a former public defender "
                         "and Trump-administration aide who wrote a book naming "
                         "'deep state' officials and has vowed to overhaul the "
                         "bureau top to bottom. Supporters call the FBI overdue for "
                         "it; critics hear an enemies list. The ten-year term is "
                         "designed to outlast presidents — this one starts with a "
                         "two-vote margin."),
            },
        ],
    },
    {
        "id": "this-congress",
        "title": "This Congress",
        "era": "119th Congress · 2025",
        "intro": ("Unified Republican government moves at reconciliation speed: an "
                  "immigration bill in January, a megabill by July, and a test of "
                  "whether Congress will claw back its own appropriations."),
        "senators": [
            ("collins",   "Chairing Appropriations in a year the White House treats "
                          "spending laws as suggestions, Maine's moderate is "
                          "defending both her committee's power and a 2026 "
                          "re-election in a state that votes blue for president."),
            ("murkowski", "Alaska's dealmaker drives the hardest bargains of the "
                          "year — carve-outs for her state are her price, and she "
                          "describes her biggest vote of the summer as 'agonizing.' "
                          "Nobody works a 50-50 chamber better."),
            ("rpaul",     "Kentucky's libertarian is the loneliest kind of "
                          "consistent: for the spending cuts, against the debt- "
                          "ceiling increases, and immune to pressure from a White "
                          "House he often votes against and never stops praising."),
            ("fetterman", "The Senate's most unpredictable Democrat: pro-border- "
                          "enforcement, pro-Israel, and openly bored by his party's "
                          "orthodoxies — but a Medicaid vote is a different animal "
                          "in a state with 3 million enrollees."),
            ("tillis",    "North Carolina's pragmatist announced he won't seek "
                          "re-election — one day after the President threatened to "
                          "primary him over the megabill. A lame duck now, with "
                          "eighteen months left and nothing to lose."),
        ],
        "bills": [
            {
                "congress": 119, "session": 1, "vote": 7,
                "name": "The Laken Riley Act",
                "desc": ("January 20, 2025 — inauguration day. The new Congress's "
                         "first bill: mandatory federal detention for undocumented "
                         "immigrants charged with theft, burglary, or assaulting a "
                         "police officer, and standing for state attorneys general "
                         "to sue federal immigration authorities. Named for the "
                         "Georgia nursing student murdered by a Venezuelan man in "
                         "the country illegally. A dozen Democrats are ready to "
                         "sign on."),
            },
            {
                "congress": 119, "session": 1, "vote": 372,
                "name": "The One Big Beautiful Bill",
                "desc": ("July 1, 2025, after a 27-hour vote-a-rama. The "
                         "reconciliation megabill: the 2017 tax cuts made "
                         "permanent, no taxes on tips and overtime, a huge border "
                         "and defense buildup — paid for in part by Medicaid work "
                         "requirements and provider-tax cuts projected to leave "
                         "millions uninsured, plus a $5 trillion debt-limit "
                         "increase. The tally stands at 50-50; the Vice President "
                         "is in the chair."),
            },
            {
                "congress": 119, "session": 1, "vote": 411,
                "name": "The $9 Billion Clawback",
                "desc": ("July 17, 2025, 2:18 a.m. A rescissions package canceling "
                         "money Congress already appropriated: roughly $8 billion "
                         "in foreign aid and $1.1 billion for the Corporation for "
                         "Public Broadcasting — the funding stream behind NPR and "
                         "PBS stations. The White House calls it a down payment on "
                         "DOGE's cuts; appropriators in both parties call it a "
                         "dangerous precedent."),
            },
        ],
    },
    {
        "id": "overtime",
        "title": "The Gang of Fourteen",
        "era": "109th Congress · 2005",
        "intro": ("The Senate is one vote from the 'nuclear option' — abolishing "
                  "judicial filibusters by fiat — when fourteen senators cut a "
                  "midnight deal to save the old rules. Two days later, the deal "
                  "meets John Bolton."),
        "senators": [
            ("mccain",    "The maverick at maximum wattage: chief architect of the "
                          "Gang of Fourteen compromise, to the fury of "
                          "conservatives who wanted the filibuster dead. He loves "
                          "the institution, hates wasteful spending — and is "
                          "already running for 2008."),
            ("byrd",      "The Senate's 87-year-old constitutional conscience, who "
                          "gave four floor orations against the nuclear option and "
                          "joined the Gang to stop it. For him the rules are the "
                          "republic — but a deal is a deal."),
            ("voinovich", "Ohio's mild-mannered former governor, a deficit hawk with "
                          "a stubborn independent streak. He stunned his party by "
                          "balking at Bolton in committee — and will plead from the "
                          "floor, near tears, that the nomination is a mistake."),
            ("obama",     "The freshman phenomenon from Illinois, five months into "
                          "the job: deferential to Senate customs, wary of looking "
                          "obstructionist, and taking careful notes on how the "
                          "chamber's power games are played."),
            ("graham",    "South Carolina's quick-witted operator, a Gang of "
                          "Fourteen member who took real heat at home for the deal. "
                          "A JAG officer and unapologetic hawk: he'll protect the "
                          "Senate's rules and the President's nominees, in that "
                          "order — or is it the other way around?"),
        ],
        "bills": [
            {
                "congress": 109, "session": 1, "vote": 127,
                "name": "The Deal's First Test: Priscilla Owen",
                "desc": ("May 24, 2005 — twelve hours after the Gang of Fourteen "
                         "signed its memorandum. Cloture on Priscilla Owen, the "
                         "Texas justice Democrats have filibustered for four years, "
                         "now guaranteed a vote as one of the deal's named judges. "
                         "This roll call measures whether the truce holds: even "
                         "senators who'll oppose her confirmation must decide "
                         "whether to let debate end."),
            },
            {
                "congress": 109, "session": 1, "vote": 129,
                "name": "Ending Debate on John Bolton",
                "desc": ("May 26, 2005. Two days later, the truce meets its limits: "
                         "cloture on John Bolton, Bush's famously abrasive nominee "
                         "for UN ambassador, accused of bullying intelligence "
                         "analysts. Democrats say they're not filibustering — just "
                         "demanding documents the White House won't release. "
                         "Sixty votes ends debate; the Gang's memo covers judges, "
                         "not ambassadors."),
            },
            {
                "congress": 109, "session": 1, "vote": 158,
                "name": "The Energy Policy Act",
                "desc": ("June 28, 2005. The first big energy law in a decade: "
                         "loan guarantees for new nuclear plants, subsidies and "
                         "royalty relief across oil, gas, coal, and ethanol, and "
                         "daylight-saving time stretched by a month. Critics in "
                         "both parties call it a grab bag for producers that "
                         "does nothing about gasoline prices; its authors call it "
                         "an overdue investment in everything."),
            },
        ],
    },
]
