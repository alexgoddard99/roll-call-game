# Batch A — pre-1989 (voteview) puzzles A1-A13, plus two 101st-Congress
# (senate.gov) puzzles A14-A15. Verified via: python3 fetch.py batches/batch_A.py

SENATORS_EXTRA = {
    # key: (bioguide, display name, party, state) — era-accurate party labels
    "humphrey":   ("H000953", "Hubert Humphrey", "D", "MN"),
    "dirksen":    ("D000360", "Everett Dirksen", "R", "IL"),
    "russell":    ("R000536", "Richard Russell", "D", "GA"),
    "goldwater":  ("G000267", "Barry Goldwater", "R", "AZ"),
    "mcsmith":    ("S000590", "Margaret Chase Smith", "R", "ME"),
    "mansfield":  ("M000113", "Mike Mansfield", "D", "MT"),
    "rfkennedy":  ("K000114", "Robert F. Kennedy", "D", "NY"),
    "thurmond":   ("T000254", "Strom Thurmond", "R", "SC"),
    "fulbright":  ("F000401", "J. William Fulbright", "D", "AR"),
    "javits":     ("J000064", "Jacob Javits", "R", "NY"),
    "bayh":       ("B000254", "Birch Bayh", "D", "IN"),
    "ervin":      ("E000211", "Sam Ervin", "D", "NC"),
    "church":     ("C000388", "Frank Church", "D", "ID"),
    "hbaker":     ("B000063", "Howard Baker", "R", "TN"),
    "hayakawa":   ("H000384", "S.I. Hayakawa", "R", "CA"),
    "proxmire":   ("P000553", "William Proxmire", "D", "WI"),
    "jwarner":    ("W000154", "John Warner", "R", "VA"),
    "mitchell":   ("M000811", "George Mitchell", "D", "ME"),
    "hatch":      ("H000338", "Orrin Hatch", "R", "UT"),
    "metzenbaum": ("M000678", "Howard Metzenbaum", "D", "OH"),
    "danforth":   ("D000030", "John Danforth", "R", "MO"),
}

PUZZLES = [
    {
        "id": "longest-debate",
        "title": "The Longest Debate",
        "era": "88th Congress · 1964",
        "intro": ("An election year like no other: a martyred president's program on the "
                  "floor, a 60-day filibuster to break, a tax cut to pass — and, one August "
                  "morning, a resolution about two destroyers in a distant gulf."),
        "senators": [
            ("humphrey", "The Senate's happy warrior: Minneapolis's evangelist of liberalism, "
                         "majority whip, and floor general of the civil rights forces — while "
                         "auditioning, everyone knows, to be Lyndon Johnson's running mate."),
            ("dirksen",  "The Minority Leader from Illinois, a baroque orator with a voice like "
                         "a pipe organ. He loves the Senate, the Republic, and being "
                         "indispensable — his price is being courted, publicly and at length."),
            ("russell",  "The courtly Georgian who commands the Southern bloc and knows the "
                         "rulebook better than the parliamentarian. Johnson's old mentor, a "
                         "defense hawk to his marrow — and the general of the longest "
                         "filibuster in Senate history."),
            ("goldwater","Arizona's flinty individualist, weeks from seizing the Republican "
                         "presidential nomination from the party's Eastern establishment. He "
                         "reads most federal power as constitutional trespass and votes that "
                         "way, whatever it costs him in November."),
            ("mcsmith",  "Maine's independent Republican, the first woman ever placed in "
                         "nomination for president by a major party. She made her name defying "
                         "Joe McCarthy in 1950 and has answered to no one since."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 88, "roll": 409,
                "name": "The Civil Rights Act of 1964",
                "question": "On Passage of H.R. 7152", "result": "Bill Passed",
                "desc": ("June 19, 1964 — one year to the day after President Kennedy sent the "
                         "bill to Congress. It outlaws segregation in restaurants, hotels, and "
                         "theaters, and discrimination in hiring. The Southern filibuster ran "
                         "60 working days before the Senate invoked cloture on a civil rights "
                         "bill for the first time in its history."),
            },
            {
                "source": "voteview", "congress": 88, "roll": 264,
                "name": "The Kennedy Tax Cut",
                "question": "On Passage of H.R. 8363", "result": "Bill Passed",
                "desc": ("February 7, 1964. The Revenue Act: the biggest tax cut in American "
                         "history to date, slashing the top individual rate from 91% to 70% to "
                         "goose a sluggish economy. Kennedy proposed it; Johnson muscled it "
                         "through by promising to hold the budget under $100 billion. "
                         "Deficit-wary conservatives are not soothed."),
            },
            {
                "source": "voteview", "congress": 88, "roll": 481,
                "name": "The Gulf of Tonkin Resolution",
                "question": "On Passage of H.J. Res. 1145", "result": "Resolution Passed",
                "desc": ("August 7, 1964, three days after reported North Vietnamese attacks "
                         "on the destroyers Maddox and Turner Joy. The resolution approves "
                         "'all necessary measures' to repel armed attack in Southeast Asia — "
                         "no declaration of war, no expiration date. Debate takes less than "
                         "nine hours; only two senators are opposed."),
            },
        ],
    },
    {
        "id": "great-society",
        "title": "The Great Society",
        "era": "89th Congress · 1965",
        "intro": ("Johnson's landslide has delivered a two-to-one Democratic Senate, and he "
                  "intends to spend every ounce of it — on the vote, on the old, and on who "
                  "gets to become an American."),
        "senators": [
            ("mansfield","The Majority Leader: a laconic Montanan and former history professor "
                         "who leads by patience where Johnson led by the lapels. He considers "
                         "every senator's conscience his own business — including his own."),
            ("dirksen",  "The Republican leader, fresh from delivering the votes that broke "
                         "the 1964 filibuster. He calls himself 'not a moss-back' — but every "
                         "Great Society bill must survive his theatrical scrutiny first."),
            ("rfkennedy","The freshman from New York — attorney general ten months ago, "
                         "carrying his brother's unfinished agenda and a following no "
                         "first-termer has ever had. Liberal, restless, and impatient with "
                         "the Senate's pace."),
            ("thurmond", "South Carolina's converted Republican — he bolted the Democratic "
                         "Party last September to campaign for Goldwater. The 1948 Dixiecrat "
                         "nominee still holds the record for the longest one-man filibuster, "
                         "set against a civil rights bill."),
            ("byrd",     "West Virginia's tireless workhorse, a coal-country New Dealer on "
                         "economics who joined the Southerners' filibuster against last "
                         "year's civil rights act. He is studying the rulebook — and playing "
                         "a longer game than most notice."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 89, "roll": 78,
                "name": "The Voting Rights Act",
                "question": "On Passage of S. 1564", "result": "Bill Passed",
                "desc": ("May 26, 1965, ten weeks after state troopers clubbed marchers at "
                         "the Edmund Pettus Bridge in Selma. The bill suspends literacy tests "
                         "in states with a history of disenfranchisement and sends federal "
                         "examiners south to register Black voters directly. Cloture ended "
                         "the Southern filibuster the day before."),
            },
            {
                "source": "voteview", "congress": 89, "roll": 151,
                "name": "Medicare",
                "question": "On Passage of H.R. 6675", "result": "Bill Passed",
                "desc": ("July 9, 1965. Health insurance for every American over 65, funded "
                         "through Social Security — the cause organized medicine has fought "
                         "as 'socialized medicine' since Truman proposed it in 1945. The "
                         "package adds Medicaid for the poor. The AMA warns of bureaucrats "
                         "between doctor and patient."),
            },
            {
                "source": "voteview", "congress": 89, "roll": 232,
                "name": "The Immigration and Nationality Act",
                "question": "On Passage of H.R. 2580", "result": "Bill Passed",
                "desc": ("September 22, 1965. The bill abolishes the national-origins quota "
                         "system that has favored Northern Europeans since 1924, replacing it "
                         "with preferences for family reunification and skills. Supporters "
                         "insist it will barely change the country's demographic mix; "
                         "opponents call the old system common sense."),
            },
        ],
    },
    {
        "id": "sixty-eight",
        "title": "1968",
        "era": "90th Congress · 1968",
        "intro": ("The most convulsive year in postwar politics: King assassinated in April, "
                  "Kennedy in June, cities burning, a war souring, a president renouncing "
                  "re-election — and the Senate voting through all of it."),
        "senators": [
            ("fulbright","Chairman of Foreign Relations and the war's most prominent critic — "
                         "his televised hearings made dissent respectable. But the Rhodes "
                         "Scholar from Arkansas signed the Southern Manifesto, and his civil "
                         "rights record reads like his region's."),
            ("thurmond", "The South Carolina Republican, this year's kingmaker: he is holding "
                         "the South for Richard Nixon at the convention and demanding a say "
                         "on judges in return. Order, he believes, is on the ballot."),
            ("kennedy",  "The last Kennedy brother, 36 years old. Robert was murdered in June; "
                         "Ted has returned to the floor grief-stricken but determined, the "
                         "family's causes — the poor, the disenfranchised, gun laws — now "
                         "his alone to carry."),
            ("mcsmith",  "Twenty years into her Senate career, Maine's flinty Republican "
                         "matriarch: hawkish on defense, protective of institutions, and "
                         "immune to pressure campaigns from any direction."),
            ("javits",   "New York's liberal Republican — a Lincoln Republican, he'd say — "
                         "who votes for civil rights, urban aid, and gun control as readily "
                         "as any Democrat, and usually earlier."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 90, "roll": 346,
                "name": "The Fair Housing Act",
                "question": "On Passage of H.R. 2516", "result": "Bill Passed",
                "desc": ("March 11, 1968. The last great civil rights bill: a ban on racial "
                         "discrimination in the sale and rental of most of the nation's "
                         "housing, attached to protections for civil rights workers. It "
                         "survived weeks of filibuster on a knife's-edge cloture vote. One "
                         "month later, King is dead and the House passes it in days."),
            },
            {
                "source": "voteview", "congress": 90, "roll": 558,
                "name": "The Gun Control Act of 1968",
                "question": "On Passage of H.R. 17735", "result": "Bill Passed",
                "desc": ("September 18, 1968, after a spring and summer of assassination. "
                         "The bill bans mail-order sales of rifles and shotguns — the way "
                         "Oswald bought his carbine — bars felons from buying guns, and "
                         "requires dealers to be licensed. The NRA calls it a step toward "
                         "confiscation; sportsmen's states are restive."),
            },
            {
                "source": "voteview", "congress": 90, "roll": 570,
                "name": "Cloture on Abe Fortas",
                "question": "On Cloture on the Nomination of Abe Fortas",
                "result": "Cloture Motion Rejected",
                "desc": ("October 1, 1968. Johnson has nominated Justice Abe Fortas — his "
                         "confidant — to be Chief Justice, and a coalition of Republicans and "
                         "Southern Democrats has filibustered a Supreme Court nomination for "
                         "the first time. Critics cite cronyism, outside fees, and the Warren "
                         "Court itself. A yea is a vote to end debate and save the nomination."),
            },
        ],
    },
    {
        "id": "rejected-judges",
        "title": "The Rejected Judges",
        "era": "91st Congress · 1969–1970",
        "intro": ("Richard Nixon promised the South a different kind of Supreme Court "
                  "justice. Twice he sends one up; twice the Senate does something it has "
                  "not done in decades. Then it kills his airplane, too."),
        "senators": [
            ("bayh",     "Indiana's boyish second-termer, suddenly the chamber's chief "
                         "nomination-slayer: he is marshaling the case against Nixon's court "
                         "picks from the Judiciary Committee while drafting constitutional "
                         "amendments on the side."),
            ("goldwater","Restored to the Senate after his 1964 wipeout and elder statesman "
                         "of the right: loyal to Nixon's court strategy, contemptuous of "
                         "federal subsidies — and of Washington fads of every kind."),
            ("mcsmith",  "The Senate's senior woman, whose vote no leader can take for "
                         "granted. She weighs nominations like a juror and regards White "
                         "House pressure as an argument for the other side."),
            ("fulbright","The Arkansas patrician, still running Foreign Relations and still "
                         "voting Southern on most domestic matters — though a nominee's "
                         "competence, he allows, is a separate question from his region."),
            ("thurmond", "The architect of Nixon's Southern strategy, now collecting on it: "
                         "he wants strict constructionists on the Court and considers every "
                         "rejection a purge of the South."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 91, "roll": 135,
                "name": "Confirming Clement Haynsworth",
                "question": "On the Nomination of Clement Haynsworth",
                "result": "Nomination Rejected",
                "desc": ("November 13, 1969. Nixon's first try for the Fortas seat: a "
                         "Fourth Circuit judge from South Carolina. Labor and civil rights "
                         "groups oppose his record; the fatal wound is ethics — he sat on "
                         "cases touching companies in which he held stock. Seventeen "
                         "Republicans abandon their president."),
            },
            {
                "source": "voteview", "congress": 91, "roll": 357,
                "name": "Confirming G. Harrold Carswell",
                "question": "On the Nomination of G. Harrold Carswell",
                "result": "Nomination Rejected",
                "desc": ("April 1970. Nixon's second try: a Florida judge with a 1948 "
                         "white-supremacy speech in his past and a reversal rate that makes "
                         "even allies wince — one defender argues mediocre people deserve "
                         "representation too. The White House calls opposition an insult to "
                         "the South and demands party discipline."),
            },
            {
                "source": "voteview", "congress": 91, "roll": 623,
                "name": "Killing the Supersonic Transport",
                "question": "On the Amendment to Strike SST Funding",
                "result": "Amendment Agreed to",
                "desc": ("December 3, 1970. An amendment striking $290 million for the "
                         "Boeing SST, America's answer to the Concorde. Backers call it "
                         "national prestige and 150,000 jobs; a new environmental coalition "
                         "cites sonic booms, the ozone layer, and a subsidy for businessmen "
                         "in a hurry. A yea kills the plane."),
            },
        ],
    },
    {
        "id": "equal-rights",
        "title": "The Equal Rights Spring",
        "era": "92nd Congress · 1972",
        "intro": ("In one late-winter stretch the Senate takes up women's rights, school "
                  "busing, and job discrimination — three arguments about equality, each "
                  "drawing a different line through the chamber."),
        "senators": [
            ("bayh",     "The Hoosier constitutional handyman — author of two ratified "
                         "amendments already and Senate champion of the equal rights "
                         "amendment, which he has pushed through years of hearings."),
            ("ervin",    "North Carolina's country-lawyer constitutionalist, quick with "
                         "Scripture and Shakespeare. He believes the Constitution already "
                         "says what it needs to — and that federal judges and social "
                         "engineers keep discovering things in it that aren't there."),
            ("mcsmith",  "In her final year, as it turns out: 32 years in Congress, the "
                         "chamber's senior Republican woman, still casting votes with the "
                         "same flinty independence she showed Joe McCarthy."),
            ("goldwater","The conscience of conservatism, suspicious of grand constitutional "
                         "renovations and of Washington telling states how to run their "
                         "schools — though he likes to say his libertarian streak cuts in "
                         "unexpected directions."),
            ("kennedy",  "The liberal standard-bearer now, rebuilding after Chappaquiddick: "
                         "floor leader for civil rights causes and a reliable vote against "
                         "anything that retreats from desegregation."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 92, "roll": 533,
                "name": "The Equal Rights Amendment",
                "question": "On Passage of H.J. Res. 208", "result": "Resolution Passed",
                "desc": ("March 22, 1972. 'Equality of rights under the law shall not be "
                         "denied or abridged... on account of sex.' After 49 years of "
                         "introduction and burial, the ERA reaches a final vote, every "
                         "weakening amendment — on the draft, on protective labor laws — "
                         "already beaten back. Ratification by 38 states awaits."),
            },
            {
                "source": "voteview", "congress": 92, "roll": 477,
                "name": "Barring Court-Ordered Busing",
                "question": "On the Amendment to Bar Court-Ordered Busing",
                "result": "Amendment Agreed to",
                "desc": ("February 25, 1972. An amendment to the higher-education bill "
                         "barring federal courts from ordering the busing of schoolchildren "
                         "on the basis of race. Busing is the rawest issue in American "
                         "politics this year — George Wallace is winning primaries on it — "
                         "and Northern liberals are feeling the ground shift. A yea "
                         "restricts the courts."),
            },
            {
                "source": "voteview", "congress": 92, "roll": 468,
                "name": "Breaking the EEOC Filibuster",
                "question": "On Cloture on S. 2515", "result": "Cloture Invoked",
                "desc": ("February 22, 1972. Cloture on the Equal Employment Opportunity "
                         "Act, which for the first time lets the EEOC take job-discrimination "
                         "cases to court itself rather than merely conciliate. A Southern "
                         "filibuster has held the bill for weeks; a yea ends the talking and "
                         "moves the bill toward passage."),
            },
        ],
    },
    {
        "id": "war-powers",
        "title": "The War Powers Autumn",
        "era": "93rd Congress · 1973",
        "intro": ("Watergate is devouring the White House, the Middle East is at war, oil "
                  "is a weapon, and a vice president has just resigned in disgrace. "
                  "Congress decides it is time to take some power back."),
        "senators": [
            ("church",   "Idaho's orator-moralist, a Vietnam critic since 1965. He believes "
                         "Congress has surrendered its war-making power to an imperial "
                         "presidency — and that the surrender ends now. Wilderness and "
                         "wild rivers are his other religion."),
            ("javits",   "The New York Republican polymath and principal author of the war "
                         "powers legislation — a liberal internationalist determined to bind "
                         "presidents of both parties to the Constitution's war clause."),
            ("goldwater","The right's constitutional purist, on the opposite side of this "
                         "one: the commander-in-chief power, he argues, is not Congress's "
                         "to fence in. Development of the West, oil included, needs no "
                         "apology either."),
            ("byrd",     "The Democratic whip, a coal-and-industry Democrat who mistrusts "
                         "executive overreach on institutional grounds — and reads the "
                         "Constitution from a copy in his breast pocket."),
            ("kennedy",  "The liberal lion in his prime: against the war machine, "
                         "skeptical of Big Oil's shortcuts, and increasingly the man "
                         "Democrats imagine on a national ticket."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 93, "roll": 462,
                "name": "The War Powers Resolution",
                "question": "On Overriding the Veto of H.J. Res. 542",
                "result": "Veto Overridden",
                "desc": ("November 7, 1973. Nixon has vetoed the bill requiring presidents "
                         "to consult Congress before sending forces into hostilities and to "
                         "withdraw them within 60 days absent authorization. Days after the "
                         "Saturday Night Massacre, a weakened White House watches Congress "
                         "muster two-thirds. A yea overrides the veto."),
            },
            {
                "source": "voteview", "congress": 93, "roll": 286,
                "name": "Fast-Tracking the Alaska Pipeline",
                "question": "On the Gravel Amendment to S. 1081",
                "result": "Amendment Agreed to",
                "desc": ("July 17, 1973. The Gravel amendment declares the trans-Alaska "
                         "oil pipeline compliant with environmental law and bars further "
                         "court review — the environmental movement's nightmare precedent, "
                         "energy hawks' answer to dependence on Arab crude. It passes by a "
                         "single vote, months before the embargo makes it look prophetic."),
            },
            {
                "source": "voteview", "congress": 93, "roll": 499,
                "name": "Confirming Gerald Ford as Vice President",
                "question": "On the Nomination of Gerald R. Ford",
                "result": "Nomination Confirmed",
                "desc": ("November 27, 1973. Spiro Agnew has resigned and pleaded no contest "
                         "to tax evasion; under the new 25th Amendment, Congress must confirm "
                         "his successor. Nixon sends up the House Republican leader — genial, "
                         "unspectacular, trusted — while everyone in the chamber quietly "
                         "wonders whether they are choosing the next president."),
            },
        ],
    },
    {
        "id": "ford-years",
        "title": "The Ford Years",
        "era": "94th Congress · 1975–1976",
        "intro": ("An unelected president, a wrecked economy, and a Congress swollen with "
                  "post-Watergate reformers — busy investigating spies, extending the "
                  "franchise, and arguing about how to revive a stagflated country."),
        "senators": [
            ("church",   "Now chairman of the select committee bearing his name, spending "
                         "1975 dragging CIA assassination plots and NSA cable-reading into "
                         "daylight — convinced secrecy without oversight corrupts everything "
                         "it touches."),
            ("goldwater","A member of the same Church Committee and its in-house dissenter: "
                         "he thinks airing the agencies' secrets weakens the country, and "
                         "that most of Washington's post-Watergate penance is theater."),
            ("biden",    "The Senate's youngest member — elected at 29, sworn in weeks after "
                         "losing his wife and daughter. A Delaware Democrat with working-class "
                         "instincts, a moderate's caution, and a surprising deficit streak."),
            ("thurmond", "The South's iron man, past 70 and doing push-ups to prove it: "
                         "pro-Pentagon, anti-Washington, and unreconciled to federal "
                         "supervision of Southern elections."),
            ("humphrey", "Back in the Senate after the vice presidency and the heartbreak of "
                         "1968: the happy warrior turned elder, still preaching full "
                         "employment and federal activism as if the New Deal never ended."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 94, "roll": 112,
                "name": "The Tax Cut of 1975",
                "question": "On Passage of H.R. 2166", "result": "Bill Passed",
                "desc": ("March 21, 1975. With unemployment past 8% and the economy in its "
                         "worst slump since the Depression, a $30 billion emergency tax cut: "
                         "rebates on 1974 taxes, credits for home-buyers, and relief tilted "
                         "toward lower incomes. Ford wants a smaller bill; deficit hawks in "
                         "both parties want none at all."),
            },
            {
                "source": "voteview", "congress": 94, "roll": 329,
                "name": "Extending the Voting Rights Act",
                "question": "On Passage of H.R. 6219", "result": "Bill Passed",
                "desc": ("July 24, 1975. A seven-year extension of the Voting Rights Act, "
                         "adding permanent protections for 'language minorities' — Spanish "
                         "speakers, Native Americans — and keeping Southern states under "
                         "federal preclearance. Opponents ask when, if ever, the South will "
                         "be trusted to run its own elections again."),
            },
            {
                "source": "voteview", "congress": 94, "roll": 792,
                "name": "Creating the Intelligence Committee",
                "question": "On Agreeing to S. Res. 400", "result": "Resolution Agreed to",
                "desc": ("May 19, 1976. After a year of revelations — assassination plots, "
                         "mail-opening, surveillance of Americans — the Senate votes to "
                         "create a permanent Select Committee on Intelligence with power "
                         "over the agencies' budgets and secrets. Defenders of the old "
                         "order call it a standing leak waiting to happen."),
            },
        ],
    },
    {
        "id": "the-canal",
        "title": "The Canal",
        "era": "95th Congress · 1978",
        "intro": ("Jimmy Carter has signed treaties handing the Panama Canal to Panama by "
                  "century's end, and ratification needs 67 votes. The New Right smells "
                  "the defining cause of the decade. Every senator counts the mail."),
        "senators": [
            ("byrd",     "Majority Leader at last, the fiddle-playing parliamentarian from "
                         "West Virginia. He came to the treaties a skeptic and now steers "
                         "them personally, senator by senator, reservation by reservation — "
                         "his leadership's first great test."),
            ("hbaker",   "The Republican leader, gifted with the party's best temperament "
                         "and worst timing: he wants to run for president in 1980, and 'the "
                         "man who gave away the canal' is not the slogan his strategists "
                         "had in mind. He read the treaties anyway."),
            ("goldwater","The old standard-bearer: to him the canal is American soil, "
                         "bought and paid for, and giving it up under pressure invites "
                         "every adversary to push. His mail runs hot, and so does he."),
            ("church",   "Foreign Relations' liberal heavyweight, floor-managing "
                         "ratification: he argues the canal is defensible only with "
                         "Panamanian consent — and that clinging to a colonial enclave "
                         "poisons the whole hemisphere. Idaho's phone lines disagree."),
            ("hayakawa", "California's freshman celebrity — the semanticist who faced down "
                         "student radicals at San Francisco State in a tam-o'-shanter. He "
                         "campaigned saying the canal was ours; scholars' second thoughts "
                         "are, for him, an occupational habit."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 95, "roll": 702,
                "name": "The Canal Neutrality Treaty",
                "question": "On the Resolution of Ratification", "result": "Treaty Ratified",
                "desc": ("March 16, 1978. The first of the two Panama treaties: the canal's "
                         "permanent neutrality, with the U.S. keeping the right to defend it "
                         "forever. Weeks of debate over a 'DeConcini condition' on American "
                         "intervention have inflamed Panama City. Ratification requires "
                         "two-thirds — 67 votes, with none to spare."),
            },
            {
                "source": "voteview", "congress": 95, "roll": 755,
                "name": "The Panama Canal Treaty",
                "question": "On the Resolution of Ratification", "result": "Treaty Ratified",
                "desc": ("April 18, 1978. The main event: full transfer of the canal to "
                         "Panama on December 31, 1999. Conservative groups have raised "
                         "millions against it; senators who vote yes are promised primary "
                         "opponents. Carter calls wavering members from the White House "
                         "until the final hour. Again, 67 votes or death."),
            },
            {
                "source": "voteview", "congress": 95, "roll": 1047,
                "name": "The Natural Gas Compromise",
                "question": "On the Conference Report on H.R. 5289",
                "result": "Conference Report Agreed to",
                "desc": ("September 27, 1978. The heart of Carter's energy plan after 18 "
                         "months of trench warfare: phased deregulation of new natural gas "
                         "prices by 1985. Producers call it too slow, consumer champions "
                         "call it a giveaway, and the conference report survives on a "
                         "coalition nobody can quite explain."),
            },
        ],
    },
    {
        "id": "malaise",
        "title": "Malaise",
        "era": "96th Congress · 1979",
        "intro": ("Gas lines, 13% inflation, a president talking about a national crisis "
                  "of confidence — and a Massachusetts senator measuring the Oval Office "
                  "drapes. Washington's answer: create, rescue, and tax."),
        "senators": [
            ("kennedy",  "The liberal heir apparent, polling ahead of his own president: by "
                         "November he has announced against Carter. Big institutions — "
                         "national health insurance, federal activism — remain articles "
                         "of faith."),
            ("dole",     "Kansas's flinty wit, back from the 1976 ticket and running for "
                         "president himself: a farm-state conservative with a heart for "
                         "food stamps and the disabled, and a bookkeeper's eye on every "
                         "new federal outlay."),
            ("byrd",     "The Majority Leader, keeping a restive Democratic caucus moving "
                         "through an ugly economy — loyal to the party's program, if not "
                         "always to the man in the White House."),
            ("lugar",    "Indiana's methodical freshman, the former Indianapolis mayor "
                         "known as Nixon's favorite: a fiscal conservative who does his "
                         "homework and distrusts bailouts — though Indiana builds a lot "
                         "of Chryslers."),
            ("proxmire", "Wisconsin's ascetic scourge of waste, inventor of the Golden "
                         "Fleece Award, chairman of Banking — and sworn enemy of the "
                         "proposition that Washington should rescue badly run companies."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 96, "roll": 70,
                "name": "The Department of Education",
                "question": "On Passage of S. 210", "result": "Bill Passed",
                "desc": ("April 30, 1979. Carter's payoff to the teachers who elected him, "
                         "critics say; overdue recognition of a national priority, backers "
                         "answer. The bill carves a cabinet Department of Education out of "
                         "HEW. Conservatives warn of federal control of the classroom; the "
                         "AFL-CIO's teachers are watching the roll call."),
            },
            {
                "source": "voteview", "congress": 96, "roll": 495,
                "name": "The Windfall Profits Tax",
                "question": "On Passage of H.R. 3919", "result": "Bill Passed",
                "desc": ("December 17, 1979. Carter is decontrolling oil prices; this is "
                         "the price of the price: an excise tax on the industry's resulting "
                         "windfall, projected in the hundreds of billions, funding energy "
                         "aid for the poor and synthetic fuels. Oil-state senators call it "
                         "confiscation of an industry the country needs drilling."),
            },
            {
                "source": "voteview", "congress": 96, "roll": 501,
                "name": "The Chrysler Bailout",
                "question": "On Passage of H.R. 5860", "result": "Bill Passed",
                "desc": ("December 19, 1979. Chrysler is weeks from collapse; the bill "
                         "guarantees $1.5 billion in loans, conditioned on union wage "
                         "concessions. Unprecedented, says nearly everyone — the argument "
                         "is whether that's the objection or the point. Half a million "
                         "jobs ride on the answer."),
            },
        ],
    },
    {
        "id": "morning-in-america",
        "title": "Morning in America",
        "era": "97th Congress · 1981",
        "intro": ("Reagan arrives with a mandate, a Republican Senate — the first in a "
                  "generation — and a bullet wound that made him a legend by April. "
                  "Washington spends 1981 discovering what it can't refuse him."),
        "senators": [
            ("hbaker",   "Majority Leader of a chamber his party hasn't run since 1954, "
                         "shelving his own presidential ambitions to be Reagan's "
                         "indispensable man in the Senate — herding 53 Republicans through "
                         "an agenda he privately calls a riverboat gamble."),
            ("dole",     "The new Finance Committee chairman, wry as ever: he'll carry the "
                         "president's tax bill, but the deficit projections keep him up "
                         "nights, and he doesn't pretend otherwise."),
            ("kennedy",  "Suddenly in the minority for the first time in his career, the "
                         "left's anchor against the Reagan tide — picking which fights "
                         "can still be won."),
            ("moynihan", "The Harvard social scientist turned New York Democrat, allergic "
                         "to orthodoxy in both directions: he likes ideas more than "
                         "parties, Israel and Social Security more than either."),
            ("goldwater","The movement's founding father, watching his revolution finally "
                         "take power — chairing Intelligence, guarding the Pentagon, and "
                         "saying exactly what he thinks about everyone."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 97, "roll": 239,
                "name": "The Reagan Tax Cut",
                "question": "On the Finance Committee Substitute to H.J. Res. 266",
                "result": "Agreed to",
                "desc": ("July 29, 1981. The Economic Recovery Tax Act: individual rates "
                         "cut 25% across the board over three years, indexed against "
                         "inflation, with sweetened depreciation for business. Supply-side "
                         "economics gets its full-scale national test. Democrats, reading "
                         "the election returns, largely decline to stand in front of it."),
            },
            {
                "source": "voteview", "congress": 97, "roll": 338,
                "name": "Blocking the AWACS Sale",
                "question": "On the Resolution of Disapproval", "result": "Resolution Rejected",
                "desc": ("October 28, 1981. A resolution to block Reagan's $8.5 billion "
                         "sale of AWACS radar planes to Saudi Arabia — opposed by Israel, "
                         "AIPAC, and, at the outset, a Senate majority. Reagan works "
                         "waverers one by one: 'It is not the business of other nations to "
                         "make American foreign policy.' A yea kills the sale."),
            },
            {
                "source": "voteview", "congress": 97, "roll": 274,
                "name": "Confirming Sandra Day O'Connor",
                "question": "On the Nomination of Sandra Day O'Connor",
                "result": "Nomination Confirmed",
                "desc": ("September 21, 1981. Reagan keeps a campaign promise and names "
                         "the first woman to the Supreme Court: an Arizona appeals judge "
                         "and former state senate majority leader. Some anti-abortion "
                         "groups grumble about her record in Phoenix; the Senate is not "
                         "in a grumbling mood."),
            },
        ],
    },
    {
        "id": "helms-objection",
        "title": "The Helms Objection",
        "era": "98th Congress · 1983",
        "intro": ("A year of repair work — rescuing Social Security, honoring Dr. King, "
                  "funding the MX — with one senator from North Carolina determined to "
                  "make every consensus as expensive as possible."),
        "senators": [
            ("helms",    "The right's parliamentary guerrilla, up for re-election in 1984: "
                         "he forces recorded votes on school prayer, abortion, and busing "
                         "that colleagues spend years explaining. Compromise, he likes to "
                         "say, is how the other side wins slowly."),
            ("dole",     "Finance chairman at the height of his dealmaking powers: he "
                         "brokered the Social Security rescue and has begun nudging his "
                         "party toward arithmetic — a habit the supply-siders resent."),
            ("kennedy",  "The liberal lion in opposition: fighting Reagan's defense buildup "
                         "and budget cuts, championing the nuclear freeze, and lending the "
                         "King holiday campaign three decades of family weight."),
            ("moynihan", "The scholar-senator who helped save Social Security on the "
                         "commission that bears no one's name: proudly pro-arms-control, "
                         "increasingly certain the deficit is an engineered trap."),
            ("kassebaum","Kansas's understated Republican — Alf Landon's daughter — with an "
                         "internationalist head and a moderate's voting record she declines "
                         "to apologize for. Defense votes she takes case by case."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 98, "roll": 53,
                "name": "Rescuing Social Security",
                "question": "On Passage of H.R. 1900", "result": "Bill Passed",
                "desc": ("March 23, 1983. Social Security is months from missing checks. "
                         "The Greenspan Commission's rescue: accelerate payroll-tax "
                         "increases, tax benefits for higher incomes, raise the retirement "
                         "age to 67 over decades, and cover new federal workers. Everyone's "
                         "sacred cow gets a haircut — that's the design."),
            },
            {
                "source": "voteview", "congress": 98, "roll": 114,
                "name": "Funding the MX Missile",
                "question": "On Agreeing to S. Con. Res. 26", "result": "Resolution Agreed to",
                "desc": ("May 25, 1983. The resolution releases funds to build and base the "
                         "MX — ten warheads per missile, dubbed 'Peacekeeper' — in existing "
                         "Minuteman silos. Reagan calls it leverage for arms talks with "
                         "Moscow; freeze advocates call it a first-strike weapon in a "
                         "vulnerable hole. The nuclear politics of 1983 in one vote."),
            },
            {
                "source": "voteview", "congress": 98, "roll": 293,
                "name": "The King Holiday",
                "question": "On Passage of H.R. 3706", "result": "Bill Passed",
                "desc": ("October 19, 1983. A federal holiday for Martin Luther King Jr., "
                         "15 years after Memphis. Helms has filibustered, circulated FBI "
                         "smears, and sued to open the King files — drawing a public rebuke "
                         "on the floor even from fellow Republicans. Reagan, once opposed, "
                         "has agreed to sign."),
            },
        ],
    },
    {
        "id": "mandate-of-84",
        "title": "The Second Term",
        "era": "99th Congress · 1985–1986",
        "intro": ("Re-elected in a 49-state landslide, Reagan meets a Senate ready to "
                  "legislate around him: automatic deficit cuts, a once-a-generation tax "
                  "code rewrite — and, on South Africa, an open revolt."),
        "senators": [
            ("dole",     "Majority Leader now, running the chamber with a legislator's "
                         "cunning and a compulsive candidate's calendar: 1988 is coming, "
                         "and every vote is a general-election exhibit."),
            ("lugar",    "Chairman of Foreign Relations at his careful, unflashy best — a "
                         "Reagan loyalist on most things who has concluded, after Manila "
                         "and Johannesburg, that loyalty and foreign policy are different "
                         "subjects."),
            ("helms",    "The hard right's anchor, defending the Pretoria government as an "
                         "anti-communist ally and the tax code's sanctities selectively — "
                         "tobacco's above all."),
            ("kennedy",  "Fresh from visiting Soweto and Winnie Mandela: he has made "
                         "apartheid a moral cause of the American left and intends to make "
                         "Republicans vote on it repeatedly."),
            ("gramm",    "The Texas economist who switched parties mid-career and arrived "
                         "in the Senate with an algorithm: if the deficit is the disease, "
                         "make the cuts automatic and let no appropriator escape."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 99, "roll": 371,
                "name": "Gramm-Rudman-Hollings",
                "question": "On the Conference Report on H.J. Res. 372",
                "result": "Conference Report Agreed to",
                "desc": ("December 11, 1985. The deficit doomsday machine: fixed annual "
                         "deficit targets reaching balance by 1991, enforced by automatic "
                         "across-the-board cuts — 'sequestration' — if Congress misses. "
                         "Attached to a must-pass debt-limit increase. Critics in both "
                         "parties call it government by autopilot; it passes anyway."),
            },
            {
                "source": "voteview", "congress": 99, "roll": 677,
                "name": "The Tax Reform Act of 1986",
                "question": "On the Conference Report on H.R. 3838",
                "result": "Conference Report Agreed to",
                "desc": ("September 27, 1986. The improbable grand bargain: the top "
                         "individual rate falls from 50% to 28%, corporate loopholes close "
                         "by the hundreds, and six million working poor drop off the income "
                         "tax rolls entirely. Lobbyists filled Gucci Gulch for two years "
                         "and lost. Purists on both flanks still object."),
            },
            {
                "source": "voteview", "congress": 99, "roll": 692,
                "name": "South Africa Sanctions Override",
                "question": "On Overriding the Veto of H.R. 4868",
                "result": "Veto Overridden",
                "desc": ("October 2, 1986. Reagan has vetoed the Comprehensive Anti-Apartheid "
                         "Act — bans on new investment, South African imports, and airport "
                         "landing rights. His own party's Senate must decide whether "
                         "'constructive engagement' with Pretoria has failed. A yea "
                         "overrides a president's foreign-policy veto — the first since "
                         "War Powers."),
            },
        ],
    },
    {
        "id": "bork",
        "title": "The Bork Fight",
        "era": "100th Congress · 1987–1988",
        "intro": ("Lewis Powell's retirement leaves the Supreme Court balanced on one "
                  "seat, and Reagan names the most famous conservative judge in America. "
                  "Twelve weeks later, confirmation politics has a new verb."),
        "senators": [
            ("biden",    "Judiciary chairman at 44, running the hearings days after his "
                         "own presidential campaign collapsed in a plagiarism storm — "
                         "determined to prove the gavel steadier than the candidate, and "
                         "to fight the nomination on judicial philosophy, not scandal."),
            ("kennedy",  "The opposition's alarm bell: within an hour of the nomination he "
                         "took the floor to paint 'Robert Bork's America' in the darkest "
                         "tones — a speech admirers call mobilization and critics call "
                         "caricature."),
            ("thurmond", "The Judiciary Committee's ancient ranking Republican, shepherd "
                         "of Reagan's judges: to him Bork is simply the most qualified "
                         "nominee in decades being punished for candor."),
            ("specter",  "Pennsylvania's ex-prosecutor, the committee's swing vote: he "
                         "spent days cross-examining the nominee on original intent like "
                         "a hostile witness, and half of Washington still can't predict "
                         "his verdict."),
            ("byrd",     "Majority Leader again in a recaptured Democratic Senate — an "
                         "institution man who thinks the Court, like the Senate, belongs "
                         "to no president."),
        ],
        "bills": [
            {
                "source": "voteview", "congress": 100, "roll": 60,
                "name": "The Highway Bill Override",
                "question": "On Overriding the Veto of H.R. 2", "result": "Veto Overridden",
                "desc": ("April 2, 1987. Reagan has vetoed an $88 billion highway and "
                         "transit bill as a budget-buster stuffed with 152 earmarked "
                         "'demonstration projects' — and come to the Capitol personally to "
                         "hold Republicans, telling them to 'win one more for the Gipper.' "
                         "The new Democratic Senate, and a few defectors, answer."),
            },
            {
                "source": "voteview", "congress": 100, "roll": 348,
                "name": "Confirming Robert Bork",
                "question": "On the Nomination of Robert H. Bork",
                "result": "Nomination Rejected",
                "desc": ("October 23, 1987. After 12 days of televised hearings on original "
                         "intent, privacy, and civil rights, the most exhaustively examined "
                         "Supreme Court nomination in history reaches the floor, its "
                         "outcome no longer in doubt — Bork refused to withdraw, insisting "
                         "on a recorded vote for history."),
            },
            {
                "source": "voteview", "congress": 100, "roll": 436,
                "name": "Confirming Anthony Kennedy",
                "question": "On the Nomination of Anthony M. Kennedy",
                "result": "Nomination Confirmed",
                "desc": ("February 3, 1988. The third nominee for the Powell seat — after "
                         "Bork's defeat and Douglas Ginsburg's marijuana-shortened nine "
                         "days — is a mild Sacramento appellate judge who testifies that "
                         "the Constitution protects a sphere of liberty. An exhausted "
                         "Senate, and both parties, are ready to say yes."),
            },
        ],
    },
    {
        "id": "read-my-lips",
        "title": "Read My Lips",
        "era": "101st Congress · 1989–1990",
        "intro": ("George H.W. Bush begins with a cabinet rejection unprecedented in "
                  "three decades, fights the flag wars of 1990 — and then, at Andrews Air "
                  "Force Base, trades away the six most famous words he ever spoke."),
        "senators": [
            ("nunn",     "Chairman of Armed Services and the Democrats' Pentagon "
                         "conscience: methodical, conservative, and unsparing when he "
                         "concludes a man — any man — shouldn't sit atop the Defense "
                         "Department."),
            ("jwarner",  "Virginia's courtly Republican, Armed Services' ranking member "
                         "and a former Navy secretary: a defender of the services, the "
                         "president's prerogatives, and the Senate's good manners, in "
                         "roughly that order."),
            ("mccain",   "The former POW in his first Senate term, already the chamber's "
                         "bluntest voice on military matters — and a fierce friend of "
                         "John Tower, whose treatment he considers a disgrace."),
            ("mitchell", "The new Majority Leader: a former federal judge from Maine with "
                         "a prosecutor's calm and a partisan's memory, happy to let Bush "
                         "own every broken promise."),
            ("kassebaum","The Kansas moderate, twelve years in: internationalist abroad, "
                         "deficit-serious at home, and stubbornly unimpressed by loyalty "
                         "tests from her own party's White House."),
        ],
        "bills": [
            {
                "congress": 101, "session": 1, "vote": 20,
                "name": "The Tower Nomination",
                "desc": ("March 9, 1989. John Tower — four terms in this Senate, former "
                         "Armed Services chairman — is Bush's choice for Secretary of "
                         "Defense. The FBI file and the hearings dwell on drinking, women, "
                         "and defense-contractor consulting fees. No cabinet nominee has "
                         "been rejected since 1959, and never one of the Senate's own."),
            },
            {
                "congress": 101, "session": 2, "vote": 128,
                "name": "The Flag Desecration Amendment",
                "desc": ("June 26, 1990. The Supreme Court has twice ruled flag-burning "
                         "protected speech — striking down Texas's law, then the federal "
                         "statute Congress passed in response. This is the remaining "
                         "option: a constitutional amendment authorizing flag-desecration "
                         "bans. Two-thirds required, with the fall campaigns watching "
                         "every nay."),
            },
            {
                "congress": 101, "session": 2, "vote": 326,
                "name": "The 1990 Budget Deal",
                "desc": ("October 27, 1990. The five-year, $490 billion deficit package "
                         "from the Andrews summit: spending caps, pay-as-you-go rules — "
                         "and higher income and gasoline taxes, eighteen months after "
                         "'read my lips: no new taxes.' Conservatives call it betrayal; "
                         "the White House calls it governing."),
            },
        ],
    },
    {
        "id": "culture-wars-open",
        "title": "The Culture Wars Open",
        "era": "101st Congress · 1990",
        "intro": ("AIDS, art, and access: in a single year the Senate writes the federal "
                  "response to an epidemic, votes on what government may sponsor, and "
                  "passes the broadest civil rights law in a generation."),
        "senators": [
            ("helms",    "North Carolina's happy warrior of the right, mid-way through the "
                         "ugliest re-election fight of 1990: he sees federal AIDS spending "
                         "as reward for conduct he condemns, and publicly funded art as "
                         "subsidized blasphemy. He relishes making colleagues vote on it."),
            ("kennedy",  "Chairman of Labor and Human Resources and the machine behind "
                         "both the AIDS bill and the disability act — pairing with "
                         "whichever Republican will co-sign, and usually finding one."),
            ("hatch",    "Utah's constitutional conservative with a soft spot for "
                         "public-health causes: the religious right counts on him, but "
                         "his unlikely partnership with Kennedy keeps producing "
                         "legislation that surprises them."),
            ("metzenbaum","Ohio's millionaire scourge of business: a combative liberal "
                         "who reads every unanimous-consent request twice and treats "
                         "civil rights bills as the reason he's there."),
            ("danforth", "Missouri's Republican and an ordained Episcopal priest — a "
                         "moralist uncomfortable with obscenity and with censorship alike, "
                         "which in 1990 is an increasingly crowded corner."),
        ],
        "bills": [
            {
                "congress": 101, "session": 2, "vote": 97,
                "name": "The Ryan White CARE Act",
                "desc": ("May 16, 1990, five weeks after Ryan White's death at 18. The "
                         "first comprehensive federal AIDS-care program: emergency relief "
                         "for the hardest-hit cities and grants for every state, for "
                         "testing, drugs, and treatment. By now over 120,000 Americans "
                         "have been diagnosed; the bill's sponsors read the numbers on "
                         "the floor."),
            },
            {
                "congress": 101, "session": 2, "vote": 152,
                "name": "The Americans with Disabilities Act",
                "desc": ("July 13, 1990. The 'emancipation proclamation' for 43 million "
                         "disabled Americans: bans on employment discrimination, "
                         "accessible buses and trains, ramps and accommodations in every "
                         "public place. Business groups warn about costs and lawsuits; "
                         "veterans of the epidemic note it covers people with HIV, too."),
            },
            {
                "congress": 101, "session": 2, "vote": 307,
                "name": "The Helms Arts Amendment",
                "desc": ("October 24, 1990. After Mapplethorpe and Serrano made the "
                         "National Endowment for the Arts a household argument, Helms "
                         "proposes flatly barring NEA funds for works depicting sexual or "
                         "excretory activities or organs. A yea writes the content ban "
                         "into law; a nay leaves obscenity to the courts and the "
                         "Endowment's new procedures."),
            },
        ],
    },
]
