import streamlit as st
from utils.session_manager import initialize_session_state, get_llm_chain_from_session
from components.sidebar import create_sidebar
from components.chat_interface import display_chat_messages, handle_chat_input
import google.generativeai as genai

# Set your Google API key directly in the code
GOOGLE_API_KEY = "AIzaSyBVOM4Pct30jaUcFUiXpbMy4hVOv2f3kKk"

# Set page title and logo - This must be the first Streamlit command
st.set_page_config(
    page_title="Data Science Tutor",
    page_icon="static/ai_tutor_icon.png"  # Ensure this path is correct
)

# Include the CSS file
st.markdown(
    '<link href="static/style.css" rel="stylesheet">',
    unsafe_allow_html=True
)

# Initialize session state and LLM chain
initialize_session_state()

# Create sidebar
create_sidebar()

# Main chat interface
st.title("🤖 AI Data Science Tutor Chat")

# Display chat messages
display_chat_messages(st.session_state["messages"])

# Handle chat input
handle_chat_input(st.session_state["messages"], get_llm_chain_from_session())

# Footer Section
st.markdown("---")
st.markdown("**Developed by [Aashish Niranjan BarathyKannan](https://www.linkedin.com/in/aashishniranjanb/)** | [GitHub](https://github.com/aashishniranjanb)")

