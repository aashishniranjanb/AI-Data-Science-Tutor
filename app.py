import streamlit as st
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyBVOM4Pct30jaUcFUiXpbMy4hVOv2f3kKk"

st.set_page_config(
    page_title="AI Data Science Tutor",
    page_icon="ai_tutor_icon.png",  # Image must be in the same directory
    layout="wide"
)

if "messages" not in st.session_state:
    st.session_state["messages"] = []

st.sidebar.image("ai_tutor_icon.png", width=100)
st.sidebar.title("🔍 Navigation")
page_choice = st.sidebar.radio(
    "Select a page:", ["Chat", "Learning Path", "Quizzes", "Settings"]
)

dark_mode = st.sidebar.checkbox("🌙 Enable Dark Mode", value=False)

if dark_mode:
    dark_css = """
    <style>
        body, .stApp { background-color: #1e1e1e !important; color: #f5f5f5 !important; }
        .stTextInput, .stButton, .stMarkdown, .stRadio { color: #f5f5f5 !important; }
        .stSidebar { background-color: #2c2c2c !important; }
    </style>
    """
    st.markdown(dark_css, unsafe_allow_html=True)

def display_chat():
    st.title("🤖 AI Data Science Tutor Chat")
    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

    user_input = st.chat_input("Ask a question...")
    if user_input:
        st.session_state["messages"].append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        ai_response = f"🔹 AI Tutor: Here’s an answer to '{user_input}'!"
        st.session_state["messages"].append({"role": "ai", "content": ai_response})
        st.chat_message("ai").write(ai_response)

# Learning Path Section
def display_learning_path():
    st.title("📚 Personalized Learning Path")
    st.markdown("Explore topics based on your skill level. We'll track your progress!")
    st.info("🚀 Feature under development.")

# Quizzes Section
def display_quizzes():
    st.title("📝 Quizzes & Challenges")
    st.markdown("Test your knowledge with interactive quizzes!")
    st.warning("🎉 Coming Soon!")

# Settings Section
def display_settings():
    st.title("⚙️ Settings & Preferences")
    st.markdown("Customize your experience.")
    st.success("All changes are saved automatically.")

# Page Navigation
if page_choice == "Chat":
    display_chat()
elif page_choice == "Learning Path":
    display_learning_path()
elif page_choice == "Quizzes":
    display_quizzes()
elif page_choice == "Settings":
    display_settings()

# Footer Section
st.markdown("---")
st.markdown("**Developed by [Aashish Niranjan BarathyKannan](https://www.linkedin.com/in/aashishniranjanb/)** | [GitHub](https://github.com/aashishniranjanb)")

