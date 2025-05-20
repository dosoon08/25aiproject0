import streamlit as st
import random
import time

# MBTI와 관련된 직업 추천 데이터
mbti_jobs = {
    "INTJ": ["Scientist 🧑‍🔬", "Engineer 🔧", "Researcher 📚"],
    "INTP": ["Philosopher 🤔", "Scientist 🧑‍🔬", "Writer ✍️"],
    "ENTJ": ["CEO 💼", "Project Manager 📋", "Entrepreneur 💡"],
    "ENTP": ["Inventor 💡", "Consultant 💬", "Entrepreneur 🚀"],
    "INFJ": ["Counselor 🧘‍♀️", "Psychologist 🧠", "Writer 📖"],
    "INFP": ["Artist 🎨", "Counselor 💬", "Writer ✍️"],
    "ENFJ": ["Teacher 🍎", "Psychologist 🧠", "Leader 🌟"],
    "ENFP": ["Artist 🎨", "Motivational Speaker 🎤", "Social Worker ❤️"],
    "ISTJ": ["Accountant 🧾", "Manager 💼", "Engineer 🔧"],
    "ISFJ": ["Nurse 🩺", "Teacher 🍎", "Social Worker 🤝"],
    "ESTJ": ["Manager 🧑‍💼", "Entrepreneur 💼", "Police Officer 🚔"],
    "ESFJ": ["Nurse 🩺", "Teacher 👩‍🏫", "Event Planner 🎉"],
    "ISFP": ["Artist 🎨", "Designer 👗", "Photographer 📸"],
    "INFP": ["Poet ✍️", "Counselor 🧘‍♀️", "Artist 🎨"],
    "ESFP": ["Entertainer 🎭", "Actor 🎬", "Musician 🎶"],
    "ESTP": ["Entrepreneur 💼", "Salesperson 💵", "Detective 🕵️‍♂️"],
}

# Streamlit App
st.title("MBTI 직업 추천 앱 🎉")

# MBTI 선택을 위한 드롭다운 메뉴
mbti_choice = st.selectbox(
    "당신의 MBTI는 무엇인가요? 🤔",
    ["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP",
     "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISFP", "INFP", "ESFP", "ESTP"]
)

# 애니메이션 효과를 위한 텍스트
st.write("선택한 MBTI에 맞는 직업을 추천합니다... 🚀")

# 잠깐 대기 후 직업 추천 표시
time.sleep(2)

# 직업 추천
if mbti_choice in mbti_jobs:
    recommended_jobs = random.choice(mbti_jobs[mbti_choice])
    st.subheader(f"추천 직업은: {recommended_jobs} 🎉")
    st.balloons()  # 풍선 효과
else:
    st.write("잘못된 MBTI입니다. 다시 시도해주세요! 🎈")

