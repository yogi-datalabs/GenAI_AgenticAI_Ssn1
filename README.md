# LLM to Advanced RAG with Optimization

This project demonstrates the complete lifecycle of building an AI system:

- LLM Basics  
- RAG (Retrieval Augmented Generation)  
- RAG Optimization (Prompting, MMR, Evaluation)  
- Deployment using Streamlit  

---

## Project Structure

```
GenAI_AgenticAI_Ssn1/
│
├── notebooks/
│   ├── llms_to_advanced_rags_with_optimization.ipynb
│   ├── llms_to_advanced_rags_with_optimization.html
│
├── src/
│   └── app/
│       └── streamlit_app.py
│
├── chroma_db/   (generated after running notebook)
├── requirements.txt
├── .env
└── README.md
```

---

## Step 1: Setup Environment

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate   # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Step 2: Setup API Keys

Create a `.env` file in the root folder:

```bash
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key   # optional (for Llama evaluation)
```

---

## Step 3: Run the Notebook

Open:

```bash
notebooks/llms_to_advanced_rags_with_optimization.ipynb
```

Run all cells step-by-step.

This will:

- Load documents  
- Chunk data  
- Generate embeddings  
- Create vector database (`chroma_db`)  
- Build RAG pipeline  
- Improve responses (prompt + MMR)  
- Evaluate responses using another LLM  

---

## Important Note

Before creating vector DB, always delete old DB:

```python
import shutil
import os

if os.path.exists("../chroma_db"):
    shutil.rmtree("../chroma_db")
```

This avoids duplicate embeddings.

---

## Step 4: Run Streamlit App

Run this command from the root folder:

```bash
streamlit run src/app/streamlit_app.py
```

---

## What the App Does

- Takes user question  
- Retrieves relevant document chunks using MMR  
- Generates answer using RAG  
- Displays answer with retrieved context  

---

## Key Concepts Covered

- LLM vs RAG  
- Chunking and Embeddings  
- Vector Databases (Chroma)  
- Semantic Search vs MMR  
- Prompt Engineering  
- LLM-as-a-Judge Evaluation  
- Streamlit Deployment  

---

## Learning Outcome

By the end of this project, you will understand:

- How to build RAG systems from scratch  
- How to improve LLM outputs  
- How to evaluate AI responses  
- How to deploy AI applications  

---

## Next Steps

You can extend this project by:

- Using different datasets   
- Adding Agentic AI workflows  
- Building multi-step reasoning systems  
- Adding memory or personalization  

---

## Instructor Note

This project demonstrates a complete progression:

```
LLM → RAG → Optimized RAG → Evaluated RAG → Deployed AI App
```

---

## Questions

Feel free to experiment, break things, and rebuild.

That is how you truly learn AI systems.