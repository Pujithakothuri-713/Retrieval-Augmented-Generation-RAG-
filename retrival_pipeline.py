import re
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load embeddings (same as ingestion)
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector DB
db = Chroma(
    persist_directory="db/chroma_db",
    embedding_function=embedding_model
)

# Question
query = "Who founded Microsoft and in which year was it founded?"

# Retrieve top chunks
docs = db.similarity_search(query, k=5)

# Combine retrieved text
combined_text = " ".join(doc.page_content for doc in docs)

# ---- SIMPLE ANSWER EXTRACTION ----

# Extract year (e.g., 1975)
year_match = re.search(r"\b(19\d{2}|20\d{2})\b", combined_text)

# Extract founders
founders = []
if "Bill Gates" in combined_text:
    founders.append("Bill Gates")
if "Paul Allen" in combined_text:
    founders.append("Paul Allen")

# Build final answer
if year_match and founders:
    year = year_match.group(0)
    founders_str = " and ".join(founders)
    answer = f"Microsoft was founded in {year} by {founders_str}."
else:
    answer = "Answer not found in the documents."

# Print single-line answer
print("\nAnswer:")
print(answer)
