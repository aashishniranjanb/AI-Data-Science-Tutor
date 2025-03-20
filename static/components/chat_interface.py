import streamlit as st
from utils.data_classes import Message

def display_chat_messages(messages):
    for message in messages:
        if message.sender == "user":
            st.markdown(f"<div class='chat-message user-message'>{message.content}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-message ai-message'>{message.content}</div>", unsafe_allow_html=True)

def handle_chat_input(messages, llm_chain):
    user_input = st.text_input("Ask your data science question:")
    if st.button("Send"):
        messages.append(Message(sender="user", content=user_input))
        
        # Generate response using the LLM
        response = llm_chain(user_input)
        
        messages.append(Message(sender="ai", content=response))
