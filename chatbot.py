########################################################################################
########################################################################################
import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage,  HumanMessage

# Load variables from .env file
load_dotenv()

# Initialize the Mistral model
model = ChatMistralAI(
    model='mistral-small-latest',
    temperature=0.9,
    mistral_api_key=os.getenv("MISTRAL_API_KEY")
)

messages = [
    SystemMessage(content='you are a funny AI agent')
]

print("\n---------------- WELCOME TYPE 0 TO EXIT THE APPLICATION ----------------")
while True:
    
    prompt = input("You: ")

    # ✅ EXIT CONDITION FIRST
    if prompt.strip() == "0":
        print("Exiting application...")
        break

    # ✅ Add user message
    messages.append(HumanMessage(content=prompt))

    # ✅ Get response
    response = model.invoke(messages)

    # ✅ Add bot response
    messages.append(AIMessage(content= response.content))

    # ✅ Print response
    print("Bot:", response.content)