# emmdedding : it is 

# from langchain_openai import OpenAI, OpenAIEmbeddings
# from dotenv import load_dotenv
# load_dotenv()
# embeddings   =OpenAIEmbeddings(
#     model='text-embedding-3-large'
# )

# vector = embeddings.embed_query('you are going to gen ai')
# print(vector)




####################################################################
#####################################################33

from langchain_huggingface import HuggingFaceEmbeddings
embedding=HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2'
)

texts=[
    'hello this is arjun verma ',
    'hi what is your name ',
    'and you all are evry beautiful'
]

vector=embedding.embed_documents(texts)

print(vector)