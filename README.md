# Retrieval-Augmented Generation (RAG) Chatbot

## Overview

This project is a Retrieval-Augmented Generation (RAG) system built using LangChain, ChromaDB, Hugging Face Embeddings, and Ollama.

The system allows users to ask questions about a collection of documents and receive answers grounded in the information contained within those documents.

Instead of relying solely on an LLM's pre-trained knowledge, the chatbot first retrieves relevant information from a custom knowledge base and then generates answers based on the retrieved context.

---

## Why RAG?

Large Language Models (LLMs) are powerful, but they have limitations:

* They may hallucinate facts.
* They cannot access private documents by default.
* Their knowledge may be outdated.
* They cannot reliably answer questions about custom datasets.

Retrieval-Augmented Generation (RAG) solves these problems by combining:

1. Information Retrieval
2. Large Language Models

The retrieval component finds relevant information from a document database, while the language model uses that information to generate accurate responses.

---

## Project Workflow

### 1. Document Ingestion Pipeline

The system first builds a searchable knowledge base.

#### Step 1: Load Documents

Text documents are loaded from the `docs/` folder.

Examples:

* Microsoft.txt
* Google.txt
* Nvidia.txt
* Tesla.txt
* SpaceX.txt

#### Step 2: Chunking

Large documents are split into smaller chunks.

Example:

Original document:

Microsoft was founded by Bill Gates and Paul Allen in 1975...

Chunks:

Chunk 1
Chunk 2
Chunk 3
...

Chunking improves retrieval accuracy and allows the system to process large documents efficiently.

#### Step 3: Generate Embeddings

Each chunk is converted into a vector representation using:

`sentence-transformers/all-MiniLM-L6-v2`

Embeddings capture semantic meaning rather than exact words.

#### Step 4: Store in Vector Database

The embeddings are stored in ChromaDB.

This creates a searchable vector database where similar pieces of information are stored close together.

---

### 2. Retrieval Pipeline

When a user asks a question:

Example:

"Who founded Microsoft?"

The system:

1. Converts the question into an embedding.
2. Searches ChromaDB using cosine similarity.
3. Finds the most relevant document chunks.
4. Returns the top matching results.

---

### 3. Generation Layer

Retrieved chunks are passed to a local LLM running through Ollama.

The model uses the retrieved context to generate an answer grounded in the source documents.

Example:

Question:

Who founded Microsoft?

Retrieved Context:

Microsoft was founded by Bill Gates and Paul Allen in 1975.

Generated Answer:

Microsoft was founded by Bill Gates and Paul Allen in 1975.

---

## Architecture

User Question

↓

Embedding Model

↓

Vector Search (ChromaDB)

↓

Relevant Chunks Retrieved

↓

LLM (Llama 3 via Ollama)

↓

Final Answer

---

## Technologies Used

### Frameworks

* LangChain

### Vector Database

* ChromaDB

### Embedding Model

* sentence-transformers/all-MiniLM-L6-v2

### Local LLM

* Llama 3 (Ollama)

### Programming Language

* Python

---

## Features

* Custom document ingestion
* Automatic chunking
* Vector embeddings
* ChromaDB vector storage
* Semantic search using cosine similarity
* Retrieval pipeline
* Local LLM integration
* Interactive chatbot interface
* No paid API required

---

## Project Structure

RAG/

├── docs/

│ ├── Microsoft.txt

│ ├── Google.txt

│ ├── Nvidia.txt

│ ├── Tesla.txt

│ └── SpaceX.txt

│

├── ingestion_pipeline.py

├── retrieval_pipeline.py

├── rag_chatbot.py

├── db/

│ └── chroma_db/

│

├── requirements.txt

└── README.md

---

## How to Run

### 1. Clone Repository

git clone <repository-url>

cd RAG

### 2. Create Virtual Environment

python -m venv venv

### 3. Activate Environment

Windows:

venv\Scripts\activate

### 4. Install Dependencies

pip install -r requirements.txt

### 5. Build Vector Database

python ingestion_pipeline.py

### 6. Start Chatbot

python rag_chatbot.py

---

## Future Improvements

* Streamlit Web Interface
* Conversation Memory
* Multi-document Retrieval
* Hybrid Search
* Metadata Filtering
* Source Citation
* PDF Support
* Advanced RAG Techniques
* Agentic RAG Workflows

---

## Learning Outcomes

Through this project I learned:

* How Retrieval-Augmented Generation works
* Document chunking strategies
* Embeddings and vector representations
* Cosine similarity search
* Vector databases
* LangChain workflows
* ChromaDB integration
* Local LLM deployment with Ollama
* Building end-to-end GenAI applications

---

## Author

Pujitha Kothuri

Built as part of my journey into Generative AI, Retrieval-Augmented Generation (RAG), and AI-powered applications.
