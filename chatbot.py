import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools import DuckDuckGoSearchRun

# env loads 
load_dotenv()


openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OpenAI API 키가 설정되지 않았습니다. .env 파일을 확인하세요.")

#  model setting 
llm = ChatOpenAI(model="gpt-4", openai_api_key=openai_api_key)

# search tool setting (duckduckgo)
search_tool = DuckDuckGoSearchRun()

# langchain agent intialize
agent = initialize_agent(
    tools=[search_tool],  # search function for new datas
    llm=llm,  # GPT-4 model 
    agent=AgentType.OPENAI_FUNCTIONS,  # OpenAI
    verbose=True
)


st.title("🤖Yehjin's Chatbot")

@st.cache_resource
def load_model():
    print("GPT-4 Model Loaded...")
    return agent

agent = load_model()

# conversation history check
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# previous conversation check
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# input message 
if prompt := st.chat_input("메시지를 입력하세요..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("ai"):

        response = agent.run(prompt)
        st.markdown(response)

    # conversation history update (save)
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    st.session_state.chat_history.append({"role": "ai", "content": response})
