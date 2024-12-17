import streamlit as st
from services.rag_service import RAGService

def show():
    st.title("Educational Resources")
    
    # Search and Filter
    search = st.text_input("Search health topics")
    category = st.selectbox("Category", ["All", "Nutrition", "Exercise", "Mental Health"])
    
    if search:
        rag = RAGService()
        results = rag.search_resources(search, category)
        display_resources(results)

