# 🚀 Chatbot 

### 📌 Overview 
langchain exercise 를 위한 Chatbot

OpenAI GPT-4와 DuckDuckGo 검색을 활용한 AI 챗봇 

Streamlit을 기반으로 동작하며, LangChain을 활용하여 검색 기능을 포함한 대화형 AI를 제공

### 🛠 Tech Stack

- Language: Python

- Web Framework Streamlit

- AI Model: OpenAI GPT-4 (via LangChain)

- API: OpenAI API, DuckDuckGo Search API

- Agent : Langchain Agent



### 🚀 How to work
1. 환경 변수 설정
.env 파일을 생성하고 아래 내용을 추가하세요
```Python
OPENAI_API_KEY=your_openai_api_key
```

2. 패키지 설치
```Python
pip install -r requirements.txt
```
3. 실행
```Python
streamlit run app.py
```

### 📌 Improvements & Plan to.. 
(1) Agent 추가: 최신 데이터를 검색하고 보다 강력한 대화 기능을 제공하기 위해 LangChain의 Agent 기능을 도입 

(2) 응답 속도 최적화: 현재 답변 시간이 30초 이상 걸리는 경우가 있어, 비동기 처리 및 캐싱을 통해 속도를 개선할 예정

(3) VLM 적용: Vision-Language Model(VLM)을 적용하여 이미지-텍스트 인식 기능을 추가할 계획

