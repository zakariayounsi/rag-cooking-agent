from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.messages import HumanMessage, SystemMessage


load_dotenv(override=True)

llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)

response = llm.invoke(
    [
        SystemMessage(content="You are a helpful assistant. The output should be in Markdown."),
        HumanMessage(content="C'est quoi un Agent AI ?"),
    ]
)

print(response.content)
