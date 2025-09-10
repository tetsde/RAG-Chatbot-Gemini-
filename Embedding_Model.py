
import json
import numpy as np
from sentence_transformers import SentenceTransformer
def build_embeddings(json_file, output_file="database/embeddings.npz"):
    model = SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L3-v2")
    with open(json_file, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    documents = []
    embeddings = []

    for item in dataset:
        doc_text = f"Title: {item['title']}\nContent: {item['content']}"
        
        emb = model.encode(doc_text)   

        documents.append(item)
        embeddings.append(emb)
    np.savez(output_file, embeddings=np.array(embeddings), documents=np.array(documents))

    print(f"Saved embeddings to {output_file}")

if __name__ == "__main__":
    build_embeddings("database/Input_database.json")
