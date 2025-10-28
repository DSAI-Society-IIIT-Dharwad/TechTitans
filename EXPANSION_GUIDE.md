# Knowledge Base Expansion Guide

## 📊 Current Coverage Status

### ✅ **NOW COVERED (13 Sectors)**

| # | Sector | Efficiency | Keywords | Acts Covered |
|---|--------|-----------|----------|--------------|
| 1 | **Property Law** | 90% | 9 | Transfer of Property Act, Registration Act |
| 2 | **Inheritance & Succession** | 90% | 9 | Hindu Succession Act |
| 3 | **Constitutional Rights** | 85% | 8 | Constitution (Articles 12-35) |
| 4 | **Criminal Procedures (FIR/Bail)** | 85% | 7 | CrPC, IPC |
| 5 | **Consumer Protection** | 85% | 7 | Consumer Protection Act 2019 |
| 6 | **Contract Law** | 75% | 6 | Indian Contract Act 1872 |
| 7 | **Employment Law** | 80% | 8 | Wages Act, EPF, ESI, Industrial Disputes |
| 8 | **Family Law** | 90% | 6 | Hindu Marriage Act, DV Act |
| 9 | **General Legal Info** | 70% | 9 | CPC, Limitation Act, RTI |
| 10 | **Cyber Law** ⭐ NEW | 85% | 11 | IT Act 2000 |
| 11 | **Cheque Bounce** ⭐ NEW | 90% | 7 | Negotiable Instruments Act |
| 12 | **Motor Vehicles** ⭐ NEW | 85% | 10 | Motor Vehicles Act 1988 |
| 13 | **Greeting/Welcome** | 100% | 10 | - |

**Total:** 13 sectors | 150+ keywords | 20+ Acts | 100+ sections

---

## ❌ **HIGH PRIORITY - Still Missing**

These are the most commonly asked queries that are NOT yet covered:

### 1. **Tax Law** (CRITICAL)
**Why important:** Very common queries
**Keywords:** income tax, GST, TDS, tax return, PAN, refund, tax notice
**Acts:** Income Tax Act 1961, GST Act 2017
**Estimated addition time:** 2-3 hours

### 2. **Tenant/Landlord Disputes** (HIGH)
**Why important:** Common urban issues
**Keywords:** rent, tenant, landlord, eviction, rent agreement, security deposit
**Acts:** Rent Control Act (varies by state), Transfer of Property Act
**Estimated addition time:** 1-2 hours

### 3. **Banking & Loans** (HIGH)
**Why important:** Financial disputes common
**Keywords:** loan default, bank fraud, KYC, credit card, EMI, foreclosure
**Acts:** Banking Regulation Act, SARFAESI Act, RBI Act
**Estimated addition time:** 2 hours

### 4. **Education Law** (MEDIUM-HIGH)
**Why important:** Parents frequently ask
**Keywords:** school admission, RTE, fee, education rights, teacher, student
**Acts:** RTE Act 2009, UGC Act
**Estimated addition time:** 1-2 hours

### 5. **Real Estate (RERA)** (MEDIUM-HIGH)
**Why important:** Builder disputes
**Keywords:** builder, RERA, construction delay, refund, possession, flat booking
**Acts:** RERA 2016
**Estimated addition time:** 2 hours

---

## 🚀 **How to Add New Sector (Step-by-Step)**

### Example: Adding TAX LAW

#### Step 1: Research (30 minutes)
- Identify common queries (ITR filing, TDS, refund, notices)
- List relevant acts (Income Tax Act 1961, GST Act 2017)
- Note key sections (Section 139, 140, 194)

#### Step 2: Structure Content (1 hour)
```python
{
    "keywords": ["income tax", "itr", "tax return", "tds", "gst", "pan", 
                 "tax refund", "tax notice", "income tax act", "tax filing"],
    "category": "Tax Law",
    "response": """# Income Tax in India

## Legal Framework
**Governed by:** Income Tax Act, 1961 | GST Act, 2017

## ITR Filing

### Who Must File ITR?
**Mandatory for:**
- Income > ₹2.5 lakh (₹3 lakh for senior citizens)
- Foreign asset holders
- Directors of companies
- Persons claiming refund

### ITR Forms
- **ITR-1 (Sahaj):** Salary income up to ₹50 lakh
- **ITR-2:** Capital gains, multiple properties
- **ITR-3:** Business/professional income
- **ITR-4 (Sugam):** Presumptive income

### Filing Deadline
- **Individuals:** July 31 (for AY 2024-25)
- **Businesses (audit required):** October 31
- **Late filing:** Penalty of ₹5,000 (₹1,000 if income < ₹5 lakh)

## TDS (Tax Deducted at Source)

### Common TDS Sections:
- **Section 194A:** Interest on fixed deposits (10%)
- **Section 194C:** Contractor payments
- **Section 194H:** Commission (5%)
- **Section 194I:** Rent (10% for plant/machinery, 2% for land/building)
- **Section 194J:** Professional fees (10%)

### TDS Certificate:
- **Form 16:** Salary TDS (by employer)
- **Form 16A:** Non-salary TDS (by deductor)
- Must be issued by June 15

## Tax Refund

### How to Claim:
1. File accurate ITR
2. Verify ITR within 30 days (Aadhaar OTP/EVC/DSC)
3. Refund processed in 4-6 weeks
4. Credited to bank account (mentioned in ITR)

### Refund Status:
- Check on: https://incometaxindia.gov.in/
- Login → View Refund Status
- Track using PAN and acknowledgment number

## Tax Notices

### Common Notices:
1. **Section 143(1):** Intimation (mismatch in ITR)
2. **Section 139(9):** Defective return
3. **Section 148:** Reassessment notice (income escaped)
4. **Section 156:** Demand notice

### How to Respond:
- Don't panic - notices are common
- Check notice type and reason
- Respond within 30 days
- File rectification request if error

### Where to Respond:
- E-filing portal: https://www.incometax.gov.in/
- Upload response with supporting documents

## GST Basics

### GST Registration:
- **Mandatory if:** Turnover > ₹40 lakh (₹20 lakh for NE states)
- **Services:** Turnover > ₹20 lakh (₹10 lakh for NE)

### GST Returns:
- **GSTR-1:** Outward supplies (monthly/quarterly)
- **GSTR-3B:** Summary return (monthly)
- **GSTR-9:** Annual return

## Important Points
⚠️ Always file ITR on time - avoid penalties
⚠️ Keep salary slips, Form 16, investment proofs
⚠️ Respond to tax notices promptly
⚠️ Claim all deductions (80C, 80D, 80G)
⚠️ Link PAN with Aadhaar

## Tax Saving Options (Section 80C)
- PPF (up to ₹1.5 lakh)
- ELSS mutual funds
- Life insurance premium
- Home loan principal repayment
- Tuition fees
- NSC, FDs (5 years)

**Limit:** ₹1.5 lakh under 80C

---
**Legal Citations:** Income Tax Act, 1961 (Sections 139, 140, 143, 148, 156, 194) | GST Act, 2017""",
    "citations": ["Income Tax Act, 1961", "GST Act, 2017"]
}
```

#### Step 3: Add to legal_knowledge.py (2 minutes)
- Open `backend/services/legal_knowledge.py`
- Add the new entry before the GREETING entry
- Save file

#### Step 4: Test (5 minutes)
```bash
# Restart backend
python backend/main.py

# Test queries:
- "How to file ITR?"
- "What is TDS?"
- "Tax refund process"
- "GST registration"
```

**Total Time:** ~1.5-2 hours for complete Tax Law coverage!

---

## 📈 **Expansion Roadmap**

### Phase 1: Complete by Week 1 (High Priority)
- [ ] Tax Law (Income Tax, GST)
- [ ] Tenant/Landlord Disputes
- [ ] Banking & Loan Disputes
- [ ] Education Law (RTE, school admissions)

**After Phase 1:** 17 sectors, 200+ keywords

### Phase 2: Complete by Week 2 (Medium Priority)
- [ ] Real Estate (RERA, builder disputes)
- [ ] Intellectual Property (patents, trademarks)
- [ ] Company Law (registration, compliance)
- [ ] Medical Negligence

**After Phase 2:** 21 sectors, 250+ keywords

### Phase 3: Complete by Week 3 (Lower Priority)
- [ ] Environmental Law
- [ ] Child Rights (POCSO, JJ Act)
- [ ] Senior Citizen Rights
- [ ] SC/ST Act
- [ ] Disability Rights
- [ ] Agriculture Law

**After Phase 3:** 27+ sectors, 350+ keywords

---

## 💡 **Tips for Fast Expansion**

### 1. Use Template Structure
Every entry follows same pattern:
- Legal Framework
- Main sections/procedures
- How to file/claim
- Required documents
- Time limits
- Dos and Don'ts
- Legal citations

### 2. Focus on Common Queries
Don't try to cover everything - focus on:
- Most frequently asked questions
- Practical procedures
- Required documents
- Time limits
- Where to file

### 3. Reuse Format
Copy an existing entry, modify content
- Saves 50% time
- Maintains consistency
- Easy to update

### 4. Verify Sources
Always cite official acts:
- India Code: https://www.indiacode.nic.in/
- Ministry websites
- Official legal databases

---

## 🎯 **Efficiency Improvement Timeline**

| Phase | Sectors | Efficiency | Timeline |
|-------|---------|-----------|----------|
| **Current** | 13 | ~70% overall | - |
| **After Phase 1** | 17 | ~85% overall | 1 week |
| **After Phase 2** | 21 | ~90% overall | 2 weeks |
| **After Phase 3** | 27+ | ~95% overall | 3 weeks |

---

## ✅ **Quality Checklist**

Before adding new sector, ensure:
- [ ] Researched from official sources
- [ ] Covers most common queries
- [ ] Includes practical procedures
- [ ] Lists required documents
- [ ] Mentions time limits
- [ ] Cites official acts/sections
- [ ] Clear, simple language
- [ ] Structured with headings
- [ ] Tested with sample queries

---

## 🔍 **Testing New Entries**

After adding new sector:

1. **Exact Match Test:**
   - "Income tax filing"
   - "GST registration"
   
2. **Partial Match Test:**
   - "How to file ITR?"
   - "Tax refund process"
   
3. **Related Query Test:**
   - "TDS on salary"
   - "Tax notice response"

If all 3 types work correctly, entry is good! ✅

---

## 📞 **Next Steps**

To expand knowledge base:

1. **Identify priority sectors** (see list above)
2. **Research official sources** (1-2 hours per sector)
3. **Structure content** (following template)
4. **Add to `legal_knowledge.py`**
5. **Test thoroughly**
6. **Update `DATA_SOURCES.md`** (documentation)

**Goal:** 90%+ coverage of common legal queries within 3 weeks!

---

**Remember:** The system is already efficient and scalable. We just need to add more knowledge entries. Each new sector takes only 1-2 hours to add completely!

