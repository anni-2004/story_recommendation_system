import streamlit as st
import requests

st.set_page_config(page_title="Pratilipi Ranker")
st.title("📚 Story Recommendation System")

user_id = st.number_input("Enter User ID", min_value=1, value=1)

if st.button("Get Recommendations"):
    try:
        # Connects to your FastAPI backend
        response = requests.get(f"http://127.0.0.1:8000/recommend/{user_id}")
        data = response.json()
        
        for item in data:
            st.subheader(item['title'])
            st.write(f"Genre: {item['genres']}")
            st.divider()
    except:
        st.error("Is the FastAPI backend running? (uvicorn api.app:app)")