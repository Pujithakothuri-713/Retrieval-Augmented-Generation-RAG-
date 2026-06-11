from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

# Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Connect to ChromaDB
db = Chroma(
    persist_directory="db/chroma_db",
    embedding_function=embedding_model
)

# Load Llama3
llm = Ollama(model="llama3")

print("RAG Chatbot Started! Type 'quit' to exit.\n")

while True:
    query = input("You: ")

    if query.lower() == "quit":
        print("Bot: Goodbye!")
        break

    # Retrieve relevant chunks
    docs = db.similarity_search(query, k=3)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a helpful assistant.

Answer ONLY using the provided context.

Context:
{context}

Question:
{query}

Answer briefly and accurately.
"""

    response = llm.invoke(prompt)

    print(f"\nBot: {response}\n")