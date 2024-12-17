import streamlit as st
import plotly.express as px
from services.wearable_service import WearableService

def show():
    st.title("Lifestyle Monitoring")
    
    # Activity Tracking
    st.subheader("Daily Activity")
    wearable = WearableService()
    activity_data = wearable.get_activity_data()
    
    # Visualizations
    fig = px.line(activity_data, x="date", y="steps", title="Daily Steps")
    st.plotly_chart(fig)
    
    # Goals
    st.subheader("Goals")
    step_goal = st.number_input("Daily Step Goal", min_value=1000, value=10000)
    sleep_goal = st.number_input("Sleep Goal (hours)", min_value=4, value=8)
