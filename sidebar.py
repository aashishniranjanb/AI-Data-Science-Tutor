import streamlit as st

def create_sidebar():
    
    # Display the icon at the top of the sidebar
    st.sidebar.image("static/images/ds_tutor_icon.png", width=100)
    
    # Sidebar Title
    st.sidebar.title("⚛️ AI Data Science Tutor")
    st.sidebar.markdown("---")
    
    # User Greeting
    if "user_name" not in st.session_state:
        st.session_state["user_name"] = "Guest"
    user_name = st.sidebar.text_input("Enter your name:", st.session_state["user_name"])
    st.session_state["user_name"] = user_name
    
    st.sidebar.markdown(f"**Hello, {user_name}!**")
    
    # Navigation
    st.sidebar.subheader("🔍 Navigation")
    page_choice = st.sidebar.radio(
        "Go to:",
        ["Chat", "Learning Path", "Quizzes", "Settings"]
    )
    
    st.sidebar.markdown("---")
    
    # Dark Mode Toggle
    dark_mode = st.sidebar.checkbox("🌙 Dark Mode", value=False)
    st.session_state["dark_mode"] = dark_mode
    
    # External Links
    st.sidebar.markdown("**Resources**")
    st.sidebar.markdown("[GitHub](https://github.com/aashishniranjanb)")
    st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/aashishniranjanb/)")
    
    return page_choice
