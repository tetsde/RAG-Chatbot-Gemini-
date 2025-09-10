import json
import numpy as np
from sentence_transformers import SentenceTransformer

# --- Thêm chunking ---
def chunk_text(text, max_chars=500, overlap=50):
    """Chunk text nếu quá dài"""
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        chunks.append(text[start:end])
        start += max_chars - overlap
    return chunks

def build_embeddings(json_file, output_file="database/embeddings.npz", max_chars=500):
    model = SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L3-v2")
    
    with open(json_file, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    documents = []
    embeddings = []

    for item in dataset:
        doc_text = f"Title: {item['title']}\nContent: {item['content']}"
        
        # Nếu text quá dài, chunk ra
        chunks = chunk_text(doc_text, max_chars=max_chars)
        
        for chunk in chunks:
            emb = model.encode(chunk)
            embeddings.append(emb)
            # Lưu metadata gốc cùng chunk
            documents.append({"original_item": item, "chunk_text": chunk})

    np.savez(output_file, embeddings=np.array(embeddings), documents=np.array(documents))
    print(f"Saved embeddings to {output_file}")

if __name__ == "__main__":
    build_embeddings("database/company_dataset.json")
