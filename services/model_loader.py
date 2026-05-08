from sentence_transformers import SentenceTransformer

print("Loading model...")

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model loaded")