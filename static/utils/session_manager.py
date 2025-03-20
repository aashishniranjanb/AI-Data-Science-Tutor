import streamlit as st

def initialize_session_state():
    """
    Ensures critical session state variables are set
    for the chat application.
    """
    if "messages" not in st.session_state:
        # Pre-populate with a greeting from the assistant
        st.session_state["messages"] = [
            {
                "role": "assistant",
                "content": "Hello! I'm your AI Data Science Tutor. How can I help you today? 🤖"
            }
        ]
    
    if "dark_mode" not in st.session_state:
        st.session_state["dark_mode"] = False

    if "user_name" not in st.session_state:
        st.session_state["user_name"] = "Guest"
