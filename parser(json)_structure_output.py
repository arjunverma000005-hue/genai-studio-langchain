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
prompt = ChatPromptTemplate.from_messages([
    ('system','''
Extract movie information from the paragraph
     {format_instruction}
'''),
('human','{paragraph}')
])
    

# User input
para = input("Enter your paragraph: ")


final_prompt=prompt.invoke({'paragraph':para,
                            'format_instruction':parser.get_format_instructions()})
# Create final prompt
# messages = prompt.format_messages(input_text=para)

# Run model
response = model.invoke(final_prompt)
movie_data=parser.parse(response.content)
# Print result
print("\nExtracted Information:\n")
print(movie_data)



