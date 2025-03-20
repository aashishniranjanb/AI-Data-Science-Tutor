import streamlit as st

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

def get_llm_chain_from_session():
    # This function should return the LLM chain initialized with your API key
    from utils.llm_utils import get_llm
    return get_llm
