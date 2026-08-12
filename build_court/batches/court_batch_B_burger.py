# The Court — Batch B: The Burger Court (1969–1986).
# Votes are NOT written here — fetch_court.py verifies every justice's vote
# against the Supreme Court Database (SCDB justice-centered CSV).

JUSTICES_EXTRA = {
    # key: (SCDB justiceName, display name, English Wikipedia page title)
    "burger":    ("WEBurger", "Warren Burger", "Warren E. Burger"),
    "black":     ("HLBlack", "Hugo Black", "Hugo Black"),
    "douglas":   ("WODouglas", "William O. Douglas", "William O. Douglas"),
    "harlan":    ("JHarlan2", "John Marshall Harlan", "John Marshall Harlan II"),
    "brennan":   ("WJBrennan", "William Brennan", "William J. Brennan Jr."),
    "stewart":   ("PStewart", "Potter Stewart", "Potter Stewart"),
    "white":     ("BRWhite", "Byron White", "Byron White"),
    "marshall":  ("TMarshall", "Thurgood Marshall", "Thurgood Marshall"),
    "blackmun":  ("HABlackmun", "Harry Blackmun", "Harry Blackmun"),
    "powell":    ("LFPowell", "Lewis Powell", "Lewis F. Powell Jr."),
    "rehnquist": ("WHRehnquist", "William Rehnquist", "William Rehnquist"),
    "stevens":   ("JPStevens", "John Paul Stevens", "John Paul Stevens"),
    "oconnor":   ("SDOConnor", "Sandra Day O'Connor", "Sandra Day O'Connor"),
}

# ---- Blurbs, by era (reused across cases on the same bench) ----------------

BURGER_EARLY = (
    "Nixon's chief justice, installed to steady a Court he believes ran wild "
    "under Earl Warren. A stickler for order and the dignity of institutions, "
    "he is more cautious conservative than crusader — and ever mindful of the "
    "Court's public standing.")
BURGER_LATE = (
    "Seventeen years into the center chair, as much administrator as judge — "
    "obsessed with judicial efficiency and courtroom decorum. Reliably "
    "conservative on crime and social questions, though colleagues grumble "
    "that his opinion assignments follow strategy more than principle.")

BLACK_71 = (
    "At 85, the New Deal's last titan and the First Amendment's fiercest "
    "literalist — 'no law abridging' means no law, period. Frail and near the "
    "end of 34 years on the bench, he still writes with the old fire.")

DOUGLAS_EARLY = (
    "A New Deal wunderkind grown into the Court's absolutist loner — three "
    "decades on the bench, four wives, a shelf of his own books. He votes for "
    "the individual against the government almost reflexively, and writes "
    "opinions at breakneck speed.")

HARLAN_71 = (
    "The Court's patrician conservative conscience, a lawyer's lawyer of "
    "precision and restraint. Nearly blind, he reads briefs held an inch from "
    "his eyes — and insists that judging is a matter of process and "
    "precedent, never passion.")

BRENNAN_EARLY = (
    "The Warren Court's master coalition-builder, an Eisenhower appointee "
    "turned architect of its liberal revolution. His first rule — with five "
    "votes you can do anything — still guides him as the bench tilts "
    "rightward around him.")
BRENNAN_MID = (
    "Twenty years on, the great liberal playmaker works a Court that has "
    "drifted away from him. He still counts to five better than anyone alive, "
    "hunting the center for partners case by case.")
BRENNAN_LATE = (
    "The aging captain of the Court's shrinking liberal wing, three decades "
    "in. He can still conjure a majority from thin air on a good day — but "
    "these days he is more often assigning dissents than opinions.")

STEWART_EARLY = (
    "A pragmatic Ohio Republican wary of grand theory, he decides cases "
    "narrowly and one at a time. Neither wing can count on him: he distrusts "
    "government overreach and judicial adventure in roughly equal measure.")
STEWART_MID = (
    "The Court's studied centrist, a judge of narrow rulings and practical "
    "lines. Eighteen years in, he remains the man both blocs court — "
    "skeptical of absolutes, attentive to how the law actually operates.")

WHITE_EARLY = (
    "The Kennedys' deputy attorney general, an All-America halfback turned "
    "no-nonsense pragmatist. Tough on crime and skeptical of newly minted "
    "rights, yet often found with the liberals on race and civil rights.")
WHITE_LATE = (
    "JFK's last appointee has hardened into the Court's flintiest "
    "pragmatist — tough on crime, dismissive of rights he cannot find in the "
    "Constitution's text, still steady on race and equal protection.")

MARSHALL_EARLY = (
    "The architect of Brown v. Board and the Court's first Black justice. He "
    "judges from lived experience — Jim Crow courtrooms, clients facing the "
    "electric chair — and defends the poor and powerless with unembarrassed "
    "consistency.")
MARSHALL_LATE = (
    "The civil-rights giant in winter, increasingly isolated as the Court "
    "moves right. He and Brennan vote as a pair on the death penalty and much "
    "else, filing dissent after dissent for a future Court to find.")

BLACKMUN_EARLY = (
    "The junior justice, a shy Minnesota Republican and longtime counsel to "
    "the Mayo Clinic. Washington calls him and his boyhood friend the Chief "
    "the 'Minnesota Twins' — so far he votes Burger's way more often than "
    "not.")
BLACKMUN_MID = (
    "The Mayo Clinic's meticulous former counsel, an anxious drafter who "
    "agonizes over every case. Once dismissed as Burger's 'Minnesota Twin,' "
    "he is drifting from the Chief, case by case, toward a path of his own.")
BLACKMUN_LATE = (
    "The onetime 'Minnesota Twin' has completed a long migration: the shy "
    "Nixon appointee now votes more often with Brennan and Marshall than with "
    "the Chief he grew up beside — above all on privacy and equality.")

POWELL_EARLY = (
    "A courtly Richmond corporate lawyer and former ABA president, newly "
    "arrived on the bench. The establishment's ideal judge: moderate, "
    "balancing, allergic to extremes — he weighs each case like a client "
    "matter and lands, usually, near the center.")
POWELL_LATE = (
    "The Court's gentle fulcrum. The courtly Richmond lawyer decides the "
    "close ones — law clerks joke that the Constitution means whatever Lewis "
    "Powell thinks it means — balancing order against liberty with a "
    "counselor's caution.")

REHNQUIST_EARLY = (
    "The junior justice and its boldest conservative — a 47-year-old Nixon "
    "Justice Department lawyer with a brilliant pen and no fear of standing "
    "alone. He doubts much of what the Warren Court built.")
REHNQUIST_LATE = (
    "The Court's anchor on the right, so fond of solo dissents that his "
    "clerks once gave him a Lone Ranger doll. Federalism, law enforcement, "
    "judicial restraint: his positions never wobble — and the Court, "
    "increasingly, comes to him.")

STEVENS_MID = (
    "The newest justice, a bow-tied Chicago antitrust lawyer chosen by "
    "Gerald Ford for sheer legal craftsmanship. He belongs to no bloc, writes "
    "separate opinions constantly, and steers by his own idiosyncratic "
    "compass.")
STEVENS_LATE = (
    "The bow-tied Chicagoan defies sorting — a Ford Republican drifting "
    "toward the Court's left flank, case by idiosyncratic case. He writes "
    "more separate opinions than anyone, trusting his own reading of the law "
    "over any bloc's.")

OCONNOR_LATE = (
    "The first woman on the Court, a former Arizona legislative leader who "
    "judges like a lawmaker — narrow rulings, workable compromises, close "
    "attention to the facts. Reliably conservative on crime; harder to "
    "predict everywhere else.")

# ---- Puzzles ---------------------------------------------------------------

PUZZLES = [
    {
        "id": "new-york-times-v-united-states",
        "era": "The Burger Court · October Term 1970",
        "caseTitle": "New York Times Co. v. United States",
        "scdb": "1970-145",
        "question": "May the government stop newspapers from publishing the classified Pentagon Papers?",
        "answer": "no",
        "intro": ("June 1971. The New York Times begins printing a secret "
                  "Pentagon history of the Vietnam War, and Nixon's Justice "
                  "Department races into court to stop the presses — something "
                  "no administration has ever done."),
        "desc": ("A defense analyst named Daniel Ellsberg has leaked 7,000 "
                 "pages of classified Vietnam War history — the Pentagon "
                 "Papers — to the press. A federal injunction has stopped the "
                 "Times' presses for nearly two weeks, with the Washington "
                 "Post enjoined close behind, while the government warns of "
                 "grave damage to national security. The Justices hear "
                 "argument on a Saturday and rule four days later — the "
                 "fastest major case in memory, with the First Amendment's "
                 "rule against prior restraint squarely on the line."),
        "justices": [
            ("burger", BURGER_EARLY),
            ("black", BLACK_71),
            ("douglas", DOUGLAS_EARLY),
            ("harlan", HARLAN_71),
            ("brennan", BRENNAN_EARLY),
            ("stewart", STEWART_EARLY),
            ("white", WHITE_EARLY),
            ("marshall", MARSHALL_EARLY),
            ("blackmun", BLACKMUN_EARLY),
        ],
    },
    {
        "id": "reed-v-reed",
        "era": "The Burger Court · October Term 1971",
        "caseTitle": "Reed v. Reed",
        "scdb": "1971-014",
        "question": "May a state automatically prefer men over women for the job of administering an estate?",
        "answer": "no",
        "intro": ("Boise, Idaho. A separated couple both ask to administer "
                  "their dead son's tiny estate, and Idaho law settles the tie "
                  "automatically: 'males must be preferred to females.'"),
        "desc": ("Sally Reed's teenage son died by his own hand, leaving an "
                 "estate worth less than a thousand dollars; the probate "
                 "court appointed her estranged ex-husband to administer it, "
                 "as Idaho law commanded whenever a man and a woman were "
                 "equally entitled. A Rutgers law professor named Ruth Bader "
                 "Ginsburg co-writes the ACLU's brief attacking the statute. "
                 "In more than a century under the Fourteenth Amendment, the "
                 "Court has never once struck down a law for discriminating "
                 "against women. A seven-member bench — two seats vacant — "
                 "hears the case."),
        "justices": [
            ("burger", BURGER_EARLY),
            ("douglas", DOUGLAS_EARLY),
            ("brennan", BRENNAN_EARLY),
            ("stewart", STEWART_EARLY),
            ("white", WHITE_EARLY),
            ("marshall", MARSHALL_EARLY),
            ("blackmun", BLACKMUN_EARLY),
        ],
    },
    {
        "id": "furman-v-georgia",
        "era": "The Burger Court · October Term 1971",
        "caseTitle": "Furman v. Georgia",
        "scdb": "1971-170",
        "question": "Does the death penalty, as states now administer it, violate the Constitution?",
        "answer": "yes",
        "intro": ("1972. Six hundred men wait on death row while the Court "
                  "weighs whether capital punishment — as America actually "
                  "practices it — can survive the Eighth Amendment's ban on "
                  "cruel and unusual punishments."),
        "desc": ("William Henry Furman, a Black handyman from Savannah, shot "
                 "a homeowner during a botched midnight burglary — he says "
                 "the gun went off as he fled. Georgia juries choose between "
                 "life and death with no standards at all, and the studies "
                 "say the penalty falls overwhelmingly on the poor and the "
                 "Black. Executions nationwide have quietly stopped while the "
                 "country awaits the answer. The Court has never faced the "
                 "question this squarely — and no one is sure the nine can "
                 "agree on a single reason for whatever they decide."),
        "justices": [
            ("burger", BURGER_EARLY),
            ("douglas", DOUGLAS_EARLY),
            ("brennan", BRENNAN_EARLY),
            ("stewart", STEWART_EARLY),
            ("white", WHITE_EARLY),
            ("marshall", MARSHALL_EARLY),
            ("blackmun", BLACKMUN_EARLY),
            ("powell", POWELL_EARLY),
            ("rehnquist", REHNQUIST_EARLY),
        ],
    },
    {
        "id": "roe-v-wade",
        "era": "The Burger Court · October Term 1972",
        "caseTitle": "Roe v. Wade",
        "scdb": "1972-048",
        "question": "Does the constitutional right of privacy protect a woman's decision to end her pregnancy?",
        "answer": "yes",
        "intro": ("A Dallas waitress suing under the name 'Jane Roe' "
                  "challenges the Texas law — nearly a century old — that "
                  "makes almost every abortion a crime."),
        "desc": ("Norma McCorvey, twenty-two, poor and pregnant for the third "
                 "time, could not lawfully end her pregnancy anywhere in "
                 "Texas except to save her own life. Two young Texas lawyers "
                 "built her case into an attack on the abortion laws of most "
                 "of the nation. Argued twice — once before a short-handed "
                 "bench, again before the full nine — the case asks whether "
                 "the 'right of privacy' the Court found in the marital "
                 "bedroom in 1965 reaches a woman's decision not to bear a "
                 "child."),
        "justices": [
            ("burger", BURGER_EARLY),
            ("douglas", DOUGLAS_EARLY),
            ("brennan", BRENNAN_EARLY),
            ("stewart", STEWART_EARLY),
            ("white", WHITE_EARLY),
            ("marshall", MARSHALL_EARLY),
            ("blackmun", BLACKMUN_EARLY),
            ("powell", POWELL_EARLY),
            ("rehnquist", REHNQUIST_EARLY),
        ],
    },
    {
        "id": "miller-v-california",
        "era": "The Burger Court · October Term 1972",
        "caseTitle": "Miller v. California",
        "scdb": "1972-158",
        "question": "May a state ban the sale of obscene material, judged by local community standards?",
        "answer": "yes",
        "intro": ("The sexual revolution meets the mailbox: a Los Angeles "
                  "man mass-mails brochures for adult books, and one "
                  "unwilling recipient's complaint becomes the test of what "
                  "states may ban as obscene."),
        "desc": ("Marvin Miller ran a mail-order 'adult' business and "
                 "blanketed California with graphic advertising; one envelope "
                 "was opened by a Newport Beach restaurant owner and his "
                 "mother. For sixteen years the Court has floundered over "
                 "obscenity — screening seized films in its own basement, "
                 "reversing convictions without ever agreeing on a test. Now, "
                 "with four Nixon appointees seated, the question is whether "
                 "local juries may judge obscenity by their own community's "
                 "standards rather than a single national one."),
        "justices": [
            ("burger", BURGER_EARLY),
            ("douglas", DOUGLAS_EARLY),
            ("brennan", BRENNAN_EARLY),
            ("stewart", STEWART_EARLY),
            ("white", WHITE_EARLY),
            ("marshall", MARSHALL_EARLY),
            ("blackmun", BLACKMUN_EARLY),
            ("powell", POWELL_EARLY),
            ("rehnquist", REHNQUIST_EARLY),
        ],
    },
    {
        "id": "gregg-v-georgia",
        "era": "The Burger Court · October Term 1975",
        "caseTitle": "Gregg v. Georgia",
        "scdb": "1975-173",
        "question": "May a state impose the death penalty for murder under a statute that guides the jury's discretion?",
        "answer": "yes",
        "intro": ("Four years after Furman emptied every death row in "
                  "America, thirty-five states have rewritten their capital "
                  "statutes — and the Court must decide whether the death "
                  "penalty can come back."),
        "desc": ("Troy Gregg was condemned for robbing and murdering two men "
                 "who gave him a ride. Georgia's new statute is the model "
                 "reform: a separate sentencing trial, jury findings of "
                 "specific aggravating circumstances, automatic review in the "
                 "state's highest court. The national moratorium has held "
                 "since 1972 while hundreds of new death sentences pile up, "
                 "waiting. The question the Court sidestepped in Furman is "
                 "now unavoidable: is capital punishment itself cruel and "
                 "unusual — or was the problem only how juries imposed it?"),
        "justices": [
            ("burger", BURGER_EARLY),
            ("brennan", BRENNAN_MID),
            ("stewart", STEWART_MID),
            ("white", WHITE_EARLY),
            ("marshall", MARSHALL_EARLY),
            ("blackmun", BLACKMUN_MID),
            ("powell", POWELL_EARLY),
            ("rehnquist", REHNQUIST_EARLY),
            ("stevens", STEVENS_MID),
        ],
    },
    {
        "id": "tva-v-hill",
        "era": "The Burger Court · October Term 1977",
        "caseTitle": "Tennessee Valley Authority v. Hill",
        "scdb": "1977-115",
        "question": "Must a nearly finished federal dam be halted to protect an endangered fish?",
        "answer": "yes",
        "intro": ("The Tellico Dam is virtually complete after a decade of "
                  "construction when a three-inch fish called the snail "
                  "darter — found nowhere else on Earth — swims into the path "
                  "of federal law."),
        "desc": ("The Endangered Species Act of 1973 forbids federal actions "
                 "that would destroy the critical habitat of a listed "
                 "species. A University of Tennessee biologist discovered the "
                 "snail darter in the very stretch of the Little Tennessee "
                 "River the dam would flood, and a law student's lawsuit has "
                 "kept the gates from closing. Congress, unmoved, keeps "
                 "appropriating money for the project anyway. With tens of "
                 "millions already spent, the Justices must decide whether a "
                 "statute means exactly what it says — whatever the cost."),
        "justices": [
            ("burger", BURGER_EARLY),
            ("brennan", BRENNAN_MID),
            ("stewart", STEWART_MID),
            ("white", WHITE_EARLY),
            ("marshall", MARSHALL_EARLY),
            ("blackmun", BLACKMUN_MID),
            ("powell", POWELL_EARLY),
            ("rehnquist", REHNQUIST_EARLY),
            ("stevens", STEVENS_MID),
        ],
    },
    {
        "id": "sony-v-universal",
        "era": "The Burger Court · October Term 1983",
        "caseTitle": "Sony Corp. v. Universal City Studios",
        "scdb": "1983-022",
        "question": "Is the maker of home video recorders liable because viewers tape TV shows to watch later?",
        "answer": "no",
        "intro": ("Hollywood sues the Betamax. The movie studios say every "
                  "living-room video recorder is a piracy machine — and they "
                  "want the manufacturer held to account for it."),
        "desc": ("Sony's Betamax lets ordinary families do something new: "
                 "tape a broadcast and watch it later. Universal and Disney "
                 "call that mass copyright infringement, and they sued in "
                 "1976 to make Sony answer for its customers' recording. "
                 "Hollywood's chief lobbyist tells Congress the VCR is to the "
                 "American film industry 'as the Boston Strangler is to the "
                 "woman home alone.' Millions of machines already sit in "
                 "American living rooms; a ruling for the studios could make "
                 "every 'time-shifting' viewer an infringer."),
        "justices": [
            ("burger", BURGER_LATE),
            ("brennan", BRENNAN_LATE),
            ("white", WHITE_LATE),
            ("marshall", MARSHALL_LATE),
            ("blackmun", BLACKMUN_LATE),
            ("powell", POWELL_LATE),
            ("rehnquist", REHNQUIST_LATE),
            ("stevens", STEVENS_LATE),
            ("oconnor", OCONNOR_LATE),
        ],
    },
    {
        "id": "new-jersey-v-tlo",
        "era": "The Burger Court · October Term 1984",
        "caseTitle": "New Jersey v. T.L.O.",
        "scdb": "1984-022",
        "question": "May school officials search a student's purse without a warrant or probable cause?",
        "answer": "yes",
        "intro": ("A Piscataway freshman caught smoking in the girls' room "
                  "denies everything — so the vice principal opens her purse, "
                  "and the Fourth Amendment goes to high school."),
        "desc": ("Inside fourteen-year-old T.L.O.'s purse the vice principal "
                 "found cigarettes, then rolling papers, then marijuana, a "
                 "wad of dollar bills, and an index card listing students who "
                 "owed her money. New Jersey used all of it to prosecute her "
                 "as a delinquent. The Warrant Clause was written for "
                 "constables, not vice principals: schools say they need "
                 "swift discipline in an era of drugs in the hallways; her "
                 "lawyers answer that children do not shed the Constitution "
                 "at the schoolhouse door."),
        "justices": [
            ("burger", BURGER_LATE),
            ("brennan", BRENNAN_LATE),
            ("white", WHITE_LATE),
            ("marshall", MARSHALL_LATE),
            ("blackmun", BLACKMUN_LATE),
            ("powell", POWELL_LATE),
            ("rehnquist", REHNQUIST_LATE),
            ("stevens", STEVENS_LATE),
            ("oconnor", OCONNOR_LATE),
        ],
    },
    {
        "id": "batson-v-kentucky",
        "era": "The Burger Court · October Term 1985",
        "caseTitle": "Batson v. Kentucky",
        "scdb": "1985-078",
        "question": "Does a prosecutor's striking of jurors because of their race violate the Constitution?",
        "answer": "yes",
        "intro": ("Picking a jury in Louisville, the prosecutor uses his "
                  "peremptory strikes to remove every Black member of the "
                  "panel — and an all-white jury convicts James Batson of "
                  "burglary."),
        "desc": ("Peremptory challenges are as old as the jury itself: each "
                 "side may strike a juror without giving any reason at all. "
                 "Prosecutors have long used them, quietly, to keep Black "
                 "citizens off juries in cases against Black defendants — and "
                 "a 1965 precedent, Swain v. Alabama, makes such "
                 "discrimination nearly impossible to prove. Batson, "
                 "convicted by the all-white jury that resulted, asks the "
                 "Court to confront what everyone in the courthouse can "
                 "plainly see. Only the old precedent stands in the way."),
        "justices": [
            ("burger", BURGER_LATE),
            ("brennan", BRENNAN_LATE),
            ("white", WHITE_LATE),
            ("marshall", MARSHALL_LATE),
            ("blackmun", BLACKMUN_LATE),
            ("powell", POWELL_LATE),
            ("rehnquist", REHNQUIST_LATE),
            ("stevens", STEVENS_LATE),
            ("oconnor", OCONNOR_LATE),
        ],
    },
    {
        "id": "bowers-v-hardwick",
        "era": "The Burger Court · October Term 1985",
        "caseTitle": "Bowers v. Hardwick",
        "scdb": "1985-144",
        "question": "Does the Constitution protect private, consensual sex between adults of the same sex?",
        "answer": "no",
        "intro": ("An Atlanta police officer, serving an invalid warrant, "
                  "walks into Michael Hardwick's bedroom — and Georgia's "
                  "sodomy law lands at the Supreme Court."),
        "desc": ("Hardwick was arrested in his own bedroom with another man "
                 "under a Georgia statute punishing sodomy with up to twenty "
                 "years in prison. The district attorney dropped the charge, "
                 "but Hardwick sued, arguing that the Court's privacy "
                 "cases — contraception, abortion, the sanctity of the "
                 "home — must protect consensual adult intimacy too. Half the "
                 "states have repealed such laws; Georgia defends its own as "
                 "ancient moral tradition. The gay-rights movement, not two "
                 "decades after Stonewall, faces its first great test in the "
                 "marble temple."),
        "justices": [
            ("burger", BURGER_LATE),
            ("brennan", BRENNAN_LATE),
            ("white", WHITE_LATE),
            ("marshall", MARSHALL_LATE),
            ("blackmun", BLACKMUN_LATE),
            ("powell", POWELL_LATE),
            ("rehnquist", REHNQUIST_LATE),
            ("stevens", STEVENS_LATE),
            ("oconnor", OCONNOR_LATE),
        ],
    },
    {
        "id": "us-v-nixon",
        "era": "The Burger Court · October Term 1973",
        "caseTitle": "United States v. Nixon",
        "scdb": "1973-172",
        "question": "Must the President surrender his White House tapes to a criminal subpoena?",
        "answer": "yes",
        "intro": ("July 1974. The Watergate special prosecutor wants sixty-four "
                  "White House tapes. The President claims an absolute executive "
                  "privilege over his own conversations. Eight justices — three of "
                  "them Nixon appointees — must decide, with impeachment hearings "
                  "already underway."),
        "desc": ("The subpoena names the President of the United States and the "
                 "tapes everyone knows exist — the ones with eighteen and a half "
                 "minutes already missing. Nixon's lawyers argue no court can "
                 "compel the executive; the special prosecutor answers that no "
                 "man, president or not, may withhold evidence from a criminal "
                 "trial. William Rehnquist, a Nixon Justice Department alumnus, "
                 "has recused himself. The country waits to learn whether the "
                 "Court's writ runs to the Oval Office."),
        "justices": [
            ("burger", BURGER_EARLY),
            ("douglas", DOUGLAS_EARLY),
            ("brennan", BRENNAN_EARLY),
            ("stewart", STEWART_EARLY),
            ("white", WHITE_EARLY),
            ("marshall", MARSHALL_EARLY),
            ("blackmun", BLACKMUN_EARLY),
            ("powell", POWELL_EARLY),
        ],
    },
]
