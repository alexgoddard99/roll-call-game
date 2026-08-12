# The Court — Batch C: The Rehnquist Court (1986–2005).
# Votes are NOT written here — fetch_court.py pulls every justice's vote from
# the Supreme Court Database (justice-centered file) and verifies the rosters.

JUSTICES_EXTRA = {
    # key: (SCDB justiceName, display name, English Wikipedia page title)
    # --- the late-eighties bench (Texas v. Johnson, Cruzan) ---
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
}

# Shared blurbs — the 1989–90 bench (used by Texas v. Johnson and Cruzan).
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

# Shared blurbs — the stable nine of 1994–2005, the longest-serving bench in
# the Court's history (used by every other case in this batch).
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

_BENCH_88 = [(k, _B88[k]) for k in
             ["rehnquist88", "brennan", "white", "marshall", "blackmun",
              "stevens88", "oconnor88", "scalia88", "kennedy88"]]
_BENCH_NINE = [(k, _B[k]) for k in
               ["rehnquist", "stevens", "oconnor", "scalia", "kennedy",
                "souter", "thomas", "ginsburg", "breyer"]]

PUZZLES = [
    {
        "id": "texas-v-johnson",
        "era": "The Rehnquist Court · October Term 1988",
        "caseTitle": "Texas v. Johnson",
        "scdb": "1988-124",
        "question": "May the government punish burning the American flag as political protest?",
        "answer": "no",
        "intro": ("Outside the 1984 Republican National Convention in Dallas, a "
                  "demonstrator douses an American flag in kerosene and sets it alight. "
                  "Five years later the flag, the First Amendment, and the national "
                  "temper arrive at the Court together."),
        "desc": ("Gregory Lee Johnson burned the flag while protesters chanted "
                 "'America, the red, white, and blue, we spit on you.' Texas convicted "
                 "him under its venerated-objects law: a year in jail and a $2,000 "
                 "fine. No one was hurt; a great many were offended. Texas says the "
                 "flag is a unique national symbol the state may protect. Johnson says "
                 "torching it was pure political expression. Forty-eight states ban "
                 "flag desecration, and the veterans' groups are watching."),
        "justices": _BENCH_88,
    },
    {
        "id": "cruzan-v-missouri",
        "era": "The Rehnquist Court · October Term 1989",
        "caseTitle": "Cruzan v. Director, Missouri Dept. of Health",
        "scdb": "1989-126",
        "question": ("May a state demand clear proof of a patient's own wishes before "
                     "her family can end life support?"),
        "answer": "yes",
        "intro": ("In a Missouri state hospital, Nancy Cruzan has lain in a persistent "
                  "vegetative state for seven years since a car wreck. Her parents ask "
                  "to remove her feeding tube. The state answers: not without proof of "
                  "what Nancy herself wanted."),
        "desc": ("Nancy Cruzan was 25 when her car overturned on an icy road; her "
                 "brain went without oxygen for fourteen minutes, and her doctors say "
                 "she will never wake. Her parents, certain she would not want to live "
                 "this way, asked to withdraw the tube that feeds her. Missouri's "
                 "highest court refused: without 'clear and convincing evidence' of "
                 "Nancy's own wishes, the state's interest in preserving life "
                 "prevails. The first right-to-die case ever to reach the Court, with "
                 "medicine, religion, and the American family pressing in."),
        "justices": _BENCH_88,
    },
    {
        "id": "us-v-lopez",
        "era": "The Rehnquist Court · October Term 1994",
        "caseTitle": "United States v. Lopez",
        "scdb": "1994-051",
        "question": ("Does Congress's power over interstate commerce let it ban guns "
                     "near schools?"),
        "answer": "no",
        "intro": ("A San Antonio twelfth-grader walks into Edison High with a "
                  "concealed .38 and five bullets. He is charged not under Texas law "
                  "but under an act of Congress — and his lawyers ask what any of this "
                  "has to do with interstate commerce."),
        "desc": ("Alfonso Lopez Jr. was arrested under the federal Gun-Free School "
                 "Zones Act of 1990, which makes it a federal crime to possess a gun "
                 "within a thousand feet of a school. Since the New Deal, the Court "
                 "has never met a commerce-clause claim it wouldn't sustain — the "
                 "government argues that guns disrupt classrooms, classrooms produce "
                 "workers, and workers feed the national economy. Skeptics answer "
                 "that by that logic Congress could regulate anything at all, and the "
                 "word 'commerce' would mean nothing."),
        "justices": _BENCH_NINE,
    },
    {
        "id": "romer-v-evans",
        "era": "The Rehnquist Court · October Term 1995",
        "caseTitle": "Romer v. Evans",
        "scdb": "1995-053",
        "question": ("May a state constitution bar every law that protects gay people "
                     "from discrimination?"),
        "answer": "no",
        "intro": ("Denver, Boulder, and Aspen pass ordinances shielding gay residents "
                  "from discrimination. Colorado's voters answer with Amendment 2, "
                  "wiping the ordinances out statewide — and the fight moves from the "
                  "ballot box to the Court."),
        "desc": ("Passed by referendum in 1992, Amendment 2 repealed every local "
                 "gay-rights ordinance in Colorado and forbade the state or any city "
                 "from ever adopting another. Richard Evans, a Denver municipal "
                 "employee, sued Governor Roy Romer — who had campaigned against the "
                 "measure he was now bound to defend. Colorado says the amendment "
                 "merely denies 'special rights' and leaves gay citizens the same "
                 "protections as everyone else. The challengers say it fences one "
                 "class of people out of ordinary politics altogether."),
        "justices": _BENCH_NINE,
    },
    {
        "id": "clinton-v-jones",
        "era": "The Rehnquist Court · October Term 1996",
        "caseTitle": "Clinton v. Jones",
        "scdb": "1996-059",
        "question": ("Can a private lawsuit against a sitting president go forward "
                     "while he holds office?"),
        "answer": "yes",
        "intro": ("A former Arkansas state clerk sues the President of the United "
                  "States over what she says happened in a Little Rock hotel room in "
                  "1991. The White House asks the courts to wait until he leaves "
                  "office. She asks why a president is different."),
        "desc": ("Paula Corbin Jones alleges that Bill Clinton, while governor of "
                 "Arkansas, had a state trooper summon her to his suite at the "
                 "Excelsior Hotel and crudely propositioned her; she filed a federal "
                 "civil-rights suit in 1994 seeking $700,000. Clinton's lawyers argue "
                 "the presidency is a full-time constitutional office — that "
                 "litigation would distract the chief executive and invite a flood of "
                 "politically motivated suits. Nixon v. Fitzgerald immunized "
                 "presidents for official acts; this conduct, everyone agrees, was "
                 "nothing of the kind."),
        "justices": _BENCH_NINE,
    },
    {
        "id": "printz-v-us",
        "era": "The Rehnquist Court · October Term 1996",
        "caseTitle": "Printz v. United States",
        "scdb": "1996-095",
        "question": ("May Congress order local sheriffs to run background checks on "
                     "handgun buyers?"),
        "answer": "no",
        "intro": ("The Brady Bill is law, named for the press secretary shot beside "
                  "President Reagan. Until a national instant-check system comes "
                  "online, county sheriffs must vet every handgun sale — and two "
                  "Western sheriffs say Washington cannot draft them."),
        "desc": ("Jay Printz, sheriff of Ravalli County, Montana, and Richard Mack "
                 "of Graham County, Arizona, sued over the Brady Act's interim "
                 "command that local chief law-enforcement officers perform federal "
                 "background checks. The United States says it is a modest, temporary "
                 "duty in service of an urgent national problem. The sheriffs say the "
                 "Constitution created two governments, not one — and that Congress "
                 "may no more commandeer a county sheriff than a state legislature. "
                 "Nothing in the text answers it squarely; structure and history must."),
        "justices": _BENCH_NINE,
    },
    {
        "id": "boy-scouts-v-dale",
        "era": "The Rehnquist Court · October Term 1999",
        "caseTitle": "Boy Scouts of America v. Dale",
        "scdb": "1999-085",
        "question": ("Does the First Amendment let the Boy Scouts expel a gay "
                     "assistant scoutmaster?"),
        "answer": "yes",
        "intro": ("James Dale is an Eagle Scout with a decade of merit badges — until "
                  "a newspaper photo identifies him as a leader of a gay campus group, "
                  "and the Boy Scouts revoke his membership by letter. New Jersey law "
                  "says they can't."),
        "desc": ("Dale, an assistant scoutmaster in Monmouth Council, was expelled in "
                 "1990 after the Scouts learned he was co-president of the Rutgers "
                 "gay and lesbian student alliance. He sued under New Jersey's "
                 "public-accommodations law, and the state's highest court ordered "
                 "him reinstated. The Scouts — six million strong, chartered by "
                 "Congress — say homosexuality contradicts the oath's promise to be "
                 "'morally straight,' and that forcing them to keep Dale rewrites "
                 "their message. Dale says a scout troop is not a debating society, "
                 "and discrimination is not speech."),
        "justices": _BENCH_NINE,
    },
    {
        "id": "atkins-v-virginia",
        "era": "The Rehnquist Court · October Term 2001",
        "caseTitle": "Atkins v. Virginia",
        "scdb": "2001-070",
        "question": "May a state execute a murderer who is intellectually disabled?",
        "answer": "no",
        "intro": ("Daryl Atkins sits on Virginia's death row for the abduction and "
                  "murder of a young airman. A psychologist puts his IQ at 59. "
                  "Thirteen years ago the Court let such executions proceed — since "
                  "then, state after state has banned them."),
        "desc": ("Atkins and an accomplice abducted airman Eric Nesbitt outside a "
                 "convenience store, forced him to withdraw cash from an ATM, and "
                 "shot him eight times. His guilt is not before the Court; his mind "
                 "is. In 1989 only two death-penalty states spared mentally retarded "
                 "offenders, and the Court found no national consensus against the "
                 "practice. Now eighteen do. The Eighth Amendment turns on 'evolving "
                 "standards of decency' — and the justices must decide whether the "
                 "standards have evolved, and who gets to say so."),
        "justices": _BENCH_NINE,
    },
    {
        "id": "lawrence-v-texas",
        "era": "The Rehnquist Court · October Term 2002",
        "caseTitle": "Lawrence v. Texas",
        "scdb": "2002-083",
        "question": ("May a state make it a crime for two adults of the same sex to "
                     "have sex in private?"),
        "answer": "no",
        "intro": ("Houston police, answering a false report of an armed intruder, "
                  "enter John Lawrence's apartment and arrest him and Tyron Garner "
                  "under the Texas Homosexual Conduct law. The fine is $200. The "
                  "question reaches back seventeen years, to Bowers v. Hardwick."),
        "desc": ("Lawrence and Garner spent a night in jail for conduct that was "
                 "legal for any opposite-sex couple in Texas. In 1986 the Court "
                 "upheld Georgia's sodomy law, scoffing at the claimed right as "
                 "'facetious'; since then the number of states with such laws has "
                 "fallen from twenty-five to thirteen, and only four enforce them "
                 "against homosexuals alone. Texas says the law expresses its "
                 "citizens' moral judgment, which has always been reason enough. The "
                 "challengers say the Constitution leaves adults' private lives to "
                 "adults — and asks the Court to say Bowers was wrong."),
        "justices": _BENCH_NINE,
    },
    {
        "id": "kelo-v-new-london",
        "era": "The Rehnquist Court · October Term 2004",
        "caseTitle": "Kelo v. City of New London",
        "scdb": "2004-069",
        "question": ("May a city take homes by eminent domain and hand the land to a "
                     "private developer?"),
        "answer": "yes",
        "intro": ("Susette Kelo's little pink house overlooks the Thames River in New "
                  "London, Connecticut — squarely inside ninety acres the struggling "
                  "city has promised to a private redevelopment plan anchored by a "
                  "gleaming new Pfizer research campus."),
        "desc": ("New London, its Navy base closed and its unemployment double the "
                 "state's, approved a plan for offices, upscale housing, and a hotel "
                 "beside Pfizer's new headquarters — and condemned the Fort Trumbull "
                 "homes in the way. Kelo, a nurse, and her neighbors, including a "
                 "woman born in her house in 1918, refuse to sell. The Fifth "
                 "Amendment permits takings only for 'public use.' The city says "
                 "jobs and taxes are use enough; the homeowners say that reading "
                 "lets any government trade anyone's home to a richer owner."),
        "justices": _BENCH_NINE,
    },
]
