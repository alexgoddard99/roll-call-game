# The Court — Batch E: The Warren Court, second pack, 1958–1969.
# Votes are NOT written here — fetch_court.py verifies every justice's vote
# against the Supreme Court Database (justice-centered, 2024 release).
# Keys and tuples below are identical to court_batch_A_warren.py.

JUSTICES_EXTRA = {
    # key: (SCDB justiceName, display name, English Wikipedia page title)
    "warren":      ("EWarren", "Earl Warren", "Earl Warren"),
    "black":       ("HLBlack", "Hugo Black", "Hugo Black"),
    "frankfurter": ("FFrankfurter", "Felix Frankfurter", "Felix Frankfurter"),
    "douglas":     ("WODouglas", "William O. Douglas", "William O. Douglas"),
    "burton":      ("HHBurton", "Harold Burton", "Harold Hitz Burton"),
    "clark":       ("TCClark", "Tom C. Clark", "Tom C. Clark"),
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

B_WARREN = ("The former California governor, now the most consequential Chief Justice "
            "in a century. He asks lawyers one question — 'But is it fair?' — and "
            "works the conference like the politician he never stopped being.")
B_BLACK = ("An Alabama New Dealer who carries the Constitution in his coat pocket and "
           "reads it literally. 'No law' means no law — but rights he cannot find in "
           "the text, he will not invent.")
B_FRANKFURTER = ("The former Harvard professor and apostle of judicial restraint: "
                 "courts, he preaches, must defer to legislatures even when the "
                 "results offend. His seminars continue at conference, whether his "
                 "colleagues want them or not.")
B_DOUGLAS = ("A restless westerner and the Court's fastest pen — impatient with "
             "doctrine, indifferent to precedent, and instinctively on the side of "
             "the lone individual against the government in nearly any form it takes.")
B_BURTON = ("A former Republican senator from Ohio appointed by his old colleague "
            "Harry Truman — a diligent, modest workhorse who reads every record and "
            "rarely makes headlines. Colleagues call him the fairest-minded man on "
            "the bench.")
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
B_WHITTAKER58 = ("A Missouri railroad lawyer who rose from farm poverty to the bench — "
                 "cautious, conservative, and visibly agonized by close cases. He "
                 "drafts opinions for both sides before choosing, and the choosing "
                 "costs him sleep.")
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

BENCH_1958 = [  # Special Term, August 1958 — before Stewart took Burton's seat
    ("warren", B_WARREN), ("black", B_BLACK), ("frankfurter", B_FRANKFURTER),
    ("douglas", B_DOUGLAS), ("burton", B_BURTON), ("clark", B_CLARK),
    ("harlan", B_HARLAN), ("brennan", B_BRENNAN), ("whittaker", B_WHITTAKER58),
]
BENCH_1961_NO_WHITTAKER = [  # Whittaker, ill, did not take part
    ("warren", B_WARREN), ("black", B_BLACK), ("frankfurter", B_FRANKFURTER),
    ("douglas", B_DOUGLAS), ("clark", B_CLARK), ("harlan", B_HARLAN),
    ("brennan", B_BRENNAN), ("stewart", B_STEWART),
]
BENCH_1961_SEVEN = [  # Frankfurter stricken, White too new: seven sat
    ("warren", B_WARREN), ("black", B_BLACK), ("douglas", B_DOUGLAS),
    ("clark", B_CLARK), ("harlan", B_HARLAN), ("brennan", B_BRENNAN),
    ("stewart", B_STEWART),
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
BENCH_1967_NO_MARSHALL = [  # Marshall, lately Solicitor General, recused
    ("warren", B_WARREN), ("black", B_BLACK), ("douglas", B_DOUGLAS),
    ("harlan", B_HARLAN), ("brennan", B_BRENNAN), ("stewart", B_STEWART),
    ("white", B_WHITE), ("fortas", B_FORTAS),
]
BENCH_MARSHALL = [
    ("warren", B_WARREN), ("black", B_BLACK), ("douglas", B_DOUGLAS),
    ("harlan", B_HARLAN), ("brennan", B_BRENNAN), ("stewart", B_STEWART),
    ("white", B_WHITE), ("fortas", B_FORTAS), ("marshall", B_MARSHALL),
]
BENCH_1969_EIGHT = [  # after Fortas's resignation, May 1969
    ("warren", B_WARREN), ("black", B_BLACK), ("douglas", B_DOUGLAS),
    ("harlan", B_HARLAN), ("brennan", B_BRENNAN), ("stewart", B_STEWART),
    ("white", B_WHITE), ("marshall", B_MARSHALL),
]

PUZZLES = [
    {
        "id": "cooper-v-aaron",
        "era": "The Warren Court · Special Term, August 1958",
        "caseTitle": "Cooper v. Aaron",
        "scdb": "1958-002",
        "question": ("May a school board postpone court-ordered desegregation because "
                     "of the violent resistance it has met?"),
        "answer": "no",
        "intro": ("Little Rock, one year after the 101st Airborne escorted nine Black "
                  "students into Central High. The school board asks for a "
                  "two-and-a-half-year pause, and the justices return from summer "
                  "recess to hear it before school opens."),
        "desc": ("Governor Orval Faubus called out the Arkansas National Guard to keep "
                 "the Little Rock Nine out of Central High; President Eisenhower sent "
                 "paratroopers to get them in. The year was ugly — mobs, threats, "
                 "students harassed in the halls. Now the board says chaos makes "
                 "integration impossible for now, and a federal judge has agreed. "
                 "Faubus and the legislature insist Brown binds only the parties to "
                 "it, not Arkansas. Thurgood Marshall answers that a right which "
                 "yields to a mob is no right at all."),
        "justices": BENCH_1958,
    },
    {
        "id": "baker-v-carr",
        "era": "The Warren Court · October Term 1961",
        "caseTitle": "Baker v. Carr",
        "scdb": "1961-051",
        "question": ("May federal courts hear a claim that a state's legislative "
                     "districts are so unequal they deny equal protection?"),
        "answer": "yes",
        "intro": ("Tennessee has not redrawn its legislative map since 1901. A vote in "
                  "rural Moore County now counts nineteen times a vote in Memphis, and "
                  "the legislature that benefits will never fix it. Memphis voters ask "
                  "a federal court to step in."),
        "desc": ("Charles Baker, a Republican county judge from suburban Memphis, sues "
                 "Tennessee's secretary of state over a legislature frozen in the "
                 "farm era: cities have grown for sixty years while their seats have "
                 "not. The lower court threw the case out under Colegrove v. Green, "
                 "where Frankfurter warned judges to stay out of the 'political "
                 "thicket' of districting. Solicitor General Archibald Cox argues "
                 "for the voters. The case has been argued twice and the conference "
                 "is split down the middle; whatever the Court says will reach every "
                 "statehouse in America."),
        "justices": BENCH_1961_NO_WHITTAKER,
    },
    {
        "id": "engel-v-vitale",
        "era": "The Warren Court · October Term 1961",
        "caseTitle": "Engel v. Vitale",
        "scdb": "1961-105",
        "question": ("May a public school open each day with a short, nondenominational "
                     "prayer written by state officials?"),
        "answer": "no",
        "intro": ("Every morning in New Hyde Park, Long Island, schoolchildren recite "
                  "twenty-two words composed by the New York Board of Regents: "
                  "'Almighty God, we acknowledge our dependence upon Thee...' Five "
                  "parents say the state has no business writing prayers."),
        "desc": ("Steven Engel, a Jewish father, joined four other parents — Jewish, "
                 "Unitarian, Ethical Culture, and one nonbeliever — to sue the school "
                 "board headed by William Vitale. The Regents' prayer is voluntary "
                 "and names no denomination, and New York's courts upheld it as "
                 "harmless civic piety. The parents answer that a government which "
                 "composes a prayer and leads children in it has established religion "
                 "as surely as any state church. Religious groups across the country "
                 "wait on the answer; a ruling either way will land in a thousand "
                 "classrooms."),
        "justices": BENCH_1961_SEVEN,
    },
    {
        "id": "sherbert-v-verner",
        "era": "The Warren Court · October Term 1962",
        "caseTitle": "Sherbert v. Verner",
        "scdb": "1962-150",
        "question": ("May a state deny unemployment benefits to a worker fired for "
                     "refusing to work on her Sabbath?"),
        "answer": "no",
        "intro": ("Adell Sherbert ran a loom in a Spartanburg textile mill for 35 "
                  "years. When the mill went to a six-day week, she would not work "
                  "Saturdays — her Sabbath as a Seventh-day Adventist — and South "
                  "Carolina says that makes her ineligible for benefits."),
        "desc": ("Fired for refusing Saturday shifts, Sherbert found every other mill "
                 "in town on the same schedule and applied for unemployment "
                 "compensation. The state commission ruled she had refused 'suitable "
                 "work' without good cause; South Carolina's Sunday-closing laws, "
                 "meanwhile, spare Sunday worshippers the same choice. Her lawyers "
                 "call the denial a fine on her faith. The state answers that it "
                 "forbids nothing — it simply declines to pay people who will not "
                 "take the jobs on offer. The Free Exercise Clause has rarely been "
                 "read to demand exemptions from neutral rules."),
        "justices": BENCH_GOLDBERG,
    },
    {
        "id": "reynolds-v-sims",
        "era": "The Warren Court · October Term 1963",
        "caseTitle": "Reynolds v. Sims",
        "scdb": "1963-140",
        "question": ("Must both houses of a state legislature be apportioned on the "
                     "basis of population?"),
        "answer": "yes",
        "intro": ("Two years after Baker v. Carr opened the courthouse door, six "
                  "states' legislatures arrive at once. Alabama's map dates from 1900: "
                  "Jefferson County, with 600,000 people, has one senator — the same as "
                  "a county of 15,000."),
        "desc": ("Alabama's constitution requires reapportionment every ten years; "
                 "the legislature has ignored it for sixty. Voters in Birmingham and "
                 "Mobile sued, and a federal court found the map flagrant. The "
                 "states reply with the federal analogy: the U.S. Senate gives "
                 "Wyoming and New York two seats apiece, so why may a state not "
                 "apportion one house by county? Cases from New York, Maryland, "
                 "Virginia, Delaware and Colorado — where voters approved their "
                 "unequal senate by referendum — are argued alongside. Whatever rule "
                 "emerges will redraw most statehouses in America."),
        "justices": BENCH_GOLDBERG,
    },
    {
        "id": "heart-of-atlanta-motel",
        "era": "The Warren Court · October Term 1964",
        "caseTitle": "Heart of Atlanta Motel v. United States",
        "scdb": "1964-017",
        "question": ("May Congress use its power over interstate commerce to forbid a "
                     "motel from turning away Black guests?"),
        "answer": "yes",
        "intro": ("Hours after President Johnson signed the Civil Rights Act of 1964, "
                  "the owner of a 216-room motel beside the interstate in downtown "
                  "Atlanta filed suit to keep refusing Black travelers. By December "
                  "the Act's fate is before the Court."),
        "desc": ("Moreton Rolleston Jr., the lawyer who owns the motel, argues his "
                 "own case: Congress may regulate commerce, not morality, and "
                 "forcing him to rent rooms is involuntary servitude. The Justice "
                 "Department, wary of the Fourteenth Amendment since the Civil "
                 "Rights Cases of 1883 gutted it, hangs Title II on the Commerce "
                 "Clause instead — three-quarters of the motel's guests come from "
                 "out of state, and segregation, it argues, chokes the national "
                 "travel economy. A companion case asks the same about Ollie's "
                 "Barbecue in Birmingham, which serves almost no travelers."),
        "justices": BENCH_GOLDBERG,
    },
    {
        "id": "harper-v-virginia",
        "era": "The Warren Court · October Term 1965",
        "caseTitle": "Harper v. Virginia Board of Elections",
        "scdb": "1965-079",
        "question": ("May a state require payment of a poll tax as a condition of "
                     "voting in state elections?"),
        "answer": "no",
        "intro": ("Virginia charges $1.50 a year to vote, payable six months before "
                  "the election, three years in arrears if you have lapsed. The "
                  "Twenty-fourth Amendment abolished the tax in federal elections "
                  "two years ago; state elections are another matter."),
        "desc": ("Annie Harper, a retired domestic worker from Fairfax County, cannot "
                 "afford Virginia's poll tax and sues to vote without paying it. Four "
                 "states still levy one. The Court upheld such taxes in 1937, and "
                 "Virginia notes that a modest fee applies to everyone regardless of "
                 "race. The challengers answer that the tax was adopted in 1902 to "
                 "clear Black and poor white voters from the rolls, and that it "
                 "works. May wealth have anything to do with the franchise — and "
                 "should the Court, rather than an amendment, say so?"),
        "justices": BENCH_FORTAS,
    },
    {
        "id": "south-carolina-v-katzenbach",
        "era": "The Warren Court · October Term 1965",
        "caseTitle": "South Carolina v. Katzenbach",
        "scdb": "1965-064",
        "question": ("May Congress require states with a history of voting "
                     "discrimination to get federal approval before changing their "
                     "election laws?"),
        "answer": "yes",
        "intro": ("Seven months after Selma, the Voting Rights Act of 1965 suspends "
                  "literacy tests across the Deep South and sends federal examiners "
                  "to register voters. South Carolina goes straight to the Supreme "
                  "Court to call the whole thing unconstitutional."),
        "desc": ("The Act covers any state that used a literacy test and had less "
                 "than half its adults voting in 1964 — six Southern states and part "
                 "of a seventh. None may change a voting rule without clearance from "
                 "the Attorney General or a federal court in Washington. South "
                 "Carolina, backed by five other states, says Congress has singled "
                 "out sovereign states for punishment and seized their power over "
                 "the ballot. Attorney General Nicholas Katzenbach answers that "
                 "ninety-five years of case-by-case litigation failed, and the "
                 "Fifteenth Amendment lets Congress enforce it."),
        "justices": BENCH_FORTAS,
    },
    {
        "id": "schmerber-v-california",
        "era": "The Warren Court · October Term 1965",
        "caseTitle": "Schmerber v. California",
        "scdb": "1965-132",
        "question": ("May police have a doctor draw blood from a drunk-driving suspect "
                     "over his objection and use the result against him?"),
        "answer": "yes",
        "intro": ("Armando Schmerber crashed his car in Los Angeles and was taken to "
                  "the hospital smelling of liquor. On a police officer's orders, and "
                  "over Schmerber's refusal on his lawyer's advice, a physician drew "
                  "his blood. It tested drunk."),
        "desc": ("The blood sample convicted Schmerber of driving under the "
                 "influence. His lawyers say the needle violated nearly everything: "
                 "due process, the privilege against self-incrimination, the right "
                 "to counsel, and the ban on unreasonable searches — a seizure not "
                 "of papers but of the body itself. California answers that alcohol "
                 "in the blood vanishes by the hour, that the procedure was routine "
                 "and painless, and that the Fifth Amendment protects what a man "
                 "says, not what his veins contain. The Court last faced the "
                 "question in 1957."),
        "justices": BENCH_FORTAS,
    },
    {
        "id": "walker-v-birmingham",
        "era": "The Warren Court · October Term 1966",
        "caseTitle": "Walker v. City of Birmingham",
        "scdb": "1966-128",
        "question": ("May marchers be punished for defying a court order against "
                     "demonstrating if they never asked a court to lift it?"),
        "answer": "yes",
        "intro": ("Good Friday, 1963. Martin Luther King Jr. and Ralph Abernathy lead "
                  "a march through Birmingham in open defiance of an injunction "
                  "obtained two days earlier by Bull Connor's city. King's cell "
                  "produced a famous letter; the contempt conviction produced this "
                  "case."),
        "desc": ("A state judge forbade the marches at the city's request, citing an "
                 "ordinance that let Connor deny parade permits at will. King, "
                 "Abernathy, Wyatt Tee Walker and five others marched anyway, served "
                 "five days for contempt, and appealed. Everyone agrees the ordinance "
                 "was probably unconstitutional. The question is procedure: the city "
                 "says a court order must be obeyed until a court overturns it, "
                 "however wrong it may be; the ministers say they could not wait on "
                 "Alabama's courts to vindicate a right the Constitution already "
                 "gave them."),
        "justices": BENCH_FORTAS,
    },
    {
        "id": "in-re-gault",
        "era": "The Warren Court · October Term 1966",
        "caseTitle": "In re Gault",
        "scdb": "1966-094",
        "question": ("Does a child facing juvenile court have a constitutional right "
                     "to notice of the charges, a lawyer, and the chance to confront "
                     "his accusers?"),
        "answer": "yes",
        "intro": ("Gerald Gault, fifteen, was picked up in Gila County, Arizona, for "
                  "a lewd phone call to a neighbor. An adult would have faced a $50 "
                  "fine or two months in jail. Gerald was committed to the state "
                  "industrial school until he turned twenty-one."),
        "desc": ("Gerald's parents learned of the hearing after it began; the "
                 "complaining neighbor never appeared; no witnesses were sworn, no "
                 "record kept, no lawyer present, and Arizona allows no appeal. "
                 "Juvenile courts have worked this way since 1899, on the theory "
                 "that the state acts as a kindly parent and formal rights would "
                 "only get in the way. Reformers say the theory has produced a "
                 "system with the punishments of criminal law and none of its "
                 "protections. The Court must decide whether the Bill of Rights is "
                 "for adults only."),
        "justices": BENCH_FORTAS,
    },
    {
        "id": "katz-v-united-states",
        "era": "The Warren Court · October Term 1967",
        "caseTitle": "Katz v. United States",
        "scdb": "1967-043",
        "question": ("Does the Fourth Amendment require a warrant before federal "
                     "agents bug a public telephone booth?"),
        "answer": "yes",
        "intro": ("Charles Katz, a Los Angeles bookmaker, placed his bets from a glass "
                  "phone booth on Sunset Boulevard. The FBI never entered it: agents "
                  "taped a microphone to its roof and recorded him from outside."),
        "desc": ("The recordings convicted Katz of transmitting wagering information "
                 "across state lines. Since Olmstead in 1928 the rule has been "
                 "physical: no trespass, no search, so a tap that touches no property "
                 "is outside the Fourth Amendment entirely. The government argues "
                 "that a booth is public and its glass walls let anyone see in. "
                 "Katz's lawyers answer that what he paid for when he shut the door "
                 "was not invisibility but privacy — and that the Amendment protects "
                 "people, not places. Electronic surveillance has arrived; has the "
                 "Constitution?"),
        "justices": BENCH_1967_NO_MARSHALL,
    },
    {
        "id": "duncan-v-louisiana",
        "era": "The Warren Court · October Term 1967",
        "caseTitle": "Duncan v. Louisiana",
        "scdb": "1967-122",
        "question": ("Must a state provide a jury trial to a defendant charged with a "
                     "serious crime?"),
        "answer": "yes",
        "intro": ("Gary Duncan, a 19-year-old Black man in Plaquemines Parish, "
                  "touched a white boy's arm while breaking up a roadside argument. "
                  "Charged with simple battery, he asked for a jury. Louisiana tries "
                  "crimes carrying up to two years without one."),
        "desc": ("Duncan got sixty days and a $150 fine from a judge sitting alone, "
                 "in a parish ruled by segregationist boss Leander Perez, where the "
                 "schools had just been ordered to integrate and the charge, his "
                 "lawyers say, was retaliation. The Sixth Amendment guarantees a "
                 "jury in federal court; whether the Fourteenth imposes the same "
                 "rule on the states has been argued since 1884. Louisiana calls "
                 "the offense petty. The Court has been applying the Bill of Rights "
                 "to the states one clause at a time; the jury is next."),
        "justices": BENCH_MARSHALL,
    },
    {
        "id": "jones-v-alfred-h-mayer",
        "era": "The Warren Court · October Term 1967",
        "caseTitle": "Jones v. Alfred H. Mayer Co.",
        "scdb": "1967-181",
        "question": ("May Congress forbid a private developer from refusing to sell a "
                     "home to a buyer because he is Black?"),
        "answer": "yes",
        "intro": ("Joseph Lee Jones and his wife Barbara tried to buy a house in "
                  "Paddock Woods, a new subdivision in St. Louis County. The developer "
                  "would not sell to a Black man. Their lawyers reach for a law "
                  "passed in 1866."),
        "desc": ("The Civil Rights Act of 1866 gives all citizens the same right 'as "
                 "is enjoyed by white citizens' to buy and sell property. For a "
                 "century courts read it to reach only state action — Jim Crow "
                 "statutes, not private bigotry. The Joneses argue the plain words "
                 "cover any seller, and that the Thirteenth Amendment, which bans "
                 "slavery and its badges, let Congress say so. The developer answers "
                 "that choosing one's buyer was never a badge of slavery. Meanwhile "
                 "Dr. King is murdered and Congress passes a Fair Housing Act."),
        "justices": BENCH_MARSHALL,
    },
    {
        "id": "shapiro-v-thompson",
        "era": "The Warren Court · October Term 1968",
        "caseTitle": "Shapiro v. Thompson",
        "scdb": "1968-081",
        "question": ("May a state deny welfare benefits to needy families who moved "
                     "there less than a year ago?"),
        "answer": "no",
        "intro": ("Vivian Thompson, nineteen, pregnant and the mother of a toddler, "
                  "moved from Boston to Hartford to be near her mother. Connecticut "
                  "turned down her application for aid: she had not lived in the "
                  "state for a year."),
        "desc": ("Forty states and the District of Columbia impose a one-year "
                 "residency requirement for public assistance, and Congress has "
                 "expressly permitted it. The states say the rule protects their "
                 "treasuries from an influx of the poor and ensures newcomers have "
                 "some stake in the community before drawing on it. Thompson's "
                 "lawyers, from the new federally funded legal-services movement, "
                 "answer that the Constitution guarantees a right to travel, and "
                 "that sorting citizens into old and new residents — the new left "
                 "hungry — denies equal protection. The case has been argued twice."),
        "justices": BENCH_MARSHALL,
    },
    {
        "id": "powell-v-mccormack",
        "era": "The Warren Court · October Term 1968",
        "caseTitle": "Powell v. McCormack",
        "scdb": "1968-127",
        "question": ("May the House of Representatives refuse to seat a duly elected "
                     "member who meets the Constitution's age, citizenship and "
                     "residency requirements?"),
        "answer": "no",
        "intro": ("Adam Clayton Powell Jr., Harlem's congressman for 22 years and "
                  "chairman of the Education and Labor Committee, was re-elected in "
                  "1966 by a landslide. In March 1967 the House voted 307 to 116 not "
                  "to let him in."),
        "desc": ("A House committee found that Powell had misused travel funds, kept "
                 "his wife on the payroll in Puerto Rico, and defied New York courts "
                 "in a defamation case. Rather than seat and then expel him, which "
                 "takes two-thirds, the House excluded him by majority vote. Powell "
                 "sued Speaker John McCormack; Harlem re-elected him twice, and the "
                 "new Congress has seated him with a fine. The House says each "
                 "chamber judges its own members and courts cannot second-guess it. "
                 "Powell says the Constitution lists three qualifications, and he "
                 "meets them all."),
        "justices": BENCH_1969_EIGHT,
    },
    {
        "id": "brandenburg-v-ohio",
        "era": "The Warren Court · October Term 1968",
        "caseTitle": "Brandenburg v. Ohio",
        "scdb": "1968-124",
        "question": ("May a state punish a speaker for advocating violence in general "
                     "terms, without inciting imminent lawless action?"),
        "answer": "no",
        "intro": ("A Cincinnati television crew films a Ku Klux Klan rally on a farm "
                  "outside town: a dozen hooded figures, a burning cross, and a leader "
                  "promising 'revengeance' if Washington keeps suppressing the white "
                  "race. Ohio convicts him under a 1919 syndicalism law."),
        "desc": ("Clarence Brandenburg, a Klan leader, invited the reporter himself; "
                 "the footage shows guns, slurs against Black Americans and Jews, "
                 "and talk of marching on Congress on the Fourth of July. He drew one "
                 "to ten years and a $1,000 fine for advocating 'the duty, necessity, "
                 "or propriety' of violence as a means of reform. The Court upheld an "
                 "identical California statute in 1927, over Brandeis's famous "
                 "protest. The ACLU argues his case; the question is what is left of "
                 "the clear-and-present-danger test after two decades of Cold War "
                 "prosecutions."),
        "justices": BENCH_1969_EIGHT,
    },
]
