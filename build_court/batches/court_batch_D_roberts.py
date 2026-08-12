# The Court — Batch D: The Roberts Court (2005–2024)
# Votes are NOT written here — fetch_court.py reads them from the SCDB
# justice-centered CSV. This file supplies framing only.

JUSTICES_EXTRA = {
    # key: (SCDB justiceName, display name, English Wikipedia page title)
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

# ---- Per-bench blurbs (reused across that bench's cases) ----------------

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

# ---- Bench line-ups (seniority order) -----------------------------------

BENCH_2007 = [
    ("roberts", ROBERTS_EARLY), ("stevens_roberts", STEVENS),
    ("scalia_roberts", SCALIA), ("kennedy_roberts", KENNEDY),
    ("souter_roberts", SOUTER), ("thomas_roberts", THOMAS),
    ("ginsburg_roberts", GINSBURG), ("breyer_roberts", BREYER),
    ("alito", ALITO),
]

BENCH_2009 = [
    ("roberts", ROBERTS_EARLY), ("stevens_roberts", STEVENS),
    ("scalia_roberts", SCALIA), ("kennedy_roberts", KENNEDY),
    ("thomas_roberts", THOMAS), ("ginsburg_roberts", GINSBURG),
    ("breyer_roberts", BREYER), ("alito", ALITO),
    ("sotomayor", SOTOMAYOR),
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
    {
        "id": "dc-v-heller",
        "era": "The Roberts Court · October Term 2007",
        "caseTitle": "District of Columbia v. Heller",
        "scdb": "2007-071",
        "question": ("Does the Second Amendment protect an individual's right "
                     "to keep a handgun at home, apart from militia service?"),
        "answer": "yes",
        "intro": ("A security guard in the nation's capital wants to keep his "
                  "revolver at home. The Court has not squarely read the "
                  "Second Amendment in nearly seventy years — and must now "
                  "decide what 'a well regulated Militia' has to do with it."),
        "desc": ("Dick Heller carries a gun all day guarding the Federal "
                 "Judicial Center — and cannot legally keep one at home under "
                 "Washington's 1976 handgun ban, the strictest in America. "
                 "His lawsuit asks what the amendment's tangled clauses "
                 "actually promise: a militia's collective prerogative, or an "
                 "individual's right? Both sides come armed with founding-era "
                 "history, and every gun law in the country is watching. Even "
                 "some conservatives fear what an honest answer might "
                 "unleash."),
        "justices": BENCH_2007,
    },
    {
        "id": "citizens-united",
        "era": "The Roberts Court · October Term 2009",
        "caseTitle": "Citizens United v. FEC",
        "scdb": "2009-012",
        "question": ("May the government limit corporations' independent "
                     "spending on political speech in candidate elections?"),
        "answer": "no",
        "intro": ("A conservative nonprofit made a ninety-minute film "
                  "attacking Hillary Clinton and was told it couldn't air "
                  "during primary season. The Court ordered the case "
                  "reargued — a signal it may reach far beyond one movie."),
        "desc": ("Hillary: The Movie is unrelieved attack, and under "
                 "McCain-Feingold a corporation may not broadcast "
                 "'electioneering' close to an election. Citizens United, the "
                 "nonprofit behind it, sued. At the first argument the "
                 "government's lawyer conceded its logic might even reach "
                 "banning books — and the Court took the rare step of "
                 "scheduling a September reargument on whether decades of "
                 "restrictions on corporate political money should survive "
                 "at all. The foundations of campaign-finance law are on the "
                 "table."),
        "justices": BENCH_2009,
    },
    {
        "id": "nfib-v-sebelius",
        "era": "The Roberts Court · October Term 2011",
        "caseTitle": "NFIB v. Sebelius",
        "scdb": "2011-077",
        "question": ("May the Affordable Care Act's individual mandate — buy "
                     "health insurance or pay a penalty — stand as a valid "
                     "exercise of Congress's taxing power?"),
        "answer": "yes",
        "intro": ("Obamacare's fate reaches the Court in an election year: "
                  "three days of argument, protesters ringing the plaza, and "
                  "one question underneath it all — can Congress make "
                  "Americans buy insurance?"),
        "desc": ("The Affordable Care Act's machinery depends on the "
                 "individual mandate: carry health insurance or pay a penalty "
                 "with your taxes. Twenty-six states and a small-business "
                 "federation call that an unprecedented command to enter "
                 "commerce; the government calls it regulation of a market "
                 "everyone is already in — and, in the alternative, a tax. "
                 "After the mandate takes a beating at argument, Washington "
                 "spends three months bracing for the law to fall, and "
                 "intrigue about the outcome consumes the capital."),
        "justices": BENCH_2010_16,
    },
    {
        "id": "shelby-county-v-holder",
        "era": "The Roberts Court · October Term 2012",
        "caseTitle": "Shelby County v. Holder",
        "scdb": "2012-073",
        "question": ("May Congress keep requiring selected states, under a "
                     "decades-old coverage formula, to get federal approval "
                     "before changing their voting laws?"),
        "answer": "no",
        "intro": ("Since 1965, states with histories of discrimination have "
                  "needed Washington's permission to change their election "
                  "rules. An Alabama county argues the South of 2013 should "
                  "no longer be judged by the sins of 1965."),
        "desc": ("The Voting Rights Act's preclearance regime made the "
                 "federal government the South's election monitor, and "
                 "Congress reauthorized it in 2006 — 98 to 0 in the Senate. "
                 "But the formula deciding which states are covered still "
                 "turns on registration data from the 1960s and '70s. Shelby "
                 "County, Alabama, says the emergency is over and the old map "
                 "unconstitutional; civil-rights veterans answer that the law "
                 "works precisely because it has never been allowed to lapse. "
                 "The Court must decide whether history still governs."),
        "justices": BENCH_2010_16,
    },
    {
        "id": "obergefell-v-hodges",
        "era": "The Roberts Court · October Term 2014",
        "caseTitle": "Obergefell v. Hodges",
        "scdb": "2014-070",
        "question": ("Does the Fourteenth Amendment require every state to "
                     "license and recognize same-sex marriages?"),
        "answer": "yes",
        "intro": ("Jim Obergefell married his dying partner on a medical "
                  "plane on a Maryland tarmac — and Ohio refused to put his "
                  "name on the death certificate. The marriage question the "
                  "Court has circled for years finally arrives whole."),
        "desc": ("In two years same-sex marriage has spread from a handful of "
                 "states to most of the country, largely by court order — "
                 "until the Sixth Circuit upheld four states' bans and forced "
                 "the issue. Dozens of plaintiffs — widowers, adoptive "
                 "parents, an Army sergeant — ask whether Ohio, Michigan, "
                 "Kentucky, and Tennessee may define marriage as one man and "
                 "one woman. Crowds camp outside the building for argument "
                 "seats. Everyone understands this is the endgame."),
        "justices": BENCH_2010_16,
    },
    {
        "id": "masterpiece-cakeshop",
        "era": "The Roberts Court · October Term 2017",
        "caseTitle": "Masterpiece Cakeshop v. Colorado",
        "scdb": "2017-020",
        "question": ("Did Colorado violate the Constitution when it punished "
                     "a baker who refused to create a cake for a same-sex "
                     "wedding?"),
        "answer": "yes",
        "intro": ("A Colorado baker turned away two men seeking a wedding "
                  "cake, citing his faith. Five years of litigation later, "
                  "the collision between gay rights and religious conscience "
                  "reaches the Court on remarkably particular facts."),
        "desc": ("Jack Phillips will sell Charlie Craig and David Mullins "
                 "anything in his shop — but not a custom cake celebrating "
                 "their wedding, which his Christianity forbids. Colorado's "
                 "civil-rights commission found illegal discrimination, and "
                 "one commissioner compared religious-freedom arguments to "
                 "defenses of slavery and the Holocaust. Phillips says the "
                 "state is compelling his art and punishing his faith; the "
                 "couple answers that a business open to the public must "
                 "serve all of it. Both sides brace for a landmark."),
        "justices": BENCH_2017,
    },
    {
        "id": "carpenter-v-united-states",
        "era": "The Roberts Court · October Term 2017",
        "caseTitle": "Carpenter v. United States",
        "scdb": "2017-021",
        "question": ("Must the government get a warrant before obtaining "
                     "months of a suspect's cell-phone location records?"),
        "answer": "yes",
        "intro": ("To tie Timothy Carpenter to a string of armed robberies, "
                  "the FBI obtained 127 days of his cell-phone location "
                  "records — no warrant required. The question: does the "
                  "Fourth Amendment know what a smartphone is?"),
        "desc": ("Carriers log a phone's position every time it connects to a "
                 "tower, and under a 1986 statute the government collected "
                 "12,898 location points tracing Carpenter's movements for "
                 "four months — enough to convict him of robbing cell-phone "
                 "stores. Under the 'third-party doctrine,' records you share "
                 "with a company get no Fourth Amendment protection: a rule "
                 "built for the age of landlines and bank slips. Carpenter's "
                 "lawyers call cell records a time machine into anyone's "
                 "entire life."),
        "justices": BENCH_2017,
    },
    {
        "id": "bostock-v-clayton-county",
        "era": "The Roberts Court · October Term 2019",
        "caseTitle": "Bostock v. Clayton County",
        "scdb": "2019-004",
        "question": ("Does Title VII's ban on employment discrimination "
                     "'because of sex' protect gay and transgender workers "
                     "from being fired?"),
        "answer": "yes",
        "intro": ("Gerald Bostock says he was fired after joining a gay "
                  "softball league. Title VII bans employment discrimination "
                  "'because of sex' — words written in 1964. The question is "
                  "what those words cover in 2020."),
        "desc": ("Three cases arrive together: a Georgia child-welfare "
                 "coordinator fired after joining a gay recreational league, "
                 "a New York skydiving instructor fired days after mentioning "
                 "he was gay, and a Michigan funeral director fired after "
                 "telling her boss she was transgender. No federal statute "
                 "names sexual orientation or gender identity. The workers "
                 "argue you cannot fire a man for loving men without firing "
                 "him 'because of sex' — turning textualism's own logic into "
                 "the battlefield."),
        "justices": BENCH_2019,
    },
    {
        "id": "nysrpa-v-bruen",
        "era": "The Roberts Court · October Term 2021",
        "caseTitle": "New York State Rifle & Pistol Assn. v. Bruen",
        "scdb": "2021-013",
        "question": ("Does the Second Amendment protect a right to carry a "
                     "handgun in public for self-defense?"),
        "answer": "yes",
        "intro": ("New York will license your handgun at home; carrying it "
                  "outside requires 'proper cause' — a special need beyond "
                  "wanting protection. Fourteen years after Heller, the "
                  "Second Amendment steps out the front door."),
        "desc": ("Since 1911, New York has demanded that anyone seeking to "
                 "carry a concealed pistol show a particular need for "
                 "self-protection — ordinary fear of crime doesn't qualify, "
                 "and licensing officers hold broad discretion. Two upstate "
                 "men, denied unrestricted permits, sued alongside the state "
                 "rifle association. Heller secured the handgun in the home "
                 "but said little about the street. Half a dozen states with "
                 "similar laws cover a quarter of the country's population — "
                 "including its biggest cities."),
        "justices": BENCH_2021,
    },
    {
        "id": "dobbs-v-jackson",
        "era": "The Roberts Court · October Term 2021",
        "caseTitle": "Dobbs v. Jackson Women's Health",
        "scdb": "2021-019",
        "question": ("May a state ban most abortions after fifteen weeks of "
                     "pregnancy, well before fetal viability?"),
        "answer": "yes",
        "intro": ("Mississippi bans most abortions after fifteen weeks — a "
                  "law written to defy Roe v. Wade and force exactly this "
                  "case. A leaked draft opinion has already set the country "
                  "on fire. Now comes the decision itself."),
        "desc": ("Jackson Women's Health, the last abortion clinic in "
                 "Mississippi, challenges the state's Gestational Age Act: "
                 "almost no abortions after fifteen weeks, two months short "
                 "of the viability line that Roe and Casey made the "
                 "constitutional rule for half a century. Mississippi asks "
                 "the Court not merely to uphold the law but to overrule Roe "
                 "outright. Between argument and decision, a draft opinion "
                 "leaks to the press — an unprecedented breach that puts "
                 "security fencing around the building."),
        "justices": BENCH_2021,
    },
    {
        "id": "303-creative-v-elenis",
        "era": "The Roberts Court · October Term 2022",
        "caseTitle": "303 Creative v. Elenis",
        "scdb": "2022-019",
        "question": ("May a state require a designer of custom wedding "
                     "websites to create them for same-sex weddings over her "
                     "religious objections?"),
        "answer": "no",
        "intro": ("A Colorado web designer wants to build wedding sites — "
                  "but not for same-sex weddings, which her faith rejects. "
                  "She sued before designing a single one. The question "
                  "Masterpiece Cakeshop sidestepped is back, framed as pure "
                  "speech."),
        "desc": ("Lorie Smith says Colorado's public-accommodations law "
                 "would force her to design websites celebrating marriages "
                 "her Christianity opposes, on pain of investigation and "
                 "fines — so she went to court preemptively, before taking a "
                 "single wedding client. The state answers that a business "
                 "selling a service must sell it to everyone; her lawyers "
                 "answer that custom websites are speech, and Colorado is "
                 "scripting it. Five years after the baker's case, the "
                 "compelled-speech question arrives clean."),
        "justices": BENCH_2022,
    },
    {
        "id": "trump-v-united-states",
        "era": "The Roberts Court · October Term 2023",
        "caseTitle": "Trump v. United States",
        "scdb": "2023-061",
        "question": ("Does a former president enjoy at least presumptive "
                     "immunity from criminal prosecution for his official "
                     "acts in office?"),
        "answer": "yes",
        "intro": ("For the first time, a former president stands indicted "
                  "for trying to overturn an election he lost — and he "
                  "answers that presidents cannot be prosecuted at all. The "
                  "Court is asked to define the office itself."),
        "desc": ("Special counsel Jack Smith's January 6 indictment charges "
                 "Donald Trump with conspiring to overturn the 2020 "
                 "election. Trump claims sweeping immunity for anything "
                 "within a president's official duties — otherwise, his "
                 "lawyers warn, every president will leave office fearing "
                 "his successor's prosecutors. The special counsel answers "
                 "that no man is above the law and the trial should start "
                 "now. The election is four months off, and the calendar "
                 "itself may be the real prize."),
        "justices": BENCH_2022,
    },
]
