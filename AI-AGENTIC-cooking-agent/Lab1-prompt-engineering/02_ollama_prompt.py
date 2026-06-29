import os

from dotenv import load_dotenv
from langchain_ollama import ChatOllama


load_dotenv()

model_name = os.getenv("OLLAMA_MODEL", "llama3.2:3b")

llm = ChatOllama(model=model_name, temperature=0)

response = llm.invoke(
    [
        {"role": "system", "content": "You are a helpful assistant. The output should be in Markdown."},
        {"role": "user", "content": "C'est quoi un Agent AI ?"},
    ]
)

print(response.content)
