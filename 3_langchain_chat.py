from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

#Use Langchain to create Prompt Templates.  This can help with structuring prompts if you want your
#LLM to only serve specific purposes such as telling jokes

llm = ChatOllama(model='llama3')
prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")

chain = prompt | llm | StrOutputParser()

user_message = input("Enter a topic to make a joke about: ")
print(chain.invoke({'topic': user_message}))
