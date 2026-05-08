import chromadb
from sentence_transformers import SentenceTransformer
import os


model = SentenceTransformer("all-MiniLM-L6-v2")


client = chromadb.Client()

collection = client.get_or_create_collection("knowledge_base")

folder = "knowledge_base"

documents = []
ids = []


for index, filename in enumerate(os.listdir(folder)):
    filepath = os.path.join(folder, filename)

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

        documents.append(text)
        ids.append(str(index))


embeddings = model.encode(documents).tolist()


collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=ids
)

print("✅ Successfully seeded ChromaDB with 10 documents")