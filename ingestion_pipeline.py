import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

# ----------------------------
# STEP 1: LOAD DOCUMENTS
# ----------------------------
def load_documents(docs_path="docs"):
    print(f"Loading documents from {docs_path}...")

    if not os.path.exists(docs_path):
        raise FileNotFoundError(
            f"The directory {docs_path} does not exist. Please create it and add your company files."
        )

    loader = DirectoryLoader(
        path=docs_path,
        glob="*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8-sig"}
    )

    documents = loader.load()

    if not documents:
        raise FileNotFoundError(
            f"No .txt files found in {docs_path}. Please add your company documents."
        )

    for i, doc in enumerate(documents[:2]):
        print(f"\nDocument {i+1}:")
        print(f"  Source: {doc.metadata['source']}")
        print(f"  Content length: {len(doc.page_content)} characters")
        print(f"  Preview: {doc.page_content[:100]}...")

    return documents


# ----------------------------
# STEP 2: SPLIT DOCUMENTS
# ----------------------------
def split_documents(documents, chunk_size=1000, chunk_overlap=100):
    print("Splitting documents into chunks...")

    splitter = CharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")
    return chunks


# ----------------------------
# STEP 3: CREATE VECTOR STORE
# ----------------------------
def create_vector_store(chunks, persist_directory="db/chroma_db"):
    print("Creating embeddings and storing in ChromaDB...")

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
        collection_metadata={"hnsw:space": "cosine"}
    )

    print(f"Vector store created and saved to {persist_directory}")
    return vectorstore


# ----------------------------
# MAIN PIPELINE
# ----------------------------
def main():
    print("=== RAG Document Ingestion Pipeline ===\n")

    docs_path = "docs"
    persist_directory = "db/chroma_db"

    if os.path.exists(persist_directory):
        print("✅ Vector store already exists. Skipping ingestion.")
        return

    documents = load_documents(docs_path)
    chunks = split_documents(documents)
    create_vector_store(chunks, persist_directory)

    print("\n✅ Ingestion complete! Documents are ready for RAG queries.")


if __name__ == "__main__":
    main()
