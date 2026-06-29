import streamlit as st
from langchain.messages import HumanMessage
from chef_agent import chef_agent

# ✅ مهم: config
config = {"configurable": {"thread_id": "streamlit_demo"}}

st.title("🍝 AI Cooking Assistant")

user_input = st.text_input("Pose ta question:")

if user_input:
    response = chef_agent.invoke(
        {"messages": [HumanMessage(content=user_input)], "preferences": []},
        config=config   # ✅ هذا هو الحل
    )
    st.write("👨‍🍳 Chef :", response["messages"][-1].content)