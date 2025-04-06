import sqlite3
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def get_embedding_dimension():
    conn = sqlite3.connect("candidates.db")
    cursor = conn.cursor()
    cursor.execute("SELECT embedding FROM candidate_embeddings")
    for row in cursor.fetchall():
        emb = pickle.loads(row[0])
        if isinstance(emb, np.ndarray):
            conn.close()
            return len(emb)
    conn.close()
    raise ValueError("No valid embeddings found.")

def match_candidates(job_embedding, top_n=5):
    conn = sqlite3.connect("candidates.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, email, embedding FROM candidate_embeddings")
    rows = cursor.fetchall()

    results = []
    for name, email, emb_blob in rows:
        candidate_emb = pickle.loads(emb_blob)

        # Skip if dimension doesn't match
        if len(candidate_emb) != len(job_embedding):
            print(f"⚠️ Skipping {name}: embedding shape mismatch")
            continue

        similarity = cosine_similarity([job_embedding], [candidate_emb])[0][0]
        similarity_percent = similarity * 100

        if similarity_percent >= 80.0:
            results.append((name, email, similarity_percent))

    conn.close()

    # Sort by similarity descending and return top N
    top_candidates = sorted(results, key=lambda x: x[2], reverse=True)[:top_n]
    return top_candidates