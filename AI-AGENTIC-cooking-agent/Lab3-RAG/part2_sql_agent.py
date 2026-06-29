from langchain_community.utilities import SQLDatabase
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent

# --- Connexion à la base SQLite ---
db = SQLDatabase.from_uri("sqlite:///Chinook.db")

# --- Tool personnalisé pour interroger la base SQL ---
@tool
def sql_query(query: str) -> str:
    """Obtain information from the database using SQL queries"""
    try:
        print(f"Executing SQL query: {query}")
        return db.run(query)
    except Exception as e:
        return f"Error: {e}"

# Test direct du tool
print("--- Test du tool sql_query ---")
print(sql_query.invoke("SELECT * FROM Artist LIMIT 10"))

# --- Création de l'agent SQL ---
model = ChatOllama(
    model="llama3.2:3b",
)

system_prompt = """You are a SQL expert.

Rules:
- Only use sql_query tool
- The sql_query tool takes a SQL query as input and returns the result of the query.
- Only use available columns
- If information does not exist, say so
- Do not guess
- you have to return the results in a human readable format, do not return raw SQL results or a sql query.

Database schema:
Table Artist:
- ArtistId
- Name
"""

agent = create_react_agent(
    model=model,
    tools=[sql_query],
    prompt=system_prompt
)

# --- Interrogation en langage naturel ---
question = HumanMessage(content="Give me the first 5 artists in the database")
response = agent.invoke(
    {"messages": [question]}
)
print("\n--- Réponse de l'Agent SQL ---")
print(response["messages"][-1].content)
