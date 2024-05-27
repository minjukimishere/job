import streamlit as st
import streamlit.components.v1 as components

st.header("AI HR", divider='orange')

col1,col2= st.columns(2)
with col1:
    st.page_link("pages/match_input.py", label="고용인") 
    st.text("AI 기반 고용 시스템을 사용 해 보시겠어요?")
with col2:
    st.page_link("pages/resume_make.py", label="구직자") 
    st.text("AI 기반 이력서를 작성 해 드려요.")

st.markdown(' ')

st.page_link("pages/ai_interview.py", label="인터뷰") 
st.text("AI 모의 인터뷰")