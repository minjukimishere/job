import time

import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# GPT-4 모델을 호출하는 llm 객체 생성
llm = ChatOpenAI()

# 프롬프트 템플릿 설정 (한글로)
prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 전문 이력서 작성자입니다. 전문적인 이력서를 작성해 주세요."),
    ("user", "이름: {name}\n연락처: {contact}\n자기소개: {summary}\n경력: {experience}\n학력: {education}\n기술: {skills}\n"),
    ("system", "다음 정보를 이력서 작성에 사용할 수 있습니다: 시작 연도: {start_year}, 종료 연도: {end_year}, 회사: {company}, 직무: {jobs}, URL: {url}")
])

# 출력 파서 생성 (GPT-4의 출력을 문자열로 파싱)
output_parser = StrOutputParser()

# 프롬프트 템플릿, GPT-4 모델, 출력 파서를 체인으로 연결
chain = prompt | llm | output_parser

st.title('이력서 생성기')

# 세션 상태에서 데이터 읽기

start_year = st.session_state.get('start_year', "신입")
end_year = st.session_state.get('end_year', "15년 이상")
company = st.session_state.get('company', "")
jobs = st.session_state.get('jobs', [])
url = st.session_state.get('url', "")
name = st.session_state.get('name', "")
contact = st.session_state.get('contact', "")
summary = st.session_state.get('summary', "")
experience = st.session_state.get('experience', "")
education = st.session_state.get('education', "")
skills = st.session_state.get('skills', "")

#ai 로 코드생성
# 버튼이 눌리면 '작성 중입니다...'라는 메시지와 함께 스피너 표시
with st.spinner('작성 중입니다...'):
    time.sleep(5)
# 생성된 이력서를 화면에 출력
    # 체인을 호출하여 사용자가 입력한 내용을 기반으로 GPT-4 모델을 호출하고 결과를 생성
    input_data = {
    "start_year": start_year,
    "end_year": end_year,
    "company": company,
    "jobs": jobs,
    "url": url,
    "name": name,
    "contact": contact,
    "summary": summary,
    "experience": experience,
    "education": education,
    "skills": skills
        }
    result = chain.invoke(input_data)
st.write(result)


       



