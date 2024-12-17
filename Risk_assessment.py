import streamlit as st
from services.risk_assessment_service import RiskAssessmentService

def show():
    st.title("Health Risk Assessment")
    
    # Personal Factors
    st.subheader("Personal Factors")
    age = st.number_input("Age", min_value=0, max_value=120)
    weight = st.number_input("Weight (kg)", min_value=0.0)
    height = st.number_input("Height (cm)", min_value=0.0)
    
    # Lifestyle Factors
    st.subheader("Lifestyle Factors")
    exercise = st.slider("Weekly Exercise (hours)", 0, 40, 5)
    sleep = st.slider("Average Sleep (hours)", 0, 12, 7)
    stress = st.slider("Stress Level (1-10)", 1, 10, 5)
    
    if st.button("Calculate Risk"):
        service = RiskAssessmentService()
        risks = service.calculate_risks(locals())
        display_risk_results(risks)
