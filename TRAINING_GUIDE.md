# 🎓 AI Legal Chatbot - Training Guide

## Overview

This guide explains how to train your AI Legal Chatbot with Indian legal knowledge.

## Current Status

Your chatbot currently has **very limited knowledge** (only 1 document). Let's expand it!

## Training Methods

### Method 1: Add Pre-built Indian Legal Knowledge (RECOMMENDED) ⚡

**Fastest way to get started with comprehensive knowledge!**

```bash
# Step 1: Add Indian legal knowledge (Constitution, IPC, Acts)
python add_legal_knowledge.py

# Step 2: Build the vectorstore
python train_model.py
```

This will add **10+ comprehensive legal documents** covering:
- ✅ Fundamental Rights (Articles 14, 19, 23-24, 32)
- ✅ Indian Penal Code (Sections 420, 375-376, 498A)
- ✅ Hindu Succession Act
- ✅ Consumer Protection Act
- ✅ Right to Information Act
- ✅ And more!

**Time:** ~5 minutes

---

### Method 2: Scrape Legal Websites 🌐

**Add real-world legal content from trusted sources**

1. **Edit the URLs** in `backend/scraper/scrape_legal_data.py`:

```python
urls = [
    "https://www.kaanoon.com/your-legal-topic-1",
    "https://www.kaanoon.com/your-legal-topic-2",
    # Add more URLs here
]
```

2. **Run the scraper:**

```bash
python backend/scraper/scrape_legal_data.py
```

3. **Build vectorstore:**

```bash
python train_model.py
```

**Sources you can scrape from:**
- [Kaanoon.com](https://www.kaanoon.com) - Legal questions and answers
- [IndiaCode.nic.in](https://www.indiacode.nic.in) - Official Indian laws
- [India.gov.in](https://www.india.gov.in) - Constitution and acts

**Time:** 30-60 minutes (depends on number of URLs)

---

### Method 3: Add Your Own Custom Content 📝

**Add specific legal knowledge for your use case**

1. **Create a JSON file** in `data/raw/custom_knowledge.json`:

```json
[
  {
    "title": "Your Legal Topic",
    "content": "Detailed legal information here...",
    "url": "https://source-url.com",
    "metadata": {
      "category": "Category Name",
      "section": "Section Number"
    },
    "qa_pairs": [],
    "scraped_at": "2025-10-28 00:00:00"
  }
]
```

2. **Merge with existing data:**

```python
import json

# Load existing
with open('data/raw/legal_data.json', 'r') as f:
    existing = json.load(f)

# Load your custom
with open('data/raw/custom_knowledge.json', 'r') as f:
    custom = json.load(f)

# Merge and save
all_data = existing + custom
with open('data/raw/legal_data.json', 'w') as f:
    json.dump(all_data, f, indent=2)
```

3. **Rebuild vectorstore:**

```bash
python train_model.py
```

**Time:** Varies

---

## Complete Training Workflow

### 🚀 Quick Start (Recommended for Beginners)

```bash
# 1. Add pre-built legal knowledge
python add_legal_knowledge.py

# 2. Train the model
python train_model.py

# 3. Start the backend
python start_backend_simple.py

# 4. In another terminal, start the frontend
cd frontend
npm start

# 5. Visit http://localhost:3000
```

---

### 🎯 Advanced Training (For Maximum Knowledge)

```bash
# Step 1: Add pre-built knowledge
python add_legal_knowledge.py

# Step 2: Scrape additional websites (optional)
# Edit backend/scraper/scrape_legal_data.py first
python backend/scraper/scrape_legal_data.py

# Step 3: Add your custom content (optional)
# Create and merge custom_knowledge.json

# Step 4: Train the model
python train_model.py

# Step 5: Test it
python start_backend_simple.py
```

---

## Understanding the Training Process

### What Happens During Training?

1. **Data Collection:**
   - Scrapes or loads legal documents
   - Saves to `data/raw/legal_data.json`

2. **Text Processing:**
   - Splits documents into chunks (500 characters each)
   - Creates embeddings (vector representations)

3. **Vector Store Creation:**
   - Stores embeddings in ChromaDB
   - Saved in `vectorstore/` directory
   - Enables semantic search

4. **Ready to Use:**
   - Backend loads vectorstore
   - Can answer questions using RAG (Retrieval-Augmented Generation)

---

## Training Parameters

You can modify these in `train_model.py`:

```python
# Chunk size - smaller = more precise, larger = more context
chunk_size = 500

# Chunk overlap - prevents information loss at boundaries
chunk_overlap = 50

# Number of retrieved chunks for answers
k = 3  # in rag_service.py, line 172
```

---

## Verifying Training

After training, check:

1. **Check data files:**
```bash
# Should show JSON and TXT files
ls -lh data/raw/

# Check how many documents
python -c "import json; print(len(json.load(open('data/raw/legal_data.json'))))"
```

2. **Check vectorstore:**
```bash
# Should show database files
ls -lh vectorstore/
```

3. **Test the chatbot:**
   - Start backend and frontend
   - Ask questions
   - Check if responses are relevant

---

## Expanding Knowledge Base

### Topics to Add:

**Essential Indian Laws:**
- [ ] More IPC sections (302, 304, 354, 376D, 506, etc.)
- [ ] CrPC sections (154, 161, 197, 482, etc.)
- [ ] More constitutional articles
- [ ] Negotiable Instruments Act (Section 138 - Cheque Bounce)
- [ ] Motor Vehicles Act
- [ ] Information Technology Act, 2000

**Common Legal Issues:**
- [ ] Divorce procedures
- [ ] Property disputes
- [ ] Tenant rights
- [ ] Employment law
- [ ] GST and tax law basics
- [ ] Company law basics
- [ ] Intellectual Property Rights

**Procedures:**
- [ ] How to file FIR
- [ ] How to file consumer complaint
- [ ] How to file RTI
- [ ] Court procedures
- [ ] Bail procedures

---

## Troubleshooting

### Issue: "No data was scraped"

**Solution:** Check URL validity, internet connection, or use Method 1 (pre-built knowledge)

### Issue: "Vector store is empty"

**Solution:**
```bash
# Delete old vectorstore
rm -rf vectorstore/

# Retrain
python train_model.py
```

### Issue: "Chatbot gives irrelevant answers"

**Solutions:**
1. Add more relevant data
2. Reduce chunk_size for more precision
3. Increase k value for more context

### Issue: "Training is slow"

**Normal:** First-time training loads embedding model (~90MB), takes 2-5 minutes

---

## Best Practices

1. **Start Small:** Begin with Method 1 (pre-built knowledge)
2. **Test Often:** After each training, test the chatbot
3. **Expand Gradually:** Add 10-20 documents at a time
4. **Quality over Quantity:** Better to have 50 high-quality documents than 500 poor ones
5. **Keep Backups:** Save `data/raw/legal_data.json` before major changes
6. **Update Regularly:** Add new laws and judgments periodically

---

## Need Help?

- Check `backend/services/rag_service.py` for RAG implementation
- Check `backend/scraper/scrape_legal_data.py` for scraping logic
- See `README.md` for general setup instructions

---

## Next Steps

After training:

1. ✅ Test with various legal questions
2. ✅ Identify knowledge gaps
3. ✅ Add more content for those gaps
4. ✅ Retrain
5. ✅ Repeat until satisfied!

---

**Happy Training! 🎉**

