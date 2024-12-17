import streamlit as st
from services.mistral_service import MistralLLM

def show():
    st.title("Symptom Checker")
    
    # Symptom Input
    symptoms = st.text_area("Describe your symptoms")
    duration = st.selectbox("Duration", ["Today", "Few days", "Week", "Month+"])
    severity = st.slider("Severity (1-10)", 1, 10, 5)
    
    if st.button("Check Symptoms"):
        llm = MistralLLM()
        analysis = llm.analyze_symptoms(symptoms, duration, severity)
        display_symptom_analysis(analysis)
