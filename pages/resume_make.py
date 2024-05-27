import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# GPT-4 모델을 호출하는 llm 객체 생성
llm = ChatOpenAI()

# 제목과 설명 추가
st.title('경력사항을 입력해주세요')
st.markdown("")

# start_year 입력 받기, end_year 입력 받기
start_year, end_year = st.select_slider(
    "근무기간",
    options=["신입", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15년 이상"],
    value=("신입", "15년 이상"))

st.write("입사 연차:", start_year)
st.write("퇴사 연차:", end_year)

# 직장명 입력 받기
company = st.text_input("직장명")
st.write("Company:", company)

# Jobs 입력 받기 (여러 개 선택 가능)
jobs = st.multiselect(
    "직무",
    ["DevOps/시스템 관리자", "HW/임베디드 개발자", "IOS 개발자",
     "데이터 사이언티스트", "데이터 엔지니어", "서버/백엔드 개발자",
     "안드로이드 개발자", "프론트엔드 개발자", "게임 서버 개발자",
     "게임 클라이언트 개발자"])

st.write("직무:", jobs)

# URL 입력 받기
url = st.text_input("나의 역량이 잘 나타날 수 있는 URL을 입력해주세요")

st.write("URL:", url)

# 추가 정보 입력 받기
name = st.text_input("이름")
contact = st.text_input("연락처")
summary = st.text_area("자기소개")
experience = st.text_area("경력")
education = st.text_area("학력")
skills = st.text_area("기술")

# 상태 저장
if 'company' not in st.session_state:
    st.session_state.company = ""
if 'start_year' not in st.session_state:
    st.session_state.start_year = ""
if 'end_year' not in st.session_state:
    st.session_state.end_year = ""
if 'jobs' not in st.session_state:
    st.session_state.jobs = []
if 'url' not in st.session_state:
    st.session_state.url = ""
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'contact' not in st.session_state:
    st.session_state.contact = ""
if 'summary' not in st.session_state:
    st.session_state.summary = ""
if 'experience' not in st.session_state:
    st.session_state.experience = ""
if 'education' not in st.session_state:
    st.session_state.education = ""
if 'skills' not in st.session_state:
    st.session_state.skills = ""

st.session_state.start_year = start_year
st.session_state.end_year = end_year
st.session_state.company = company
st.session_state.jobs = jobs
st.session_state.url = url
st.session_state.name = name
st.session_state.contact = contact
st.session_state.summary = summary
st.session_state.experience = experience
st.session_state.education = education
st.session_state.skills = skills

# 페이지 이동 버튼
st.page_link("pages/resume_maked.py", label="이력서 생성하기")

# 확인용 결과창
if st.button('결과 출력'):
    st.markdown("### 결과:")
    st.write(f"start_year: {st.session_state.start_year}")
    st.write(f"end_year: {st.session_state.end_year}")
    st.write(f"company: {st.session_state.company}")
    st.write(f"jobs: {st.session_state.jobs}")
    st.write(f"url: {st.session_state.url}")
    st.write(f"name: {st.session_state.name}")
    st.write(f"contact: {st.session_state.contact}")
    st.write(f"summary: {st.session_state.summary}")
    st.write(f"experience: {st.session_state.experience}")
    st.write(f"education: {st.session_state.education}")
    st.write(f"skills: {st.session_state.skills}")

st.markdown("---")
