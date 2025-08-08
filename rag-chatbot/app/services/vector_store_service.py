from typing import List
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

vector_db = []

def add_to_vector_store(text: str, embedding: List[float]):
    vector_db.append((embedding, text))

def search_similar_vectors(query_embedding: List[float], top_k=3) -> List[str]:
    if not vector_db:
        return []
    embeddings = np.array([v[0] for v in vector_db])
    scores = cosine_similarity([query_embedding], embeddings)[0]
    top_indices = scores.argsort()[-top_k:][::-1]
    return [vector_db[i][1] for i in top_indices]
