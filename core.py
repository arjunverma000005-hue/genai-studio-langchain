from dotenv import load_dotenv
load_dotenv()
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from typing import List , Optional
from langchain_core.output_parsers import PydanticOutputParser

# Initialize model
model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0
)

class Movie(BaseModel):
    title:str
    release_year:Optional[int]
    genre:List[str]
    director:Optional[str]
    cast:List[str]
    rating:Optional[float]
    summary:str

parser= PydanticOutputParser(pydantic_object=Movie)

# Prompt Template
chat_prompt = ChatPromptTemplate.from_messages([
    ("system",
    """You are a highly accurate movie information extraction assistant.

Your job is to analyze the given text and extract only relevant movie-related details in a clean, structured format.

Rules:
- Do NOT assume missing information
- If information is missing write "Not Available"
- Return ONLY the formatted output
"""),

    ("human",
    """
Extract the following information from the text.

Output Format:

Movie Name: <value>
Release Year: <value>
Genre: <comma-separated list>
Director: <comma-separated list>
Cast: <comma-separated list>
Main Characters: <comma-separated list>
Setting: <1 line description>

Plot Summary:
<3–5 lines summary>

Key Events:
- <event 1>
- <event 2>
- <event 3>

Themes:
- <theme 1>
- <theme 2>

Scientific Concepts:
- <concept 1>
- <concept 2>

Important Numbers:
- <number or fact>

Production Details:
- <detail>

Quick Summary:
<2–3 lines summary>

Text:
{input_text}
""")
])

# User input
para = input("Enter your paragraph: ")

# Create final prompt
messages = chat_prompt.format_messages(input_text=para)

# Run model
response = model.invoke(messages)

# Print result
print("\nExtracted Information:\n")
print(response.content)