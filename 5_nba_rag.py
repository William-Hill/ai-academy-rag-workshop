import argparse
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from langchain_community.embeddings.ollama import OllamaEmbeddings

#Creating a RAG application to be able to query the NBA Collective Bargaining Agreement (CBA)
#Need to run the 5_populate_database.py script first to add the CBA PDF to the ChromaDB first


CHROMA_PATH = "chroma_nba_cba"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def get_embedding_function():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings



def query_rag():
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    #Finish adding the RAG query below


query_rag()
