import streamlit as st

def create_sidebar():

    st.sidebar.image("static/ai_tutor_icon.png", use_column_width=True)
    
    st.sidebar.title("Settings")
    st.sidebar.markdown("### Links")
    st.sidebar.markdown("[GitHub](https://github.com/aashishniranjanb)")
    st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/aashishniranjanb/)")
    st.sidebar.markdown("### About")
    st.sidebar.markdown("This is a Data Science Tutor powered by Gemini 1.5 Pro.")
    st.sidebar.markdown("### 📚 Personalized Learning Path")
    st.sidebar.markdown("Explore topics based on your skill level. We'll track your progress!")
    st.sidebar.markdown("🚀 Feature under development.")
