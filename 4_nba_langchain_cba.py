from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

#Change the prompt template from telling a joke to teaching you about a topic. We will see
#a demostration of the LLM hallucinating on topics outside of its training data

llm = ChatOllama(model='llama3')
prompt = ChatPromptTemplate.from_template("Teach about this {topic}")

chain = prompt | llm | StrOutputParser()

user_message = input("Enter a topic to learn about: ")
print(chain.invoke({'topic': user_message}))
