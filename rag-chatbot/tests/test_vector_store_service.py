
import unittest
from services.vector_store_service import VectorStoreService

class TestVectorStoreService(unittest.TestCase):

    def setUp(self):
        self.vector_service = VectorStoreService()

    def test_similarity_search_returns_results(self):
        # Simulated example embeddings and documents
        embeddings = [
            ([0.1, 0.2, 0.3], "Document 1"),
            ([0.4, 0.5, 0.6], "Document 2"),
            ([0.7, 0.8, 0.9], "Document 3")
        ]
        query_vector = [0.1, 0.2, 0.3]
        
        results = self.vector_service.similarity_search(query_vector, embeddings, top_k=2)
        
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 2)
        self.assertIn("Document 1", [doc for _, doc in results])

if __name__ == '__main__':
    unittest.main()
