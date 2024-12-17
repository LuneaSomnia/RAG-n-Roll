import unittest
from services.rag_service import RAGService
from services.mistral_service import MistralLLM
from database.models import UserProfile

class FeatureVerification(unittest.TestCase):
    def test_user_profile(self):
        # Verify all profile fields
        profile_fields = UserProfile.__table__.columns.keys()
        required_fields = [
            'full_name', 'date_of_birth', 'gender', 
            'medical_history', 'lifestyle_data'
        ]
        self.assertTrue(all(field in profile_fields for field in required_fields))
    
    def test_rag_implementation(self):
        rag = RAGService()
        test_query = "diabetes prevention"
        results = rag.search_resources(test_query)
        self.assertIsNotNone(results)
    
    def test_mistral_integration(self):
        llm = MistralLLM()
        response = llm.analyze_symptoms(["headache", "fever"])
        self.assertIsNotNone(response)
