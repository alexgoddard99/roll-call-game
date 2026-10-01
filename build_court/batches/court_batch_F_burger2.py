# The Court — Batch F: The Burger Court, second helping (1971–1985).
# Votes are NOT written here — fetch_court.py verifies every justice's vote
# against the Supreme Court Database (SCDB justice-centered CSV).

JUSTICES_EXTRA = {
    # key: (SCDB justiceName, display name, English Wikipedia page title)
    # Identical to court_batch_B_burger.py — the pipeline requires it.
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
# Those marked (B) are copied verbatim from court_batch_B_burger.py.

BURGER_EARLY = (  # (B)
    "Nixon's chief justice, installed to steady a Court he believes ran wild "
    "under Earl Warren. A stickler for order and the dignity of institutions, "
    "he is more cautious conservative than crusader — and ever mindful of the "
    "Court's public standing.")
BURGER_80S = (
    "A dozen years into the center chair, the silver-maned Chief looks the "
    "part and guards the institution's dignity above all. Conservative on "
    "crime and schools, surprisingly pragmatic elsewhere, he assigns opinions "
    "with one eye on the headlines.")
BURGER_LATE = (  # (B)
    "Seventeen years into the center chair, as much administrator as judge — "
    "obsessed with judicial efficiency and courtroom decorum. Reliably "
    "conservative on crime and social questions, though colleagues grumble "
    "that his opinion assignments follow strategy more than principle.")

BLACK_71 = (  # (B)
    "At 85, the New Deal's last titan and the First Amendment's fiercest "
    "literalist — 'no law abridging' means no law, period. Frail and near the "
    "end of 34 years on the bench, he still writes with the old fire.")

DOUGLAS_EARLY = (  # (B)
    "A New Deal wunderkind grown into the Court's absolutist loner — three "
    "decades on the bench, four wives, a shelf of his own books. He votes for "
    "the individual against the government almost reflexively, and writes "
    "opinions at breakneck speed.")

HARLAN_71 = (  # (B)
    "The Court's patrician conservative conscience, a lawyer's lawyer of "
    "precision and restraint. Nearly blind, he reads briefs held an inch from "
    "his eyes — and insists that judging is a matter of process and "
    "precedent, never passion.")

BRENNAN_EARLY = (  # (B)
    "The Warren Court's master coalition-builder, an Eisenhower appointee "
    "turned architect of its liberal revolution. His first rule — with five "
    "votes you can do anything — still guides him as the bench tilts "
    "rightward around him.")
BRENNAN_MID = (  # (B)
    "Twenty years on, the great liberal playmaker works a Court that has "
    "drifted away from him. He still counts to five better than anyone alive, "
    "hunting the center for partners case by case.")
BRENNAN_80S = (
    "A quarter-century in, the Warren Court's great playmaker now leads a "
    "liberal wing of two or three. He still hunts the center vote in every "
    "conference, and still lands a surprising number of them — his clerks "
    "call it the rule of five.")
BRENNAN_LATE = (  # (B)
    "The aging captain of the Court's shrinking liberal wing, three decades "
    "in. He can still conjure a majority from thin air on a good day — but "
    "these days he is more often assigning dissents than opinions.")

STEWART_EARLY = (  # (B)
    "A pragmatic Ohio Republican wary of grand theory, he decides cases "
    "narrowly and one at a time. Neither wing can count on him: he distrusts "
    "government overreach and judicial adventure in roughly equal measure.")
STEWART_MID = (  # (B)
    "The Court's studied centrist, a judge of narrow rulings and practical "
    "lines. Eighteen years in, he remains the man both blocs court — "
    "skeptical of absolutes, attentive to how the law actually operates.")

WHITE_EARLY = (  # (B)
    "The Kennedys' deputy attorney general, an All-America halfback turned "
    "no-nonsense pragmatist. Tough on crime and skeptical of newly minted "
    "rights, yet often found with the liberals on race and civil rights.")
WHITE_LATE = (  # (B)
    "JFK's last appointee has hardened into the Court's flintiest "
    "pragmatist — tough on crime, dismissive of rights he cannot find in the "
    "Constitution's text, still steady on race and equal protection.")

MARSHALL_EARLY = (  # (B)
    "The architect of Brown v. Board and the Court's first Black justice. He "
    "judges from lived experience — Jim Crow courtrooms, clients facing the "
    "electric chair — and defends the poor and powerless with unembarrassed "
    "consistency.")
MARSHALL_LATE = (  # (B)
    "The civil-rights giant in winter, increasingly isolated as the Court "
    "moves right. He and Brennan vote as a pair on the death penalty and much "
    "else, filing dissent after dissent for a future Court to find.")

BLACKMUN_EARLY = (  # (B)
    "The junior justice, a shy Minnesota Republican and longtime counsel to "
    "the Mayo Clinic. Washington calls him and his boyhood friend the Chief "
    "the 'Minnesota Twins' — so far he votes Burger's way more often than "
    "not.")
BLACKMUN_MID = (  # (B)
    "The Mayo Clinic's meticulous former counsel, an anxious drafter who "
    "agonizes over every case. Once dismissed as Burger's 'Minnesota Twin,' "
    "he is drifting from the Chief, case by case, toward a path of his own.")
BLACKMUN_LATE = (  # (B)
    "The onetime 'Minnesota Twin' has completed a long migration: the shy "
    "Nixon appointee now votes more often with Brennan and Marshall than with "
    "the Chief he grew up beside — above all on privacy and equality.")

POWELL_EARLY = (  # (B)
    "A courtly Richmond corporate lawyer and former ABA president, newly "
    "arrived on the bench. The establishment's ideal judge: moderate, "
    "balancing, allergic to extremes — he weighs each case like a client "
    "matter and lands, usually, near the center.")
POWELL_MID = (
    "The courtly Richmond lawyer has settled into the Court's center seat, "
    "a balancer who distrusts bright lines and sweeping theories alike. He "
    "weighs each case like a client matter, writes with a counselor's "
    "caution, and seldom finds himself in dissent.")
POWELL_LATE = (  # (B)
    "The Court's gentle fulcrum. The courtly Richmond lawyer decides the "
    "close ones — law clerks joke that the Constitution means whatever Lewis "
    "Powell thinks it means — balancing order against liberty with a "
    "counselor's caution.")

REHNQUIST_EARLY = (  # (B)
    "The junior justice and its boldest conservative — a 47-year-old Nixon "
    "Justice Department lawyer with a brilliant pen and no fear of standing "
    "alone. He doubts much of what the Warren Court built.")
REHNQUIST_MID = (
    "The Court's most unapologetic conservative, a brilliant and cheerful "
    "writer who would rather dissent alone than join an opinion he doubts. "
    "States' rights, law enforcement, judicial restraint — his compass "
    "never wavers, whatever the company.")
REHNQUIST_LATE = (  # (B)
    "The Court's anchor on the right, so fond of solo dissents that his "
    "clerks once gave him a Lone Ranger doll. Federalism, law enforcement, "
    "judicial restraint: his positions never wobble — and the Court, "
    "increasingly, comes to him.")

STEVENS_MID = (  # (B)
    "The newest justice, a bow-tied Chicago antitrust lawyer chosen by "
    "Gerald Ford for sheer legal craftsmanship. He belongs to no bloc, writes "
    "separate opinions constantly, and steers by his own idiosyncratic "
    "compass.")
STEVENS_LATE = (  # (B)
    "The bow-tied Chicagoan defies sorting — a Ford Republican drifting "
    "toward the Court's left flank, case by idiosyncratic case. He writes "
    "more separate opinions than anyone, trusting his own reading of the law "
    "over any bloc's.")

OCONNOR_NEW = (
    "The newest justice and the first woman to sit on the Court, a former "
    "Arizona legislative leader sworn in last fall. She judges like a "
    "lawmaker — narrow rulings, workable compromises, close attention to the "
    "facts — and no one yet knows where she lands.")
OCONNOR_LATE = (  # (B)
    "The first woman on the Court, a former Arizona legislative leader who "
    "judges like a lawmaker — narrow rulings, workable compromises, close "
    "attention to the facts. Reliably conservative on crime; harder to "
    "predict everywhere else.")

# ---- Benches ---------------------------------------------------------------

BENCH_1971 = [
    ("burger", BURGER_EARLY),
    ("black", BLACK_71),
    ("douglas", DOUGLAS_EARLY),
    ("harlan", HARLAN_71),
    ("brennan", BRENNAN_EARLY),
    ("stewart", STEWART_EARLY),
    ("white", WHITE_EARLY),
    ("marshall", MARSHALL_EARLY),
    ("blackmun", BLACKMUN_EARLY),
]
BENCH_1972_75 = [
    ("burger", BURGER_EARLY),
    ("douglas", DOUGLAS_EARLY),
    ("brennan", BRENNAN_EARLY),
    ("stewart", STEWART_EARLY),
    ("white", WHITE_EARLY),
    ("marshall", MARSHALL_EARLY),
    ("blackmun", BLACKMUN_EARLY),
    ("powell", POWELL_EARLY),
    ("rehnquist", REHNQUIST_EARLY),
]
BENCH_1976 = [
    ("burger", BURGER_EARLY),
    ("brennan", BRENNAN_MID),
    ("stewart", STEWART_MID),
    ("white", WHITE_EARLY),
    ("marshall", MARSHALL_EARLY),
    ("blackmun", BLACKMUN_MID),
    ("powell", POWELL_MID),
    ("rehnquist", REHNQUIST_MID),
    ("stevens", STEVENS_MID),
]
BENCH_1981 = [
    ("burger", BURGER_80S),
    ("brennan", BRENNAN_MID),
    ("stewart", STEWART_MID),
    ("white", WHITE_LATE),
    ("marshall", MARSHALL_LATE),
    ("blackmun", BLACKMUN_MID),
    ("powell", POWELL_MID),
    ("rehnquist", REHNQUIST_MID),
    ("stevens", STEVENS_MID),
]
BENCH_1982 = [
    ("burger", BURGER_80S),
    ("brennan", BRENNAN_80S),
    ("white", WHITE_LATE),
    ("marshall", MARSHALL_LATE),
    ("blackmun", BLACKMUN_LATE),
    ("powell", POWELL_LATE),
    ("rehnquist", REHNQUIST_LATE),
    ("stevens", STEVENS_LATE),
    ("oconnor", OCONNOR_NEW),
]
BENCH_1984 = [
    ("burger", BURGER_LATE),
    ("brennan", BRENNAN_LATE),
    ("white", WHITE_LATE),
    ("marshall", MARSHALL_LATE),
    ("blackmun", BLACKMUN_LATE),
    ("powell", POWELL_LATE),
    ("rehnquist", REHNQUIST_LATE),
    ("stevens", STEVENS_LATE),
    ("oconnor", OCONNOR_LATE),
]

# ---- Puzzles ---------------------------------------------------------------

PUZZLES = [
    {
        "id": "swann-v-charlotte-mecklenburg",
        "era": "The Burger Court · October Term 1970",
        "caseTitle": "Swann v. Charlotte-Mecklenburg Board of Education",
        "scdb": "1970-082",
        "question": "May a federal judge order a city to bus schoolchildren across town to desegregate its schools?",
        "answer": "yes",
        "intro": ("Charlotte, North Carolina. Seventeen years after Brown, "
                  "a federal judge has ordered the South's model school system "
                  "to bus thousands of children out of their neighborhoods — "
                  "and the city is in an uproar."),
        "desc": ("Charlotte-Mecklenburg runs 84,000 pupils through a single "
                 "countywide system, and most of its Black children still "
                 "attend schools that are all but entirely Black. Judge James "
                 "McMillan, a local Presbyterian elder, has ordered pairing "
                 "of inner-city and suburban schools and daily busing to make "
                 "every school's enrollment resemble the county's — then "
                 "received death threats and seen his effigy burned. The "
                 "school board says Brown required only an end to assignment "
                 "by race, not racial balance. The Nixon administration, "
                 "campaigning against 'forced busing,' sides with the board."),
        "justices": BENCH_1971,
    },
    {
        "id": "cohen-v-california",
        "era": "The Burger Court · October Term 1970",
        "caseTitle": "Cohen v. California",
        "scdb": "1970-121",
        "question": "May a state convict a man for wearing a jacket reading 'F--- the Draft' in a courthouse corridor?",
        "answer": "no",
        "intro": ("A nineteen-year-old walks through the Los Angeles County "
                  "Courthouse in a jacket bearing three words about the "
                  "draft — and spends thirty days in jail for it. Now the "
                  "words reach the marble temple."),
        "desc": ("Paul Robert Cohen wore the jacket through a corridor full "
                 "of women and children in April 1968; he took it off in "
                 "the courtroom and was arrested anyway for 'offensive "
                 "conduct' disturbing the peace. Nobody fought, nobody was "
                 "threatened — the only offense was the word. The Chief "
                 "Justice warns counsel it will not be necessary to say it "
                 "aloud. California argues a state may "
                 "police the vocabulary of public places; Cohen's lawyers "
                 "answer that the Constitution protects the emotion of a "
                 "message as well as its content."),
        "justices": BENCH_1971,
    },
    {
        "id": "lemon-v-kurtzman",
        "era": "The Burger Court · October Term 1970",
        "caseTitle": "Lemon v. Kurtzman",
        "scdb": "1970-141",
        "question": "May a state use tax money to help pay the salaries of teachers in church-run schools?",
        "answer": "no",
        "intro": ("Catholic schools are closing by the hundreds, and "
                  "Pennsylvania and Rhode Island have begun writing checks "
                  "to keep their teachers paid. A Philadelphia taxpayer "
                  "named Alton Lemon says the checks must stop."),
        "desc": ("Pennsylvania reimburses parochial schools for teachers' "
                 "salaries, textbooks and materials in secular subjects; "
                 "Rhode Island pays a fifteen-percent supplement straight to "
                 "nonpublic-school teachers, nearly all of them in Catholic "
                 "classrooms. The states insist the money buys mathematics "
                 "and reading, not catechism. The challengers answer that no "
                 "one can police where arithmetic ends and religion begins, "
                 "and that the policing itself entangles church and state. "
                 "Thurgood Marshall sits out the Pennsylvania case; eight "
                 "justices will write the rule for every state tempted to "
                 "follow."),
        "justices": [j for j in BENCH_1971 if j[0] != "marshall"],
    },
    {
        "id": "branzburg-v-hayes",
        "era": "The Burger Court · October Term 1971",
        "caseTitle": "Branzburg v. Hayes",
        "scdb": "1971-176",
        "question": "Does the First Amendment let a reporter refuse to tell a grand jury what he saw while reporting?",
        "answer": "no",
        "intro": ("A Louisville reporter watches two young men cook hashish "
                  "for a story, promises not to name them — and is "
                  "subpoenaed. Three newsmen, three grand juries, one "
                  "question: does the press get a privilege?"),
        "desc": ("Paul Branzburg of the Courier-Journal wrote about the drug "
                 "trade from the inside; Earl Caldwell of the New York Times "
                 "earned the trust of the Black Panthers; Paul Pappas, a "
                 "New Bedford cameraman, spent a night in a Panther "
                 "headquarters. Each has refused a grand jury's demand to "
                 "testify, arguing that sources will dry up the moment "
                 "reporters become investigators' eyes. Prosecutors answer "
                 "that every citizen owes the grand jury his evidence. "
                 "Nineteen states have shield laws; the Constitution has "
                 "never been read to contain one."),
        "justices": BENCH_1972_75,
    },
    {
        "id": "san-antonio-v-rodriguez",
        "era": "The Burger Court · October Term 1972",
        "caseTitle": "San Antonio Independent School District v. Rodriguez",
        "scdb": "1972-083",
        "question": "Does funding public schools through local property taxes, which leaves poor districts with far less per pupil, violate the Equal Protection Clause?",
        "answer": "no",
        "intro": ("Two San Antonio school districts a few miles apart: "
                  "Edgewood taxes itself at the highest rate in the county "
                  "and raises a fraction of what Alamo Heights spends on "
                  "each child. A sheet-metal worker sues."),
        "desc": ("Demetrio Rodriguez's children attend Edgewood schools "
                 "where the roof leaks, many teachers are uncertified and "
                 "the district spends $356 per pupil; across town, Alamo "
                 "Heights spends $594 at a lower tax rate, because its homes "
                 "are worth so much more. Texas, like nearly every state, "
                 "finances schools largely from local property wealth. A "
                 "three-judge federal court found the system unconstitutional. "
                 "If the Justices agree, school finance in forty-nine states "
                 "must be rebuilt — and they must decide whether education "
                 "is a fundamental right and the poor a specially protected "
                 "class."),
        "justices": BENCH_1972_75,
    },
    {
        "id": "milliken-v-bradley",
        "era": "The Burger Court · October Term 1973",
        "caseTitle": "Milliken v. Bradley",
        "scdb": "1973-173",
        "question": "May a federal court order Detroit's suburbs into a busing plan to desegregate the city's schools?",
        "answer": "no",
        "intro": ("Detroit's schools are nearly three-quarters Black and the "
                  "suburbs nearly all white. A federal judge has decided "
                  "there is only one way to integrate them: fold fifty-three "
                  "suburban districts into one metropolitan plan."),
        "desc": ("Ronald Bradley was a kindergartner when the NAACP sued in "
                 "his name. Judge Stephen Roth found Detroit had deliberately "
                 "segregated its schools, then concluded that any remedy "
                 "confined to the city would only speed white flight across "
                 "its borders — so he ordered buses across them. The suburbs, "
                 "never found to have done anything wrong, say they are being "
                 "punished for Detroit's sins. The NAACP answers that a "
                 "district line is just a line. This is the Court's first "
                 "look at busing beyond the city limits."),
        "justices": BENCH_1972_75,
    },
    {
        "id": "goss-v-lopez",
        "era": "The Burger Court · October Term 1974",
        "caseTitle": "Goss v. Lopez",
        "scdb": "1974-028",
        "question": "Must a public school give a student notice and a chance to tell his side before suspending him?",
        "answer": "yes",
        "intro": ("Columbus, Ohio, in a winter of racial unrest. Seventy-five "
                  "students are suspended for ten days each in a single "
                  "sweep — many without being told what they were accused "
                  "of. Nine of them sue."),
        "desc": ("Dwight Lopez says he was a bystander when a lunchroom "
                 "disturbance broke out at Central High; he was sent home "
                 "for ten days and learned the reason, if at all, by letter. "
                 "Ohio law lets principals suspend without any hearing. The "
                 "students argue that a free public education is a right the "
                 "state has granted and cannot snatch away without due "
                 "process; the board replies that principals are not judges "
                 "and hallways are not courtrooms. At stake is whether the "
                 "Fourteenth Amendment follows a teenager into the "
                 "principal's office."),
        "justices": BENCH_1972_75,
    },
    {
        "id": "craig-v-boren",
        "era": "The Burger Court · October Term 1976",
        "caseTitle": "Craig v. Boren",
        "scdb": "1976-025",
        "question": "May Oklahoma let women buy 3.2 percent beer at eighteen while making men wait until twenty-one?",
        "answer": "no",
        "intro": ("A college fraternity man and the owner of the Honk n' "
                  "Holler drive-in in Stillwater, Oklahoma, go to the "
                  "Supreme Court over near beer — and over how hard the "
                  "Constitution looks at laws that sort people by sex."),
        "desc": ("Curtis Craig, an Oklahoma State student, could not buy the "
                 "weak beer his female classmates bought freely; Carolyn "
                 "Whitener, who sold it, faced losing her license if she "
                 "served him. Oklahoma points to arrest statistics: young men "
                 "are far more often picked up for drunk driving. The "
                 "challengers, with Ruth Bader Ginsburg of the ACLU at "
                 "counsel table, say the numbers are thin and the stereotype "
                 "thick. Five years after Reed v. Reed the Justices still "
                 "have no agreed standard for sex-discrimination cases; this "
                 "unlikely vehicle may force one."),
        "justices": BENCH_1976,
    },
    {
        "id": "rostker-v-goldberg",
        "era": "The Burger Court · October Term 1980",
        "caseTitle": "Rostker v. Goldberg",
        "scdb": "1980-136",
        "question": "May Congress require only men, and not women, to register for a military draft?",
        "answer": "yes",
        "intro": ("The Soviets are in Afghanistan, and President Carter has "
                  "revived draft registration. He asked Congress to register "
                  "women too; Congress refused. A lawsuit filed by draft "
                  "resisters a decade earlier springs back to life."),
        "desc": ("Robert Goldberg and other young men first sued in 1971, "
                 "when the Vietnam draft was live, arguing that a system "
                 "that conscripts men alone discriminates against them. The "
                 "case lay dormant until registration returned in 1980. "
                 "Congress held hearings and concluded that because women "
                 "are barred from combat, registering them would serve no "
                 "military purpose. A federal court struck the law down days "
                 "before the first registration deadline. The Justices must "
                 "weigh their new scrutiny of sex-based laws against the "
                 "deference they have always given Congress over the armed "
                 "forces."),
        "justices": BENCH_1981,
    },
    {
        "id": "plyler-v-doe",
        "era": "The Burger Court · October Term 1981",
        "caseTitle": "Plyler v. Doe",
        "scdb": "1981-120",
        "question": "May Texas deny a free public education to children who are in the country illegally?",
        "answer": "no",
        "intro": ("Tyler, Texas. The school district begins charging a "
                  "thousand dollars a year to any child who cannot prove "
                  "lawful residence — and four families of Mexican "
                  "farmworkers, suing as 'Doe,' ask a federal court to stop "
                  "it."),
        "desc": ("A 1975 Texas law withholds state money for the schooling "
                 "of children not legally admitted to the country and lets "
                 "districts bar them outright. Tyler chose tuition instead, "
                 "a sum no farmworker family can pay. Texas says it owes "
                 "nothing to children whose presence violates federal law. "
                 "The children's lawyers answer that the Fourteenth "
                 "Amendment protects every 'person within its jurisdiction,' "
                 "and that a state cannot create an underclass of "
                 "illiterates for the sins of their parents. Nine years "
                 "earlier the Court said education was not a fundamental "
                 "right."),
        "justices": BENCH_1982,
    },
    {
        "id": "nixon-v-fitzgerald",
        "era": "The Burger Court · October Term 1981",
        "caseTitle": "Nixon v. Fitzgerald",
        "scdb": "1981-140",
        "question": "Is a former President immune from being sued for damages over his official acts in office?",
        "answer": "yes",
        "intro": ("An Air Force cost analyst told Congress the truth about "
                  "a two-billion-dollar overrun, lost his job in a "
                  "'reorganization,' and sued the man he says ordered it: "
                  "Richard Nixon."),
        "desc": ("A. Ernest Fitzgerald testified in 1968 about runaway costs "
                 "on the C-5A cargo plane; in 1970 his position was "
                 "abolished. On the White House tapes Nixon can be heard "
                 "saying to get rid of him, and at a 1973 press conference "
                 "the President took responsibility before his staff "
                 "retracted it. Nixon, out of office and pardoned, "
                 "argues that a President who can be sued over every "
                 "official decision cannot govern. Fitzgerald answers that "
                 "no office in America places a man above the law. Nixon has "
                 "already quietly paid him $142,000."),
        "justices": BENCH_1982,
    },
    {
        "id": "bob-jones-university-v-us",
        "era": "The Burger Court · October Term 1982",
        "caseTitle": "Bob Jones University v. United States",
        "scdb": "1982-084",
        "question": "May the IRS deny tax-exempt status to a religious university that bans interracial dating?",
        "answer": "yes",
        "intro": ("A fundamentalist college in Greenville, South Carolina, "
                  "forbids its students to date across racial lines, citing "
                  "Scripture. The IRS says that forfeits its tax exemption. "
                  "The Reagan administration, mid-case, switches sides."),
        "desc": ("Bob Jones University admitted no Black students until "
                 "1971 and still expels any student who dates or marries "
                 "outside his race. Since 1970 the IRS has refused charitable "
                 "status to schools that discriminate by race, reasoning "
                 "that a charity must serve the public good. In January 1982 "
                 "the Reagan Justice Department switched to the university's "
                 "side, and the Court appointed an outside lawyer, William "
                 "Coleman, to defend the government's old position. At "
                 "stake: whether the tax code may enforce national policy "
                 "against sincere religious belief."),
        "justices": BENCH_1982,
    },
    {
        "id": "ins-v-chadha",
        "era": "The Burger Court · October Term 1982",
        "caseTitle": "INS v. Chadha",
        "scdb": "1982-130",
        "question": "May one house of Congress, by resolution alone, overturn a decision the executive branch made under authority Congress delegated?",
        "answer": "no",
        "intro": ("A Kenyan-born student of Indian descent overstays his "
                  "visa, wins permission to remain from an immigration "
                  "judge — and loses it when the House of Representatives "
                  "passes a resolution, without debate, naming him."),
        "desc": ("Jagdish Chadha was a man without a country: neither Kenya "
                 "nor Britain would take him back, and in 1974 an immigration "
                 "judge suspended his deportation. Under a 1952 statute "
                 "either house of Congress may veto such a suspension by "
                 "simple resolution, and in December 1975 the House did, "
                 "with no hearing and no recorded vote. The 'legislative "
                 "veto' appears in nearly two hundred "
                 "federal laws, from war powers to arms sales; Congress calls "
                 "it an essential check on the agencies. Chadha's lawyers "
                 "call it lawmaking without a law."),
        "justices": BENCH_1982,
    },
    {
        "id": "lynch-v-donnelly",
        "era": "The Burger Court · October Term 1983",
        "caseTitle": "Lynch v. Donnelly",
        "scdb": "1983-048",
        "question": "May a city include a Nativity scene in its official Christmas display?",
        "answer": "yes",
        "intro": ("Every December for forty years Pawtucket, Rhode Island, "
                  "has set up Santa's house, a Christmas tree, reindeer and "
                  "a manger scene downtown. A local resident and the ACLU "
                  "ask the courts to take the manger away."),
        "desc": ("The crèche is city-owned, erected by city workers in a "
                 "park beside the shopping district, surrounded by cut-out "
                 "carolers, a talking wishing well and a banner reading "
                 "SEASONS GREETINGS. Daniel Donnelly says a city that "
                 "displays the infant Jesus endorses Christianity, and two "
                 "lower courts agreed. Mayor Dennis Lynch calls the display "
                 "a secular holiday tradition that happens to acknowledge "
                 "its origin, and the Reagan administration backs him. "
                 "Thirteen years after the Lemon test, the Justices must say "
                 "whether the Establishment Clause reaches a plastic manger "
                 "in a public square."),
        "justices": BENCH_1984,
    },
    {
        "id": "united-states-v-leon",
        "era": "The Burger Court · October Term 1983",
        "caseTitle": "United States v. Leon",
        "scdb": "1983-170",
        "question": "May evidence seized under a search warrant later found defective still be used at trial if the police relied on the warrant in good faith?",
        "answer": "yes",
        "intro": ("Burbank police watch a house for months, write up a "
                  "warrant, and seize a drug dealer's cocaine. A judge later "
                  "decides the warrant should never have issued — and the "
                  "exclusionary rule faces its sharpest test in twenty years."),
        "desc": ("Alberto Leon and his partners ran a trafficking operation "
                 "that officers tracked through surveillance and an "
                 "informant of unproven reliability. A magistrate signed "
                 "the warrant; a district judge found the affidavit fell "
                 "short of probable cause and threw out the drugs. Since "
                 "Mapp v. Ohio, evidence taken in violation of the Fourth "
                 "Amendment has been barred from every trial. The Justice "
                 "Department argues that suppression punishes nobody when "
                 "the police did everything right; defense lawyers answer "
                 "that a 'good faith' exception would make the warrant "
                 "requirement a formality."),
        "justices": BENCH_1984,
    },
    {
        "id": "tennessee-v-garner",
        "era": "The Burger Court · October Term 1984",
        "caseTitle": "Tennessee v. Garner",
        "scdb": "1984-065",
        "question": "May police shoot a fleeing, unarmed burglary suspect simply to prevent his escape?",
        "answer": "no",
        "intro": ("Memphis, an October night in 1974. A fifteen-year-old "
                  "with ten dollars and a stolen purse scrambles over a "
                  "backyard fence, and a police officer shoots him in the "
                  "back of the head."),
        "desc": ("Edward Garner was slight, unarmed and, the officer later "
                 "admitted, almost certainly not dangerous; Tennessee law "
                 "allowed 'all the necessary means' to stop a fleeing felon, "
                 "a rule inherited from the common law, when every felony "
                 "was a hanging offense. Garner's father sued the city and "
                 "the officer. Half the states still permit deadly force "
                 "against any fleeing felon; police departments say officers "
                 "cannot be asked to let suspects run. The question is "
                 "whether the Fourth Amendment's bar on unreasonable "
                 "seizures governs the most final seizure of all."),
        "justices": BENCH_1984,
    },
    {
        "id": "wallace-v-jaffree",
        "era": "The Burger Court · October Term 1984",
        "caseTitle": "Wallace v. Jaffree",
        "scdb": "1984-115",
        "question": "May a state set aside a minute of classroom silence 'for meditation or voluntary prayer'?",
        "answer": "no",
        "intro": ("Mobile, Alabama. A father of three complains that his "
                  "children are being led in prayer at public school, and "
                  "the state answers with a law reserving a daily minute of "
                  "silence 'for meditation or voluntary prayer.'"),
        "desc": ("Ishmael Jaffree, an agnostic legal-aid lawyer, says his "
                 "children were taunted for sitting out classroom prayers. "
                 "Alabama already had a moment-of-silence law for "
                 "'meditation'; in 1981 the legislature added 'or voluntary "
                 "prayer,' and its sponsor said plainly that the purpose was "
                 "to return prayer to the schools. A federal judge upheld "
                 "the law by ruling that the Establishment Clause does not "
                 "bind the states at all. Twenty-three years after the Court "
                 "barred official school prayer, the question is whether a "
                 "silent minute labeled for prayer crosses the same line."),
        "justices": BENCH_1984,
    },
]
