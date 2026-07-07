import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

# Load API key
load_dotenv()

# Page title
st.title("🎬 Movie Information Extractor by ARJ")

# Initialize model
model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0
)

# Prompt template
chat_prompt = ChatPromptTemplate.from_messages([
    ("system",
    """You are a movie information extraction assistant.
Extract only the information present in the text.
If something is missing write 'Not Available'.
Return only the formatted output."""
    ),

    ("human",
    """
Extract the following information.

Movie Name: <value>
Release Year: <value>
Genre: <value>
Director: <value>
Cast: <value>
Main Characters: <value>
Setting: <value>

Plot Summary:
<3-5 lines>

Key Events:
- event 1
- event 2
- event 3

Themes:
- theme 1
- theme 2

Text:
{input_text}
"""
    )
])

# Input box
text = st.text_area("Enter movie paragraph")

# Button
if st.button("Extract Information"):

    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        messages = chat_prompt.format_messages(input_text=text)
        response = model.invoke(messages)

        st.subheader("Result")
        st.write(response.content)