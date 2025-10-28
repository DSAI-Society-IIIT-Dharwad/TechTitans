"""
Add Comprehensive Indian Legal Knowledge
Includes Constitution, IPC, CrPC, and common legal information
"""

import json
from pathlib import Path


# Comprehensive Indian Legal Knowledge Base
INDIAN_LEGAL_KNOWLEDGE = [
    {
        "title": "Right to Equality - Article 14",
        "category": "Fundamental Rights",
        "content": """Article 14 of the Indian Constitution guarantees equality before law and equal protection of laws. 

Key Points:
• The State shall not deny to any person equality before the law or the equal protection of the laws within the territory of India
• This right is available to all persons - citizens and non-citizens alike
• It prohibits discrimination and ensures equal treatment in similar circumstances
• Forms the foundation of rule of law in India

Applications:
- No person can be discriminated against based on arbitrary classification
- Laws must apply equally to all persons in similar circumstances
- Special provisions can be made for disadvantaged groups (reservation policies)
""",
        "url": "https://www.india.gov.in/constitution",
        "metadata": {"section": "Article 14", "act": "Indian Constitution"}
    },
    
    {
        "title": "Right to Freedom - Article 19",
        "category": "Fundamental Rights",
        "content": """Article 19 of the Indian Constitution guarantees six fundamental freedoms to all citizens of India.

Six Freedoms:
1. Freedom of speech and expression
2. Freedom to assemble peaceably and without arms
3. Freedom to form associations or unions
4. Freedom to move freely throughout India
5. Freedom to reside and settle in any part of India
6. Freedom to practice any profession, or to carry on any occupation, trade or business

Reasonable Restrictions:
The State can impose reasonable restrictions on these freedoms in the interests of:
• Sovereignty and integrity of India
• Security of the State
• Public order, decency, or morality
• Contempt of court
• Defamation
• Incitement to an offense

This right is only available to citizens of India, not to foreign nationals.
""",
        "url": "https://www.india.gov.in/constitution",
        "metadata": {"section": "Article 19", "act": "Indian Constitution"}
    },
    
    {
        "title": "Right Against Exploitation - Article 23-24",
        "category": "Fundamental Rights",
        "content": """Articles 23 and 24 protect citizens against exploitation.

Article 23 - Prohibition of Traffic in Human Beings:
• Prohibits traffic in human beings and forced labor (begar)
• Any violation is punishable by law
• Exception: State can impose compulsory service for public purposes (like military service)

Article 24 - Prohibition of Child Labor:
• No child below 14 years shall be employed in any factory, mine, or hazardous employment
• Protects children from exploitation
• Aims to ensure proper childhood and education for all children

Impact:
- Child labor is a punishable offense
- Bonded labor and human trafficking are criminal offenses
- Forced labor without payment is unconstitutional
""",
        "url": "https://www.india.gov.in/constitution",
        "metadata": {"section": "Article 23-24", "act": "Indian Constitution"}
    },
    
    {
        "title": "Right to Constitutional Remedies - Article 32",
        "category": "Fundamental Rights",
        "content": """Article 32 is called the 'Heart and Soul of the Constitution' by Dr. B.R. Ambedkar.

Key Features:
• Guarantees the right to approach the Supreme Court for enforcement of Fundamental Rights
• Supreme Court has the power to issue writs for enforcement of rights
• This right cannot be suspended except during Emergency

Five Types of Writs:
1. Habeas Corpus - "You may have the body" - to produce person before court
2. Mandamus - "We command" - to compel public authorities to perform duties
3. Prohibition - To prevent lower courts from exceeding jurisdiction
4. Certiorari - To quash orders of lower courts/tribunals
5. Quo Warranto - "By what authority" - to question someone's right to hold public office

This article makes Fundamental Rights enforceable and provides a constitutional remedy for their violation.
""",
        "url": "https://www.india.gov.in/constitution",
        "metadata": {"section": "Article 32", "act": "Indian Constitution"}
    },
    
    {
        "title": "Section 420 IPC - Cheating and Dishonestly Inducing Delivery of Property",
        "category": "Criminal Law",
        "content": """Section 420 of Indian Penal Code deals with cheating and dishonest inducement.

Offense:
Whoever cheats and thereby dishonestly induces the person deceived to deliver any property to any person, or to make, alter, or destroy the whole or any part of a valuable security.

Punishment:
• Imprisonment up to 7 years
• Fine
• Or both

Elements Required:
1. Deception - The accused must have deceived someone
2. Dishonest Inducement - The deception must have induced the victim to part with property
3. Mens Rea - There must be fraudulent or dishonest intention

Examples:
- Selling fake gold as real gold
- Taking advance payment and not delivering goods/services
- Identity theft for financial gain
- Fake job offers demanding fees
- Online fraud and scams

This is a cognizable, non-bailable, and non-compoundable offense.
""",
        "url": "https://www.indiacode.nic.in/ipc",
        "metadata": {"section": "420", "act": "Indian Penal Code"}
    },
    
    {
        "title": "Section 375-376 IPC - Rape",
        "category": "Criminal Law",
        "content": """Sections 375 and 376 of IPC deal with rape and its punishment.

Definition (Section 375):
A man commits rape if he has sexual intercourse with a woman under circumstances falling under any of seven descriptions, primarily without her consent or with consent obtained by coercion, fraud, or when she is unable to consent.

Punishment (Section 376):
• Minimum: 7 years (can extend to 10 years for normal cases)
• Maximum: Life imprisonment
• Also liable to fine

Aggravated Forms (More Severe Punishment):
• Gang rape - Minimum 20 years, can extend to life
• Rape of minor below 16 years - Minimum 20 years
• Rape of minor below 12 years - Life imprisonment or death
• Rape by police officer, public servant, armed forces personnel - Minimum 10 years

Important Points:
- Marital rape of wife above 15 years is not recognized as rape under IPC (controversial)
- Medical examination of victim mandatory
- Statement of victim recorded by magistrate
- Identity of victim must be protected
- Rape is a cognizable, non-bailable, and non-compoundable offense

Recent Amendments:
The Criminal Law Amendment Act 2013 (after Nirbhaya case) made punishments more stringent.
""",
        "url": "https://www.indiacode.nic.in/ipc",
        "metadata": {"section": "375-376", "act": "Indian Penal Code"}
    },
    
    {
        "title": "Section 498A IPC - Cruelty by Husband or Relatives",
        "category": "Criminal Law - Women Protection",
        "content": """Section 498A IPC protects married women from cruelty by husband and in-laws.

Offense:
Whoever, being the husband or relative of the husband of a woman, subjects such woman to cruelty shall be punished.

Definition of Cruelty:
1. Any willful conduct likely to drive the woman to commit suicide or cause grave injury
2. Harassment with a view to coerce her or her relatives to meet unlawful demands for property/dowry

Punishment:
• Imprisonment up to 3 years
• Fine
• Or both

Important Features:
- Cognizable offense (police can arrest without warrant)
- Non-bailable offense
- Non-compoundable (cannot be settled out of court without court permission)
- Only women can file complaints under this section

Common Situations:
• Dowry harassment
• Physical or mental torture
• Emotional abuse
• Harassment for not bringing enough dowry
• Threats and coercion

Supreme Court Guidelines:
- Preliminary inquiry before arrest recommended
- Arrest should not be automatic
- Magistrate should apply judicial mind before issuing warrant
- Misuse should be prevented
""",
        "url": "https://www.indiacode.nic.in/ipc",
        "metadata": {"section": "498A", "act": "Indian Penal Code"}
    },
    
    {
        "title": "Hindu Succession Act, 1956",
        "category": "Property & Inheritance Law",
        "content": """The Hindu Succession Act, 1956 governs succession and inheritance among Hindus, Buddhists, Jains, and Sikhs.

Key Provisions:

Class I Heirs (Get First Preference):
• Son, daughter, widow, mother
• Son/daughter of predeceased son
• Son/daughter of predeceased daughter
• Widow/son/daughter of predeceased son of predeceased son

Class II Heirs (If no Class I heirs):
• Father, siblings, children of predeceased siblings, etc.

Intestate Succession (Death Without Will):
• Self-acquired property is divided equally among Class I heirs
• If no Class I heirs, then Class II heirs inherit
• If no heirs, property goes to agnates (paternal relatives), then cognates (maternal relatives)

Daughter's Rights:
• 2005 Amendment: Daughters have equal rights as sons in coparcenary property
• Can demand partition
• Have same rights and liabilities
• Applies retrospectively from 1956

Succession to Widow:
• Widow takes husband's share along with children
• Gets equal share as children in husband's property

Important Points:
- Hindu Undivided Family (HUF) property follows different rules
- Ancestral property and self-acquired property treated differently
- Wills can override intestate succession
- Muslims, Christians, Parsis have separate succession laws
""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"act": "Hindu Succession Act, 1956"}
    },
    
    {
        "title": "Consumer Protection Act, 2019",
        "category": "Consumer Rights",
        "content": """The Consumer Protection Act, 2019 protects consumer rights and provides mechanism for redressal.

Who is a Consumer?
Any person who:
• Buys goods for consideration
• Hires services for consideration
• Beneficiary of such goods/services with approval of buyer
(Excludes goods bought for resale or commercial purpose)

Consumer Rights:
1. Right to Safety - Protection against hazardous goods
2. Right to Information - About quality, quantity, potency, purity, standard, price
3. Right to Choose - Access to variety of goods at competitive prices
4. Right to be Heard - Representation in consumer forums
5. Right to Seek Redressal - Against unfair trade practices
6. Right to Consumer Education

Three-Tier Dispute Resolution:
1. District Consumer Disputes Redressal Forum - Claims up to ₹1 crore
2. State Consumer Disputes Redressal Commission - Claims ₹1-10 crore
3. National Consumer Disputes Redressal Commission - Claims above ₹10 crore

Unfair Trade Practices:
• False/misleading advertisements
• Defective goods
• Deficient services
• Overcharging
• Misleading offers and schemes

Remedies Available:
- Removal of defects
- Replacement of goods
- Return of price paid
- Compensation for loss or injury
- Removal of deficiency in services
- Discontinuation of unfair practices
- Punitive damages

Time Limit:
Consumer complaints must be filed within 2 years of cause of action.
""",
        "url": "https://www.indiacode.nic.in",
        "metadata": {"act": "Consumer Protection Act, 2019"}
    },
    
    {
        "title": "Right to Information (RTI) Act, 2005",
        "category": "Public Rights",
        "content": """The Right to Information Act empowers citizens to question the government and access information.

Key Features:
• Citizens can request information from public authorities
• Authorities must respond within 30 days
• Information about self must be provided within 48 hours
• Small fee for filing application (usually ₹10)

Who Can File RTI:
• Any citizen of India
• Can file for any information from public authorities
• Can be filed online or offline

What Information Can Be Sought:
• Any information held by public authorities
• Documents, records, opinions, advice, reports, press releases, contracts, etc.
• Includes information in electronic form

Exemptions:
• Information affecting national security
• Trade secrets
• Breach of parliamentary privilege
• Personal information that has no public interest
• Information received in confidence from foreign governments

How to File:
1. Write application addressed to Public Information Officer (PIO)
2. Mention specific information required
3. Pay prescribed fee (₹10 in most states)
4. Submit at designated office or online

Time Limits:
• Normal reply: 30 days
• Life and liberty cases: 48 hours
• If information concerns a third party: 40 days

Appeal Process:
• First Appeal: To superior officer within 30 days
• Second Appeal: To State/Central Information Commission within 90 days

Penalties:
PIOs can be fined ₹250/day (up to ₹25,000) for delay or denial without reasonable cause.
""",
        "url": "https://www.rti.gov.in",
        "metadata": {"act": "Right to Information Act, 2005"}
    }
]


def save_knowledge_base():
    """Save the comprehensive knowledge base"""
    
    # Create data directory if it doesn't exist
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    
    # Convert to scraper format
    formatted_data = []
    for item in INDIAN_LEGAL_KNOWLEDGE:
        formatted_data.append({
            "url": item["url"],
            "title": item["title"],
            "content": item["content"],
            "metadata": {
                "category": item["category"],
                **item["metadata"]
            },
            "qa_pairs": [],
            "scraped_at": "2025-10-28 00:00:00"
        })
    
    # Load existing data if any
    json_path = Path("data/raw/legal_data.json")
    if json_path.exists():
        with open(json_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        print(f"Found {len(existing_data)} existing documents")
        formatted_data = existing_data + formatted_data
    
    # Save to JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(formatted_data, f, ensure_ascii=False, indent=2)
    
    print(f"[OK] Saved {len(formatted_data)} documents to {json_path}")
    
    # Also save as text
    text_path = Path("data/raw/legal_data.txt")
    with open(text_path, 'w', encoding='utf-8') as f:
        for item in formatted_data:
            f.write(f"{'='*80}\n")
            f.write(f"TITLE: {item['title']}\n")
            f.write(f"URL: {item['url']}\n")
            f.write(f"{'='*80}\n\n")
            f.write(f"{item['content']}\n\n")
    
    print(f"[OK] Saved text version to {text_path}")
    print()
    print("Next steps:")
    print("1. Run: python train_model.py")
    print("2. This will rebuild the vectorstore with all the legal knowledge")


if __name__ == "__main__":
    print("="*80)
    print("ADDING COMPREHENSIVE INDIAN LEGAL KNOWLEDGE")
    print("="*80)
    print()
    print(f"Adding {len(INDIAN_LEGAL_KNOWLEDGE)} legal documents:")
    for item in INDIAN_LEGAL_KNOWLEDGE:
        print(f"  • {item['title']}")
    print()
    
    save_knowledge_base()

