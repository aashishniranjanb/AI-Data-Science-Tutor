import streamlit as st
from utils.session_manager import initialize_session_state
from utils.llm_utils import get_llm
from utils.data_classes import Message
from components.sidebar import create_sidebar
from components.chat_interface import display_chat_messages, handle_chat_input

# 1. Configure the page (Title + Icon)
st.set_page_config(
    page_title="AI Data Science Tutor",
    page_icon="static/images/ai_tutor_icon",  # Make sure your image is in this path
    layout="wide"
)

# 2. Initialize session state
initialize_session_state()

# 3. Create sidebar and get the page choice
page_choice = create_sidebar()

# 4. Apply Dark Mode 
if st.session_state["dark_mode"]:
    # Minimal example of dark mode styling
    dark_style =
    <style>
    body {
        background-color: #1e1e1e !important;
        color: #f5f5f5 !important;
    }
    .css-1cpxqw2 {
        background-color: #1e1e1e !important;
    }
    .stTextInput, .stButton, .stMarkdown, .stRadio {
        color: #f5f5f5 !important;
    }
    .stSidebar {
        background-color: #2c2c2c !important;
    }
    </style>
    
    st.markdown(dark_style, unsafe_allow_html=True)

# 5. Main page content based on navigation
if page_choice == "Chat":
    st.title("🤖 AI Data Science Tutor Chat")
    # Display the chat
    display_chat_messages(st.session_state["messages"])
    # Handle new user input
    handle_chat_input(st.session_state["messages"], get_llm)

elif page_choice == "Learning Path":
    st.title("📚 Personalized Learning Path")
    st.markdown("""
    **Explore recommended topics** based on your current skill level.
    We'll track your progress and suggest new modules to enhance your skills.
    """)
    st.info("Feature under development. Stay tuned! 🚀")

elif page_choice == "Quizzes":
    st.title("📝 Quizzes & Challenges")
    st.markdown("""
    **Test your Data Science knowledge** with interactive quizzes.
    Compete with peers and climb the leaderboard!
    """)
    st.warning("This section is coming soon! 🎉")

elif page_choice == "Settings":
    st.title("⚙️ Settings & Preferences")
    st.markdown("""
    Customize your AI Tutor experience:
    - Change themes
    - Update your username
    - Connect to external resources
    """)
    st.success("All changes are saved automatically.")

# 6. Footer Section
st.markdown("---")
st.markdown("**Developed by [Aashish Niranjan BarathyKannan](https://www.linkedin.com/in/aashishniranjanb/)** | [GitHub](https://github.com/aashishniranjanb)")

