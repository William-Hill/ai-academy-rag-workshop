# Query the llama 3 model.
import ollama

user_message = input("Enter a prompt:")

stream = ollama.chat(model='llama3', messages=[{
    'role': 'user',
    'content': user_message,
}], 
stream=True
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)