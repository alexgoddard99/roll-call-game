# The Court — Batch G: more of the Rehnquist Court (1986–2005) and the
# Roberts Court (2005–2024).
# Votes are NOT written here — fetch_court.py pulls every justice's vote from
# the Supreme Court Database (justice-centered file) and verifies the rosters.
# Justice keys shared with batches C and D carry identical tuples.

JUSTICES_EXTRA = {
    # key: (SCDB justiceName, display name, English Wikipedia page title)
    # --- the late-eighties / early-nineties bench ---
    "rehnquist88": ("WHRehnquist", "William Rehnquist", "William Rehnquist"),
    "brennan":     ("WJBrennan", "William Brennan", "William J. Brennan Jr."),
    "white":       ("BRWhite", "Byron White", "Byron White"),
    "marshall":    ("TMarshall", "Thurgood Marshall", "Thurgood Marshall"),
    "blackmun":    ("HABlackmun", "Harry Blackmun", "Harry Blackmun"),
    "stevens88":   ("JPStevens", "John Paul Stevens", "John Paul Stevens"),
    "oconnor88":   ("SDOConnor", "Sandra Day O'Connor", "Sandra Day O'Connor"),
    "scalia88":    ("AScalia", "Antonin Scalia", "Antonin Scalia"),
    "kennedy88":   ("AMKennedy", "Anthony Kennedy", "Anthony Kennedy"),
    # --- the stable nine, 1994–2005 ---
    "rehnquist":   ("WHRehnquist", "William Rehnquist", "William Rehnquist"),
    "stevens":     ("JPStevens", "John Paul Stevens", "John Paul Stevens"),
    "oconnor":     ("SDOConnor", "Sandra Day O'Connor", "Sandra Day O'Connor"),
    "scalia":      ("AScalia", "Antonin Scalia", "Antonin Scalia"),
    "kennedy":     ("AMKennedy", "Anthony Kennedy", "Anthony Kennedy"),
    "souter":      ("DHSouter", "David Souter", "David Souter"),
    "thomas":      ("CThomas", "Clarence Thomas", "Clarence Thomas"),
    "ginsburg":    ("RBGinsburg", "Ruth Bader Ginsburg", "Ruth Bader Ginsburg"),
    "breyer":      ("SGBreyer", "Stephen Breyer", "Stephen Breyer"),
    # --- the Roberts Court ---
    "roberts":          ("JGRoberts",   "John Roberts",          "John Roberts"),
    "stevens_roberts":  ("JPStevens",   "John Paul Stevens",     "John Paul Stevens"),
    "scalia_roberts":   ("AScalia",     "Antonin Scalia",        "Antonin Scalia"),
    "kennedy_roberts":  ("AMKennedy",   "Anthony Kennedy",       "Anthony Kennedy"),
    "souter_roberts":   ("DHSouter",    "David Souter",          "David Souter"),
    "thomas_roberts":   ("CThomas",     "Clarence Thomas",       "Clarence Thomas"),
    "ginsburg_roberts": ("RBGinsburg",  "Ruth Bader Ginsburg",   "Ruth Bader Ginsburg"),
    "breyer_roberts":   ("SGBreyer",    "Stephen Breyer",        "Stephen Breyer"),
    "alito":            ("SAAlito",     "Samuel Alito",          "Samuel Alito"),
    "sotomayor":        ("SSotomayor",  "Sonia Sotomayor",       "Sonia Sotomayor"),
    "kagan":            ("EKagan",      "Elena Kagan",           "Elena Kagan"),
    "gorsuch":          ("NMGorsuch",   "Neil Gorsuch",          "Neil Gorsuch"),
    "kavanaugh":        ("BMKavanaugh", "Brett Kavanaugh",       "Brett Kavanaugh"),
    "barrett":          ("ACBarrett",   "Amy Coney Barrett",     "Amy Coney Barrett"),
    "jackson":          ("KBJackson",   "Ketanji Brown Jackson", "Ketanji Brown Jackson"),
}

# ---- Rehnquist Court blurbs ---------------------------------------------

# October Term 1987: eight justices between Powell's retirement and Kennedy's
# arrival (Hazelwood, Hustler).
_B87 = {
    "rehnquist88": ("Two terms into the chief justiceship after fifteen years as the "
                    "Court's lone-wolf conservative dissenter — a genial, poker-playing "
                    "states'-rights man who now assigns the opinions and is learning to "
                    "hold majorities rather than write dissents."),
    "brennan":     ("The architect of the Warren Court's rights revolution, now 81 and "
                    "the senior associate justice. Still the Court's great "
                    "coalition-builder — 'five votes can do anything around here' — and "
                    "with Powell gone, counting harder than ever."),
    "white":       ("A Kennedy appointee and former NFL halfback, gruff and unsentimental. "
                    "Hard on criminal defendants, skeptical of newly minted rights, steady "
                    "on civil rights — he defies every label, writes short opinions, and "
                    "asks no one's permission."),
    "marshall":    ("The lawyer who won Brown v. Board of Education, now the Court's most "
                    "unwavering liberal. He votes against every death sentence and speaks "
                    "for the poor and powerless — increasingly in dissent, shoulder to "
                    "shoulder with Brennan."),
    "blackmun":    ("The Nixon appointee who wrote Roe v. Wade and has drifted left ever "
                    "since, marked by the backlash. A meticulous former counsel to the "
                    "Mayo Clinic, sensitive and deliberate, usually found alongside "
                    "Brennan and Marshall."),
    "stevens88":   ("A Ford appointee and Chicago antitrust lawyer with a bow tie and a "
                    "ferociously independent streak. He follows his own analysis wherever "
                    "it leads and scatters solo opinions along the way — beholden to no "
                    "bloc."),
    "oconnor88":   ("The first woman on the Court, a former Arizona legislative leader who "
                    "judges the way she once governed: case by case, fact by fact, wary "
                    "of sweeping rules. With Powell retired, she is the Court's center of "
                    "gravity."),
    "scalia88":    ("Reagan's combative textualist, in only his second term and already "
                    "the Court's sharpest pen. He reads constitutional text at face value "
                    "wherever it points — and delights in skewering colleagues who "
                    "balance interests instead."),
}

# October Term 1989 (Employment Division v. Smith) — the bench of Texas v.
# Johnson and Cruzan; blurbs shared with batch C.
_B88 = {
    "rehnquist88": ("Elevated to Chief Justice in 1986 after fifteen years as the Court's "
                    "lone-wolf conservative dissenter. A states'-rights man with a genial, "
                    "poker-playing manner, he now assigns the opinions and works to move "
                    "the Court rightward without splintering his majorities."),
    "brennan":     ("The aging architect of the Warren Court's rights revolution, now 83 "
                    "and often outnumbered. The Court's great coalition-builder — 'five "
                    "votes can do anything around here' — he still hunts for a fifth vote "
                    "wherever one can be found."),
    "white":       ("A Kennedy appointee and former NFL halfback, gruff and unsentimental. "
                    "He defies every label: hard on criminal defendants, skeptical of newly "
                    "minted rights, steady on civil rights. He writes short opinions and "
                    "asks no one's permission."),
    "marshall":    ("The lawyer who argued Brown v. Board of Education, now the Court's "
                    "most unwavering liberal. He votes against every death sentence and "
                    "speaks for the poor and powerless — increasingly in dissent, side by "
                    "side with his ally Brennan."),
    "blackmun":    ("The Nixon appointee who wrote Roe v. Wade and has drifted left ever "
                    "since, marked by the backlash. A meticulous former counsel to the Mayo "
                    "Clinic, sensitive and deliberate, now usually found alongside Brennan "
                    "and Marshall."),
    "stevens88":   ("A Ford appointee and Chicago antitrust lawyer with a bow tie and a "
                    "ferociously independent streak. He follows his own analysis wherever "
                    "it leads, scattering solo opinions along the way — unpredictable by "
                    "design and beholden to no bloc."),
    "oconnor88":   ("The first woman on the Court, a former Arizona legislative leader who "
                    "judges the way she once governed: case by case, fact by fact, wary of "
                    "sweeping rules. Increasingly she is the justice both sides must "
                    "persuade."),
    "scalia88":    ("Reagan's combative textualist, three terms on the bench and already "
                    "the Court's sharpest pen. He reads constitutional text at face value "
                    "wherever it points — and delights in skewering colleagues who balance "
                    "interests instead."),
    "kennedy88":   ("The newest justice, a courtly Sacramento conservative confirmed "
                    "unanimously after the Bork nomination went down in flames. Expected "
                    "to be a dependable Reagan vote, but given to grand talk about liberty "
                    "and the dignity of the individual."),
}

# October Term 1991 (Lee v. Weisman): Brennan and Marshall gone, Souter and
# Thomas arrived — the moment the conservative turn was supposed to come.
_B92 = {
    "rehnquist88": ("Six years into the chief justiceship, a genial poker-playing "
                    "states'-rights man who finally has the numbers: Brennan and Marshall "
                    "are gone, replaced by two Bush appointees. He assigns the opinions and "
                    "expects the long-promised conservative turn to arrive."),
    "white":       ("Thirty years on the bench, the Court's gruff elder — a Kennedy "
                    "appointee and former NFL halfback who defies every label: hard on "
                    "criminal defendants, cool toward newly minted rights, steady on civil "
                    "rights. Short opinions, no apologies."),
    "blackmun":    ("The author of Roe v. Wade, now 83 and the Court's most anguished "
                    "liberal, writing with his heart on his sleeve. With Brennan and "
                    "Marshall retired he leads the diminished left — and wonders aloud how "
                    "long Roe can last."),
    "stevens88":   ("A bow-tied Ford appointee from Chicago, fiercely independent in "
                    "method, who has become the senior voice of the Court's liberal side "
                    "almost by default. He follows his own analysis wherever it leads and "
                    "scatters solo opinions along the way."),
    "oconnor88":   ("A former Arizona legislator who judges the way she once governed: "
                    "case by case, fact by fact, wary of sweeping rules. The vote both "
                    "sides must win, and increasingly the one deciding where the line "
                    "falls."),
    "scalia88":    ("Reagan's combative originalist, six terms in and the Court's sharpest "
                    "pen. He wants clear rules drawn from text and history and treats his "
                    "colleagues' balancing tests as legislation in robes — in dissent if "
                    "he must."),
    "kennedy88":   ("A courtly Sacramento Republican confirmed unanimously after the Bork "
                    "nomination collapsed. Expected to be a dependable conservative vote, "
                    "but given to grand talk about liberty and the dignity of the "
                    "individual — and lately harder to predict."),
    "souter":      ("The first President Bush's 'stealth nominee,' a frugal New Hampshire "
                    "bachelor and common-law traditionalist who has barely begun to show "
                    "his hand. Devoted to precedent, wary of grand theory, and watched "
                    "closely by both camps."),
    "thomas":      ("The newest justice, confirmed 52–48 after the Anita Hill hearings: a "
                    "Georgia-born originalist who says little at argument and writes with "
                    "uncompromising clarity. Expected to be a reliable conservative, and "
                    "already showing an appetite for first principles."),
}

# The stable nine of 1994–2005 — blurbs shared with batch C.
_B = {
    "rehnquist": ("Chief Justice for nearly two decades, a genial and ruthlessly "
                  "efficient administrator with a lifelong project: reviving states' "
                  "rights and reining in Washington. He has spent his whole career "
                  "waiting for the votes he now has."),
    "stevens":   ("The senior associate justice, a bow-tied Ford appointee from Chicago "
                  "who now marshals the Court's liberal wing. Fiercely independent in "
                  "method, he assigns the dissents whenever the Chief is on the other "
                  "side."),
    "oconnor":   ("A former Arizona legislator and the Court's pivotal vote — by common "
                  "consent the most powerful woman in America. She distrusts absolutes "
                  "and decides case by case; where she lands is usually where the law "
                  "lands."),
    "scalia":    ("The Court's combative originalist, its funniest questioner and its "
                  "fiercest dissenter. He wants clear rules drawn from text and history, "
                  "and treats his colleagues' balancing tests as legislation in robes."),
    "kennedy":   ("A courtly Sacramento Republican with a taste for sweeping language "
                  "about liberty and dignity. Conservative by default but persuadable at "
                  "the margins — one of the two votes every advocate in the courtroom is "
                  "chasing."),
    "souter":    ("The first President Bush's 'stealth nominee,' a frugal New Hampshire "
                  "bachelor who confounded his sponsors by settling into the "
                  "moderate-liberal wing. A common-law traditionalist, devoted to "
                  "precedent and wary of bold constitutional lurches."),
    "thomas":    ("The Court's most uncompromising originalist, silent at argument and "
                  "fearless in print. He would rather overrule a wrong precedent than "
                  "trim it, and he stakes out positions no other justice will yet join."),
    "ginsburg":  ("The ACLU litigator who dismantled sex-discrimination law brick by "
                  "brick, now a precise, soft-spoken justice. A minimalist by "
                  "temperament and a reliable liberal vote on questions of equal "
                  "citizenship."),
    "breyer":    ("The junior justice, a Harvard administrative-law professor who thinks "
                  "in workable purposes rather than absolutes. Pragmatic, optimistic "
                  "about government, and forever spinning elaborate hypotheticals from "
                  "the bench."),
}

_BENCH_87 = [(k, _B87[k]) for k in
             ["rehnquist88", "brennan", "white", "marshall", "blackmun",
              "stevens88", "oconnor88", "scalia88"]]
_BENCH_88 = [(k, _B88[k]) for k in
             ["rehnquist88", "brennan", "white", "marshall", "blackmun",
              "stevens88", "oconnor88", "scalia88", "kennedy88"]]
_BENCH_92 = [(k, _B92[k]) for k in
             ["rehnquist88", "white", "blackmun", "stevens88", "oconnor88",
              "scalia88", "kennedy88", "souter", "thomas"]]
_BENCH_NINE = [(k, _B[k]) for k in
               ["rehnquist", "stevens", "oconnor", "scalia", "kennedy",
                "souter", "thomas", "ginsburg", "breyer"]]

# ---- Roberts Court blurbs (shared with batch D) ---------------------------

ROBERTS_EARLY = (
    "The chief justice who won the job promising to call balls and strikes, "
    "not pitch or bat. A polished Supreme Court advocate turned umpire, he "
    "prefers narrow rulings and unanimity where he can get them — and moves "
    "the law by patient inches when he can't.")

ROBERTS_MID = (
    "A dozen years in, the chief has become the Court's institutional "
    "conscience, insisting — especially in a polarized age — that it must not "
    "look like a political body. An incrementalist by temperament: he would "
    "rather decide little than decide loudly.")

ROBERTS_LATE = (
    "No longer the Court's median vote — a six-justice conservative majority "
    "can now rule without him. He still preaches minimalism and frets over "
    "the institution's standing, hunting for narrower paths that his "
    "colleagues increasingly decline to take.")

STEVENS = (
    "The senior associate justice, pushing ninety and sharper than ever: a "
    "bow-tied Republican antitrust lawyer appointed by Gerald Ford who became "
    "the anchor of the Court's liberal wing. He insists the Court moved, "
    "not him.")

SCALIA = (
    "Originalism's happy warrior, decades into his crusade to read the "
    "Constitution as its ratifiers understood it. His opinions are the "
    "Court's best copy, his scorn for 'living constitutionalism' legendary — "
    "and his method has reshaped how every case is argued.")

KENNEDY = (
    "The swing. A courtly Sacramento Republican who controls the outcome in "
    "nearly every close case — and knows it. Liberty and dignity are his "
    "lodestars, sweeping language his signature, suspense his permanent gift "
    "to Court-watchers.")

SOUTER = (
    "A frugal New Hampshire Yankee named by the first President Bush as a "
    "'home run' for conservatives — who drifted steadily toward the Court's "
    "left instead. Skeptical of grand theories, devoted to precedent and to "
    "history's complications.")

THOMAS = (
    "The Court's most uncompromising originalist, fearless in print: he will "
    "discard decades of precedent without apology and stake out positions "
    "entirely alone, serenely confident the law will someday catch up "
    "to him.")

GINSBURG = (
    "The pioneering women's-rights litigator of the 1970s, now the liberal "
    "wing's most exacting technician. Small, quiet, and precise, she picks "
    "her battles carefully — and reads her fiercest dissents aloud from the "
    "bench when she loses one.")

BREYER = (
    "The Court's pragmatist professor: a former Senate staffer and "
    "administrative-law scholar who judges by consequences, not grand "
    "theory. Endlessly optimistic about government, allergic to absolutes, "
    "and famous for winding hypotheticals that leave lawyers blinking.")

ALITO = (
    "A former federal prosecutor from New Jersey, methodical and unflashy, "
    "with the most reliably conservative instincts on the bench — above all "
    "where crime, religion, or the culture wars are concerned. In dissent, "
    "his pen turns acid.")

SOTOMAYOR = (
    "From a Bronx housing project to Princeton to the federal trial bench: "
    "the first Latina justice never lets the Court forget how doctrine lands "
    "on actual people. A former prosecutor, relentless at argument, the "
    "liberal wing's most passionate voice.")

KAGAN = (
    "The former Harvard Law dean and solicitor general, a coalition-builder "
    "who learned her politics in the Clinton White House. The liberal wing's "
    "tactician: she writes in plain, wry English and plays a patient long "
    "game of her own.")

GORSUCH = (
    "Scalia's successor and a true-believing textualist from Colorado: read "
    "the words, then follow them off a cliff if necessary. A westerner with "
    "a libertarian streak, he votes his method wherever it leads — to either "
    "camp's occasional dismay.")

KAVANAUGH = (
    "Confirmed after the most explosive hearings in memory, the former Bush "
    "White House aide works at looking reassuringly conventional: a "
    "conservative who prizes stability, writes separately to narrow things, "
    "and courts the middle whenever there is one.")

BARRETT = (
    "Scalia's former clerk and a Notre Dame law professor, elevated to the "
    "bench days before a presidential election. An academic originalist — "
    "careful, methodical, unshowy — still drawing her own map of where "
    "method and caution part ways.")

JACKSON = (
    "The first Black woman on the Court and its first former public "
    "defender. She brings a trial judge's practicality, a performer's timing "
    "at oral argument, and no apparent interest in waiting her turn to "
    "be heard.")

BENCH_2007 = [
    ("roberts", ROBERTS_EARLY), ("stevens_roberts", STEVENS),
    ("scalia_roberts", SCALIA), ("kennedy_roberts", KENNEDY),
    ("souter_roberts", SOUTER), ("thomas_roberts", THOMAS),
    ("ginsburg_roberts", GINSBURG), ("breyer_roberts", BREYER),
    ("alito", ALITO),
]

BENCH_2010_16 = [
    ("roberts", ROBERTS_EARLY), ("scalia_roberts", SCALIA),
    ("kennedy_roberts", KENNEDY), ("thomas_roberts", THOMAS),
    ("ginsburg_roberts", GINSBURG), ("breyer_roberts", BREYER),
    ("alito", ALITO), ("sotomayor", SOTOMAYOR), ("kagan", KAGAN),
]

BENCH_2017 = [
    ("roberts", ROBERTS_MID), ("kennedy_roberts", KENNEDY),
    ("thomas_roberts", THOMAS), ("ginsburg_roberts", GINSBURG),
    ("breyer_roberts", BREYER), ("alito", ALITO),
    ("sotomayor", SOTOMAYOR), ("kagan", KAGAN), ("gorsuch", GORSUCH),
]

BENCH_2019 = [
    ("roberts", ROBERTS_MID), ("thomas_roberts", THOMAS),
    ("ginsburg_roberts", GINSBURG), ("breyer_roberts", BREYER),
    ("alito", ALITO), ("sotomayor", SOTOMAYOR), ("kagan", KAGAN),
    ("gorsuch", GORSUCH), ("kavanaugh", KAVANAUGH),
]

BENCH_2021 = [
    ("roberts", ROBERTS_LATE), ("thomas_roberts", THOMAS),
    ("breyer_roberts", BREYER), ("alito", ALITO),
    ("sotomayor", SOTOMAYOR), ("kagan", KAGAN), ("gorsuch", GORSUCH),
    ("kavanaugh", KAVANAUGH), ("barrett", BARRETT),
]

BENCH_2022 = [
    ("roberts", ROBERTS_LATE), ("thomas_roberts", THOMAS),
    ("alito", ALITO), ("sotomayor", SOTOMAYOR), ("kagan", KAGAN),
    ("gorsuch", GORSUCH), ("kavanaugh", KAVANAUGH),
    ("barrett", BARRETT), ("jackson", JACKSON),
]

# ---- Puzzles ------------------------------------------------------------

PUZZLES = [
    # ======================= The Rehnquist Court =======================
    {
        "id": "hazelwood-v-kuhlmeier",
        "era": "The Rehnquist Court · October Term 1987",
        "caseTitle": "Hazelwood School District v. Kuhlmeier",
        "scdb": "1987-019",
        "question": ("May a public school principal cut stories from a student "
                     "newspaper produced in a journalism class?"),
        "answer": "yes",
        "intro": ("At Hazelwood East High School outside St. Louis, the principal "
                  "pulls two pages from the student newspaper before it goes to "
                  "press: a story on teen pregnancy and one on divorce. Three student "
                  "journalists say he has censored them."),
        "desc": ("The Spectrum was written and edited by the Journalism II class and "
                 "printed with school money. Principal Robert Reynolds, reviewing page "
                 "proofs, found the pregnancy story — three pregnant students, "
                 "anonymous but perhaps recognizable — unfit for younger readers, and "
                 "the divorce piece unfair to a father who had no chance to respond. "
                 "With the deadline hours away, he deleted both pages. Cathy "
                 "Kuhlmeier and two classmates sued. Tinker protected students' "
                 "armbands two decades ago; the school says a classroom newspaper is "
                 "a different thing from a student's own speech."),
        "justices": _BENCH_87,
    },
    {
        "id": "hustler-v-falwell",
        "era": "The Rehnquist Court · October Term 1987",
        "caseTitle": "Hustler Magazine v. Falwell",
        "scdb": "1987-035",
        "question": ("May a public figure collect damages for emotional distress "
                     "caused by an offensive parody that no reader would take as "
                     "fact?"),
        "answer": "no",
        "intro": ("A Campari-ad parody in Hustler magazine depicts the Rev. Jerry "
                  "Falwell, founder of the Moral Majority, recalling a drunken first "
                  "time with his mother in an outhouse. Falwell sues Larry Flynt. A "
                  "Virginia jury has already awarded him $200,000."),
        "desc": ("The November 1983 issue of Hustler ran a mock advertisement, "
                 "labeled in small print 'ad parody — not to be taken seriously,' in "
                 "which Falwell describes a drunken encounter with his mother in an "
                 "outhouse. The jury rejected his libel claim — no one could believe "
                 "it was true — but awarded $200,000 for intentional infliction of "
                 "emotional distress. Flynt, the pornographer, and Falwell, the "
                 "televangelist, loathe each other in public. Political cartoonists "
                 "from Thomas Nast forward are invoked on one side; common decency on "
                 "the other."),
        "justices": _BENCH_87,
    },
    {
        "id": "employment-division-v-smith",
        "era": "The Rehnquist Court · October Term 1989",
        "caseTitle": "Employment Division v. Smith",
        "scdb": "1989-061",
        "question": ("May a state deny unemployment benefits to workers fired for "
                     "using peyote in a religious ceremony?"),
        "answer": "yes",
        "intro": ("Two drug-rehabilitation counselors in Oregon are fired for "
                  "swallowing peyote at a ceremony of the Native American Church. The "
                  "state denies them unemployment benefits. Their sacrament, they "
                  "say, is older than the state."),
        "desc": ("Alfred Smith, a Klamath Indian, and Galen Black ingested peyote — a "
                 "hallucinogenic cactus and a Schedule I drug in Oregon — as the "
                 "central rite of a Native American Church service, and lost their "
                 "jobs at a private drug-treatment agency for it. Oregon called the "
                 "firing misconduct and refused benefits. For a generation the Court "
                 "has required states to show a compelling interest before burdening "
                 "religious practice; twenty-three states exempt peyote worship "
                 "outright. Oregon does not, and asks whether a neutral criminal law "
                 "must bend to anyone's faith."),
        "justices": _BENCH_88,
    },
    {
        "id": "lee-v-weisman",
        "era": "The Rehnquist Court · October Term 1991",
        "caseTitle": "Lee v. Weisman",
        "scdb": "1991-110",
        "question": ("May a public school invite a clergyman to deliver a prayer at "
                     "its graduation ceremony?"),
        "answer": "no",
        "intro": ("At Nathan Bishop Middle School in Providence, a rabbi offers a "
                  "short nonsectarian prayer at graduation. Daniel Weisman, whose "
                  "daughter Deborah is in the eighth-grade class, asks the courts to "
                  "forbid it. The Bush administration joins the school's side."),
        "desc": ("Providence's public schools let principals invite clergy to open "
                 "and close graduation, handing them a pamphlet on composing civic "
                 "prayers. Rabbi Leslie Gutterman thanked God for 'the legacy of "
                 "America, where diversity is celebrated.' Deborah Weisman, fourteen, "
                 "attended; her father sued to stop the practice at her future high "
                 "school. Since 1962 the Court has barred classroom prayer, and the "
                 "Solicitor General now urges the justices to allow ceremonial "
                 "religion wherever no one is coerced. The school says attendance is "
                 "voluntary; the Weismans say no graduate really has a choice."),
        "justices": _BENCH_92,
    },
    {
        "id": "us-term-limits-v-thornton",
        "era": "The Rehnquist Court · October Term 1994",
        "caseTitle": "U.S. Term Limits v. Thornton",
        "scdb": "1994-059",
        "question": "May a state impose term limits on its own members of Congress?",
        "answer": "no",
        "intro": ("In 1992 Arkansas voters amend their constitution to keep anyone "
                  "who has served three terms in the House, or two in the Senate, "
                  "off the ballot. Twenty-two other states have done something "
                  "similar. Congressman Ray Thornton sues."),
        "desc": ("Amendment 73 passed with sixty percent of the vote, riding the "
                 "national term-limits wave of the early nineties. Thornton, a "
                 "Democrat seeking a fourth House term, argues that the Constitution "
                 "fixes the qualifications for Congress — age, citizenship, residence "
                 "— and that no state may add to them. U.S. Term Limits, the group "
                 "behind the measure, replies that a ballot-access rule is no "
                 "qualification, and that powers not forbidden to the states remain "
                 "theirs. Underneath lies the union itself: are members of Congress "
                 "the people's agents, or the states'?"),
        "justices": _BENCH_NINE,
    },
    {
        "id": "kyllo-v-united-states",
        "era": "The Rehnquist Court · October Term 2000",
        "caseTitle": "Kyllo v. United States",
        "scdb": "2000-069",
        "question": ("Is scanning a home with a thermal imager from the street a "
                     "'search' that requires a warrant?"),
        "answer": "yes",
        "intro": ("Federal agents suspecting Danny Kyllo of growing marijuana park "
                  "across from his Oregon triplex and aim a thermal imager at it. "
                  "The scan shows the garage roof glowing hot. They never set foot "
                  "inside — and never asked a judge."),
        "desc": ("The Agema Thermovision 210 detects infrared radiation; a few "
                 "minutes' scan from a public street showed Kyllo's garage and one "
                 "wall unusually warm, consistent with halide grow lamps. With "
                 "utility bills and a tip, that supported a warrant; agents found "
                 "more than a hundred plants. Kyllo argues that reading "
                 "the heat of a home's walls is a search of the home. The government "
                 "answers that it merely observed what leaked into the open air, as "
                 "anyone with a camera might. The Fourth Amendment meets a device "
                 "that sees through walls."),
        "justices": _BENCH_NINE,
    },
    {
        "id": "grutter-v-bollinger",
        "era": "The Rehnquist Court · October Term 2002",
        "caseTitle": "Grutter v. Bollinger",
        "scdb": "2002-078",
        "question": ("May a public university consider an applicant's race as one "
                     "factor in admissions to achieve a diverse student body?"),
        "answer": "yes",
        "intro": ("Barbara Grutter, a white Michigan resident with a 3.8 average, is "
                  "turned down by the University of Michigan Law School, which "
                  "admits to weighing race in pursuit of a 'critical mass' of "
                  "minority students. A quarter-century after Bakke, affirmative "
                  "action is back."),
        "desc": ("Michigan's law school, among the nation's most selective, reads "
                 "every file whole: grades and test scores, but also essays, "
                 "recommendations, and race — seeking enough Black, Hispanic, and "
                 "Native American students that none feels a token. Grutter, "
                 "rejected in 1997, says the policy is a quota in disguise. Retired "
                 "generals, Fortune 500 companies, and the Bush administration have "
                 "filed briefs; a companion case against the undergraduate college's "
                 "points system arrives the same day. Justice Powell's lone opinion "
                 "in Bakke allowed race as a 'plus'; no majority has ever said so."),
        "justices": _BENCH_NINE,
    },
    {
        "id": "roper-v-simmons",
        "era": "The Rehnquist Court · October Term 2004",
        "caseTitle": "Roper v. Simmons",
        "scdb": "2004-024",
        "question": ("May a state execute a murderer who was under eighteen at the "
                     "time of the crime?"),
        "answer": "no",
        "intro": ("At seventeen, Christopher Simmons broke into a Missouri home with "
                  "a friend, bound Shirley Crook with electrical wire and duct tape, "
                  "and threw her from a railroad trestle. A jury sentenced him to "
                  "death. Missouri's own supreme court has now set it aside."),
        "desc": ("Simmons planned the 1993 burglary and murder for weeks and assured "
                 "accomplices they could 'get away with it' as minors; he confessed "
                 "on videotape. In 1989 the Court upheld the "
                 "death penalty for sixteen- and seventeen-year-olds. Since then — "
                 "and after Atkins v. Virginia barred executing the mentally retarded "
                 "— the Missouri Supreme Court declared a new national consensus and "
                 "resentenced him to life. Thirty states now forbid juvenile "
                 "executions; the United States is the last country still carrying "
                 "them out. Psychologists argue the adolescent brain is unfinished."),
        "justices": _BENCH_NINE,
    },
    # ======================== The Roberts Court ========================
    {
        "id": "boumediene-v-bush",
        "era": "The Roberts Court · October Term 2007",
        "caseTitle": "Boumediene v. Bush",
        "scdb": "2007-053",
        "question": ("Do foreign detainees held at Guantánamo have a constitutional "
                     "right to challenge their detention in federal court?"),
        "answer": "yes",
        "intro": ("Six Algerians seized in Bosnia have spent six years at Guantánamo "
                  "Bay without charge. Congress has twice stripped the federal courts "
                  "of power to hear their habeas petitions. The question is whether "
                  "the Constitution reaches the base at all."),
        "desc": ("Lakhdar Boumediene, a Red Crescent aid worker, was arrested in "
                 "Sarajevo in 2001 on suspicion of a plot against the U.S. embassy, "
                 "cleared by Bosnian courts, and flown to Cuba anyway. The Military "
                 "Commissions Act of 2006 bars any court from hearing a Guantánamo "
                 "detainee's habeas corpus claim, substituting Pentagon review "
                 "tribunals. The government says a leased base on foreign soil lies "
                 "outside the Constitution's reach, and wartime detention is for the "
                 "President and Congress. The detainees say the Great Writ follows "
                 "the flag wherever America holds a man indefinitely."),
        "justices": BENCH_2007,
    },
    {
        "id": "snyder-v-phelps",
        "era": "The Roberts Court · October Term 2010",
        "caseTitle": "Snyder v. Phelps",
        "scdb": "2010-023",
        "question": ("Does the First Amendment shield funeral picketers from a "
                     "lawsuit by the grieving family they distressed?"),
        "answer": "yes",
        "intro": ("Marine Lance Corporal Matthew Snyder is killed in Iraq. At his "
                  "funeral in Westminster, Maryland, members of Westboro Baptist "
                  "Church stand a thousand feet away with signs reading 'Thank God "
                  "for Dead Soldiers.' His father sues them."),
        "desc": ("Fred Phelps and his family have picketed hundreds of military "
                 "funerals, preaching that American war deaths are God's punishment "
                 "for tolerating homosexuality. They notified police, obeyed every "
                 "ordinance, and stayed on public land where Albert Snyder saw only "
                 "the tops of their signs; he read their message later on the news. "
                 "A jury awarded him millions for intentional infliction of emotional "
                 "distress and invasion of privacy. Forty-eight states and the Senate "
                 "majority leader back Snyder; the press and civil libertarians, "
                 "holding their noses, back Westboro's right to say it."),
        "justices": BENCH_2010_16,
    },
    {
        "id": "burwell-v-hobby-lobby",
        "era": "The Roberts Court · October Term 2013",
        "caseTitle": "Burwell v. Hobby Lobby Stores",
        "scdb": "2013-070",
        "question": ("May a closely held for-profit company refuse on religious "
                     "grounds to cover contraception in its employees' health "
                     "plan?"),
        "answer": "yes",
        "intro": ("The Green family runs Hobby Lobby — 500 craft stores, 13,000 "
                  "employees — as a Christian business closed on Sundays. The "
                  "Affordable Care Act now requires their health plan to cover "
                  "contraceptives they consider abortifacients: a choice, they say, "
                  "between faith and ruin."),
        "desc": ("Under the contraceptive mandate, employer plans must cover all "
                 "FDA-approved birth control; the Greens object to four methods, "
                 "including morning-after pills and IUDs, that they believe can end "
                 "a fertilized egg. The fine for refusing would run to $475 million "
                 "a year. The Religious Freedom Restoration Act forbids the "
                 "government to substantially burden a 'person's' exercise of "
                 "religion without a compelling reason. Does a for-profit corporation "
                 "have religion to exercise? Churches and nonprofits already have "
                 "exemptions; the government says the line stops there. Thousands of "
                 "employees' coverage hangs on it."),
        "justices": BENCH_2010_16,
    },
    {
        "id": "trump-v-hawaii",
        "era": "The Roberts Court · October Term 2017",
        "caseTitle": "Trump v. Hawaii",
        "scdb": "2017-074",
        "question": ("May the president bar entry to nationals of several mostly "
                     "Muslim countries under his power to suspend immigration?"),
        "answer": "yes",
        "intro": ("A week into his presidency, Donald Trump bars travelers from seven "
                  "Muslim-majority countries, and chaos erupts at the airports. Two "
                  "rewrites and eighteen months later, the third version of the "
                  "travel ban reaches the Court."),
        "desc": ("Proclamation 9645 restricts entry from Iran, Libya, Somalia, Syria, "
                 "Yemen, and North Korea, plus certain Venezuelan officials, after a "
                 "worldwide review of vetting practices. Hawaii, joined by an imam "
                 "whose Syrian mother-in-law cannot visit, argues it exceeds the "
                 "President's immigration powers and — given candidate Trump's call "
                 "for 'a total and complete shutdown of Muslims entering the United "
                 "States' — violates the Establishment Clause. The government says "
                 "the statute lets the President suspend entry of 'any class of "
                 "aliens' he finds detrimental, and that courts may not second-guess "
                 "national security."),
        "justices": BENCH_2017,
    },
    {
        "id": "rucho-v-common-cause",
        "era": "The Roberts Court · October Term 2018",
        "caseTitle": "Rucho v. Common Cause",
        "scdb": "2018-062",
        "question": ("May federal courts strike down an election map as an "
                     "unconstitutional partisan gerrymander?"),
        "answer": "no",
        "intro": ("North Carolina Republicans drew their congressional map to elect "
                  "ten Republicans and three Democrats, and said so out loud. In "
                  "Maryland, Democrats erased a Republican seat. Both maps arrive "
                  "together, asking whether a gerrymander can go too far."),
        "desc": ("Representative David Lewis told the redistricting committee he "
                 "proposed a 10–3 map 'because I do not believe it's possible to "
                 "draw a map with 11 Republicans and 2 Democrats.' In Maryland, "
                 "Governor O'Malley's team reshaped the Sixth District to flip it. Lower courts struck down both maps. Gerrymandering is as "
                 "old as Elbridge Gerry, and the Court has never found a standard "
                 "for judging it; computers now draw maps with surgical precision. "
                 "Common Cause asks the justices to draw a line. The states ask them "
                 "to admit there isn't one."),
        "justices": BENCH_2019,
    },
    {
        "id": "kennedy-v-bremerton",
        "era": "The Roberts Court · October Term 2021",
        "caseTitle": "Kennedy v. Bremerton School District",
        "scdb": "2021-061",
        "question": ("Does the Constitution protect a public-school football coach's "
                     "postgame prayer at midfield?"),
        "answer": "yes",
        "intro": ("After each game, Bremerton High's assistant football coach Joseph "
                  "Kennedy walks to the fifty-yard line, kneels, and prays. For "
                  "years players joined him. When the Washington school district "
                  "tells him to stop, he refuses, and loses his job."),
        "desc": ("Kennedy, a former Marine, began the prayers alone in 2008; they "
                 "grew into huddles with players from both teams. Alerted by a visiting coach's complaint, the district "
                 "offered him a private place to pray; he prayed at midfield "
                 "instead, with news cameras and a state legislator looking on. The "
                 "district put him on leave and let his contract lapse. He says the "
                 "First Amendment protects a citizen's quiet prayer; the district "
                 "says a coach on duty is the government speaking — and students "
                 "felt they had to kneel."),
        "justices": BENCH_2021,
    },
    {
        "id": "biden-v-nebraska",
        "era": "The Roberts Court · October Term 2022",
        "caseTitle": "Biden v. Nebraska",
        "scdb": "2022-038",
        "question": ("May the Education Secretary cancel hundreds of billions of "
                     "dollars in student debt under the HEROES Act's power to "
                     "'waive or modify' aid rules?"),
        "answer": "no",
        "intro": ("President Biden announces up to $20,000 in student-loan "
                  "forgiveness for 43 million borrowers, invoking a post-9/11 law "
                  "written for soldiers at war. Six Republican-led states sue. The "
                  "price tag is about $430 billion."),
        "desc": ("The HEROES Act of 2003 lets the Education Secretary 'waive or "
                 "modify' student-aid rules in a national emergency; the "
                 "administration says the pandemic is one and that cancellation keeps "
                 "borrowers from default. Missouri's loan-servicing agency, MOHELA, "
                 "would lose fees, giving the states a path into court. They argue "
                 "that no Congress wrote a $430 billion giveaway into a wartime "
                 "waiver, and that a decision this big belongs to legislators. "
                 "Borrowers have applied in the millions; the forgiveness is frozen "
                 "pending the Court's answer."),
        "justices": BENCH_2022,
    },
    {
        "id": "united-states-v-rahimi",
        "era": "The Roberts Court · October Term 2023",
        "caseTitle": "United States v. Rahimi",
        "scdb": "2023-012",
        "question": ("May the government disarm a person who is under a "
                     "domestic-violence restraining order?"),
        "answer": "yes",
        "intro": ("Zackey Rahimi, under a Texas restraining order for assaulting his "
                  "girlfriend, fires guns in five separate incidents in two months, "
                  "including into the air at a Whataburger. Federal law bars him "
                  "from having a gun at all. He says the Second Amendment disagrees."),
        "desc": ("A 1994 federal statute disarms anyone subject to a domestic-violence "
                 "protective order. Rahimi, who also threatened to shoot his "
                 "girlfriend if she told anyone about the assault, pleaded guilty — "
                 "then the Fifth Circuit threw out his conviction under Bruen's new "
                 "test, finding no founding-era law quite like it. Two years after "
                 "Bruen, the Court must say how closely a modern gun law has to match "
                 "history. The government points to old 'surety' and 'going armed' "
                 "laws; Rahimi's lawyers say the founders never disarmed anyone on a "
                 "civil court's say-so."),
        "justices": BENCH_2022,
    },
]
