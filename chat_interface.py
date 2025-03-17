import streamlit as st

def display_chat_messages(messages):
    
    for idx, msg in enumerate(messages):
        # Display user messages
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.markdown(f"**{msg['content']}**")
        # Display AI (assistant) messages
        else:
            with st.chat_message("assistant"):
                st.markdown(msg["content"])

def handle_chat_input(messages, llm_function):
    
    user_input = st.text_input(
        "Ask a question about Data Science:",
        placeholder="E.g., What is linear regression?",
        key="chat_input"
    )
    
    if user_input:
        # Add user message to chat
        messages.append({"role": "user", "content": user_input})
        
        with st.spinner("Thinking..."):
            response = llm_function(user_input)
        
        # Add AI response to chat
        messages.append({"role": "assistant", "content": response})
        
        # Update session state
        st.session_state["messages"] = messages
        
        # Rerun to display the new messages
        st.experimental_rerun()
