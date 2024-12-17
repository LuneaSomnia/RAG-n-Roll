import streamlit as st
from datetime import datetime
import json

def show():
    st.title("User Profile")
    
    # Basic Information
    st.header("Basic Information")
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("Full Name")
        dob = st.date_input("Date of Birth")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        email = st.text_input("Email")
        phone = st.text_input("Phone")
    
    # Health Background
    st.header("Health Background")
    medical_history = st.text_area("Medical History")
    family_history = st.text_area("Family Medical History")
    medications = st.text_area("Current Medications")
    
    # Lifestyle Information
    st.header("Lifestyle Information")
    smoking = st.selectbox("Smoking Status", ["Never", "Former", "Current"])
    alcohol = st.selectbox("Alcohol Consumption", ["None", "Occasional", "Regular"])
    diet = st.multiselect("Dietary Preferences", ["Vegetarian", "Vegan", "Gluten-Free", "None"])
    
    if st.button("Save Profile"):
        save_profile(locals())
