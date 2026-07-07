import streamlit as st
import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# 1. Load environment variables
load_dotenv()

# 2. Page Configuration
st.set_page_config(page_title="Funny AI Agent", page_icon="🤖")
st.title("🤖 Funny AI Agent")

# 3. Initialize model in session state (so it doesn't reload every time)
if "model" not in st.session_state:
    st.session_state.model = ChatMistralAI(
        model='mistral-small-latest',
        temperature=0.9,
        mistral_api_key=os.getenv("MISTRAL_API_KEY")
    )

# 4. Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content='you are a funny AI agent')
    ]

# 5. Display chat messages from history on app rerun
for message in st.session_state.messages:
    if isinstance(message, SystemMessage):
        continue  # Don't show the system prompt to the user
    role = "user" if isinstance(message, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(message.content)

# 6. React to user input
if prompt := st.chat_input("Say something funny..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Store user message in history
    st.session_state.messages.append(HumanMessage(content=prompt))

    # Generate response
    with st.chat_message("assistant"):
        # You can use st.write_stream if you want the typing effect later!
        response = st.session_state.model.invoke(st.session_state.messages)
        st.markdown(response.content)
    
    # Store bot response in history
    st.session_state.messages.append(AIMessage(content=response.content))
