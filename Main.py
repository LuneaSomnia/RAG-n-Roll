from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from services.rag_service import RAGService
from services.mistral_service import MistralLLM
from database.models import UserProfile

app = FastAPI(title="Preventive Care API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/risk-assessment")
async def assess_health_risks(user_data: UserProfile):
    rag_service = RAGService()
    risk_factors = await rag_service.analyze_risk_factors(user_data)
    return risk_factors

@app.post("/api/symptom-check")
async def check_symptoms(symptoms: list):
    llm = MistralLLM()
    analysis = await llm.analyze_symptoms(symptoms)
    return analysis
