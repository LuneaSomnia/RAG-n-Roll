import streamlit as st
from pages import (
    user_profile,
    risk_assessment,
    symptom_checker,
    lifestyle_monitoring,
    educational_resources
)

st.set_page_config(
    page_title="Preventive Care Assistant",
    page_icon="🏥",
    layout="wide"
)

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a feature",
        ["User Profile", "Risk Assessment", "Symptom Checker", 
         "Lifestyle Monitoring", "Educational Resources"]
    )
    
    if page == "User Profile":
        user_profile.show()
    elif page == "Risk Assessment":
        risk_assessment.show()
    elif page == "Symptom Checker":
        symptom_checker.show()
    elif page == "Lifestyle Monitoring":
        lifestyle_monitoring.show()
    elif page == "Educational Resources":
        educational_resources.show()

if __name__ == "__main__":
    main()
