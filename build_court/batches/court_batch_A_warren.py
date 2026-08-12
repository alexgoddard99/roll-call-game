# The Court — Batch A: The Warren Court, 1953–1969.
# Votes are NOT written here — fetch_court.py verifies every justice's vote
# against the Supreme Court Database (justice-centered, 2024 release).

JUSTICES_EXTRA = {
    # key: (SCDB justiceName, display name, English Wikipedia page title)
    "warren54":    ("EWarren", "Earl Warren", "Earl Warren"),
    "warren":      ("EWarren", "Earl Warren", "Earl Warren"),
    "black":       ("HLBlack", "Hugo Black", "Hugo Black"),
    "reed":        ("SFReed", "Stanley Reed", "Stanley Forman Reed"),
    "frankfurter": ("FFrankfurter", "Felix Frankfurter", "Felix Frankfurter"),
    "douglas":     ("WODouglas", "William O. Douglas", "William O. Douglas"),
    "rhjackson":     ("RHJackson", "Robert H. Jackson", "Robert H. Jackson"),
    "burton":      ("HHBurton", "Harold Burton", "Harold Hitz Burton"),
    "clark":       ("TCClark", "Tom C. Clark", "Tom C. Clark"),
    "minton":      ("SMinton", "Sherman Minton", "Sherman Minton"),
    "harlan":      ("JHarlan2", "John Marshall Harlan", "John Marshall Harlan II"),
    "brennan":     ("WJBrennan", "William Brennan", "William J. Brennan Jr."),
    "whittaker":   ("CEWhittaker", "Charles Whittaker", "Charles Evans Whittaker"),
    "stewart":     ("PStewart", "Potter Stewart", "Potter Stewart"),
    "white":       ("BRWhite", "Byron White", "Byron White"),
    "goldberg":    ("AJGoldberg", "Arthur Goldberg", "Arthur Goldberg"),
    "fortas":      ("AFortas", "Abe Fortas", "Abe Fortas"),
    "marshall":    ("TMarshall", "Thurgood Marshall", "Thurgood Marshall"),
}

# --- Reusable blurbs (per justice, case-agnostic within the era used) ---

B_WARREN54 = ("Eisenhower's brand-new Chief Justice: a three-term California governor "
              "with no judicial experience and a politician's gift for the personal "
              "touch. Washington is still guessing whether he will be a caretaker — "
              "or something else entirely.")
B_WARREN = ("The former California governor, now the most consequential Chief Justice "
            "in a century. He asks lawyers one question — 'But is it fair?' — and "
            "works the conference like the politician he never stopped being.")
B_BLACK = ("An Alabama New Dealer who carries the Constitution in his coat pocket and "
           "reads it literally. 'No law' means no law — but rights he cannot find in "
           "the text, he will not invent.")
B_REED = ("A courtly Kentuckian and FDR's former Solicitor General — a moderate New "
          "Dealer with Southern instincts, deeply anxious about how far, and how "
          "fast, nine unelected judges should push the country.")
B_FRANKFURTER = ("The former Harvard professor and apostle of judicial restraint: "
                 "courts, he preaches, must defer to legislatures even when the "
                 "results offend. His seminars continue at conference, whether his "
                 "colleagues want them or not.")
B_DOUGLAS = ("A restless westerner and the Court's fastest pen — impatient with "
             "doctrine, indifferent to precedent, and instinctively on the side of "
             "the lone individual against the government in nearly any form it takes.")
B_JACKSON = ("FDR's Solicitor General and the chief Nuremberg prosecutor — the "
             "Court's finest stylist, just back from a heart attack, and wary of "
             "judicial power exercised without a firm footing in law.")
B_BURTON = ("A former Republican senator from Ohio appointed by his old colleague "
            "Harry Truman — a diligent, modest workhorse who reads every record and "
            "rarely makes headlines. Colleagues call him the fairest-minded man on "
            "the bench.")
B_MINTON = ("Truman's poker partner from Indiana, a former senator and loyal New "
            "Dealer who believes judging means restraint: the Court should follow "
            "the elected branches, not lead them anywhere.")
B_CLARK = ("Truman's Attorney General in a trademark bow tie — the Court's "
           "law-and-order Texan. He backs the police and the prosecutor by instinct, "
           "but he ran federal law enforcement himself and knows its temptations "
           "from the inside.")
B_HARLAN = ("The Wall Street patrician and grandson of a great dissenter — the "
            "Court's conservative conscience. He believes in ordered liberty and "
            "lawyerly process, and objects, elegantly, when the majority moves too "
            "far, too fast.")
B_BRENNAN = ("The Court's Irish charmer and master coalition-builder, an Eisenhower "
             "appointee who turned out to be its most effective liberal. His first "
             "rule of the shop: with five votes, you can do anything.")
B_WHITTAKER = ("A Missouri railroad lawyer who rose from farm poverty to the bench — "
               "cautious, conservative, and visibly agonized. Every close case is a "
               "torment; he is months from resigning under the strain.")
B_STEWART = ("A moderate Ohio Republican who resists both blocs' grand theories. He "
             "decides cases one at a time, asks what the Constitution actually "
             "commands, and lands — unpredictably — somewhere in the middle.")
B_WHITE = ("'Whizzer' White, the All-American halfback turned Kennedy's deputy "
           "attorney general — tough-minded, unsentimental, and skeptical of newly "
           "minted rights, especially the kind that make police work harder.")
B_GOLDBERG = ("Kennedy's labor secretary, new to the bench in Frankfurter's old seat "
              "and his opposite in every way: an exuberant liberal who believes the "
              "Constitution grows, and that the Court should help it along.")
B_FORTAS = ("LBJ's confidant and Washington's premier lawyer, still quietly advising "
            "the President from the bench. As an advocate he won poor defendants "
            "their counsel; as a justice he champions the underdog — children "
            "included.")
B_MARSHALL = ("The architect of the NAACP's litigation war on Jim Crow and the first "
              "Black justice — a storyteller who has seen the criminal law from the "
              "defendant's side of the table and never forgets it.")

# --- Benches, seniority order ---

BENCH_1954 = [
    ("warren54", B_WARREN54), ("black", B_BLACK), ("reed", B_REED),
    ("frankfurter", B_FRANKFURTER), ("douglas", B_DOUGLAS),
    ("rhjackson", B_JACKSON), ("burton", B_BURTON), ("clark", B_CLARK),
    ("minton", B_MINTON),
]
BENCH_1961 = [
    ("warren", B_WARREN), ("black", B_BLACK), ("frankfurter", B_FRANKFURTER),
    ("douglas", B_DOUGLAS), ("clark", B_CLARK), ("harlan", B_HARLAN),
    ("brennan", B_BRENNAN), ("whittaker", B_WHITTAKER), ("stewart", B_STEWART),
]
BENCH_GOLDBERG = [
    ("warren", B_WARREN), ("black", B_BLACK), ("douglas", B_DOUGLAS),
    ("clark", B_CLARK), ("harlan", B_HARLAN), ("brennan", B_BRENNAN),
    ("stewart", B_STEWART), ("white", B_WHITE), ("goldberg", B_GOLDBERG),
]
BENCH_FORTAS = [
    ("warren", B_WARREN), ("black", B_BLACK), ("douglas", B_DOUGLAS),
    ("clark", B_CLARK), ("harlan", B_HARLAN), ("brennan", B_BRENNAN),
    ("stewart", B_STEWART), ("white", B_WHITE), ("fortas", B_FORTAS),
]
BENCH_MARSHALL = [
    ("warren", B_WARREN), ("black", B_BLACK), ("douglas", B_DOUGLAS),
    ("harlan", B_HARLAN), ("brennan", B_BRENNAN), ("stewart", B_STEWART),
    ("white", B_WHITE), ("fortas", B_FORTAS), ("marshall", B_MARSHALL),
]

PUZZLES = [
    {
        "id": "brown-v-board",
        "era": "The Warren Court · October Term 1953",
        "caseTitle": "Brown v. Board of Education",
        "scdb": "1953-069",
        "question": ("Does racial segregation of public schools violate the "
                     "Constitution's guarantee of equal protection?"),
        "answer": "yes",
        "intro": ("Thurgood Marshall argues for the schoolchildren of Topeka; John "
                  "W. Davis, in the last great case of his career, defends "
                  "segregation. A brand-new Chief Justice presides over a question "
                  "the Court has put off for years."),
        "desc": ("Linda Brown walks past a whites-only school to catch a bus across "
                 "Topeka. Black families in four states and the District are suing "
                 "over segregated schools, and Plessy v. Ferguson's 'separate but "
                 "equal' has stood for 58 years. The Justice Department calls "
                 "segregation a Cold War embarrassment; the South promises massive "
                 "resistance. The case has already been argued twice — the justices, "
                 "deadlocked under the late Chief Justice Vinson, ordered reargument. "
                 "Now Earl Warren must produce an answer the country can live with."),
        "justices": BENCH_1954,
    },
    {
        "id": "mapp-v-ohio",
        "era": "The Warren Court · October Term 1960",
        "caseTitle": "Mapp v. Ohio",
        "scdb": "1960-133",
        "question": ("Must state courts throw out evidence that police obtained "
                     "through an illegal search?"),
        "answer": "yes",
        "intro": ("Cleveland, 1957. Police hunting a bombing suspect force their way "
                  "into Dollree Mapp's house waving a paper they call a warrant. "
                  "They never find their fugitive — but they prosecute her for what "
                  "they do find."),
        "desc": ("Officers ransacked Mapp's home without a genuine warrant, found "
                 "sexually explicit books in a trunk, and Ohio convicted her of "
                 "possessing obscene material. Federal courts have excluded illegally "
                 "seized evidence since 1914, but the Supreme Court has let each "
                 "state decide for itself — and about half still admit whatever the "
                 "police bring in, however they got it. Mapp's own lawyers barely "
                 "raise the search issue, attacking the obscenity law instead. The "
                 "deeper question: does the Fourth Amendment mean the same thing in "
                 "state court?"),
        "justices": BENCH_1961,
    },
    {
        "id": "gideon-v-wainwright",
        "era": "The Warren Court · October Term 1962",
        "caseTitle": "Gideon v. Wainwright",
        "scdb": "1962-058",
        "question": ("Must a state provide a lawyer to a criminal defendant too poor "
                     "to hire one?"),
        "answer": "yes",
        "intro": ("A Florida drifter, convicted of burglarizing a pool hall after "
                  "defending himself at trial, mails the Supreme Court a five-page "
                  "petition written in pencil on prison stationery. The Court takes "
                  "his case."),
        "desc": ("Clarence Earl Gideon asked the trial judge for counsel; Florida "
                 "appoints lawyers only in capital cases, so he cross-examined "
                 "witnesses himself and drew five years. Twenty years ago, in Betts "
                 "v. Brady, the Court held that states need not furnish counsel to "
                 "poor defendants absent 'special circumstances.' Gideon, reading "
                 "law in the prison library, insists the Constitution says "
                 "otherwise. The Court has appointed Washington superlawyer Abe "
                 "Fortas to argue his side — a hint, perhaps, of what it thinks of "
                 "Betts."),
        "justices": BENCH_GOLDBERG,
    },
    {
        "id": "times-v-sullivan",
        "era": "The Warren Court · October Term 1963",
        "caseTitle": "New York Times v. Sullivan",
        "scdb": "1963-067",
        "question": ("Does the First Amendment shield the press from libel judgments "
                     "won by public officials over honest errors?"),
        "answer": "yes",
        "intro": ("An Alabama jury has ordered the New York Times to pay $500,000 "
                  "over a civil-rights advertisement containing minor mistakes. "
                  "Dozens of similar suits are queued behind it — enough to bankrupt "
                  "every paper covering the South."),
        "desc": ("'Heed Their Rising Voices,' a 1960 fund-raising ad for Martin "
                 "Luther King's legal defense, got small details wrong — which song "
                 "the protesters sang, how many times King had been arrested. "
                 "Montgomery commissioner L.B. Sullivan, never named in the ad, sued "
                 "the Times and won half a million dollars. Under Alabama law, false "
                 "statements get no protection and damage is simply presumed. "
                 "Southern officials have discovered that libel law can do what "
                 "censorship cannot: drive the national press out of the "
                 "segregation story."),
        "justices": BENCH_GOLDBERG,
    },
    {
        "id": "escobedo-v-illinois",
        "era": "The Warren Court · October Term 1963",
        "caseTitle": "Escobedo v. Illinois",
        "scdb": "1963-164",
        "question": ("Does a suspect have the right to consult his lawyer during a "
                     "police interrogation?"),
        "answer": "yes",
        "intro": ("Chicago, 1960. Danny Escobedo's lawyer stands in the station "
                  "house demanding to see his client; down the hall, detectives tell "
                  "Escobedo his lawyer 'didn't want to see' him. By morning they "
                  "have a confession."),
        "desc": ("Escobedo, a 22-year-old laborer, was arrested for his "
                 "brother-in-law's murder and questioned through the night, "
                 "handcuffed and standing. His retained lawyer was in the building "
                 "for hours and repeatedly turned away while officers urged Escobedo "
                 "to pin the shooting on another man — statements that convicted him "
                 "instead. The right to counsel has always attached at trial; "
                 "prosecutors warn that extending it into the squad room would end "
                 "confessions altogether. Defense lawyers answer that a right which "
                 "begins after the confession comes too late."),
        "justices": BENCH_GOLDBERG,
    },
    {
        "id": "griswold-v-connecticut",
        "era": "The Warren Court · October Term 1964",
        "caseTitle": "Griswold v. Connecticut",
        "scdb": "1964-121",
        "question": ("May a state make it a crime for married couples to use "
                     "contraceptives?"),
        "answer": "no",
        "intro": ("Estelle Griswold opened a Planned Parenthood clinic in New Haven "
                  "and was arrested within ten days — exactly as she planned. "
                  "Connecticut's 1879 ban on contraception is finally before the "
                  "Court."),
        "desc": ("Connecticut forbids using 'any drug or article' to prevent "
                 "conception and punishes anyone who counsels it — a law enforced "
                 "just often enough to keep birth-control clinics closed. Griswold "
                 "and Yale physician C. Lee Buxton were fined $100 apiece for "
                 "advising married couples. No privacy clause appears anywhere in "
                 "the Constitution, and the justices must decide whether one is "
                 "implied — or whether, as the skeptics warn, striking down a silly "
                 "law would revive the free-wheeling judicial lawmaking of the "
                 "Lochner era."),
        "justices": BENCH_GOLDBERG,
    },
    {
        "id": "miranda-v-arizona",
        "era": "The Warren Court · October Term 1965",
        "caseTitle": "Miranda v. Arizona",
        "scdb": "1965-122",
        "question": ("Must police warn a suspect of his rights before interrogating "
                     "him?"),
        "answer": "yes",
        "intro": ("Ernesto Miranda confessed to kidnapping and rape after two hours "
                  "in a Phoenix interrogation room — never told he could remain "
                  "silent or see a lawyer. Police chiefs say the confession is the "
                  "backbone of American policing."),
        "desc": ("Miranda, a 23-year-old warehouse worker, signed a confession "
                 "beneath a printed line saying he understood his rights; no one had "
                 "told him what they were. Escobedo hinted two years ago that the "
                 "Constitution reaches into the station house, and lower courts have "
                 "split ever since. Four cases arrive together asking for a rule. "
                 "Law enforcement warns that lawyers in the interrogation room mean "
                 "the end of confessions; civil libertarians answer that the Fifth "
                 "Amendment was never meant to carry an asterisk for the poor and "
                 "unlettered."),
        "justices": BENCH_FORTAS,
    },
    {
        "id": "loving-v-virginia",
        "era": "The Warren Court · October Term 1966",
        "caseTitle": "Loving v. Virginia",
        "scdb": "1966-119",
        "question": "May a state criminalize marriage between people of different races?",
        "answer": "no",
        "intro": ("Richard and Mildred Loving married in Washington, then were "
                  "arrested in their Virginia bedroom at 2 a.m. The sentence: a year "
                  "in jail, suspended if they leave the state for twenty-five."),
        "desc": ("Virginia's Racial Integrity Act of 1924 makes the Lovings' "
                 "marriage a felony, and fifteen other states still enforce laws "
                 "like it. The trial judge wrote that God 'did not intend for the "
                 "races to mix.' Exiled to Washington, the Lovings want to go home "
                 "to Caroline County. Virginia argues its law punishes both spouses "
                 "equally and therefore discriminates against no one — the same "
                 "arithmetic that once sustained separate-but-equal. Mildred's "
                 "letter to Robert Kennedy started the case; the ACLU has carried "
                 "it here."),
        "justices": BENCH_FORTAS,
    },
    {
        "id": "terry-v-ohio",
        "era": "The Warren Court · October Term 1967",
        "caseTitle": "Terry v. Ohio",
        "scdb": "1967-157",
        "question": ("May an officer stop and frisk a suspect without probable cause "
                     "for an arrest?"),
        "answer": "yes",
        "intro": ("A veteran Cleveland detective watches two men pace past a "
                  "storefront a dozen times, conferring after each pass. Certain "
                  "they are casing it, he spins John Terry around and pats him "
                  "down — and finds a revolver."),
        "desc": ("Detective Martin McFadden had 39 years on the beat but no probable "
                 "cause for an arrest when he frisked Terry — only trained "
                 "suspicion. The pistol he found made the conviction; the question "
                 "is whether it was ever lawfully found. Police call the street stop "
                 "basic self-preservation in an armed country. Civil-rights lawyers, "
                 "a year after Newark and Detroit burned, warn the Court it is about "
                 "to license the wholesale harassment of Black men. The Fourth "
                 "Amendment, both sides note, forbids only 'unreasonable' searches."),
        "justices": BENCH_MARSHALL,
    },
    {
        "id": "tinker-v-des-moines",
        "era": "The Warren Court · October Term 1968",
        "caseTitle": "Tinker v. Des Moines",
        "scdb": "1968-043",
        "question": ("Does the First Amendment protect public-school students who "
                     "wear armbands in political protest?"),
        "answer": "yes",
        "intro": ("December 1965. Thirteen-year-old Mary Beth Tinker wears a black "
                  "armband to junior high to mourn the dead of Vietnam. Des Moines "
                  "banned armbands two days earlier — and suspends her by "
                  "afternoon."),
        "desc": ("Mary Beth, her brother John, and Christopher Eckhardt planned a "
                 "silent protest: black armbands through the holidays, nothing more. "
                 "School officials, hearing of the plan, banned armbands "
                 "specifically — political buttons and even Iron Crosses remained "
                 "permitted — and suspended the three who wore them anyway. No class "
                 "was disrupted. With campuses in open revolt by the time the case "
                 "is argued in 1968, the schools say discipline demands deference; "
                 "the students' lawyers say children do not shed the Constitution "
                 "at the schoolhouse gate."),
        "justices": BENCH_MARSHALL,
    },
]
