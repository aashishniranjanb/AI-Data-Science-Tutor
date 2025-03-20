import streamlit as st

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
        
        # Custom responses for specific inputs
        if user_input.lower() in ["hi", "hello"]:
            response = "🔹 AI Tutor: Here’s an answer to '{}': Hello! How can I assist you today?".format(user_input)
        elif user_input.lower() == "what is eda":
            response = "🔹 AI Tutor: Here’s an answer to 'what is eda': EDA, or Exploratory Data Analysis, is a critical step in the data analysis process where you summarize the main characteristics of a dataset, often using visual methods."
        else:
            response = llm_chain.run(user_input)  # Fallback to LLM for other questions
        
        messages.append(Message(sender="ai", content=response))
