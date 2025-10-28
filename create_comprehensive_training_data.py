"""
Create Comprehensive Training Data for AI Legal Chatbot
Merges structured QA data with comprehensive legal knowledge
"""

import json
from pathlib import Path


# Read existing comprehensive data
def load_comprehensive_data():
    """Load comprehensive Indian law data"""
    try:
        # Import from comprehensive_indian_law.py
        import sys
        sys.path.append('.')
        from comprehensive_indian_law import COMPREHENSIVE_KNOWLEDGE
        return COMPREHENSIVE_KNOWLEDGE
    except:
        return []


# Create structured training data with 50+ topics
TRAINING_DATA = [
    # URGENT / HIGH PRIORITY TOPICS
    {
        "url": "https://www.indiacode.nic.in",
        "title": "What to do if a teacher beats a student severely?",
        "content": """**Immediate Actions:**

1. **Medical Attention**: Get the child medically examined immediately. Keep medical reports.

2. **File FIR**: Go to nearest police station and file FIR under:
   • Section 323 IPC - Voluntarily causing hurt (imprisonment up to 1 year)
   • Section 325 IPC - Voluntarily causing grievous hurt (imprisonment up to 7 years)
   • Section 506 IPC - Criminal intimidation (if threatened)

3. **Complaint to Education Department**:
   • File written complaint to:
     - School Principal
     - District Education Officer (DEO)
     - State Education Department
   • Demand action under RTE Act 2009

4. **Complain to Child Welfare Committee (CWC)**:
   • Under Juvenile Justice Act, 2015
   • CWC can take action against teacher
   • Protect child's rights

**Legal Provisions:**

**Corporal Punishment is COMPLETELY BANNED** in India:
• Right to Education Act, 2009 - Section 17(1) prohibits corporal punishment
• Supreme Court Ban (2000) - Banned in all schools
• National Commission for Protection of Child Rights (NCPCR) guidelines

**Teacher Can Face:**
• Criminal case under IPC
• Suspension/dismissal from service
• Debarment from teaching
• Compensation to victim

**Evidence to Collect:**
• Photographs of injuries
• Medical certificate
• Witness statements (other students, parents)
• CCTV footage (if available)
• Previous complaints (if any)

**Legal Rights of Student:**
• Right to dignity (Article 21)
• Right to education without fear (Article 21A)
• Protection from violence (JJ Act)

**Contact:**
• Child Helpline: 1098
• Women Helpline: 1091
• Police: 100

**Important:** Act immediately. Corporal punishment is a cognizable offense - police must register FIR.""",
        "metadata": {
            "intent": "corporal_punishment",
            "patterns": ["teacher beat student", "teacher hit child", "corporal punishment", "school violence"],
            "legal_basis": ["Section 323 IPC", "Section 325 IPC", "RTE Act 2009"],
            "complexity": "high_priority",
            "urgency": "immediate"
        }
    },
    
    {
        "url": "https://www.indiacode.nic.in",
        "title": "Is corporal punishment legal in Indian schools?",
        "content": """**NO. Corporal Punishment is COMPLETELY ILLEGAL in India.**

**Legal Provisions:**

1. **Right to Education Act, 2009 - Section 17**:
   "No child shall be subjected to physical punishment or mental harassment"
   
2. **Supreme Court Judgment (2000)**:
   • Complete ban on corporal punishment in schools
   • Violators face criminal action

3. **National Commission for Protection of Child Rights (NCPCR)**:
   • Issued guidelines prohibiting corporal punishment
   • Schools must display "No Corporal Punishment" boards

4. **Juvenile Justice Act, 2015**:
   • Protects children from all forms of abuse
   • Corporal punishment is child abuse

**Punishment for Teachers:**
• Criminal case under Section 323/325 IPC
• Immediate suspension
• Dismissal from service
• Compensation to victim
• Imprisonment

**What is Corporal Punishment:**
• Physical beating, hitting, slapping
• Mental harassment, humiliation
• Making child stand for long hours
• Punishment causing physical/mental pain

**Parents' Rights:**
• File FIR immediately
• Complain to education department
• Demand action against teacher
• Seek compensation

**Zero Tolerance:** No form of corporal punishment is acceptable or legal.""",
        "metadata": {
            "intent": "corporal_punishment",
            "legal_basis": ["RTE Act 2009", "IPC"],
            "complexity": "basic"
        }
    },
    
    {
        "url": "https://www.indiacode.nic.in",
        "title": "Right to Education (RTE) Act 2009 - Article 21A",
        "content": """Right to Education Act 2009 implements Article 21A. Free and compulsory education for children aged 6-14 years.

**Government Schools:**
• Must admit all children, no fee
• Cannot deny admission

**Private Schools:**
• 25% seats reserved for EWS/disadvantaged
• Government pays fee for reserved seats

**Key Provisions:**
• No donation or capitation fee
• No screening procedure/interview for admission
• No detention policy till Class 8 (discontinued in many states)
• No corporal punishment
• Pupil-teacher ratio: 30:1 (primary), 35:1 (upper primary)

**Infrastructure Requirements:**
• Separate toilets for boys and girls
• Safe drinking water facility
• Library with books
• Playground
• All-weather building

**Academic Requirements:**
• Academic calendar: 200 working days minimum
• Instruction hours: 800 hours (primary), 1,000 hours (upper primary)
• Teacher qualifications: D.El.Ed/B.El.Ed/B.Ed mandatory
• Continuous Comprehensive Evaluation (CCE)

**School Management Committee:**
• Must be formed with parent representatives
• 75% parents + 25% teachers and local authority members
• Prepares school development plan

**Complaints Mechanism:**
• File complaint to Block Education Officer
• Escalate to District Education Officer
• State Education Department for higher appeals

**Recognition:**
• Schools must obtain recognition from government
• Non-compliance: Fine up to Rs. 1 lakh
• Withdrawal of recognition possible

**Special Provisions:**
• Special training for out-of-school children
• No child can be expelled till completing elementary education
• Neighborhood school concept: Within 1 km (primary), 3 km (upper primary)
• Transfer certificate must be issued within 7 days for migration""",
        "metadata": {
            "intent": "right_to_education",
            "legal_basis": ["Article 21A", "RTE Act 2009"],
            "complexity": "medium"
        }
    },
    
    {
        "url": "https://www.indiacode.nic.in",
        "title": "School Fee Refund Disputes and Student Rights",
        "content": """No specific central law, but consumer forums and state rules govern fee disputes.

**Fee Regulation:**
• State Fee Regulatory Committees decide fee structure for private schools
• Annual fee hike limited (usually 10-15%)

**Admission Withdrawal:**
• If before academic year starts: Full refund minus processing fee
• If after classes start: Refund as per school policy (usually proportionate)

**Illegal Practices:**
• Capitation fee: Illegal, complaint to education department
• Arbitrary fee hike: Complaint to Fee Regulatory Committee
• Forced purchase: School cannot force purchase of uniforms, books from specific vendor
• Extra coaching: School cannot force students to take paid coaching from teachers

**Non-Discrimination:**
• Based on religion, caste prohibited
• Admission denial: RTE Act mandates 25% EWS quota, cannot be denied

**Fee Transparency:**
• Fee structure must be displayed on website and notice board
• Fee receipt mandatory
• Security deposit: Refundable at time of leaving school

**Complaint Mechanisms:**
• Education Department
• Consumer Forum (for deficiency in service)
• State Commission for Protection of Child Rights

**Expulsion Rules:**
• Cannot be arbitrary
• Must follow natural justice principles
• Show cause notice and hearing mandatory

**Additional Rules:**
• Mid-year fee hike: Generally not allowed unless approved by fee committee
• Transparency: Schools must disclose all charges upfront
• Refund timeline: Usually 30-60 days""",
        "metadata": {
            "intent": "school_fees",
            "legal_basis": ["Consumer Protection Act", "RTE Act"],
            "complexity": "medium"
        }
    },
    
    {
        "url": "https://www.indiacode.nic.in",
        "title": "How to register house after parents demise?",
        "content": """**Complete Procedure for House Registration After Parents' Death:**

**Step 1: Obtain Death Certificate**
• Get certified death certificate from Municipal Corporation
• Multiple copies needed (at least 5-6)

**Step 2: Get Legal Heir Certificate**
• Apply to Tahsildar/Revenue Office
• Required documents:
  - Death certificate
  - Family members' Aadhaar cards
  - Ration card
  - Affidavit declaring legal heirs
• Time: 15-30 days
• Fee: ₹50-100

**Step 3: Get Succession Certificate** (if needed)
• Apply to District Court
• Required when:
  - Multiple heirs and disputes
  - Property value is high
  - Debts involved
• Time: 3-6 months
• Fee: Based on property value

**Step 4: Mutation in Revenue Records**
• Apply to local Municipal Corporation/Gram Panchayat
• Documents needed:
  - Death certificate
  - Legal heir certificate
  - Property tax receipts
  - Original property documents
  - ID proofs of all legal heirs
• Fee: ₹500-2,000
• Time: 2-4 weeks

**Step 5: Registration** (if transferring to specific heir)
• Draft Release Deed/Relinquishment Deed
• All legal heirs must sign
• Register at Sub-Registrar Office
• Stamp duty: 1-7% of property value (varies by state)
• Registration fee: 1% of property value

**Documents Required:**
1. Death certificate of deceased
2. Legal heir certificate
3. Succession certificate (if applicable)
4. Original property documents (sale deed, etc.)
5. Latest property tax receipts
6. Encumbrance certificate (last 13 years)
7. ID proofs of all legal heirs
8. Passport-size photographs
9. PAN cards of all heirs

**Legal Heirs Under Hindu Succession Act:**
• Class I Heirs: Son, daughter, widow, mother
• Get equal share
• If father died before 2005: ancestral property follows old rules
• If father died after 2005: daughter gets equal rights

**Time Frame:**
• Mutation: 2-4 weeks
• Registration: 1 day (after documents ready)
• Total: 1-3 months (if no disputes)

**Costs:**
• Legal heir certificate: ₹50-100
• Mutation: ₹500-2,000
• Stamp duty: 1-7% of property value
• Registration: 1% of property value
• Lawyer fees: ₹10,000-50,000

**Important Points:**
• No specific time limit to claim inheritance
• But complete within 1-2 years to avoid complications
• If property is self-acquired: all Class I heirs get equal share
• If ancestral property: coparcenary rights apply
• Will overrides succession laws

**For NRI Heirs:**
• Can execute Power of Attorney (POA) from abroad
• POA must be notarized and apostilled
• Can be sent to India and adjudicated""",
        "metadata": {
            "intent": "property_inheritance",
            "legal_basis": ["Hindu Succession Act 1956", "Transfer of Property Act 1882"],
            "complexity": "high"
        }
    },
    
    {
        "url": "https://www.indiacode.nic.in",
        "title": "What to do in case of domestic violence?",
        "content": """**Immediate Actions for Domestic Violence Victims:**

**1. Ensure Safety First:**
• Leave the house if in immediate danger
• Go to parents/friend's place
• Call Women Helpline: 1091 or 181
• Call Police: 100

**2. File Complaint:**

**Option A - File FIR** (Criminal Case):
• Go to police station
• File FIR under Section 498A IPC (Cruelty by husband)
• Also cite: Section 323/325/326 IPC (Assault causing hurt)
• Section 506 IPC (Criminal intimidation)
• Police MUST register FIR for domestic violence

**Option B - Domestic Violence Act** (Civil Remedy):
• Approach Magistrate directly
• File application under DV Act 2005
• Can get:
  - Protection Order
  - Residence Order
  - Monetary Relief
  - Custody of Children
  - Compensation

**3. Get Protection Order:**
• Court can pass ex-parte order (without husband present)
• Restrains husband from:
  - Committing any act of violence
  - Entering your residence
  - Contacting you
  - Alienating assets
• Immediate relief within 3 days

**4. Collect Evidence:**
• Medical certificate if injured
• Photographs of injuries
• Torn clothes, broken items
• WhatsApp messages, emails
• Call recordings
• Witness statements
• Previous complaints (if any)

**5. Get Medical Examination:**
• Go to government hospital
• Get medico-legal certificate (MLC)
• Document all injuries
• Keep copies

**Legal Remedies Available:**

**Under Section 498A IPC:**
• Cognizable, non-bailable offense
• Punishment: Imprisonment up to 3 years + fine
• Police can arrest without warrant
• Applies to husband and in-laws

**Under DV Act 2005:**
• Protection order - Stop violence
• Residence order - Right to live in shared household
• Monetary relief - Maintenance, medical expenses
• Compensation - For mental agony, injuries
• Custody order - Custody of children
• Recovery of stridhan - Your jewelry, gifts

**Who Can File:**
• Wife (legally married or live-in partner)
• Sister, Mother
• Any woman in shared household

**Where to File:**
• Police station (FIR)
• Magistrate court (DV Act complaint)
• Protection Officer (at District level)
• Service Provider NGOs

**Support Services:**
• Women Helpline: 1091, 181
• Legal aid: Free legal services authority
• Shelter homes: State-run protection homes
• Counseling: Mahila Mandals, NGOs
• Police protection: Can be sought

**Important Rights:**
• Right to live with dignity (Article 21)
• Right to shared household (even if rented)
• Right to maintenance
• Right to stridhan
• Right to police protection

**Time Frame:**
• Protection order: Within 3 days
• Final orders: 60 days (extendable)
• Criminal trial: 1-3 years

**Note:** You can file BOTH criminal (498A) AND civil (DV Act) cases simultaneously.""",
        "metadata": {
            "intent": "domestic_violence",
            "legal_basis": ["Section 498A IPC", "DV Act 2005"],
            "complexity": "high_priority",
            "urgency": "immediate"
        }
    },
    
    {
        "url": "https://www.indiacode.nic.in",
        "title": "How to file cybercrime complaint?",
        "content": """**Complete Guide to File Cybercrime Complaint:**

**Step 1: Report Online** (Fastest Method)
• Visit: www.cybercrime.gov.in
• Click "Report Anonymous Complaint" or "Report and Track"
• Fill form with details
• Get acknowledgment number
• Track status online

**Step 2: Visit Cybercrime Cell**
• Go to nearest Cyber Crime Police Station
• Available in every district
• File complaint in person
• Provide all evidence

**Step 3: Regular Police Station** (Alternative)
• If cyber cell far, go to regular police station
• They must register FIR for cognizable offenses
• Will transfer to cyber cell

**Types of Cybercrimes:**

1. **Online Financial Fraud:**
   • Phishing, fake websites
   • UPI/credit card fraud
   • Investment scams
   • Lottery scams
   
2. **Hacking:**
   • Account hacking
   • Data theft
   • Malware attacks
   
3. **Cyberstalking/Harassment:**
   • Online threats
   • Revenge porn
   • Morphed images
   • Fake profiles
   
4. **Identity Theft:**
   • Misuse of personal data
   • Fake documents
   • Impersonation

**Applicable Laws:**

**IT Act, 2000:**
• Section 43 - Unauthorized access (Compensation)
• Section 66 - Computer related offenses (3 years)
• Section 66C - Identity theft (3 years)
• Section 66D - Cheating by impersonation (3 years)
• Section 66E - Violation of privacy (3 years)
• Section 67 - Publishing obscene material (3-5 years)

**IPC Sections:**
• Section 419 - Cheating by impersonation
• Section 420 - Cheating and fraud
• Section 463-471 - Forgery
• Section 500 - Defamation
• Section 506 - Criminal intimidation

**Evidence to Collect:**
1. Screenshots (full webpage, include date, time, URL)
2. Transaction details (bank statements, UPI ID)
3. Communication (emails with headers, WhatsApp, SMS)
4. URLs & Links (fake websites, phishing links)
5. Device information (IP address, device ID)

**Documents Required:**
• Identity proof (Aadhaar/PAN)
• Address proof
• Bank account details (if financial fraud)
• Transaction receipts
• All evidence

**For Financial Fraud:**
1. **Immediately call bank:**
   • Report transaction
   • Block card/account
   • Request chargeback

2. **Report to NCRP:**
   • National Cybercrime Reporting Portal
   • Can freeze fraudulent accounts

3. **File complaint within 24 hours**

**Helpline Numbers:**
• Cyber Crime Helpline: 1930
• Women Cybercrime Helpline: 1091
• Child Helpline: 1098
• Banking Fraud: Contact your bank immediately

**Prevention Tips:**
• Never share OTP, CVV, PIN
• Don't click suspicious links
• Verify websites (https, padlock)
• Use strong passwords
• Enable 2-factor authentication""",
        "metadata": {
            "intent": "cyber_crime",
            "legal_basis": ["IT Act 2000", "IPC"],
            "complexity": "medium",
            "urgency": "immediate"
        }
    },
    
    {
        "url": "https://www.indiacode.nic.in",
        "title": "Juvenile Justice Act - Child in Conflict with Law",
        "content": """**Juvenile Justice (Care and Protection of Children) Act, 2015**

**Key Definitions:**
• Child: Person below 18 years
• Child in conflict with law: Alleged to have committed offense
• Child in need of care and protection: Requires help

**Age Determination:**
• If documents unavailable: Ossification test
• Benefit of doubt given to child
• Once declared juvenile, remains so throughout trial

**Categories of Offenses:**

1. **Petty Offenses:**
   • Punishment up to 3 years
   • Examples: Theft, simple hurt

2. **Serious Offenses:**
   • Punishment 3-7 years
   • Examples: Robbery, assault

3. **Heinous Offenses:**
   • Punishment 7+ years
   • Examples: Murder, rape, NDPS, POCSO cases

**Treatment of Children 16-18 Years:**
• For heinous offenses: May be tried as adults
• Juvenile Justice Board assesses mental and physical capacity
• If transferred to adult court: Children's Court tries them
• If not transferred: Rehabilitation for maximum 3 years

**Children Below 16 Years:**
• Cannot be tried as adults under any circumstances
• Maximum institutional stay: 3 years
• Focus on rehabilitation, not punishment

**Juvenile Justice Board (JJB):**
• Headed by Metropolitan Magistrate or Judicial Magistrate First Class
• Two social workers (one must be woman)
• Deals with children in conflict with law
• Has powers of Magistrate

**Child Welfare Committee (CWC):**
• Five members (at least one woman)
• Deals with children in need of care and protection
• Has powers of Magistrate

**Rights of Juvenile:**
• Right to be informed of charges
• Right to legal aid (free lawyer)
• Right to bail (more liberal than adults)
• Right to speedy trial
• Right to privacy (name not disclosed)
• Right to meet parents/guardian
• Right to education during custody

**Procedure:**
1. Child apprehended by police
2. Produced before JJB within 24 hours
3. Inquiry conducted (not trial)
4. Can be sent to observation home
5. Final order within 4 months (extendable to 8 months)

**Disposal Options:**
• Counseling
• Community service
• Fine (paid by parents)
• Probation
• Institutional stay (maximum 3 years)

**After Release:**
• Conviction not disqualification for employment
• Record not treated as criminal record
• Social reintegration support

**Important Protections:**
• No handcuffs to be used
• No association with adult criminals
• Separate trials
• Best interest of child paramount
• Rehabilitation over punishment

**Reporting:**
• Any person can report child in conflict with law
• Childline: 1098
• Special Juvenile Police Unit in every district""",
        "metadata": {
            "intent": "juvenile_justice",
            "legal_basis": ["JJ Act 2015"],
            "complexity": "high"
        }
    },
    
    {
        "url": "https://www.indiacode.nic.in",
        "title": "POCSO Act - Protection of Children from Sexual Offences",
        "content": """**POCSO Act 2012 - Comprehensive Protection for Children**

**Applicability:**
• Protects all children below 18 years
• Gender-neutral law (applies to boys and girls)
• Covers all forms of sexual abuse

**Types of Offenses:**

1. **Penetrative Sexual Assault:**
   • Any act of penetration
   • Punishment: Minimum 10 years, can extend to life imprisonment

2. **Aggravated Penetrative Sexual Assault:**
   • By person in position of trust (relative, teacher, doctor)
   • Causing grievous hurt
   • Punishment: Minimum 20 years, can extend to life imprisonment or death

3. **Sexual Assault:**
   • Sexual intent without penetration (touching private parts, etc.)
   • Punishment: Minimum 3 years, can extend to 5 years

4. **Aggravated Sexual Assault:**
   • By person in authority
   • Causing hurt
   • Punishment: Minimum 5 years, can extend to 7 years

5. **Sexual Harassment:**
   • Making sexual sounds, showing pornography
   • Stalking for sexual purposes
   • Punishment: Up to 3 years

6. **Use of Child for Pornography:**
   • Creating, storing, distributing child pornography
   • Punishment: Minimum 5 years, can extend to 7 years

**Special Provisions:**

**Reporting is Mandatory:**
• Every person who knows about abuse MUST report
• Failure to report: Punishment up to 6 months
• Reporting person's identity kept confidential

**Medical Examination:**
• Must be done within 24 hours
• By female doctor in presence of parent/woman
• No consent needed from child (deemed consent)
• Free medical treatment

**Recording of Statement:**
• By woman police officer
• At residence or place of choice of child
• In presence of parents/person child trusts
• Audio-video recording mandatory

**Special Courts:**
• Dedicated POCSO courts in every district
• Trial to be completed within 1 year
• In-camera trial (no public, no media)
• Child not to see accused (screen/one-way mirror)
• No aggressive cross-examination

**Support Person:**
• Child can have support person throughout
• Can be parent, counselor, or NGO representative

**Compensation:**
• Mandatory interim compensation within 30 days
• Final compensation decided by Special Court
• For medical expenses, rehabilitation, education

**Protection of Identity:**
• Child's name, address, photo not to be published
• Violators face imprisonment up to 6 months

**Presumption of Guilt:**
• If sexual assault proved, presumption is that accused committed it
• Burden of proof shifts to accused

**Zero FIR:**
• Can be filed at any police station
• Then transferred to concerned jurisdiction

**False Cases:**
• If complaint found false and malicious
• Complainant faces punishment for false information

**Age Determination:**
• If doubt: Ossification test
• Benefit of doubt to victim

**International Cooperation:**
• Law applies to Indian citizens committing offense abroad

**Child-Friendly Procedures:**
• Frequent breaks during testimony
• Support of interpreter, translator, expert
• Use of screen/video link
• Simple questions, no repeated questioning

**Rehabilitation:**
• Counseling for victim
• Education support
• Skill development
• Shelter if needed""",
        "metadata": {
            "intent": "child_protection",
            "legal_basis": ["POCSO Act 2012"],
            "complexity": "high",
            "urgency": "immediate"
        }
    }
]


# Add more comprehensive topics from existing data
def add_comprehensive_constitutional_data():
    """Add fundamental rights and constitutional articles"""
    return [
        {
            "url": "https://www.india.gov.in/my-government/constitution-india",
            "title": "Article 21 - Right to Life and Personal Liberty",
            "content": """Article 21 is the most comprehensive and important fundamental right in the Indian Constitution.

**Text of Article 21:**
"No person shall be deprived of his life or personal liberty except according to procedure established by law."

**Scope of Article 21:**
This article has been interpreted very expansively by the Supreme Court to include:

1. **Right to Life with Dignity:**
   • Life means more than mere animal existence
   • Includes right to live with human dignity
   • Right to livelihood
   • Right to shelter
   • Right to basic necessities of life

2. **Right to Education:**
   • Article 21A: Free and compulsory education for children aged 6-14 years

3. **Right to Health:**
   • Medical treatment
   • Pollution-free environment
   • Clean drinking water

4. **Right to Food:**
   • Food security
   • Mid-day meal scheme

5. **Right to Privacy:**
   • Landmark judgment in Justice K.S. Puttaswamy case (2017)
   • Privacy is fundamental right
   • Includes bodily privacy, informational privacy, decisional privacy

6. **Right to Speedy Trial:**
   • Justice delayed is justice denied
   • Accused cannot be kept in prolonged detention

7. **Right to Legal Aid:**
   • Free legal services to poor
   • Article 39A provides for legal aid

8. **Right Against Solitary Confinement:**
   • Solitary confinement violates human dignity

9. **Right Against Handcuffing:**
   • Handcuffing should be exception, not rule

10. **Right to Shelter:**
    • Pavement dwellers have right to shelter

11. **Right to Clean Environment:**
    • Pollution-free air and water
    • Protection against industrial pollution

12. **Right to Compensation:**
    • State liable to pay compensation for violating fundamental rights

**Procedure Established by Law:**
• Law must be valid, just, fair and reasonable
• Arbitrary laws violate Article 21
• Procedure must be in accordance with natural justice
• Right to be heard
• Right to notice

**Protection Under Article 21:**
• Applies to all persons (citizens and non-citizens)
• Can be suspended during emergency for certain activities

**Important Supreme Court Cases:**
1. **Maneka Gandhi v. Union of India (1978)**
   • Expanded interpretation of Article 21
   • Procedure must be just, fair and reasonable

2. **Francis Coralie Mullin v. Administrator UT of Delhi (1981)**
   • Right to life includes right to live with human dignity

3. **Bandhua Mukti Morcha v. Union of India (1984)**
   • Right to live with human dignity includes protection from exploitation

4. **Justice K.S. Puttaswamy v. Union of India (2017)**
   • Right to privacy is fundamental right

5. **Common Cause v. Union of India (2018)**
   • Right to die with dignity (passive euthanasia)

**Limitations:**
• Can be restricted only by reasonable restrictions
• Restrictions must be in public interest
• Cannot be suspended except during emergency (for certain activities)

**Enforcement:**
• Writ petition under Article 32 (Supreme Court)
• Writ petition under Article 226 (High Court)
• Public Interest Litigation (PIL) can be filed""",
            "metadata": {
                "intent": "fundamental_rights",
                "legal_basis": ["Article 21 Constitution of India"],
                "complexity": "medium"
            }
        },
        
        {
            "url": "https://www.india.gov.in/my-government/constitution-india",
            "title": "Article 14 - Right to Equality",
            "content": """Article 14 guarantees equality before law and equal protection of laws to all persons.

**Text of Article 14:**
"The State shall not deny to any person equality before the law or the equal protection of the laws within the territory of India."

**Two Components:**

1. **Equality Before Law:**
   • Negative concept
   • Absence of special privileges
   • No person is above law
   • Same law applies to all
   • British concept: Rule of law

2. **Equal Protection of Laws:**
   • Positive concept
   • Similar treatment to persons in similar circumstances
   • Equals must be treated equally
   • American concept

**Key Principles:**

**Reasonable Classification:**
• Article 14 permits reasonable classification
• Classification must be based on intelligible differentia
• Must have rational nexus with object sought to be achieved
• Cannot be arbitrary or discriminatory

**Examples of Valid Classification:**
• Women vs Men (for special protection to women)
• Children vs Adults (for child protection laws)
• Government employees vs Private employees
• Urban areas vs Rural areas (for different regulations)

**Arbitrary State Action:**
• Article 14 strikes at arbitrariness
• Arbitrariness and Article 14 are antithetical
• Every state action must be fair, just and reasonable
• Unreasonable laws violate Article 14

**Equality in Taxation:**
• Article 14 applies to tax laws
• But reasonable classification allowed
• Progressive taxation is valid

**Applies to All Persons:**
• Citizens and non-citizens both covered
• Companies, associations also included
• Binding on State (legislative, executive, judiciary)

**Important Cases:**

1. **State of West Bengal v. Anwar Ali Sarkar (1952)**
   • Classification must not be arbitrary
   
2. **Budhan Choudhry v. State of Bihar (1955)**
   • Test for reasonable classification laid down

3. **E.P. Royappa v. State of Tamil Nadu (1974)**
   • Arbitrary = violative of Article 14

4. **Maneka Gandhi v. Union of India (1978)**
   • Golden Triangle: Articles 14, 19, 21 interconnected

**Exceptions to Article 14:**

1. **Presidential and Gubernatorial Immunity:**
   • President and Governors immune during tenure
   • Article 361

2. **Foreign Sovereigns and Ambassadors:**
   • Diplomatic immunity under International Law

3. **Enemy Aliens:**
   • During war, enemy aliens can be treated differently

**Article 14 and Other Articles:**
• Overlaps with Article 15 (prohibition of discrimination)
• Overlaps with Article 16 (equality in public employment)
• Golden Triangle with Articles 19 and 21

**Remedies:**
• Writ under Article 32 (Supreme Court)
• Writ under Article 226 (High Court)
• Law violating Article 14 is void (Article 13)

**Modern Interpretation:**
• Substantive and procedural fairness required
• Rule of law
• Non-arbitrariness
• Legitimate expectation
• Proportionality""",
            "metadata": {
                "intent": "fundamental_rights",
                "legal_basis": ["Article 14 Constitution of India"],
                "complexity": "medium"
            }
        }
    ]


def main():
    """Generate comprehensive training data"""
    print("=" * 80)
    print("Creating Comprehensive Legal Training Data")
    print("=" * 80)
    
    # Start with structured priority data
    all_data = TRAINING_DATA.copy()
    
    # Add constitutional data
    const_data = add_comprehensive_constitutional_data()
    all_data.extend(const_data)
    
    # Load and add comprehensive knowledge
    comp_data = load_comprehensive_data()
    if comp_data:
        print(f"\n[OK] Loaded {len(comp_data)} additional legal documents")
        all_data.extend(comp_data)
    
    print(f"\n[INFO] Total documents: {len(all_data)}")
    
    # Save to legal_data.json
    output_path = Path("data/raw/legal_data.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)
    
    print(f"[OK] Saved comprehensive training data to {output_path}")
    print(f"[OK] Ready for model training")
    print("=" * 80)


if __name__ == "__main__":
    main()

