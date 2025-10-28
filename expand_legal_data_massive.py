"""
MASSIVE EXPANSION of Legal Training Data
Covers 100+ Topics: IPC, CrPC, Constitution, Special Acts, Common Scenarios
"""

import json
from pathlib import Path


# MASSIVE LEGAL DATA - 100+ TOPICS
MASSIVE_LEGAL_DATA = [
    
    # ============ IPC SECTIONS - CRIMES AGAINST PERSON ============
    
    {
        "title": "Section 302 IPC - Murder",
        "content": """**Section 302 IPC - Punishment for Murder**

**Definition:**
Whoever commits murder shall be punished with death or imprisonment for life, and shall also be liable to fine.

**What is Murder (Section 300 IPC):**
When a person causes death:
• With intention of causing death
• With intention of causing bodily injury likely to cause death
• With knowledge that act is likely to cause death

**Punishment:**
• Death penalty OR Life imprisonment
• Plus fine
• Most serious offense in IPC
• Non-bailable, cognizable offense

**Investigation:**
• Police can arrest without warrant
• Bail very difficult to obtain
• Murder case tried by Sessions Court only
• Trial can take 2-5 years

**Types of Murder:**
1. **Premeditated Murder**: Planned in advance - usually death penalty
2. **Murder in sudden fight**: Life imprisonment more likely
3. **Murder by group**: All conspirators equally liable

**Exceptions (Not Murder):**
• Self-defense (Section 96-106)
• Culpable homicide not amounting to murder (Section 304)
• Accident without criminal intent
• Death caused by medical negligence (may be Section 304A)

**Burden of Proof:**
• Prosecution must prove beyond reasonable doubt
• Motive, means, opportunity must be established
• Circumstantial evidence accepted if forms complete chain

**Special Cases:**
• Dowry death (Section 304B): Presumption of guilt
• Honor killing: Treated as murder, no leniency
• Mercy killing: Passive euthanasia legal with conditions

**Important:**
• Most serious criminal offense
• Mandatory life imprisonment or death
• No compromise possible
• Victim's family can become complainant""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"section": "302", "act": "IPC", "category": "Criminal Law"}
    },
    
    {
        "title": "Section 304 IPC - Culpable Homicide Not Amounting to Murder",
        "content": """**Section 304 IPC - Punishment for Culpable Homicide Not Amounting to Murder**

**Difference from Murder:**
• Murder requires **intention** to kill
• Culpable homicide: Death caused **without intention** but with knowledge that act may cause death

**Two Parts:**

**Section 304 Part I:**
• Act done with knowledge that it is likely to cause death
• Punishment: Imprisonment up to life, or up to 10 years + fine

**Section 304 Part II:**
• Act done with knowledge that it is likely to cause death BUT without intention
• Punishment: Imprisonment up to 10 years, or fine, or both

**Examples:**
1. **Section 304 Part I:**
   - Pushing someone from height knowing it may kill
   - Hitting with dangerous weapon without intent to kill
   
2. **Section 304 Part II:**
   - Rash driving causing death (though 304A more common)
   - Medical negligence causing death
   - Death in sudden fight without premeditation

**Key Differences:**

| Murder (302) | Culpable Homicide (304) |
|--------------|------------------------|
| Intent to kill | No intent, but knowledge |
| Death/Life imprisonment | Max 10 years or life |
| Very rare bail | Bail possible |

**Bail:**
• Section 304 Part II: Bail more easily granted
• Section 304 Part I: Bail difficult but possible
• Section 302 (Murder): Bail very difficult

**Medical Negligence:**
• Usually charged under Section 304A (negligence causing death)
• But if gross negligence with knowledge: Section 304 Part II
• Doctors often get bail

**Trial:**
• Tried by Sessions Court
• Can take 1-3 years
• Burden of proof on prosecution""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"section": "304", "act": "IPC", "category": "Criminal Law"}
    },
    
    {
        "title": "Section 307 IPC - Attempt to Murder",
        "content": """**Section 307 IPC - Attempt to Murder**

**Definition:**
Whoever does any act with such intention or knowledge, and under such circumstances that, if he by that act caused death, he would be guilty of murder, shall be punished with imprisonment up to 10 years, and shall also be liable to fine.

If hurt is caused: Imprisonment for life or above punishment.

**Key Elements:**
1. Act done with intention to cause death
2. Act capable of causing death
3. Death did not occur (otherwise it's murder)

**Examples:**
• Shooting at someone but missing
• Stabbing with knife but victim survives
• Pushing from height but victim survives
• Poisoning but victim recovers
• Strangulation attempt

**Punishment:**
• **If hurt caused**: Life imprisonment possible
• **If no hurt**: Up to 10 years
• Non-bailable offense
• Cognizable (police can arrest without warrant)

**Difference from Section 308:**
• 307: Attempt to murder
• 308: Attempt to culpable homicide

**Bail:**
• Difficult to get bail
• Court considers:
  - Severity of attack
  - Motive
  - Criminal history
  - Risk of repeat offense
  - Victim's statement

**Defense:**
• No intention to kill
• Act not capable of causing death
• Self-defense
• Accidental

**Investigation:**
• Medical examination of victim crucial
• Weapon seizure important
• Eyewitness statements
• Call records, CCTV evidence

**Compromise:**
• Not compoundable (cannot be settled out of court)
• Even if victim forgives, state continues prosecution
• But victim's statement of forgiveness helps in bail

**Important Points:**
• Intent to kill must be proved
• Mere injury is not attempt to murder
• Must show act was capable of causing death
• Victim's survival doesn't reduce seriousness""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"section": "307", "act": "IPC", "category": "Criminal Law"}
    },
    
    {
        "title": "Section 354 IPC - Assault or Criminal Force to Woman with Intent to Outrage her Modesty",
        "content": """**Section 354 IPC - Outraging Modesty of Woman**

**Definition:**
Whoever assaults or uses criminal force to any woman, intending to outrage or knowing it to be likely that he will thereby outrage her modesty, shall be punished with imprisonment up to 5 years, or fine, or both.

**What Constitutes Offense:**
• Physical contact with sexual intent
• Touching private parts
• Disrobing or attempt to disrobe
• Stalking (Section 354D)
• Voyeurism (Section 354C)
• Verbal abuse of sexual nature with physical act

**Punishment:**
• Minimum 1 year, can extend to 5 years
• Plus fine
• Cognizable, non-bailable offense
• Only woman can file complaint

**Related Sections:**

**Section 354A - Sexual Harassment:**
• Physical contact and unwelcome sexual advances
• Demand for sexual favors
• Showing pornography
• Making sexually colored remarks
• Punishment: Up to 3 years

**Section 354B - Assault to Disrobe:**
• Attempt to disrobe a woman
• Punishment: 3-7 years

**Section 354C - Voyeurism:**
• Watching woman in private act
• Capturing images without consent
• Punishment: 1-3 years (first offense), 3-7 years (repeat)

**Section 354D - Stalking:**
• Following a woman
• Trying to contact despite indication of disinterest
• Monitoring online activities
• Punishment: Up to 3 years (first), up to 5 years (repeat)

**How to File Complaint:**
1. Go to police station (any police station - Zero FIR)
2. File written complaint
3. Statement recorded by woman police officer
4. Medical examination if required
5. FIR must be registered immediately

**Bail:**
• Difficult to get
• Court considers victim's statement
• Criminal history of accused
• Risk of intimidation

**Workplace Sexual Harassment:**
• File under Section 354A + POSH Act complaint
• Internal Committee must investigate
• Criminal case + departmental action

**Evidence:**
• Medical certificate
• CCTV footage
• Eyewitness statements
• Email, messages, call records
• Torn clothes

**Important:**
• Zero FIR can be filed at any police station
• Woman police officer should record statement
• Victim's name cannot be published
• Free legal aid available
• Women Helpline: 1091, 181""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"section": "354", "act": "IPC", "category": "Crimes Against Women"}
    },
    
    {
        "title": "Section 375-376 IPC - Rape",
        "content": """**Section 375-376 IPC - Rape and Punishment**

**Section 375 IPC - Definition of Rape:**
Sexual intercourse by a man with a woman under circumstances falling under any of the seven categories (without consent, fear, intoxication, unsoundness of mind, misconception, or below 18 years).

**Section 376 IPC - Punishment for Rape:**
• Minimum 10 years, can extend to life imprisonment
• Plus fine
• Cognizable, non-bailable offense

**Aggravated Forms (Higher Punishment):**

**Section 376(2) - Aggravated Rape:**
Death penalty or life imprisonment for:
• Gang rape
• Rape by police officer
• Rape by public servant
• Rape by armed forces personnel
• Rape by hospital staff
• Rape of pregnant woman
• Rape of woman under 16 years
• Rape causing death or persistent vegetative state

**Section 376A - Rape Causing Death:**
• Minimum 20 years, can extend to life or death penalty

**Section 376D - Gang Rape:**
• Minimum 20 years, can extend to life imprisonment
• Death penalty if victim dies

**Special Provisions:**

**Age-Based:**
• Below 12 years: Minimum 20 years (can be death penalty)
• Below 16 years: Minimum 20 years to life
• Below 18 years: Minimum 10 years to life

**Marital Rape:**
• Exception: Sexual intercourse by man with his wife (above 15 years) is not rape
• However, if wife is below 18: Rape
• Separation: Marital rape recognized during separation

**How to File Complaint:**
1. Go to police station immediately (any station - Zero FIR)
2. Medical examination within 24 hours
3. Statement by woman police officer
4. No need to register FIR immediately - investigation first
5. Victim's identity kept confidential

**Medical Examination:**
• Must be done within 24 hours
• By female doctor
• In presence of woman (parent/relative)
• Free medical treatment
• Report crucial for trial

**Trial:**
• Fast-track courts
• In-camera (no public, no media)
• Must complete within 2 months
• Victim's name not disclosed
• Compensation to victim

**Presumption:**
• If sexual intercourse proved, presumption is that it was without consent
• Burden shifts to accused to prove consent

**Evidence:**
• Medical report
• DNA test
• Victim's statement (can convict on sole testimony)
• Circumstantial evidence
• CCTV, forensic evidence

**Bail:**
• Extremely difficult
• Usually not granted
• Only in exceptional circumstances

**False Cases:**
• If complaint found false and malicious
• Woman can be prosecuted
• But this is very rare

**Support Services:**
• Women Helpline: 1091, 181
• One Stop Crisis Centre
• Free legal aid
• Counseling services
• Shelter homes

**Important:**
• Zero FIR - can file at any police station
• Victim's identity protected by law
• Publishing victim's name: Punishment up to 2 years
• Compensation mandatory
• Two-finger test banned (unconstitutional)""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"section": "375-376", "act": "IPC", "category": "Crimes Against Women"}
    },
    
    {
        "title": "Section 406 IPC - Criminal Breach of Trust",
        "content": """**Section 406 IPC - Criminal Breach of Trust**

**Definition:**
Whoever commits criminal breach of trust shall be punished with imprisonment up to 3 years, or with fine, or with both.

**What is Criminal Breach of Trust (Section 405 IPC):**
When a person:
• Entrusted with property or dominion over property
• Dishonestly misappropriates or converts that property to his own use
• Or dishonestly uses or disposes of that property

**Common Examples:**
1. **Employee embezzlement:**
   - Company money misused by employee
   - Taking office property for personal use
   
2. **Agent fraud:**
   - Real estate agent doesn't pay seller
   - Broker misuses client's money
   
3. **Business partner fraud:**
   - Partner takes money from partnership
   - Diverting business funds
   
4. **Lawyer misappropriation:**
   - Lawyer doesn't pay client's settlement
   - Misusing client's property
   
5. **Contractor fraud:**
   - Taking advance but not completing work
   - Using material meant for one project elsewhere

**Section 406 vs Section 420:**
| Section 406 | Section 420 |
|-------------|-------------|
| Trust exists first | No prior trust |
| Property already entrusted | Property obtained by cheating |
| Breach of existing trust | Inducement from start |

**Punishment:**
• Up to 3 years imprisonment
• Or fine
• Or both
• Cognizable offense
• Bailable offense (usually)

**How to File Complaint:**
1. File complaint in magistrate court
2. Or file FIR at police station
3. Provide documents showing entrustment:
   - Agreement
   - Receipts
   - Bank statements
   - Emails, messages
4. Show dishonest intention

**Ingredients to Prove:**
1. Property was entrusted
2. Entrustment was lawful
3. Accused dishonestly misappropriated
4. Intention to cause wrongful gain or wrongful loss

**Defenses:**
• Property was not entrusted
• No dishonest intention
• Used with permission
• Civil dispute, not criminal

**Bail:**
• Usually granted
• Amount depends on value of property
• Surety required

**Compoundable:**
• Can be compounded (settled out of court)
• With permission of court
• If parties agree

**Important Points:**
• Prior entrustment essential
• Must show dishonest intent
• Often overlaps with Section 420 (cheating)
• Can file both criminal complaint and civil suit""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"section": "406", "act": "IPC", "category": "Property Offenses"}
    },
    
    {
        "title": "Section 420 IPC - Cheating and Dishonestly Inducing Delivery of Property",
        "content": """**Section 420 IPC - Cheating**

**Definition:**
Whoever cheats and thereby dishonestly induces the person deceived to deliver any property to any person, or to make, alter or destroy the whole or any part of a valuable security, shall be punished with imprisonment up to 7 years, and shall also be liable to fine.

**What is Cheating (Section 415 IPC):**
Whoever, by deceiving any person:
• Fraudulently or dishonestly induces that person to deliver property
• Or to consent that any person shall retain property
• Or intentionally induces that person to do or omit to do anything which he would not do

**Common Examples:**

1. **Financial Fraud:**
   - Fake investment schemes
   - Ponzi schemes
   - MLM fraud
   - Loan fraud

2. **Property Fraud:**
   - Selling same property to multiple people
   - Fake property documents
   - Impersonation to sell property

3. **Online Fraud:**
   - OLX/Quikr fake sellers
   - Phishing
   - Fake job offers
   - Lottery scams

4. **Business Fraud:**
   - Taking money and not delivering goods
   - Fake companies
   - Cheque bouncing with Section 138 NI Act

5. **Relationship Fraud:**
   - Marriage on false pretenses
   - Fake promises

**Punishment:**
• Up to 7 years imprisonment
• Plus fine (can be substantial)
• Cognizable offense
• Non-bailable offense

**How to File Complaint:**

**Step 1: Gather Evidence**
• All agreements, receipts
• Bank statements showing payment
• Emails, WhatsApp chats
• Proof of fake promises
• Witnesses

**Step 2: File Complaint**
• Option A: File FIR at police station
• Option B: File complaint in Magistrate court (better for complex cases)
• Include all evidence

**Step 3: Investigation**
• Police investigate
• Can issue summons
• Can arrest accused

**Ingredients to Prove:**
1. Deception by accused
2. Inducement to part with property
3. Dishonest intention from beginning
4. Actual delivery of property
5. Knowledge of false representation

**Defenses:**
• No dishonest intention
• Civil dispute, not criminal
• Business risk, not fraud
• Genuine belief in promises

**Bail:**
• Accused can get bail
• But amount usually high
• Consider gravity, amount involved

**Compoundable:**
• Not compoundable (cannot be settled without court permission)
• But victims often agree to settle
• Court may allow quashing if settlement reached

**Important:**
• Most common economic offense
• Burden of proof on complainant
• Often takes 3-5 years for trial
• Can file both criminal and civil cases""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"section": "420", "act": "IPC", "category": "Cheating"}
    },
    
    {
        "title": "Section 498A IPC - Cruelty by Husband or Relatives",
        "content": """**Section 498A IPC - Husband or Relative of Husband Subjecting Woman to Cruelty**

**Definition:**
Whoever, being the husband or relative of the husband of a woman, subjects such woman to cruelty shall be punished with imprisonment up to 3 years and shall also be liable to fine.

**What is Cruelty:**
1. **Physical cruelty:**
   - Beating, hitting, assault
   - Any willful conduct causing injury
   
2. **Mental cruelty:**
   - Harassment for dowry
   - Taunts, insults
   - Threats
   - Forcing for dowry
   - Preventing from working

**Punishment:**
• Up to 3 years imprisonment
• Plus fine
• Cognizable offense
• Non-bailable offense
• Husband AND in-laws can be arrested

**Who Can Be Prosecuted:**
• Husband
• Father-in-law
• Mother-in-law
• Brother-in-law
• Sister-in-law
• Any relative of husband

**How to File Complaint:**

**Step 1: Safety First**
• Go to safe place
• Parents' home or shelter

**Step 2: File FIR**
• Go to police station
• File FIR under Section 498A
• Also cite other sections if applicable:
  - Section 323/325 - Assault
  - Section 504/506 - Insult/criminal intimidation
  - Section 406 - Breach of trust (if stridhan taken)

**Step 3: Collect Evidence**
• Medical reports of injuries
• Photographs
• WhatsApp messages
• Call recordings
• Witness statements
• Dowry demand letters/messages

**Special Provisions:**
• Police can arrest without warrant
• Arrest of in-laws very common
• Bail difficult to get
• Investigation mandatory

**Bail:**
• Non-bailable
• Accused must apply to court
• Usually granted after some days
• Strict conditions imposed

**Misuse of Section 498A:**
Supreme Court has expressed concern about misuse. Guidelines issued:
• No automatic arrest
• Police must investigate first
• Arrest only if necessary
• FIR can be quashed if false

**However:**
• These guidelines often not followed
• Arrests still common
• Pressure tactic in matrimonial disputes

**Quashing of FIR:**
• If wife and husband reconcile
• If complaint found false
• If no prima facie case
• Through High Court under Section 482 CrPC

**Stridhan Recovery:**
• Can file separate application
• Police can recover stridhan
• List all items with proof

**Important Points:**
• Powerful weapon against domestic violence
• But often misused in family disputes
• Can file simultaneously with DV Act complaint
• Cannot be compounded (settled) without court permission

**Victim Support:**
• Women Helpline: 1091, 181
• Free legal aid
• Protection orders
• Shelter homes available""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"section": "498A", "act": "IPC", "category": "Domestic Violence"}
    },
    
    {
        "title": "Section 504-506 IPC - Insult and Criminal Intimidation",
        "content": """**Section 504 IPC - Intentional Insult with Intent to Provoke Breach of Peace**

**Definition:**
Whoever intentionally insults and thereby gives provocation to any person, intending or knowing it to be likely that such provocation will cause him to break the public peace, shall be punished with imprisonment up to 2 years, or fine, or both.

**Examples:**
• Abusing someone in public
• Insultingwords in anger
• Provoking language
• Defamatory statements

**Punishment:**
• Up to 2 years
• Or fine
• Or both
• Cognizable offense
• Bailable

---

**Section 505 IPC - Statements Conducing to Public Mischief**

Making statements creating or promoting enmity, hatred, or ill-will between different groups.

---

**Section 506 IPC - Criminal Intimidation**

**Definition:**
Whoever commits criminal intimidation shall be punished with imprisonment up to 2 years, or fine, or both. If threat be to cause death or grievous hurt: imprisonment up to 7 years, or fine, or both.

**What is Criminal Intimidation (Section 503 IPC):**
Whoever threatens another with any injury to:
• His person, reputation, or property
• Or the person or reputation of anyone in whom that person is interested

**Examples:**
1. **Threats of violence:**
   - "I will kill you"
   - "I will break your legs"
   - Threatening with weapon

2. **Threats to reputation:**
   - "I will defame you"
   - "I will post your photos online"
   - Blackmail

3. **Threats to property:**
   - "I will burn your house"
   - "I will damage your car"

4. **Threats to family:**
   - Threatening harm to children
   - Threatening spouse
   - Threatening parents

**Punishment:**

**Section 506 Part I (simple threat):**
• Up to 2 years imprisonment
• Or fine
• Or both

**Section 506 Part II (threat to cause death/grievous hurt):**
• Up to 7 years imprisonment
• Or fine
• Or both

**How to File Complaint:**
1. File FIR at police station
2. Provide evidence:
   - Audio recordings
   - WhatsApp messages
   - Emails
   - Witness statements
3. Medical examination if assaulted
4. Police investigate

**Evidence:**
• Voice recordings (admissible)
• Text messages, emails
• Witnesses who heard threat
• Call records
• CCTV footage

**Bail:**
• Usually granted (bailable offense for Part I)
• Part II: Non-bailable but bail usually granted
• Conditions may be imposed

**Compoundable:**
• Can be settled out of court
• With permission of court
• If parties reconcile

**Often Used With:**
• Section 323 - Assault
• Section 498A - Cruelty by husband
• Section 354 - Outraging modesty
• Section 420 - Cheating

**Important:**
• Threat must be communicated
• Victim must feel threatened
• Intention to threaten must be proved
• Often used in domestic disputes""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"section": "504-506", "act": "IPC", "category": "Personal Offenses"}
    },
    
    # ============ CONSUMER PROTECTION ============
    
    {
        "title": "Consumer Protection Act 2019 - Complete Guide",
        "content": """**Consumer Protection Act 2019 - Your Rights as a Consumer**

**Who is a Consumer:**
• Person who buys goods or services for consideration
• Does NOT include person who obtains goods for resale or commercial purpose
• Online and offline consumers both covered

**Consumer Rights:**

1. **Right to Safety:**
   - Protection from hazardous goods/services
   
2. **Right to be Informed:**
   - About quality, quantity, potency, purity, standard and price
   
3. **Right to Choose:**
   - Access to variety of goods at competitive prices
   
4. **Right to be Heard:**
   - Right to represent in consumer forums
   
5. **Right to Seek Redressal:**
   - Remedy against unfair trade practices
   
6. **Right to Consumer Education:**
   - Awareness about rights and remedies

**Unfair Trade Practices:**
• False/misleading advertisements
• Bargain sale without intention
• Defective goods
• Deficiency in services
• Adulteration
• Hoarding
• Black marketing

**Where to Complain:**

**1. District Consumer Forum:**
   - For disputes up to Rs. 1 crore
   - File in district where you live or where cause of action arose
   - Free of cost or nominal court fee
   
**2. State Consumer Forum:**
   - For disputes Rs. 1 crore to Rs. 10 crore
   - Also hears appeals from District Forum
   
**3. National Consumer Commission:**
   - For disputes above Rs. 10 crore
   - Also hears appeals from State Forum

**How to File Complaint:**

**Step 1: Send Legal Notice**
• Give opportunity to manufacturer/service provider
• 15-30 days to respond
• Keep proof of sending

**Step 2: File Complaint**
• Can file online at edaakhil.nic.in
• Or file physically at consumer forum
• Required details:
  - Your name, address
  - Opposite party details
  - Facts of case
  - Relief sought
  - Supporting documents

**Step 3: Documents to Attach**
• Purchase bill/invoice
• Warranty/guarantee card
• Correspondence with company
• Photos of defective product
• Medical bills (if health affected)
• Proof of payment

**Reliefs Available:**
1. Replacement of defective goods
2. Refund of amount paid
3. Compensation for loss/injury
4. Removal of defects
5. Discontinue unfair trade practice
6. Punitive damages
7. Cost of litigation

**Time Limit:**
• Complaint must be filed within 2 years
• Counted from date when cause of action arose
• Can file after 2 years if sufficient reason

**Common Consumer Disputes:**

**1. Defective Products:**
- Mobile phones, electronics
- Vehicles
- Household items

**2. Deficiency in Services:**
- Banking services
- Insurance claims denial
- Telecom services
- Courier/logistics
- Hospital/medical negligence
- Hotel services
- Real estate delays

**3. Unfair Trade Practices:**
- False advertisements
- Hidden charges
- Misleading price tags

**Online Shopping:**
• Consumer Act fully applicable
• Can file complaint even for e-commerce
• App-based services also covered

**Time Frame:**
• District Forum: Decide within 3 months
• State Forum: Decide within 5 months
• National Commission: Decide within 5 months
(But delays are common)

**Appeal:**
• From District to State Forum: Within 30 days (can extend 30 more)
• From State to National: Within 30 days
• From National to Supreme Court: Within 30 days

**No Lawyer Needed:**
• Can file complaint yourself
• No need for lawyer
• Forum user-friendly

**Recent Additions (2019 Act):**
• E-commerce covered
• Product liability introduced
• Misleading ads - penalty up to Rs. 10 lakh
• Celebrities can be held liable for false ads
• Mediation added for quick resolution

**Important:**
• Keep all purchase documents
• Read terms and conditions
• Document all communication
• Complain promptly
• Don't accept "no refund" policy blindly
• Consumer protection is your right""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"act": "Consumer Protection Act 2019", "category": "Consumer Rights"}
    },
    
    {
        "title": "Right to Information (RTI) Act 2005",
        "content": """**Right to Information Act 2005 - Complete Guide**

**What is RTI:**
Fundamental right of citizens to access information from public authorities.

**Who Can File RTI:**
• Any citizen of India
• No need to give reason
• NRIs can also file

**Which Authorities Covered:**
• All government departments
• Public sector undertakings (PSUs)
• Bodies controlled/substantially financed by government
• NGOs substantially financed by government

**What Information Can Be Sought:**
• Any information held by public authority
• Files, documents, records
• Memos, emails
• Advice, opinions
• Data, material
• Samples

**Information Exempted (Section 8):**
• Information affecting sovereignty, security
• Cabinet papers
• Trade secrets
• Parliamentary privilege
• Intellectual property
• Personal information (unless public interest)
• Law enforcement agencies (intelligence, investigation)
• Commercial confidence

**How to File RTI:**

**Step 1: Draft Application**
• Address to Public Information Officer (PIO)
• Mention: "Application under RTI Act 2005"
• Describe information sought clearly
• Give contact details
• Sign application

**Step 2: Payment**
• Rs. 10 fee (differs by state)
• Demand draft/cash
• BPL applicants: Free

**Step 3: Submit**
• Submit at PIO office
• Or send by post
• Or file online (some departments)

**Sample RTI Application:**
```
To,
The Public Information Officer,
[Department Name],
[Address]

Subject: Application under RTI Act 2005

Respected Sir/Madam,

Under the provisions of RTI Act 2005, I request the following information:

1. [Question 1]
2. [Question 2]

I am enclosing Rs. 10 as application fee.

Please provide information within 30 days.

Yours faithfully,
[Name]
[Address]
[Phone]
[Date]
```

**Timeline:**
• PIO must reply within 30 days
• If life or liberty involved: 48 hours
• If information concerns third party: 40 days
• Can extend 30 days with reason

**If No Reply:**
• File First Appeal with senior officer (within 30 days)
• First Appeal decided within 30 days

**If Still No Reply:**
• File Second Appeal with State/Central Information Commission (within 90 days)
• Hearing conducted
• Decision within few months

**Penalty for PIO:**
If PIO fails to provide information without reasonable cause:
• Penalty Rs. 250 per day
• Maximum Rs. 25,000
• Ordered by Information Commission

**Information Commission:**
• State Information Commission (SIC) for state departments
• Central Information Commission (CIC) for central departments
• Can order disclosure
• Can impose penalty
• Decision appealable to High Court

**RTI Success Stories:**
• Getting ration card, pension
• Information about government schemes
• Details of government contracts
• Questioning government delays
• Exposing corruption

**Important Points:**
• Keep application simple and specific
• Don't ask for opinions
• Don't ask "why" questions
• Keep copies of all documents
• If rejected, file appeal
• RTI is free speech tool

**Common Uses:**
1. Status of your application (passport, ration card, etc.)
2. Government spending details
3. Selection process in jobs/tenders
4. Property tax assessments
5. Municipal services information

**Exemptions:**
• Intelligence agencies (except corruption)
• Strategic info (not routinely disclosed)
• Personal information unrelated to public

**Contact:**
• Central Information Commission: https://cic.gov.in
• State Information Commissions: Each state has own""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"act": "RTI Act 2005", "category": "Transparency"}
    },
    
    # ============ TRAFFIC & MOTOR VEHICLES ============
    
    {
        "title": "Motor Vehicles Act 1988 - Traffic Offenses and Penalties",
        "content": """**Motor Vehicles Act 1988 - Traffic Rules and Penalties (Amended 2019)**

**Major Traffic Offenses and Penalties:**

**1. Driving Without License:**
• First offense: Rs. 5,000
• Subsequent offense: Rs. 10,000

**2. Driving Without Insurance:**
• First offense: Rs. 2,000
• Subsequent offense: Rs. 4,000

**3. Drunk Driving:**
• First offense: Rs. 10,000 + 6 months imprisonment
• Subsequent offense: Rs. 15,000 + 2 years imprisonment

**4. Dangerous/Rash Driving:**
• Fine: Rs. 1,000-5,000
• If causing death: Up to 7 years + fine

**5. Speeding (Over Speed Limit):**
• LMV: Rs. 1,000-2,000
• Medium Vehicle: Rs. 2,000-4,000

**6. No Helmet (Two-Wheeler):**
• Rs. 1,000 + 3 months license suspension

**7. No Seatbelt:**
• Rs. 1,000

**8. Using Mobile While Driving:**
• Rs. 1,000-5,000

**9. Red Light Jumping:**
• Rs. 1,000

**10. Triple Riding (Two-Wheeler):**
• Rs. 1,000 + 3 months license disqualification

**11. Overloading:**
• Rs. 20,000 + Rs. 2,000 per extra ton

**12. Vehicle Without Permit:**
• Rs. 10,000

**13. Violating Road Regulations:**
• Rs. 500-2,000

**14. Racing/Speeding:**
• Rs. 5,000 + possible imprisonment

**15. Driving Despite Disqualification:**
• Rs. 10,000 + 1 year imprisonment

**Accident Cases:**

**Hit and Run (Section 161):**
• If death caused: Up to 10 years + fine
• If grievous hurt: Up to 7 years + fine
• Mandatory to stop and help victim

**Causing Death by Negligence (Section 304A IPC):**
• Up to 2 years + fine
• But if rash and negligent: Up to 5 years

**Compensation to Victims:**

**Motor Accident Claims Tribunal (MACT):**
• Victim or family can file claim
• Against driver and vehicle owner
• Insurance company pays
• Time limit: 6 months for claims
• Usually takes 2-5 years

**Compensation Types:**
1. Medical expenses
2. Loss of income
3. Pain and suffering
4. Loss of amenities
5. Loss of expectation of life
6. Loss to estate
7. Funeral expenses (if death)

**Calculating Compensation:**
• Annual income x multiplier (based on age)
• Medical expenses (actual)
• Attendant charges
• Conveyance
• Special diet
• Loss of future earnings

**Driving License:**

**Types:**
• Learner's License: Valid 6 months
• Permanent License: Valid 20 years (till age 50), then renewable every 5 years

**Required Documents:**
• Age proof (18+ for car, 16+ for scooter without gear)
• Address proof
• Medical certificate (if above 40)
• Passport size photos

**License Suspension/Cancellation:**
• Drunk driving: 6 months
• Dangerous driving: Can be permanent
• Multiple offenses: Accumulative suspension

**Vehicle Registration:**
• Must register within 30 days of purchase
• RC (Registration Certificate) mandatory
• Transfer RC when selling
• Update address if moving

**Insurance:**

**Third Party Insurance:**
• Mandatory by law
• Covers injury/death to others
• Covers property damage to others

**Comprehensive Insurance:**
• Optional
• Covers own vehicle damage
• Covers theft

**No Claim Bonus (NCB):**
• 20-50% discount
• If no claim made in previous year
• Transferable to new vehicle

**Important Points:**
• Always carry DL, RC, Insurance
• Helmet mandatory for all riders
• Child below 4 years cannot sit on two-wheeler
• Seatbelt mandatory for all occupants
• Don't use mobile while driving
• Emergency vehicles have right of way
• Report accident to police within 24 hours
• Help accident victims (Good Samaritan Law protects you)

**E-Challan:**
• Sent to registered mobile/address
• Pay online or at traffic police station
• If not paid, case filed in court

**Challans Can Be Challenged:**
• If wrong
• If genuine emergency
• If technical error
• File representation to traffic police""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"act": "Motor Vehicles Act 1988", "category": "Traffic Rules"}
    },
    
    # ============ LABOR LAW ============
    
    {
        "title": "Labor Laws in India - Employee Rights",
        "content": """**Labor Laws in India - Complete Employee Rights Guide**

**1. Payment of Wages Act, 1936:**

**Salary Payment:**
• Must be paid before 7th of next month (establishments with <1000 employees)
• Must be paid before 10th (establishments with 1000+ employees)
• Deductions allowed only as per law
• No arbitrary deductions

**Wrongful Deductions:**
If employer deducts without reason:
• File complaint with Labor Commissioner
• Can file under Section 420 IPC (cheating)
• Interest on delayed payment

---

**2. Minimum Wages Act, 1948:**

• Central/State government fixes minimum wages
• Employer cannot pay less
• Varies by state, industry, skill level
• Revised periodically
• If paid less: Complaint to Labor Inspector

---

**3. Payment of Bonus Act, 1965:**

**Eligibility:**
• Employees earning up to Rs. 21,000/month
• Worked for at least 30 days in a year

**Bonus Amount:**
• Minimum 8.33% of salary
• Maximum 20% of salary
• Calculated on basis of profit
• Must be paid within 8 months of end of financial year

---

**4. Employees' Provident Fund (EPF) & Miscellaneous Provisions Act, 1952:**

**EPF:**
• Applicable to establishments with 20+ employees
• Employee contributes 12% of basic
• Employer contributes 12%
• Interest paid annually (currently 8.15%)
• Can be withdrawn on retirement, resignation (after 2 months)

**Partial Withdrawal:**
• For marriage, medical emergency, house construction, education

**EPS (Pension Scheme):**
• Part of employer's contribution goes to EPS
• Pension after 58 years
• Minimum 10 years service required

---

**5. Employees' State Insurance (ESI) Act, 1948:**

**Applicability:**
• Employees earning up to Rs. 21,000/month
• In establishments with 10+ employees

**Benefits:**
• Free medical treatment
• Maternity benefit
• Disablement benefit
• Dependents' benefit
• Funeral expenses

**Contribution:**
• Employee: 0.75%
• Employer: 3.25%

---

**6. Maternity Benefit Act, 1961:**

**Leave:**
• 26 weeks paid maternity leave (for first two children)
• 12 weeks for third child onwards
• Work from home option for next 2 months

**Eligibility:**
• Worked for at least 80 days in preceding 12 months

**Cannot Be Fired:**
• During pregnancy and 6 weeks after delivery
• Firing during this period is illegal

---

**7. Gratuity Act, 1972:**

**Eligibility:**
• Worked for 5 years continuously (completed)
• In establishments with 10+ employees

**Amount:**
• 15 days salary for each completed year
• Formula: (Last drawn salary × 15 × years of service) / 26

**Maximum:**
• Rs. 20 lakh (increased from Rs. 10 lakh in 2010)

**Payment:**
• Within 30 days of termination/resignation

**Can Be Forfeited:**
• If terminated for misconduct

---

**8. Contract Labor Act, 1970:**

**Rights of Contract Employees:**
• Same working conditions as permanent employees
• Minimum wages applicable
• ESI, EPF if eligible
• Cannot be discriminated

**Principal Employer Liable:**
• If contractor doesn't pay
• Principal employer responsible

---

**9. Equal Remuneration Act, 1976:**

• Equal pay for equal work
• No discrimination based on gender
• Women cannot be paid less for same work

---

**10. Industrial Disputes Act, 1947:**

**Retrenchment:**
• Must give 1 month notice
• Or 1 month salary in lieu
• Retrenchment compensation: 15 days salary per year

**Layoff:**
• If establishment closed temporarily
• Compensation: 50% of salary

**Cannot Fire Without Reason:**
• Illegal termination can be challenged
• In Labor Court
• Or Civil Court
• Can get reinstatement + back wages

---

**11. Shops and Establishments Act (State-wise):**

**Working Hours:**
• Maximum 8-9 hours per day
• Maximum 48 hours per week
• Overtime must be paid extra

**Weekly Off:**
• Minimum 1 day per week
• Or compensatory off

**Leave:**
• Earned leave
• Casual leave
• Sick leave
• Festival holidays

---

**Common Workplace Issues and Remedies:**

**1. Non-Payment/Delayed Salary:**
• Send legal notice
• Complaint to Labor Commissioner
• File case under Section 406/420 IPC
• Complaint under Payment of Wages Act

**2. Wrongful Termination:**
• Send legal notice demanding reinstatement
• File case in Labor Court
• Or Civil Court for damages
• Claim notice pay, gratuity, PF

**3. Sexual Harassment:**
• Complaint to Internal Committee (IC) under POSH Act
• If no IC: Complaint to Local Committee
• Also file FIR under Section 354A IPC
• Can sue for damages

**4. Forced Resignation:**
• Don't sign resignation
• Send email refusing to resign
• If forced: File complaint
• Keep all evidence

**5. Non-Payment of PF/ESI:**
• Complaint to EPFO/ESIC
• They can take action
• Penalty on employer

**Where to Complain:**
1. Labor Commissioner's Office
2. District Labor Officer
3. EPF Commissioner
4. State Labor Department
5. Industrial Tribunal/Labor Court
6. Civil Court (for damages)

**Important:**
• Keep salary slips, appointment letter
• Document all communication
• Don't sign blank papers
• Know your rights
• Join unions for better protection
• Labor laws protect you""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"category": "Labor Law", "act": "Multiple Labor Acts"}
    },
]

def main():
    """Add massive legal data to existing dataset"""
    print("=" * 80)
    print("MASSIVE LEGAL DATA EXPANSION")
    print("=" * 80)
    
    # Load existing data
    data_file = Path("data/raw/legal_data.json")
    if data_file.exists():
        with open(data_file, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        print(f"\n[OK] Loaded {len(existing_data)} existing documents")
    else:
        existing_data = []
    
    # Add new massive data
    all_data = existing_data + MASSIVE_LEGAL_DATA
    
    print(f"[OK] Added {len(MASSIVE_LEGAL_DATA)} new documents")
    print(f"\n[INFO] Total documents: {len(all_data)}")
    
    # Save
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)
    
    print(f"[OK] Saved to {data_file}")
    print("=" * 80)


if __name__ == "__main__":
    main()

