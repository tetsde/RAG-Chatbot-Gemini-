import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

def load_embeddings(embedding_file="database/embeddings.npz"):
    data = np.load(embedding_file, allow_pickle=True)
    embeddings = data["embeddings"]
    documents = data["documents"]
    return embeddings, documents

def create_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def search(query, index, documents, model, k=2):
    query_emb = model.encode(query)
    D, I = index.search(np.array([query_emb]), k)
    results = [documents[idx] for idx in I[0]]
    return results

def get_vectorstore():
    embeddings, documents = load_embeddings("database/embeddings.npz")

    index = create_faiss_index(embeddings)

    model = SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L3-v2")

    return index, documents, model

if __name__ == "__main__":
    index, documents, model = get_vectorstore()
    query = "Tiến độ số 1"
    results = search(query, index, documents, model, k=2)
    print("Kết quả tìm thấy:")
    for res in results:
        print(res)
