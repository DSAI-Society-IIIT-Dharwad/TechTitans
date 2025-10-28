"""
Create Structured Legal Training Data
With Intent Classification, QA Pairs, and Entity Recognition
"""

import json
from pathlib import Path


# COMPREHENSIVE STRUCTURED LEGAL DATA
STRUCTURED_LEGAL_DATA = {
    "intents": [
        {
            "tag": "corporal_punishment",
            "patterns": [
                "teacher beat student",
                "teacher hit child",
                "corporal punishment in school",
                "what to do if teacher beats student",
                "teacher physically abused student",
                "school teacher violence",
                "teacher slapped student"
            ],
            "entities": ["TEACHER", "STUDENT", "SCHOOL", "ASSAULT"],
            "legal_basis": ["Section 323 IPC", "Section 325 IPC", "RTE Act 2009", "Juvenile Justice Act"],
            "qa_pairs": [
                {
                    "question": "What to do if a teacher beats a student severely?",
                    "answer": """**Immediate Actions:**

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
                    "complexity": "high_priority",
                    "urgency": "immediate"
                },
                {
                    "question": "Is corporal punishment legal in Indian schools?",
                    "answer": """**NO. Corporal Punishment is COMPLETELY ILLEGAL in India.**

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
                    "complexity": "basic",
                    "urgency": "high"
                }
            ]
        },
        
        {
            "tag": "property_inheritance",
            "patterns": [
                "property after parents death",
                "house registration after demise",
                "inheritance law",
                "property transfer procedure",
                "succession certificate",
                "legal heir certificate"
            ],
            "entities": ["PROPERTY", "INHERITANCE", "SUCCESSION", "LEGAL_HEIR"],
            "legal_basis": ["Hindu Succession Act 1956", "Indian Succession Act 1925", "Transfer of Property Act 1882"],
            "qa_pairs": [
                {
                    "question": "How to register house after parents demise?",
                    "answer": """**Complete Procedure for House Registration After Parents' Death:**

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
• Can be sent to India and adjudicated

**Next Steps:**
1. Gather all documents
2. Get legal heir certificate
3. Apply for mutation
4. If needed, register release/relinquishment deed
5. Update property tax records""",
                    "complexity": "high",
                    "urgency": "medium"
                }
            ]
        },

        {
            "tag": "domestic_violence",
            "patterns": [
                "wife beating",
                "husband abuse",
                "domestic violence",
                "protection order",
                "498a",
                "cruelty by husband"
            ],
            "entities": ["DOMESTIC_VIOLENCE", "PROTECTION_ORDER", "498A"],
            "legal_basis": ["Section 498A IPC", "Protection of Women from Domestic Violence Act 2005"],
            "qa_pairs": [
                {
                    "question": "What to do in case of domestic violence?",
                    "answer": """**Immediate Actions for Domestic Violence Victims:**

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
• Applies to:
  - Husband
  - In-laws (if they also committed cruelty)

**Under DV Act 2005:**
• Protection order - Stop violence
• Residence order - Right to live in shared household
• Monetary relief - Maintenance, medical expenses
• Compensation - For mental agony, injuries
• Custody order - Custody of children
• Recovery of stridhan - Your jewelry, gifts

**Who Can File:**
• Wife (legally married or live-in partner)
• Sister
• Mother
• Any woman in shared household

**Where to File:**
• Police station (FIR)
• Magistrate court (DV Act complaint)
• Protection Officer (at District level)
• Service Provider NGOs

**Required Documents:**
• Marriage certificate/proof
• Identity proof
• Address proof
• Medical certificates
• Evidence of violence
• Witness details

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

**Note:** You can file BOTH criminal (498A) AND civil (DV Act) cases simultaneously.

**Don't Delay:** Act immediately for your safety and legal rights.""",
                    "complexity": "high_priority",
                    "urgency": "immediate"
                }
            ]
        },

        {
            "tag": "cyber_crime",
            "patterns": [
                "online fraud",
                "cybercrime",
                "hacking",
                "online harassment",
                "phishing",
                "identity theft"
            ],
            "entities": ["CYBERCRIME", "ONLINE_FRAUD", "HACKING"],
            "legal_basis": ["IT Act 2000", "IPC Sections 419, 420, 463-471"],
            "qa_pairs": [
                {
                    "question": "How to file cybercrime complaint?",
                    "answer": """**Complete Guide to File Cybercrime Complaint:**

**Step 1: Report Online** (Fastest Method)
• Visit: www.cybercrime.gov.in
• Click "Report Anonymous Complaint" or "Report and Track"
• Fill form with details:
  - Type of cybercrime
  - Description
  - Evidence (screenshots, URLs, etc.)
• Get acknowledgment number
• Track status online

**Step 2: Visit Cybercrime Cell**
• Go to nearest Cyber Crime Police Station
• Available in every district
• File complaint in person
• Provide:
  - Written complaint
  - All evidence
  - Transaction details (if fraud)
  - Screenshots, emails, messages

**Step 3: Regular Police Station** (Alternative)
• If cyber cell far, go to regular police station
• They must register FIR for cognizable offenses
• Will transfer to cyber cell for investigation

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

1. **Screenshots:**
   • Full webpage/message
   • Include date, time, URL
   • Don't crop

2. **Transaction Details:**
   • Bank statements
   • UPI transaction ID
   • Payment gateway details
   • Merchant information

3. **Communication:**
   • Emails (full with headers)
   • WhatsApp messages
   • SMS
   • Call recordings

4. **URLs & Links:**
   • Fake website links
   • Phishing links
   • Social media profiles

5. **Device Information:**
   • IP address
   • Device ID
   • Email IDs used

**Documents Required:**
• Identity proof (Aadhaar/PAN)
• Address proof
• Bank account details (if financial fraud)
• Transaction receipts
• All evidence mentioned above

**Action by Cyber Cell:**
• Register FIR
• Trace IP address, phone numbers
• Coordinate with banks to freeze accounts
• Contact platforms (Facebook, Google, etc.) to block accounts
• Forensic analysis
• Arrest culprits

**Time Frame:**
• Online complaint: Instant acknowledgment
• FIR: Same day
• Investigation: 60-90 days (extendable)
• Refund (if fraud): 2-6 months

**For Financial Fraud:**
1. **Immediately call bank:**
   • Report transaction
   • Block card/account
   • Request chargeback

2. **Report to NCRP:**
   • National Cybercrime Reporting Portal
   • Can freeze fraudulent accounts

3. **File complaint within 24 hours:**
   • Better chances of recovery
   • Bank can reverse transaction

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
• Enable 2-factor authentication
• Regular backup data

**Remember:** Time is critical in cybercrimes. Report immediately for better chances of action and recovery.""",
                    "complexity": "medium",
                    "urgency": "immediate"
                }
            ]
        }
    ]
}


def create_training_dataset():
    """Create comprehensive structured training dataset"""
    
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    
    # Convert to document format
    documents = []
    
    for intent in STRUCTURED_LEGAL_DATA["intents"]:
        for qa in intent["qa_pairs"]:
            doc = {
                "url": "https://www.indiacode.nic.in",
                "title": qa["question"],
                "content": qa["answer"],
                "metadata": {
                    "intent": intent["tag"],
                    "patterns": intent["patterns"],
                    "entities": intent["entities"],
                    "legal_basis": intent["legal_basis"],
                    "complexity": qa.get("complexity", "medium"),
                    "urgency": qa.get("urgency", "normal")
                },
                "qa_pairs": [],
                "scraped_at": "2025-10-28 03:00:00"
            }
            documents.append(doc)
    
    # Save
    json_path = Path("data/raw/legal_data.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(documents, f, ensure_ascii=False, indent=2)
    
    print(f"[OK] Created {len(documents)} structured QA documents")
    print("\nIntents covered:")
    for intent in STRUCTURED_LEGAL_DATA["intents"]:
        print(f"  - {intent['tag']}: {len(intent['qa_pairs'])} QA pairs")
    print(f"\nTotal patterns: {sum(len(i['patterns']) for i in STRUCTURED_LEGAL_DATA['intents'])}")


if __name__ == "__main__":
    print("="*80)
    print("CREATING STRUCTURED LEGAL TRAINING DATA")
    print("="*80)
    print()
    create_training_dataset()
    print()
    print("Next: Run 'python train_model.py' to train with structured data")

