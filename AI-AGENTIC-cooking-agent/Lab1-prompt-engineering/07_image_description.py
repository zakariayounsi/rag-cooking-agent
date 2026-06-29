import base64

from dotenv import load_dotenv
from langchain.messages import HumanMessage
from langchain_openai import ChatOpenAI


def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


load_dotenv(override=True)

image_path = "rag.png"
img = encode_image(image_path)

llm = ChatOpenAI(model="gpt-5.2")

response = llm.invoke(
    [
        HumanMessage(
            content=[
                {"type": "text", "text": "Qu'est-ce que tu vois dans cette image ?"},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img}"}},
            ]
        )
    ]
)

print(response.content)
