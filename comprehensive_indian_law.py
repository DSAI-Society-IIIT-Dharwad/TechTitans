"""
COMPREHENSIVE Indian Legal Knowledge Base
Includes extensive Constitution, IPC, CrPC, and major Acts
"""

import json
from pathlib import Path


# COMPREHENSIVE Indian Legal Knowledge
COMPREHENSIVE_KNOWLEDGE = [
    # PART III - FUNDAMENTAL RIGHTS (Detailed)
    {
        "title": "Article 12 - Definition of State",
        "category": "Constitution - Fundamental Rights",
        "content": """Article 12 defines "State" for the purposes of Part III of the Constitution.

The term 'State' includes:
1. The Government and Parliament of India
2. The Government and Legislature of each State
3. All local authorities (Municipal Corporations, Municipalities, Panchayats, etc.)
4. All other authorities within the territory of India or under the control of Government of India

This definition is crucial because Fundamental Rights (Articles 12-35) can be enforced ONLY against the State, not against private individuals.

Key Points:
• State includes legislative, executive, and judicial organs
• Also includes statutory bodies, public corporations, and government companies
• Private bodies performing public functions may be considered 'State'
• Right to enforce Fundamental Rights is against the State only

Examples of 'State' under Article 12:
- Indian Railways, Life Insurance Corporation (LIC)
- All government departments and ministries
- State-owned companies and corporations
- Universities established by statute
- BCCI (Board of Control for Cricket in India) - debatable

This is one of the most important articles as it determines the scope of Fundamental Rights enforcement.""",
        "url": "https://www.india.gov.in/my-government/constitution-india",
        "metadata": {"part": "III", "article": "12", "act": "Constitution of India"}
    },
    
    {
        "title": "Article 13 - Laws Inconsistent with Fundamental Rights",
        "category": "Constitution - Fundamental Rights",
        "content": """Article 13 declares that any law inconsistent with Fundamental Rights shall be void.

Key Provisions:

1. All pre-Constitution laws inconsistent with Part III are void to the extent of inconsistency
2. The State shall not make any law which takes away or abridges Fundamental Rights
3. Any law made in contravention of Article 13(2) shall be void

Definition of 'Law':
• Includes any ordinance, order, bye-law, rule, regulation, notification, custom or usage
• Judicial decisions are also 'law' under Article 13

Doctrine of Prospective Overruling:
• Courts can declare a law unconstitutional but give it prospective effect
• Past actions under the law remain valid

Important Supreme Court Cases:
• Kesavananda Bharati v. State of Kerala (1973) - Basic Structure Doctrine
• Minerva Mills v. Union of India (1980) - Parliament cannot destroy basic structure

Article 13 does NOT apply to Constitutional Amendments:
• Amendments under Article 368 are not 'laws' under Article 13
• But amendments cannot violate basic structure (Kesavananda Bharati)

This article is the guardian of Fundamental Rights and ensures judicial review of legislation.""",
        "url": "https://www.india.gov.in/my-government/constitution-india",
        "metadata": {"part": "III", "article": "13", "act": "Constitution of India"}
    },
    
    {
        "title": "Article 15 - Prohibition of Discrimination",
        "category": "Constitution - Fundamental Rights", 
        "content": """Article 15 prohibits discrimination on grounds of religion, race, caste, sex or place of birth.

Clause 1: The State shall not discriminate against any citizen on grounds only of:
• Religion
• Race  
• Caste
• Sex
• Place of birth

Clause 2: No citizen shall be subjected to any disability, restriction or condition with regard to:
• Access to shops, public restaurants, hotels
• Use of wells, tanks, bathing ghats, roads
• Places of public resort maintained by State or dedicated to public use

Clause 3: Nothing shall prevent the State from making special provisions for:
• Women and children

Clause 4: Special provisions for advancement of:
• Socially and educationally backward classes (SEBCs)
• Scheduled Castes (SCs) and Scheduled Tribes (STs)

Clause 5 (Added by 93rd Amendment, 2005):
• State can make special provisions for admission of SEBCs, SCs, STs in:
  - Educational institutions (including private aided/unaided)
  - Except minority educational institutions under Article 30(1)

Clause 6 (Added by 103rd Amendment, 2019):
• Economically Weaker Sections (EWS) can get up to 10% reservation
• In addition to existing SC/ST/OBC reservations
• In educational institutions and government jobs

Important Points:
• Article 15 applies to both State and private individuals (Clause 2)
• Reasonable classification is allowed, but discrimination is not
• Gender discrimination includes discrimination against transgenders
• This is the basis for reservation policy in India

Exceptions:
• Special provisions for women, children, backward classes are allowed
• These are protective discrimination, not violations

Related Articles:
• Article 16 - Equality in public employment
• Article 14 - Equality before law""",
        "url": "https://www.india.gov.in/my-government/constitution-india",
        "metadata": {"part": "III", "article": "15", "act": "Constitution of India"}
    },

    {
        "title": "Article 16 - Equality of Opportunity in Public Employment",
        "category": "Constitution - Fundamental Rights",
        "content": """Article 16 provides for equality of opportunity in matters of public employment.

Clause 1: Equality of opportunity for all citizens in matters relating to employment or appointment to any office under the State.

Clause 2: No citizen shall be discriminated in employment on grounds of:
• Religion, race, caste, sex, descent
• Place of birth, residence or any of them

Clause 3: Parliament can prescribe residence requirement for certain posts.

Clause 4: RESERVATION - Nothing shall prevent the State from making provisions for:
• Reservation of appointments or posts in favor of any backward class of citizens
• Which in the opinion of the State is not adequately represented in services

Clause 4A (Added by 77th Amendment): Reservation in promotions for SCs and STs.

Clause 4B (Added by 81st Amendment): Unfilled reserved vacancies can be carried forward as a separate category without 50% ceiling limit.

Clause 5: Religious institutions exemption:
• Laws requiring residence or knowledge of particular religion for employment in religious institutions

Clause 6 (Added by 103rd Amendment, 2019): 
• Up to 10% reservation for Economically Weaker Sections (EWS)
• In addition to existing SC/ST/OBC reservations

50% Ceiling Rule (Indra Sawhney Case, 1992):
• Total reservation cannot exceed 50% of posts
• Exceptions possible in extraordinary circumstances
• Creamy layer concept introduced for OBCs

Key Supreme Court Judgments:
• M.R. Balaji v. State of Mysore (1963) - 50% limit
• Indra Sawhney v. Union of India (1992) - Creamy layer
• Jarnail Singh v. Lacchmi Narain Gupta (2018) - No creamy layer for SC/ST

Backward Classes Definition:
• Socially and educationally backward
• Not adequately represented in services
• Determined by various commissions (Mandal Commission, etc.)

Important: This article applies ONLY to public employment under the State, not private sector.""",
        "url": "https://www.india.gov.in/my-government/constitution-india",
        "metadata": {"part": "III", "article": "16", "act": "Constitution of India"}
    },

    {
        "title": "Article 17 - Abolition of Untouchability",
        "category": "Constitution - Fundamental Rights",
        "content": """Article 17 abolishes 'untouchability' and forbids its practice in any form.

Main Provision:
• "Untouchability" is abolished
• Its practice in any form is forbidden
• Enforcement of any disability arising out of untouchability shall be an offense punishable by law

What is Untouchability?
• Social practice of discriminating against certain castes (mainly Dalits/SCs)
• Denying access to public places, temples, wells, schools
• Treating them as 'untouchable' or polluting
• Any disability, restriction or humiliation based on birth in certain castes

Implementing Legislation:
Protection of Civil Rights Act, 1955 (formerly Untouchability Offenses Act, 1955)

Offenses under Civil Rights Act:
1. Preventing access to public worship places
2. Refusing admission to hospitals, educational institutions
3. Refusing to sell goods or render services
4. Insulting a person on grounds of untouchability
5. Preventing access to water sources, shops, public places

Punishment:
• Imprisonment: Minimum 1 month, maximum 6 months
• Fine: Minimum ₹100, maximum ₹500
• For subsequent offenses: Minimum 1 year, maximum 1 year
• Some offenses carry up to 2 years imprisonment

Scheduled Castes and Scheduled Tribes (Prevention of Atrocities) Act, 1989:
• More stringent law to prevent atrocities against SCs/STs
• Covers serious crimes like murder, rape, assault, etc.
• Stricter punishments and special courts

Important Features:
• This is the ONLY Fundamental Right that is directly enforceable against private individuals
• Both State and private persons can be prosecuted
• The practice is a criminal offense, not just unconstitutional

Social Impact:
• Aimed at eradicating caste-based discrimination
• Ensures social equality and human dignity
• Complements Articles 14, 15, 16

Note: Despite constitutional abolition, untouchability practices persist in some parts of India. Strict enforcement and social awareness are needed.""",
        "url": "https://www.india.gov.in/my-government/constitution-india",
        "metadata": {"part": "III", "article": "17", "act": "Constitution of India"}
    },

    {
        "title": "Article 21 - Protection of Life and Personal Liberty",
        "category": "Constitution - Fundamental Rights",
        "content": """Article 21 is the MOST IMPORTANT Fundamental Right - Protection of Life and Personal Liberty.

Original Text:
"No person shall be deprived of his life or personal liberty except according to procedure established by law."

Expanded Scope (Through Judicial Interpretation):

Right to Life includes:
1. Right to Live with Human Dignity
2. Right to Livelihood
3. Right to Food, Water and Shelter
4. Right to Clean Environment
5. Right to Healthcare and Medical Treatment
6. Right to Education (now Article 21A)
7. Right to Privacy (K.S. Puttaswamy judgment, 2017)
8. Right to Sleep
9. Right to Die with Dignity (Passive Euthanasia - Aruna Shanbaug case)

Personal Liberty includes:
1. Right to travel abroad
2. Right to movement within India
3. Right against solitary confinement
4. Right against handcuffing
5. Right against delayed execution (prolonged death row)
6. Right to speedy trial
7. Right to Legal Aid (Hussainara Khatoon case)
8. Right to Fair Trial
9. Protection against custodial torture/death

Procedure Established by Law:
• Law must be valid, just, fair and reasonable
• Not arbitrary or fanciful
• Must comply with principles of natural justice
• Maneka Gandhi v. Union of India (1978) - landmark case

Limitations:
Article 21 can be restricted during National Emergency (Article 352), but even then:
• Restriction must be reasonable
• Cannot be arbitrary or excessive
• Right to life cannot be suspended even in emergency

Protection Against State Action:
• Applies mainly against State action
• But also protects against private violence (State has duty to protect)

Right to Privacy (2017):
• Declared a Fundamental Right under Article 21
• Protects informational, spatial, and decisional privacy
• Led to Aadhaar judgment, decriminalization of Section 377

This article is the cornerstone of human rights protection in India and has the widest scope.""",
        "url": "https://www.india.gov.in/my-government/constitution-india",
        "metadata": {"part": "III", "article": "21", "act": "Constitution of India"}
    },

    {
        "title": "Article 21A - Right to Education",
        "category": "Constitution - Fundamental Rights",
        "content": """Article 21A provides Free and Compulsory Education to all children.

Inserted by: 86th Constitutional Amendment Act, 2002

Provision:
"The State shall provide free and compulsory education to all children of the age of 6 to 14 years in such manner as the State may, by law, determine."

Implementing Legislation:
Right of Children to Free and Compulsory Education (RTE) Act, 2009

Key Features of RTE Act:

1. Free Education:
   • No child shall be liable to pay any fee or charges
   • Prevents from completing elementary education

2. Compulsory Education:
   • Appropriate Government has duty to provide education
   • Parents have duty to admit child to school

3. Quality Standards:
   • Prescribed curriculum, teacher qualifications
   • Pupil-teacher ratio (1:30)
   • Infrastructure norms (playgrounds, libraries, etc.)

4. No Detention Policy:
   • No child shall be detained in any class till Class 8
   • Continuous and comprehensive evaluation (CCE)

5. 25% Reservation:
   • Private schools must reserve 25% seats for disadvantaged/weaker sections
   • Government reimburses fees

6. Age-Appropriate Admission:
   • Children can be admitted to age-appropriate class
   • Special training to catch up

7. No Capitation Fee:
   • Schools cannot collect capitation fees
   • Cannot conduct screening during admission

Scope:
• Applies to children aged 6-14 years
• Elementary education (Class 1 to Class 8)
• Both government and private schools

Excluded:
• Minority institutions (partially exempt)
• Pre-primary education (below age 6)
• Secondary education (above age 14)

Penalties:
• Violation attracts fine up to ₹1 lakh
• Repeated violations can lead to school closure

Challenges:
• Implementation gaps in many states
• Quality of education concerns
• Infrastructure deficiencies
• Teacher shortage

86th Amendment also added:
• Article 45 - Early Childhood Care and Education (ECCE) for children below 6 years
• Article 51A(k) - Fundamental Duty of parents to provide education

This right ensures that no child is denied education due to poverty or social backwardness.""",
        "url": "https://www.india.gov.in/my-government/constitution-india",
        "metadata": {"part": "III", "article": "21A", "act": "Constitution of India"}
    },

    {
        "title": "Article 22 - Protection Against Arrest and Detention",
        "category": "Constitution - Fundamental Rights",
        "content": """Article 22 provides safeguards against arbitrary arrest and detention.

PART A - Ordinary Arrest (Clauses 1 & 2):

Clause 1 - Rights of Arrested Person:
1. Right to be informed of grounds of arrest
2. Right to consult and be defended by legal practitioner of choice
3. Right to be produced before magistrate within 24 hours (excluding travel time)

Clause 2 - Prohibition:
• No detained person can be kept in custody beyond 24 hours without magistrate's authority

These rights DO NOT apply to:
• Enemy aliens
• Persons arrested under preventive detention laws

PART B - Preventive Detention (Clauses 3-7):

What is Preventive Detention?
• Detention without trial to prevent future misconduct
• Person detained BEFORE committing any crime (preventive, not punitive)

Safeguards:

Clause 3:
• Parliament can prescribe maximum detention period
• Grounds of detention must be communicated
• Person must be given earliest opportunity to make representation

Clause 4:
• No detention beyond 3 months unless:
  - Advisory Board (of High Court Judges) reports sufficient cause
  - Or Parliament by law prescribes longer period

Clause 5:
• Detaining authority must communicate grounds within 5 days (15 days in special circumstances)
• Person has right to make representation

Clause 6:
• Maximum period of detention can be prescribed by Parliament

Clause 7:
• Parliament can prescribe circumstances and class of cases where:
  - Grounds need not be disclosed
  - Representation may not be considered

Preventive Detention Laws:

Central Laws:
• National Security Act (NSA), 1980
• Conservation of Foreign Exchange and Prevention of Smuggling Activities Act (COFEPOSA), 1974
• Prevention of Illicit Traffic in Narcotic Drugs and Psychotropic Substances Act (PITNDPS), 1988

State Laws:
• Various states have their own preventive detention laws

Criticism:
• Violates presumption of innocence
• Can be misused by governments
• Detention without trial is against natural justice

Judicial Review:
• Courts can review whether detention is legal and constitutional
• Can examine if grounds are sufficient and detention is necessary

Important Cases:
• A.K. Gopalan v. State of Madras (1950)
• Maneka Gandhi v. Union of India (1978) - expanded scope of Article 22

Note: Preventive detention is a necessary evil for national security, but must be used sparingly and with strict safeguards.""",
        "url": "https://www.india.gov.in/my-government/constitution-india",
        "metadata": {"part": "III", "article": "22", "act": "Constitution of India"}
    },

    # CRIMINAL LAW - Detailed IPC Sections
    {
        "title": "Section 300-304 IPC - Murder and Culpable Homicide",
        "category": "Criminal Law - IPC",
        "content": """Sections 300-304 deal with Murder and Culpable Homicide Not Amounting to Murder.

SECTION 300 - MURDER:

Culpable homicide is murder if:
1. Act is done with intention of causing death, OR
2. Act is done with intention of causing such bodily injury as:
   - The offender knows is likely to cause death, OR
3. Act is done with intention of causing bodily injury sufficient in ordinary course to cause death, OR  
4. Person committing act knows it is so imminently dangerous that it must in all probability cause death

Exception 1 - Grave and Sudden Provocation:
• If provocation causes loss of self-control
• Not if provoked by lawful act
• Not if provocation sought by offender
• Reduces murder to culpable homicide not amounting to murder

Exception 2 - Private Defense:
• Death caused in good faith exercise of right of private defense
• Exceeding powers given by law

Exception 3 - Public Servant:
• Public servant causing death in advancement of public justice
• Acting in good faith, believing it lawful

Exception 4 - Sudden Fight:
• Death caused in sudden fight in heat of passion
• Without premeditation
• Not if undue advantage taken

Exception 5 - Consent:
• Person above 18 years gives consent to suffer death
• Death caused without consent being obtained by threat, etc.

SECTION 301 - Culpable Homicide by Causing Death of Person Other than Person whose Death was Intended:
• If person doing act knows likely to cause death
• Commits culpable homicide
• Though intention was to cause death of another

SECTION 302 - PUNISHMENT FOR MURDER:

Whoever commits murder shall be punished with:
• Death penalty, OR
• Imprisonment for life
• Also liable to fine

Aggravating Circumstances (for death penalty):
1. Socially abhorrent crimes (dowry death, honor killing)
2. Murder of public servant
3. Murder of child, woman, scheduled caste member
4. Terrorist activities
5. Anti-social or socially abhorrent nature

Mitigating Circumstances (against death penalty):
1. Young age
2. No criminal record
3. Possibility of reformation
4. Mental instability
5. Provocation

Rarest of Rare Doctrine (Bachan Singh v. State of Punjab, 1980):
• Death penalty only in rarest of rare cases
• When alternative option is unquestionably foreclosed

SECTION 303 - Punishment for Murder by Life Convict:
• If person under sentence of life imprisonment commits murder
• Shall be punished with death
[NOTE: Section 303 struck down by Supreme Court in Mithu v. State of Punjab (1983) as unconstitutional]

SECTION 304 - CULPABLE HOMICIDE NOT AMOUNTING TO MURDER:

Part I - If knowledge that act likely to cause death:
• Imprisonment up to life
• Or imprisonment up to 10 years
• Also fine

Part II - If knowledge that act likely to cause death but without intention:
• Imprisonment up to 10 years
• Or fine
• Or both

Difference Between Murder and Culpable Homicide:

Murder (Section 300):
• Intention to cause death
• Or knowledge act imminently dangerous and likely to cause death
• More serious

Culpable Homicide Not Amounting to Murder (Section 304):
• Knowledge that act may cause death but no intention
• Or within exceptions to Section 300
• Less serious

Key Cases:
• K.M. Nanavati v. State of Maharashtra (1962) - Provocation defense
• Bachan Singh v. State of Punjab (1980) - Rarest of rare
• Machhi Singh v. State of Punjab (1983) - Aggravating circumstances

This is one of the most important sections of IPC dealing with serious crimes.""",
        "url": "https://www.indiacode.nic.in/ipc",
        "metadata": {"section": "300-304", "act": "Indian Penal Code, 1860"}
    },

{
        "title": "Section 354 IPC - Assault or Criminal Force with Intent to Outrage Modesty",
        "category": "Criminal Law - Women Protection",
        "content": """Section 354 punishes assault or criminal force to woman with intent to outrage her modesty.

SECTION 354 - Main Provision:

Whoever assaults or uses criminal force to any woman:
• Intending to outrage her modesty, OR
• Knowing it likely to outrage her modesty

Punishment:
• Imprisonment: 1 to 5 years
• Fine
• Or both

What Constitutes 'Modesty':
• Modesty is an attribute of female gender
• Includes sense of womanly propriety and dignity
• Physical contact not always necessary
• Even gestures can outrage modesty
• Victim's feeling and societal standards both considered

Examples:
• Touching private parts
• Kissing without consent
• Removing clothes
• Taking photographs/videos without consent
• Making lewd gestures
• Stalking with sexual intent

Criminal Law Amendment, 2013 Added:

SECTION 354A - SEXUAL HARASSMENT:

Punishes:
1. Physical contact and advances with sexual intent
2. Demand or request for sexual favors
3. Making sexually colored remarks
4. Showing pornography
5. Any other unwelcome physical, verbal or non-verbal conduct of sexual nature

Punishment:
• Imprisonment: 1 to 3 years
• Or fine
• Or both

SECTION 354B - ASSAULT OR USE OF CRIMINAL FORCE WITH INTENT TO DISROBE:

Any person who assaults or uses criminal force to any woman:
• With intent to disrobe her
• Compels her to be naked

Punishment:
• Imprisonment: 3 to 7 years
• Also fine

SECTION 354C - VOYEURISM:

Watching or capturing image of woman:
• Engaged in private act
• Where she would not expect to be observed
• Without her consent

Punishment:
• First conviction: 1 to 3 years + fine
• Subsequent conviction: 3 to 7 years + fine

SECTION 354D - STALKING:

Following woman or contacting/attempting to contact her:
• Despite clear indication of disinterest
• To foster personal interaction
• Monitoring use of internet, email or electronic communication

Punishment:
• First conviction: Up to 3 years + fine
• Subsequent conviction: Up to 5 years + fine

Important Points:

1. Cognizance:
• Cognizable offense (police can arrest without warrant)
• Non-bailable
• Triable by Magistrate

2. Gender:
• Only woman can be victim under Section 354
• But 354A applies to both men and women as victims

3. Consent:
• Key element is lack of consent or use of force
• Consent obtained by fraud is not valid consent

4. Workplace:
• Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013 provides additional protection

5. Evidence:
• Medical evidence helpful but not mandatory
• Victim's testimony is sufficient if credible
• Corroboration not always required

Related Sections:
• Section 509 - Word, gesture or act intended to insult modesty of woman
• Section 376 - Rape
• Section 498A - Cruelty by husband

Landmark Cases:
• Vishaka v. State of Rajasthan (1997) - Sexual harassment guidelines
• Rupan Deol Bajaj v. KPS Gill (1995) - Bottom slapping case
• State of Punjab v. Major Singh (1967) - Definition of modesty

These sections aim to protect women's dignity, privacy and bodily autonomy in all spheres.""",
        "url": "https://www.indiacode.nic.in/ipc",
        "metadata": {"section": "354", "act": "Indian Penal Code, 1860"}
    },

    {
        "title": "Section 506-507 IPC - Criminal Intimidation",
        "category": "Criminal Law - IPC",
        "content": """Sections 506-507 deal with Criminal Intimidation.

SECTION 506 - PUNISHMENT FOR CRIMINAL INTIMIDATION:

Whoever commits criminal intimidation shall be punished with:
• Imprisonment up to 2 years
• Or fine
• Or both

If threat is to cause death or grievous hurt:
• Or to cause destruction of property by fire
• Or to impute unchastity to a woman
• Or to cause offense punishable with 7 years+ imprisonment

Then punishment:
• Imprisonment up to 7 years
• Or fine
• Or both

What is Criminal Intimidation (Section 503)?
Threatening any person with injury to:
• His person, reputation or property, OR
• Person or reputation of anyone he is interested in

With intent to:
• Cause alarm
• Cause person to do any act he is not legally bound to do
• Omit to do any act he is legally entitled to do

Elements of Criminal Intimidation:
1. Threat of injury to person, reputation or property
2. Intent to cause alarm or to coerce
3. Knowledge that such threat will likely cause alarm

Types of Threats Covered:
• Physical harm (assault, murder)
• Damage to reputation (defamation)
• Destruction of property
• False criminal accusation
• Social boycott

What is NOT Criminal Intimidation:
• Lawful exercise of legal right
• Bonafide advice
• Warning to prevent illegal act
• Reasonable apprehension

SECTION 507 - CRIMINAL INTIMIDATION BY ANONYMOUS COMMUNICATION:

If criminal intimidation is:
• By anonymous communication, OR
• Having concealed name or abode of person

Punishment:
• Imprisonment up to 2 years
• In addition to punishment under Section 506

Examples:
• Threatening letters without signature
• Anonymous phone calls threatening harm
• Messages from fake social media accounts
• Emails from untraceable IDs

Digital Era Additions:
• Cyberbullying often involves Section 506
• Threatening messages on WhatsApp, Facebook
• Doxing (publishing private information with intent to threaten)
• Covered under IT Act, 2000 also

Important Points:

1. Cognizability:
• Section 506 (2 years): Non-cognizable
• Section 506 (7 years): Cognizable

2. Bail:
• 2-year offense: Bailable
• 7-year offense: Non-bailable

3. Intention:
• Mere threat not enough
• Intent to cause alarm must be proven
• But not necessary that victim was actually alarmed

4. Anonymous Communication:
• Need not always be written
• Can be oral (phone call with concealed number)
• Identity concealment is key

5. Relationship with Other Offenses:
• Often charged with assault (Section 351)
• With extortion (Section 384)
• With defamation (Section 499)
• With cybercrime (Section 66A IT Act - now struck down)

Related Sections:
• Section 503 - Definition of criminal intimidation
• Section 504 - Intentional insult with intent to provoke breach of peace
• Section 384 - Extortion
• Section 385 - Putting person in fear of injury to commit extortion

Defenses:
• Threat was not serious
• No intent to cause alarm
• Lawful exercise of right
• Self-defense

Practical Applications:
• Domestic violence cases
• Workplace harassment
• Loan recovery threats
• Political vendetta
• Online harassment

Burden of Proof:
• Prosecution must prove threat was made
• With intent to cause alarm or coerce
• Beyond reasonable doubt

These sections protect personal liberty and security by criminalizing threats and intimidation.""",
        "url": "https://www.indiacode.nic.in/ipc",
        "metadata": {"section": "506-507", "act": "Indian Penal Code, 1860"}
    },

    # PROCEDURES
    {
        "title": "How to File FIR (First Information Report)",
        "category": "Legal Procedures",
        "content": """Complete Guide to Filing FIR (First Information Report)

What is FIR?
• First Information Report - First complaint received by police about cognizable offense
• Registered under Section 154 of CrPC
• Initiates criminal investigation
• Legal document that can be used as evidence

STEP-BY-STEP PROCEDURE:

Step 1: Identify the Offense
• Check if offense is cognizable (police can arrest without warrant)
• Cognizable offenses: Murder, rape, theft, robbery, dowry death, etc.
• Non-cognizable offenses: Assault without weapon, defamation, cheating below certain amount

Step 2: Go to Police Station
• Visit police station with jurisdiction over area where offense occurred
• Can file at any police station if offense has inter-state implications
• In case of cognizable offense, police MUST register FIR

Step 3: Provide Information
Oral or Written:
• Can give information orally to police officer
• Officer will reduce it to writing
• Or can submit written complaint

Information to Include:
1. Your name, address, contact details
2. Date, time and place of incident
3. Detailed description of incident
4. Name/description of accused person(s)
5. Names of witnesses (if any)
6. Details of injuries/loss/damage
7. Any evidence you have

Step 4: Reading and Signing
• Police officer will read back the FIR to you
• Verify all details are correct
• Sign the FIR
• Officer will also sign

Step 5: Get FIR Copy
• You are entitled to FREE copy of FIR
• Police must provide copy without delay
• FIR will have unique number (FIR number)

IMPORTANT RIGHTS:

1. Right to Lodge FIR:
• Police CANNOT refuse to register FIR for cognizable offense
• If refused, can approach Superintendent of Police or file complaint to Judicial Magistrate

2. Zero FIR:
• Can file FIR at ANY police station
• Even if they don't have jurisdiction
• They must register and transfer to appropriate station

3. Online FIR:
• Many states allow online FIR registration
• Check your state police website
• Useful for minor offenses, lost articles

4. FIR by Woman:
• Woman can record statement at her residence
• If she is unable to visit police station due to assault/rape
• Female police officer should record statement

WHAT HAPPENS AFTER FIR?

1. Investigation Begins:
• Police starts investigation
• Officer-in-charge assigns investigating officer
• Investigation must be completed within reasonable time

2. Status Updates:
• You can check status of FIR online (many states)
• Visit police station for updates
• Right to know progress under RTI Act

3. Charge Sheet:
• If evidence found, police files charge sheet (within 60-90 days)
• If no evidence, files closure report
• You can oppose closure report in court

4. Court Trial:
• After charge sheet, case goes to court
• You may be called as witness
• Keep all documents and evidence safe

SPECIAL TYPES OF FIR:

1. Dying Declaration FIR:
• Statement of dying person can be basis for FIR
• Has evidentiary value

2. FIR in Accidents:
• Must be filed for road accidents with injury/death
• Required for insurance claims

3. Missing Person FIR:
• Can be filed immediately (24-hour waiting period is myth)
• Important for child trafficking cases

4. Cybercrime FIR:
• File at cybercrime cell
• Preserve digital evidence (screenshots, messages)

COMMON MISTAKES TO AVOID:

1. Delay in Filing:
• File FIR as soon as possible
• Delay can weaken case
• But there's no time limit for cognizable offenses

2. Incomplete Information:
• Provide complete, accurate details
• Vague FIR leads to weak investigation

3. Exaggeration:
• Stick to facts
• Don't exaggerate or add false details
• False FIR is punishable offense

4. Pressure to Withdraw:
• Don't withdraw FIR under pressure
• Only court can quash FIR (after investigation)

REMEDIES IF POLICE REFUSES FIR:

1. Approach Senior Officer:
• File complaint with Superintendent of Police (SP)
• Or Deputy Inspector General (DIG)

2. Judicial Magistrate:
• File complaint directly with Magistrate under Section 156(3) CrPC
• Magistrate can order police to register FIR

3. High Court/Supreme Court:
• File writ petition under Article 226/32
• Court can direct police to register FIR

4. State Human Rights Commission:
• File complaint for violation of rights
• They can recommend action against erring officers

DOCUMENTS TO CARRY:

• Identity proof (Aadhaar, PAN, driving license)
• Address proof
• Medical certificate (if injured)
• Evidence documents/photos
• List of witnesses with contact details

SPECIAL PROVISIONS:

1. Women Safety:
• Can call 100 (police helpline) or 1091 (women helpline)
• Female police officer should be present
• Can record statement at home if unable to visit station

2. Scheduled Castes/Tribes:
• FIR must be registered immediately under SC/ST Act
• Special courts for trial

3. Senior Citizens:
• Priority in registration and investigation
• Can give statement at residence if necessary

IMPORTANT SECTIONS:

• Section 154 CrPC - Information of cognizable case to police
• Section 155 CrPC - Information of non-cognizable case
• Section 156 CrPC - Power of police to investigate
• Section 157 CrPC - Procedure for investigation

Remember: Filing FIR is your right. Police cannot refuse to register FIR for cognizable offense. If they do, you have legal remedies.""",
        "url": "https://www.indiacode.nic.in/crpc",
        "metadata": {"procedure": "FIR Filing", "act": "Code of Criminal Procedure, 1973"}
    },
]


def save_comprehensive_knowledge():
    """Save comprehensive legal knowledge"""
    
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    
    # Convert to standard format
    formatted_data = []
    for item in COMPREHENSIVE_KNOWLEDGE:
        formatted_data.append({
            "url": item["url"],
            "title": item["title"],
            "content": item["content"],
            "metadata": {
                "category": item["category"],
                **item["metadata"]
            },
            "qa_pairs": [],
            "scraped_at": "2025-10-28 02:00:00"
        })
    
    # Load existing
    json_path = Path("data/raw/legal_data.json")
    if json_path.exists():
        with open(json_path, 'r', encoding='utf-8') as f:
            existing = json.load(f)
        print(f"Found {len(existing)} existing documents")
        # Replace old data with new comprehensive data
        formatted_data = formatted_data
    
    # Save
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(formatted_data, f, ensure_ascii=False, indent=2)
    
    print(f"[OK] Saved {len(formatted_data)} COMPREHENSIVE documents")
    print("\nAdded:")
    for item in COMPREHENSIVE_KNOWLEDGE:
        print(f"  - {item['title']}")


if __name__ == "__main__":
    print("="*80)
    print("ADDING COMPREHENSIVE INDIAN LEGAL KNOWLEDGE")
    print("="*80)
    print()
    save_comprehensive_knowledge()
    print()
    print("Next: Run 'python train_model.py' to retrain with this knowledge")

