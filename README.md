📚 Retrieval-Augmented Question Answering System (RAG) — From Scratch
🚀 Project Overview

This project implements a Retrieval-Augmented Generation (RAG) system from scratch to answer questions using only user-provided documents, without relying on large language models (LLMs) for generation.

Instead of generating answers from a model’s internal knowledge, this system:

retrieves relevant information from documents

grounds answers strictly in retrieved content

avoids hallucinations

works fully offline and free

This project focuses on understanding how RAG works internally, not just using APIs.

🧠 What is RAG?

Retrieval-Augmented Generation (RAG) is a system design pattern where:

Information is retrieved from a knowledge base

Relevant context is selected using semantic similarity

Answers are produced based on retrieved evidence

“Don’t guess the answer — find the answer first.”

In this implementation, we intentionally stop before generative models and instead use deterministic answer extraction, making the system:

explainable

reliable

interview-safe

❓ Why RAG is Needed

Large Language Models alone:

cannot access private data

hallucinate facts

rely on outdated training data

struggle with long documents

RAG solves this by:

separating knowledge (documents) from reasoning

enabling AI on private or domain-specific data

improving factual accuracy

🧩 System Architecture
1️⃣ Ingestion Pipeline

Load raw text documents

Split documents into chunks

Convert chunks into semantic embeddings

Store embeddings in a vector database

2️⃣ Retrieval Pipeline

Convert user query into an embedding

Compare query with document embeddings using cosine similarity

Retrieve the most relevant chunks

3️⃣ Answer Extraction

Extract factual answers directly from retrieved text

Generate a clean, single-line response

No LLM, no hallucination

🗂️ Project Structure
RAG/
│
├── docs/
│   ├── Google.txt
│   ├── Microsoft.txt
│   ├── Nvidia.txt
│   ├── SpaceX.txt
│   └── Tesla.txt
│
├── db/
│   └── chroma_db/          # Persistent vector database
│
├── ingestion_pipeline.py   # Document ingestion & embedding
├── retrieval_pipeline.py   # Question answering logic
├── .env                    # Environment variables (if needed)
├── requirements.txt
└── README.md

⚙️ Technologies Used

Python

Sentence-Transformers

Model: all-MiniLM-L6-v2

ChromaDB

Vector database for similarity search

LangChain

Document loaders, chunking, vector interfaces

⚠️ No LLMs used

No OpenAI

No GPT

No paid APIs

🔍 How Semantic Retrieval Works

Each text chunk is converted into a vector embedding

User queries are converted into embeddings

Cosine similarity measures how close meanings are

Top-K most relevant chunks are retrieved

This enables meaning-based search, not keyword matching.

🧪 Example Query

Question

Who founded Microsoft and in which year?


Answer

Microsoft was founded in 1975 by Bill Gates and Paul Allen.


✔ Answer is derived strictly from document content
✔ Fully explainable
✔ No hallucination

🧠 Key Learnings

RAG is primarily a system design problem

Embedding consistency between ingestion & retrieval is critical

Vector databases enable semantic search at scale

Retrieval ≠ generation

LLMs are optional, not mandatory

🔒 Why This Project Avoids LLMs

This project intentionally avoids generative models to:

keep the system free

reduce complexity

improve explainability

avoid hallucinations

focus on fundamentals

LLMs can be added later as an extension.

🚧 Future Improvements

Add conversational memory (LLM-free)

Support more question types

Integrate a local LLM for generation

Add a simple web UI

Improve answer extraction logic

▶️ How to Run
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Ingest documents
python ingestion_pipeline.py

3️⃣ Ask questions
python retrieval_pipeline.py

📌 Final Note

This project was built to deeply understand how RAG systems work internally, not just to produce outputs.

If you are learning AI, NLP, or applied ML — building systems like this is far more valuable than prompt-only projects.

👩‍💻 Author

Built as a learning-by-building project to understand:

semantic search

vector databases

retrieval pipelines

grounded question answering
