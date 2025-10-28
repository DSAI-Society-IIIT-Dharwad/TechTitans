"""
BATCH 2: More Legal Topics
Property, Banking, Marriage, Taxation, Common Scenarios
"""

import json
from pathlib import Path


BATCH2_LEGAL_DATA = [
    
    # ============ BANKING & FINANCIAL ============
    
    {
        "title": "Negotiable Instruments Act - Cheque Bounce (Section 138)",
        "content": """**Section 138 NI Act - Cheque Bounce**

**When is it an Offense:**
• Cheque dishonored due to insufficient funds
• Or exceeds arrangement with bank
• Cheque presented within 6 months of date (or validity period)

**Punishment:**
• Up to 2 years imprisonment
• Or fine up to twice the cheque amount
• Or both

**Procedure:**

**Step 1: Cheque Bounces**
• Bank returns cheque with "insufficient funds" or similar reason
• Get cheque return memo from bank

**Step 2: Send Legal Notice (Mandatory)**
• Must send within 30 days of receiving information about dishonor
• Demand payment within 15 days
• Send by registered post/courier
• Keep proof of sending and delivery

**Step 3: Wait 15 Days**
• If payment made: Matter closed
• If no payment: Proceed to court

**Step 4: File Complaint**
• File within 1 month of expiry of 15-day period
• In Magistrate court
• In area where:
  - Cheque was presented, OR
  - Payee's address, OR
  - Where cheque bounced

**Required Documents:**
1. Original bounced cheque
2. Cheque return memo
3. Legal notice sent
4. Proof of postal delivery
5. Reason for cheque (agreement/invoice)

**Defenses:**
1. Cheque was blank and misused
2. Amount was filled later
3. Signature forged
4. Cheque given as security
5. Debt already paid
6. Notice not received

**Compoundable:**
• Can be settled before trial
• With permission of court
• Payment + costs

**Time Frame:**
• Trial can take 1-3 years
• Appeals can extend further

**Interim Relief:**
• Court can order interim compensation
• Usually 20-25% of cheque amount
• As condition for bail

**Important:**
• Strict timelines - don't miss
• Keep all documentation
• Send notice by registered post
• Track delivery
• File complaint in time

**Alternative:**
• File civil suit for recovery
• Both criminal and civil can run parallel""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"act": "Negotiable Instruments Act", "section": "138", "category": "Banking"}
    },
    
    {
        "title": "Bank Loan Default and Recovery",
        "content": """**Bank Loan Default - What Happens and Your Rights**

**Types of Loans:**
1. **Secured Loans:**
   - Home loan, vehicle loan
   - Backed by collateral
   
2. **Unsecured Loans:**
   - Personal loan, credit card
   - No collateral

**What Happens When You Default:**

**Stage 1: Initial Default (1-90 days)**
• Bank sends reminders
• Calls from bank/recovery agents
• Penalty and late fees charged
• Interest continues

**Stage 2: NPA (90+ days)**
• Loan becomes Non-Performing Asset
• Reported to CIBIL (affects credit score)
• Recovery process intensifies

**Stage 3: Legal Action**
• For secured loans: Bank can invoke SARFAESI Act
• For unsecured loans: Civil suit or arbitration

**SARFAESI Act 2002 (for Secured Loans):**

**Bank's Power:**
• Can take possession of property without court
• Issue notice giving 60 days
• Sell property to recover dues

**Your Rights:**
• Receive proper 60-day notice
• Can file objection with DM within 30 days
• Can appeal to DRT (Debt Recovery Tribunal)
• Bank cannot use force or break open
• Bank cannot enter premises without notice

**DRT (Debt Recovery Tribunal):**
• For loan disputes above Rs. 20 lakh
• File within 45 days of bank action
• Quicker than civil court

**Personal Loan/Credit Card Default:**

**Recovery Agents:**
• Can call you
• Can visit your residence
• CANNOT harass, threaten, or abuse
• CANNOT visit between 7 PM - 7 AM
• CANNOT use force

**Your Rights:**
• RBI Guidelines protect you
• Can complain to bank if harassed
• Can complain to RBI Banking Ombudsman
• Can file police complaint if threatened

**One-Time Settlement (OTS):**
• Negotiate with bank
• Pay part amount in full settlement
• Usually 40-70% waiver possible
• Get written settlement agreement
• Take No Dues Certificate

**Restructuring:**
• Ask for loan restructuring
• Extended tenure
• Reduced EMI
• Moratorium period

**What Bank CANNOT Do:**
• Cannot threaten criminal action (loan default is civil matter)
• Cannot harass family members
• Cannot defame you
• Cannot take law into own hands
• Cannot forcibly enter home

**What You Should Do:**
1. Don't ignore bank notices
2. Communicate with bank
3. Explain financial difficulty
4. Request restructuring/OTS
5. Keep written records
6. If harassed, complain to RBI
7. Consult lawyer before signing any document

**Credit Score Impact:**
• Default reported to CIBIL
• Score drops significantly
• Affects future loans
• Remains for 7 years
• Can improve by settling dues

**Criminal Action:**
• Loan default itself NOT criminal
• But if cheque bounces: Section 138 NI Act
• Or if fraud involved: Section 420 IPC

**Important:**
• Loan default is a civil matter
• Not going to jail for personal loan default
• But can lose collateral in secured loans
• Maintain communication with bank
• Explore settlement options""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"category": "Banking", "act": "SARFAESI Act 2002"}
    },
    
    # ============ PROPERTY & RENT ============
    
    {
        "title": "Rent Agreement and Tenant Rights",
        "content": """**Rent Agreement - Complete Guide for Landlords and Tenants**

**Types of Rent Agreements:**

**1. Leave and License Agreement:**
• License to use property
• Not transfer of interest
• Most common in cities
• Valid for 11 months typically
• Can be renewed

**2. Lease Agreement:**
• Transfer of right to enjoy property
• For longer duration (usually years)
• Needs registration if more than 1 year

**Registration:**
• Agreement for 12+ months must be registered
• Stamp duty varies by state (usually 0.25% of rent x years)
• Registration fee

**Rights of Tenant:**
1. **Right to Peaceful Possession:**
   - Cannot be disturbed
   - Landlord cannot enter without permission
   
2. **Right to Basic Amenities:**
   - Water, electricity
   - Repairs by landlord
   
3. **Right to Not Pay More than Agreed Rent:**
   - Rent hike needs mutual consent
   
4. **Right to Notice:**
   - Adequate notice before eviction

**Rights of Landlord:**
1. **Receive Rent on Time:**
   - As per agreement
   
2. **Evict for Valid Reasons:**
   - Non-payment
   - Subletting without permission
   - Causing nuisance
   - Property needed for self-use
   
3. **Inspect Property:**
   - With reasonable notice

**Security Deposit:**
• Usually 2-3 months rent
• Cannot be adjusted against rent without consent
• Refundable after vacancy
• Can deduct damages

**Maintenance:**
• Minor repairs: Tenant
• Major repairs: Landlord
• Best to specify in agreement

**Rent Increase:**
• Only by mutual consent
• Or as per escalation clause
• Cannot force unilateral increase

**Eviction:**

**Valid Grounds for Eviction:**
1. Non-payment of rent for 6+ months
2. Subletting without permission
3. Using property for illegal purposes
4. Causing nuisance
5. Damaging property
6. Landlord needs for self/family use
7. Rebuilding/major repairs needed

**Eviction Procedure:**

**Step 1: Legal Notice**
• Give notice as per agreement
• Usually 1-3 months

**Step 2: If Tenant Doesn't Vacate**
• File eviction suit in civil court
• Or under Rent Control Act (if applicable)

**Step 3: Court Orders**
• If valid reason, court orders eviction
• Tenant must vacate

**Tenant Cannot Be Forcibly Evicted:**
• Landlord cannot cut water/electricity
• Cannot forcibly throw out
• Cannot change locks
• Must go through legal process
• If forcefully evicted: File police complaint

**What to Do if Landlord Forces You Out:**
1. File police complaint
2. File case for forcible dispossession
3. Can claim damages

**Non-Payment of Rent:**

**Landlord's Remedies:**
1. Send legal notice
2. File eviction suit
3. File civil suit for arrears
4. If cheque bounces: Section 138 NI Act case

**Rent Control Acts (State-Specific):**
• Many states have Rent Control Acts
• Protect tenants from eviction
• Cap rent increases
• Long legal process for eviction
• Check your state's law

**Tenancy Disputes:**
• File in civil court
• Or Rent Control Authority
• Can take 2-5 years

**Tips for Tenants:**
1. Always have written agreement
2. Pay rent by cheque/online (keep proof)
3. Keep copy of receipts
4. Document property condition at start
5. Don't damage property
6. Give proper notice before leaving
7. Settle disputes amicably

**Tips for Landlords:**
1. Thorough tenant verification
2. Written agreement mandatory
3. Police verification of tenant
4. Mention all terms clearly
5. Take adequate security deposit
6. Keep property inspection photos
7. Maintain good relationship

**Important:**
• Always have written rent agreement
• Register if duration > 11 months
• Don't take cash rent (no proof)
• Follow legal eviction process
• Don't resort to force""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"category": "Property Law", "act": "Rent Control Acts"}
    },
    
    {
        "title": "Property Disputes - Partition, Encroachment, Title Disputes",
        "content": """**Property Disputes - Complete Guide**

**Types of Property Disputes:**

**1. Partition of Property:**
When co-owners want to divide property.

**Who Can File:**
• Any co-owner
• Legal heirs wanting division

**Procedure:**
• File partition suit in civil court
• Court appoints commissioner
• Property surveyed and divided
• If not divisible physically: Sale ordered and proceeds divided

**Time:** 3-10 years

---

**2. Title Disputes:**
When ownership is challenged.

**Reasons:**
• Forged documents
• Sale by person without title
• Multiple sales
• Unclear inheritance

**Procedure:**
• File suit for declaration of title
• Provide evidence of ownership:
  - Sale deed
  - Tax receipts
  - Possession documents
  - Electricity bills
  - Ration card with address
• Court examines title
• Declares rightful owner

**Important Documents:**
• Original sale deed
• Chain of previous sale deeds (back to 30 years)
• Encumbrance certificate
• Property tax receipts
• 7/12 extract (in Maharashtra)
• Mutation records

---

**3. Encroachment:**
When someone illegally occupies your property.

**Types:**
• Government land encroachment
• Private property encroachment

**For Private Property:**

**Step 1: Send Legal Notice**
• Demand removal within 15 days

**Step 2: File Police Complaint**
• Under Section 441-447 IPC (criminal trespass)

**Step 3: File Civil Suit**
• For possession and injunction
• For damages

**Step 4: Get Injunction**
• Temporary injunction during trial
• Permanent after trial

**Forcible Dispossession:**
• If you had possession for 6+ months
• And forcibly thrown out
• File under Section 145/147 CrPC
• Or file suit for forcible dispossession
• Court restores possession

---

**4. Adverse Possession:**
Someone claiming property by continuous possession for 12 years.

**Requirements:**
• Continuous possession for 12 years
• Open, peaceful, and adverse
• Without permission of owner

**Defense:**
• Show you didn't abandon property
• Show encroacher had permission
• Show possession was not continuous

**To Prevent Adverse Possession:**
• Visit property regularly
• File trespass case within 12 years
• Keep tax receipts updated
• Maintain boundary walls

---

**5. Will Disputes:**
Challenging validity of will.

**Grounds to Challenge:**
• Testator was of unsound mind
• Will executed under duress/undue influence
• Forged signature
• Not properly witnessed
• Revoked by later will

**Procedure:**
• File suit to contest will
• Prove grounds
• If will invalid: Property distributed as per succession laws

---

**6. Specific Performance:**
When seller refuses to execute sale deed after taking money.

**Remedy:**
• File suit for specific performance
• Court can order seller to execute deed
• Or refund money with interest

**Time Limit:** 3 years from date of breach

---

**How to Verify Property Before Buying:**

**1. Title Verification:**
• Check sale deeds for last 30 years
• Verify chain of ownership
• Check for mortgages/liens

**2. Encumbrance Certificate:**
• Shows all transactions on property
• Available from Sub-Registrar office

**3. Property Tax Receipt:**
• In whose name
• All dues paid

**4. Physical Inspection:**
• Visit property
• Check boundaries
• Talk to neighbors

**5. Search Records:**
• Check mutation records
• Revenue records
• Survey numbers

**6. Legal Opinion:**
• Get lawyer to verify title
• Worth the cost

**7. No Objection Certificates:**
• From society/builder
• Development authority
• Tax clearance

---

**Prevention Better Than Cure:**

**For Owners:**
1. Keep all documents safe
2. Visit property regularly
3. Pay taxes on time
4. Keep records updated
5. Boundary walls/fencing
6. Don't leave property vacant too long
7. File case against encroachment immediately

**For Buyers:**
1. Thorough due diligence
2. Hire good lawyer
3. Check all documents
4. Physical verification
5. Don't pay full amount without registration
6. Register within time limit

**Common Mistakes:**
• Buying on power of attorney (risky)
• Not checking encumbrance certificate
• Ignoring tax receipts
• Trusting seller blindly
• Not registering sale deed

**Court Fees:**
• Based on property value
• Can be substantial
• Plan budget accordingly

**Important:**
• Property disputes take LONG time (years)
• Document everything
• Keep paying taxes even during dispute
• Consider settlement/mediation
• Consult good property lawyer""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"category": "Property Law"}
    },
    
    # ============ MARRIAGE & DIVORCE ============
    
    {
        "title": "Divorce Laws in India - Complete Guide",
        "content": """**Divorce Laws in India - Hindu, Muslim, Christian, Special Marriage Act**

**HINDU DIVORCE:**

**Applicable Laws:**
• Hindu Marriage Act, 1955
• Applies to Hindus, Buddhists, Jains, Sikhs

**Grounds for Divorce (Section 13):**

**For Both:**
1. Adultery
2. Cruelty (physical or mental)
3. Desertion for 2+ years
4. Conversion to another religion
5. Unsoundness of mind
6. Leprosy
7. Venereal disease
8. Renunciation of world
9. Not heard alive for 7+ years
10. No cohabitation after judicial separation for 1+ year
11. Not resumed cohabitation after restitution decree for 1+ year

**For Wife Only:**
12. Husband had another wife at time of marriage
13. Husband guilty of rape, sodomy, bestiality

**Mutual Consent Divorce (Section 13B):**
• Both agree to divorce
• Living separately for 1+ year
• Unable to live together
• Cannot live together in future

**Procedure for Mutual Consent:**
1. File joint petition
2. First motion
3. Wait 6 months (cooling period)
4. Second motion
5. Court grants divorce
6. Total time: 6-18 months

**Procedure for Contested Divorce:**
1. File petition in family court
2. Serve notice on spouse
3. Spouse files reply
4. Evidence stage
5. Arguments
6. Judgment
7. Time: 2-5 years (can extend further)

---

**MUSLIM DIVORCE:**

**Applicable Law:**
• Dissolution of Muslim Marriage Act, 1939
• Personal law

**Types:**

**1. Talaq:**
• By husband
• Triple talaq now banned (criminal offense)
• Must be pronounced once, wait 90 days (iddah), then can separate

**2. Khula:**
• By wife
• Return of mehr
• Husband's consent usually needed

**3. Mubarat:**
• Mutual consent

**4. Judicial Divorce (Section 2):**
Wife can seek divorce on grounds:
• Husband's whereabouts unknown for 4 years
• Failure to maintain for 2 years
• Imprisonment for 7+ years
• Impotence
• Cruelty
• Leprosy/venereal disease
• Insanity
• Marriage before 15 years (can repudiate at 18)

---

**CHRISTIAN DIVORCE:**

**Applicable Law:**
• Indian Divorce Act, 1869

**Grounds:**
• Adultery
• Ceased to be Christian
• Unsoundness of mind for 2+ years
• Leprosy/venereal disease for 2+ years
• Desertion for 2+ years
• Cruelty
• Not heard alive for 7+ years

---

**SPECIAL MARRIAGE ACT:**

**Applicable:**
• Inter-faith marriages
• Anyone can opt for this

**Grounds for Divorce:**
Same as Hindu Marriage Act

---

**MAINTENANCE:**

**During Divorce Proceedings (Interim):**
• Wife can claim maintenance under:
  - Section 24 HMA (Hindu)
  - Section 125 CrPC (all religions)
• Usually 1/3 to 1/5 of husband's income

**After Divorce (Permanent):**
• Alimony/maintenance
• One-time settlement OR
• Monthly maintenance
• Depends on husband's income, wife's needs, standard of living

**Factors Court Considers:**
1. Husband's income
2. Wife's income/ability to earn
3. Standard of living during marriage
4. Property owned
5. Duration of marriage
6. Age and health
7. Children's custody and needs

**Typical Amounts:**
• 25-40% of husband's gross income
• If wife working: Proportionately less
• One-time settlement: 20-30% of husband's assets

---

**CHILD CUSTODY:**

**Presumption:**
• Children below 7 years: Mother gets custody
• Above 7: Court decides based on child's welfare

**Factors:**
1. Age of child
2. Financial capacity
3. Emotional bond
4. Child's preference (if mature enough)
5. Parent's character
6. Stability

**Types:**
• Physical custody: Child lives with
• Legal custody: Decision-making rights
• Joint custody: Both share

**Visitation Rights:**
• Non-custodial parent gets visitation
• Usually every weekend or alternate weekends
• Holidays shared

---

**PROPERTY DIVISION:**

**Stridhan:**
• Wife's absolute property
• Gifts received during marriage
• Jewelry, clothes
• Must be returned

**Joint Property:**
• Divided based on contribution
• Or as per mutual agreement

**Self-Acquired Property:**
• Belongs to who earned
• But court may award share considering contribution

---

**PROCEDURE:**

**1. File Petition:**
• In family court
• Where:
  - Marriage solemnized
  - Last lived together
  - Wife residing (if deserted)

**2. Documents Needed:**
• Marriage certificate
• Proof of marriage (photos, invitation)
• Proof of cruelty (medical reports, messages, emails)
• Income proof
• Property documents

**3. Steps:**
• Petition filed
• Notice to spouse
• Reply
• Evidence
• Cross-examination
• Arguments
• Judgment

**4. Appeal:**
• To High Court within 90 days
• Further to Supreme Court

---

**IMPORTANT POINTS:**

**Grounds Must Be Proved:**
• Not enough to just allege
• Need evidence

**Cruelty Definition:**
• Physical: Easy to prove with medical reports
• Mental: Harder - need to show continuous harassment

**Desertion:**
• Must be without reasonable cause
• Without consent
• For continuous 2 years

**Mutual Consent Fastest:**
• 6-18 months
• Less traumatic
• Cheaper

**Contested Divorce:**
• 2-5 years minimum
• Expensive
• Emotionally draining

**Mediation:**
• Court refers to mediation
• Can help reach settlement
• Faster than trial

**False Cases:**
• If proven false
• Can face perjury charges
• Can lose maintenance

**Advice:**
1. Try counseling first
2. Mutual consent if possible
3. Keep all evidence
4. Don't give written consent under pressure
5. Hire good lawyer
6. Don't wash dirty linen in public
7. Think of children first
8. Avoid social media posts

**Helplines:**
• Women Helpline: 1091, 181
• Legal Aid: District Legal Services Authority
• Counseling: Family Courts have counselors""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"category": "Family Law", "act": "Hindu Marriage Act 1955"}
    },
    
    # ============ MISCELLANEOUS ============
    
    {
        "title": "How to File FIR - Complete Procedure",
        "content": """**How to File FIR (First Information Report) - Complete Guide**

**What is FIR:**
• First Information Report
• Formal complaint to police about cognizable offense
• Starts criminal investigation

**Cognizable vs Non-Cognizable:**

**Cognizable Offenses:**
• Police can arrest without warrant
• Police must register FIR
• Examples: Murder, rape, theft, robbery, assault, cheating (420)

**Non-Cognizable Offenses:**
• Police cannot arrest without warrant
• File complaint in Magistrate court
• Examples: Simple hurt (Section 323 if minor), defamation, trespass

**Who Can File FIR:**
• Victim
• Witness
• Anyone with knowledge of offense
• Even anonymous complaint

**Where to File:**

**1. At Police Station Where Crime Occurred:**
• Jurisdictional police station

**2. Zero FIR:**
• At ANY police station
• If you don't know jurisdiction
• Or in emergency
• That police station will transfer to concerned station

**How to File FIR:**

**Step 1: Go to Police Station**
• Approach Duty Officer/SHO
• Tell about offense

**Step 2: Oral or Written**
• Can give orally (police will write)
• Or give written complaint
• Oral preferred if emotional/injured

**Step 3: FIR Drafted**
• Police write FIR
• In local language or English
• Your statement recorded

**Step 4: Read and Sign**
• FIR read out to you
• Check all details correct
• Sign

**Step 5: Get Copy**
• You get free copy immediately
• Keep it safe
• Note FIR number

**What to Include in FIR:**
1. Date, time, place of offense
2. Detailed description of what happened
3. Names of accused (if known)
4. Names of witnesses
5. Description of accused (if don't know name)
6. Details of loss/injury
7. Your contact details

**Important Points:**

**FIR Cannot Be Changed:**
• Once registered, cannot be changed
• So be careful what you state
• Think before speaking

**Police MUST Register FIR:**
• For cognizable offenses
• Cannot refuse
• If refuse: Complaint to SP/Commissioner

**If Police Refuse to Register FIR:**

**Option 1: Insist**
• Quote Section 154 CrPC
• Tell them it's mandatory
• Record conversation (not illegal)

**Option 2: Written Complaint**
• Give written complaint
• Police must give receipt
• With stamp and signature

**Option 3: Complaint to SP/SSP**
• Send complaint to Superintendent of Police
• SP will direct registration

**Option 4: Magistrate Court**
• File complaint directly in court
• Under Section 156(3) CrPC
• Magistrate will order police to register FIR

**Option 5: Judicial Magistrate**
• File private complaint
• Magistrate can take cognizance
• Issue process against accused

**After FIR Registered:**

**Investigation Starts:**
1. Police investigate
2. Collect evidence
3. Record statements
4. Arrest accused (if needed)
5. File charge sheet within 60-90 days

**Your Cooperation:**
• Give statement under Section 161 CrPC
• Help in investigation
• Identify accused
• Provide evidence

**False FIR:**
• Don't file false FIR
• If proven false: Punishment under Section 182 IPC (up to 6 months)
• Or prosecution for defamation

**Online FIR:**
Many states allow online FIR for certain offenses:
• Lost documents
• Cyber crimes
• Vehicle theft
• Check your state police website

**FIR for Women:**
• Woman can't be arrested after sunset and before sunrise
• Must be arrested by woman police officer
• Statement recorded at residence or place of choice
• For rape: Medical exam by woman doctor

**Important Rights:**

**1. Right to Register FIR:**
• Police cannot refuse

**2. Right to Free Copy:**
• Immediately after registration

**3. Right to Know Investigation Status:**
• After 15 days of FIR
• Can ask for progress

**4. Right to Speedy Investigation:**
• Investigation should not be delayed

**5. Right to Approach Magistrate:**
• If police not investigating properly

**Types of Complaints:**

**1. FIR:**
• For cognizable offenses
• At police station

**2. NCR (Non-Cognizable Report):**
• For non-cognizable offenses
• Police won't investigate without Magistrate's order

**3. Zero FIR:**
• At any police station

**4. Private Complaint:**
• Directly in Magistrate court

**Dos:**
1. Go to police station immediately
2. Be calm and clear
3. Give all details
4. Note FIR number
5. Keep copy safe
6. Follow up investigation
7. Cooperate with police

**Don'ts:**
1. Don't file false FIR
2. Don't exaggerate
3. Don't name innocent persons
4. Don't give statement under pressure
5. Don't sign without reading
6. Don't delay filing

**Important:**
• FIR is crucial document
• Used in trial as evidence
• Contradictions later can weaken case
• So be accurate and truthful
• Keep FIR copy safely
• Take it seriously""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"section": "154", "act": "CrPC", "category": "Criminal Procedure"}
    },
    
    {
        "title": "Passport Application and Issues",
        "content": """**Passport in India - Complete Guide**

**Types of Passports:**

**1. Ordinary Passport (Blue):**
• For common citizens
• Valid for 10 years (adults)
• Valid for 5 years (minors below 18)

**2. Official Passport (White):**
• For government officials on official duty

**3. Diplomatic Passport (Maroon):**
• For diplomats

**How to Apply for New Passport:**

**Step 1: Register on Portal**
• Visit www.passportindia.gov.in
• Register with email ID
• Login

**Step 2: Fill Application**
• Select "Apply for Fresh Passport"
• Fill form carefully
• Upload documents:
  - Proof of present address
  - Proof of DOB
  - Photo (white background, 4.5cm x 3.5cm)

**Documents Required:**

**Proof of Address:**
• Aadhaar card
• Voter ID
• Electricity bill
• Ration card
• Rent agreement + owner's proof

**Proof of Date of Birth:**
• Birth certificate
• School leaving certificate (Class 10)
• PAN card
• Aadhaar card

**Step 3: Pay Fee**
• 36-page booklet: Rs. 1,500
• 60-page booklet: Rs. 2,000
• Tatkal: Additional Rs. 2,000
• Pay online

**Step 4: Book Appointment**
• Select PSK (Passport Seva Kendra)
• Select date and time
• Print application receipt

**Step 5: Visit PSK**
• Reach 15 minutes before appointment
• Carry:
  - Application receipt
  - Original documents
  - Self-attested copies
• Biometrics taken
• Documents verified
• Interview (brief)

**Step 6: Police Verification**
• Police visit your address
• Verify documents
• Check if any criminal case
• Usually takes 15-45 days

**Step 7: Passport Dispatched**
• After police clearance
• Sent by Speed Post
• Receive in 7-10 days

**Total Time:**
• Normal: 30-45 days
• Tatkal: 7-15 days

---

**Passport Reissue/Renewal:**

**When to Renew:**
• About to expire (within 1 year)
• Expired
• Pages full
• Lost/damaged
• Change of address/name

**Procedure:**
Same as fresh, but:
• Select "Reissue"
• Mention old passport details
• Attach old passport (if available)

**Police Verification:**
• May be exempted if renewed within 3 years at same address
• Or may go for post-police verification (passport issued first)

---

**Tatkal Passport:**

**Eligibility:**
• Urgent need
• Can prove with:
  - Visa appointment letter
  - Medical emergency
  - Death of family member abroad

**Additional Fee:** Rs. 2,000

**Time:** 7-15 days

---

**Police Verification:**

**What Police Check:**
1. Address verification
2. Antecedent verification (criminal record)
3. References
4. Employment verification

**If Adverse Report:**
• Passport denied
• Can re-apply after clearing issues

**Police Delays:**
• Very common
• Can take months
• Follow up with local police station
• Or apply for Tatkal

---

**Common Issues & Solutions:**

**1. Police Verification Pending:**
• Follow up with police station
• Meet SHO/Inspector
• Take local MLA/politician help if needed
• File RTI to know status

**2. Application Rejected:**
• Reason given
• Rectify and re-apply
• Or appeal

**3. Lost Passport:**
• File police complaint immediately
• Apply for reissue with "Lost" category
• Provide police complaint copy

**4. Name/DOB Mismatch in Documents:**
• Get affidavit for name change
• Publish in newspaper
• Attach to application

**5. ECR (Emigration Check Required):**
• If you haven't passed Class 10
• Need emigration clearance for some countries
• Get ECNR by passing Class 10 or getting diploma/degree

---

**Minor's Passport:**

• Parent must apply
• Valid for 5 years only
• No need to visit PSK for below 4 years (documents sent by post)
• Both parents' consent required
• Birth certificate mandatory

---

**Passport for Adopted Child:**
• Adoption deed from court
• Guardian certificate
• Proof of adoption

---

**Address Proof Issues:**

**If Renting:**
• Rent agreement + owner's ID proof
• Or owner's affidavit

**If Staying with Relatives:**
• Relative's affidavit
• Relative's ID proof

**If Address Different from ID:**
• Show current address proof
• OR
• Mention permanent address

---

**Important Points:**

1. Fill form carefully (no mistakes)
2. Upload correct size photo
3. All documents should match
4. If mismatch, get affidavit
5. Reach PSK on time
6. Be polite with officers
7. Follow up police verification
8. Keep checking status online

**Helpline:**
• 1800-258-1800 (toll-free)

**Complaints:**
• On passport portal
• Or write to Regional Passport Officer

**RTI:**
• Can file RTI for delays
• Under RPO office

**Important:**
• Passport is important document
• Keep safely
• Make photocopy
• Don't laminate
• Report if lost immediately""",
        "url": "https://www.passportindia.gov.in",
        "metadata": {"category": "Passport", "authority": "MEA"}
    },
]

def main():
    """Add batch 2 legal data"""
    print("=" * 80)
    print("BATCH 2: Legal Data Expansion")
    print("=" * 80)
    
    # Load existing
    data_file = Path("data/raw/legal_data.json")
    with open(data_file, 'r', encoding='utf-8') as f:
        existing_data = json.load(f)
    print(f"\n[OK] Loaded {len(existing_data)} existing documents")
    
    # Add batch 2
    all_data = existing_data + BATCH2_LEGAL_DATA
    
    print(f"[OK] Added {len(BATCH2_LEGAL_DATA)} new documents")
    print(f"\n[INFO] Total documents: {len(all_data)}")
    
    # Save
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)
    
    print(f"[OK] Saved to {data_file}")
    print("=" * 80)


if __name__ == "__main__":
    main()

