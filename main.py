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

mbti_description = {
    "INTJ": {
        "personality": "INTJ는 전략적이고 분석적인 성격으로, 독립적이고 혁신적입니다. 지적인 도전과 창의적인 문제 해결을 즐깁니다.",
        "jobs": "INTJ는 주로 연구, 엔지니어링, 전략 기획 등의 직업에서 두각을 나타냅니다. 과학자, 엔지니어, 분석가 등이 그 예입니다."
    },
    "INTP": {
        "personality": "INTP는 논리적이고 창의적인 성격으로, 새로운 아이디어를 탐구하는 것을 좋아합니다. 자율적이고 독립적으로 일하는 것을 선호합니다.",
        "jobs": "INTP는 철학자, 작가, 과학자 등의 직업에서 뛰어난 창의력과 분석 능력을 발휘합니다."
    },
    "ENTJ": {
        "personality": "ENTJ는 목표 지향적이고 결단력 있는 리더형 성격입니다. 체계적이고 전략적인 접근을 선호하며, 효율적인 해결책을 제시합니다.",
        "jobs": "ENTJ는 CEO, 프로젝트 관리자, 기업가 등 리더십을 발휘할 수 있는 직업에서 탁월한 능력을 발휘합니다."
    },
    "ENTP": {
        "personality": "ENTP는 창의적이고 혁신적인 사고를 가진 성격으로, 문제 해결과 새로운 아이디어 개발을 즐깁니다. 다양한 가능성을 탐구하는 것을 좋아합니다.",
        "jobs": "ENTP는 발명가, 컨설턴트, 기업가 등의 직업에서 다양한 아이디어를 실현시키는 데 능숙합니다."
    },
    "INFJ": {
        "personality": "INFJ는 깊은 이해력을 가진 성격으로, 다른 사람의 감정을 잘 이해하고 도와주는 것을 즐깁니다. 비전을 제시하고 따르는 것을 좋아합니다.",
        "jobs": "INFJ는 상담사, 심리학자, 작가 등의 직업에서 사람들을 돕고 깊이 있는 직업적 관계를 형성하는데 뛰어납니다."
    },
    "INFP": {
        "personality": "INFP는 이상주의적이고 창의적인 성격으로, 자신의 가치관에 맞는 삶을 살아가려 합니다. 예술적이고 감성적인 성향이 강합니다.",
        "jobs": "INFP는 예술가, 상담사, 작가 등 창의적이고 감성적인 직업에서 자신을 표현하는 것을 즐깁니다."
    },
    "ENFJ": {
        "personality": "ENFJ는 사람을 돕고 리더십을 발휘하는 성격으로, 다른 사람의 잠재력을 이끌어내는 능력이 뛰어납니다.",
        "jobs": "ENFJ는 교사, 심리학자, 리더 등 사람들과의 상호작용을 통해 다른 사람의 성장을 돕는 직업에서 두각을 나타냅니다."
    },
    "ENFP": {
        "personality": "ENFP는 에너지 넘치고 창의적인 성격으로, 새로운 아이디어를 구상하고 사람들과 소통하는 것을 즐깁니다.",
        "jobs": "ENFP는 예술가, 동기부여 강사, 사회복지사 등 사람들과의 연결을 통해 창의적인 해결책을 제시합니다."
    },
    "ISTJ": {
        "personality": "ISTJ는 책임감이 강하고 조직적인 성격으로, 안정적이고 규칙적인 환경을 선호합니다. 논리적이고 실용적인 성향을 지닙니다.",
        "jobs": "ISTJ는 회계사, 관리자, 엔지니어 등 실용적이고 체계적인 직업에서 높은 성과를 보입니다."
    },
    "ISFJ": {
        "personality": "ISFJ는 친절하고 헌신적인 성격으로, 사람들을 도우며 안정적인 환경을 선호합니다. 매우 세심하고 주의 깊은 성향을 가집니다.",
        "jobs": "ISFJ는 간호사, 교사, 사회복지사 등 사람들에게 직접적으로 도움을 주는 직업에서 뛰어납니다."
    },
    "ESTJ": {
        "personality": "ESTJ는 매우 조직적이고 실용적인 성격으로, 사실적이고 효율적인 접근을 선호합니다. 책임감이 강하고 규칙을 중요하게 생각합니다.",
        "jobs": "ESTJ는 관리자, 기업가, 경찰관 등 사람들을 이끌고 조직을 관리하는 직업에서 두각을 나타냅니다."
    },
    "ESFJ": {
        "personality": "ESFJ는 사람들과의 상호작용을 즐기며, 친절하고 배려 깊은 성격입니다. 협력적이고 사회적인 성향이 강합니다.",
        "jobs": "ESFJ는 간호사, 교사, 이벤트 기획자 등 사람들과의 교감을 통해 도움을 주는 직업에서 활약합니다."
    },
    "ISFP": {
        "personality": "ISFP는 예술적이고 감성적인 성격으로, 자유롭고 자연스러운 삶을 추구합니다. 미적인 감각이 뛰어나고 내성적인 성향을 가집니다.",
        "jobs": "ISFP는 예술가, 디자이너, 사진작가 등 창의적이고 감성적인 직업에서 능력을 발휘합니다."
    },
    "ESFP": {
        "personality": "ESFP는 활기차고 사람들과의 상호작용을 즐기는 성격으로, 삶을 즐기고 다른 사람들에게 즐거움을 주는 것을 선호합니다.",
        "jobs": "ESFP는 연예인, 음악가, 배우 등 사람들에게 즐거움을 주는 직업에서 두각을 나타냅니다."
    },
    "ESTP": {
        "personality": "ESTP는 활동적이고 실용적인 성격으로, 문제를 해결하기 위해 즉각적인 결정을 내리고 행동에 옮깁니다.",
        "jobs": "ESTP는 기업가, 세일즈, 탐정 등 빠른 결정이 필요한 직업에서 뛰어난 능력을 보입니다."
    }
}
# 2. 앱에 통합하기
이제 위 데이터를 streamlit 앱에 통합하여 MBTI 성격에 대한 설명과 추천 직업을 함께 보여줄 수 있도록 코드를 작성합니다.

python
복사
편집
import streamlit as st
import random
import time

# MBTI 성격 및 직업 설명 데이터
mbti_description = {
    "INTJ": {
        "personality": "INTJ는 전략적이고 분석적인 성격으로, 독립적이고 혁신적입니다. 지적인 도전과 창의적인 문제 해결을 즐깁니다.",
        "jobs": "INTJ는 주로 연구, 엔지니어링, 전략 기획 등의 직업에서 두각을 나타냅니다. 과학자, 엔지니어, 분석가 등이 그 예입니다."
    },
    "INTP": {
        "personality": "INTP는 논리적이고 창의적인 성격으로, 새로운 아이디어를 탐구하는 것을 좋아합니다. 자율적이고 독립적으로 일하는 것을 선호합니다.",
        "jobs": "INTP는 철학자, 작가, 과학자 등의 직업에서 뛰어난 창의력과 분석 능력을 발휘합니다."
    },
    "ENTJ": {
        "personality": "ENTJ는 목표 지향적이고 결단력 있는 리더형 성격입니다. 체계적이고 전략적인 접근을 선호하며, 효율적인 해결책을 제시합니다.",
        "jobs": "ENTJ는 CEO, 프로젝트 관리자, 기업가 등 리더십을 발휘할 수 있는 직업에서 탁월한 능력을 발휘합니다."
    },
    "ENTP": {
        "personality": "ENTP는 창의적이고 혁신적인 사고를 가진 성격으로, 문제 해결과 새로운 아이디어 개발을 즐깁니다. 다양한 가능성을 탐구하는 것을 좋아합니다.",
        "jobs": "ENTP는 발명가, 컨설턴트, 기업가 등의 직업에서 다양한 아이디어를 실현시키는 데 능숙합니다."
    },
    "INFJ": {
        "personality": "INFJ는 깊은 이해력을 가진 성격으로, 다른 사람의 감정을 잘 이해하고 도와주는 것을 즐깁니다. 비전을 제시하고 따르는 것을 좋아합니다.",
        "jobs": "INFJ는 상담사, 심리학자, 작가 등의 직업에서 사람들을 돕고 깊이 있는 직업적 관계를 형성하는데 뛰어납니다."
    },
    "INFP": {
        "personality": "INFP는 이상주의적이고 창의적인 성격으로, 자신의 가치관에 맞는 삶을 살아가려 합니다. 예술적이고 감성적인 성향이 강합니다.",
        "jobs": "INFP는 예술가, 상담사, 작가 등 창의적이고 감성적인 직업에서 자신을 표현하는 것을 즐깁니다."
    },
    "ENFJ": {
        "personality": "ENFJ는 사람을 돕고 리더십을 발휘하는 성격으로, 다른 사람의 잠재력을 이끌어내는 능력이 뛰어납니다.",
        "jobs": "ENFJ는 교사, 심리학자, 리더 등 사람들과의 상호작용을 통해 다른 사람의 성장을 돕는 직업에서 두각을 나타냅니다."
    },
    "ENFP": {
        "personality": "ENFP는 에너지 넘치고 창의적인 성격으로, 새로운 아이디어를 구상하고 사람들과 소통하는 것을 즐깁니다.",
        "jobs": "ENFP는 예술가, 동기부여 강사, 사회복지사 등 사람들과의 연결을 통해 창의적인 해결책을 제시합니다."
    },
    "ISTJ": {
        "personality": "ISTJ는 책임감이 강하고 조직적인 성격으로, 안정적이고 규칙적인 환경을 선호합니다. 논리적이고 실용적인 성향을 지닙니다.",
        "jobs": "ISTJ는 회계사, 관리자, 엔지니어 등 실용적이고 체계적인 직업에서 높은 성과를 보입니다."
    },
    "ISFJ": {
        "personality": "ISFJ는 친절하고 헌신적인 성격으로, 사람들을 도우며 안정적인 환경을 선호합니다. 매우 세심하고 주의 깊은 성향을 가집니다.",
        "jobs": "ISFJ는 간호사, 교사, 사회복지사 등 사람들에게 직접적으로 도움을 주는 직업에서 뛰어납니다."
    },
    "ESTJ": {
        "personality": "ESTJ는 매우 조직적이고 실용적인 성격으로, 사실적이고 효율적인 접근을 선호합니다. 책임감이 강하고 규칙을 중요하게 생각합니다.",
        "jobs": "ESTJ는 관리자, 기업가, 경찰관 등 사람들을 이끌고 조직을 관리하는 직업에서 두각을 나타냅니다."
    },
    "ESFJ": {
        "personality": "ESFJ는 사람들과의 상호작용을 즐기며, 친절하고 배려 깊은 성격입니다. 협력적이고 사회적인 성향이 강합니다.",
        "jobs": "ESFJ는 간호사, 교사, 이벤트 기획자 등 사람들과의 교감을 통해 도움을 주는 직업에서 활약합니다."
    },
    "ISFP": {
        "personality": "ISFP는 예술적이고 감성적인 성격으로, 자유롭고 자연스러운 삶을 추구합니다. 미적인 감각이 뛰어나고 내성적인 성향을 가집니다.",
        "jobs": "ISFP는 예술가, 디자이너, 사진작가 등 창의적이고 감성적인 직업에서 능력을 발휘합니다."
    },
    "ESFP": {
        "personality": "ESFP는 활기차고 사람들과의 상호작용을 즐기는 성격으로, 삶을 즐기고 다른 사람들에게 즐거움을 주는 것을 선호합니다.",
        "jobs": "ESFP는 연예인, 음악가, 배우 등 사람들에게 즐거움을 주는 직업에서 두각을 나타냅니다."
    },
    "ESTP": {
        "personality": "ESTP는 활동적이고 실용적인 성격으로, 문제를 해결하기 위해 즉각적인 결정을 내리고 행동에 옮깁니다.",
        "jobs": "ESTP는 기업가, 세일즈, 탐정 등 빠른 결정이 필요한 직업에서 뛰어난 능력을 보입니다."
    }
}

# Streamlit App
st.title("MBTI 직업 추천 앱 🎉")

# MBTI 선택을 위한 드롭다운 메뉴
mbti_choice = st.selectbox(
    "당신의 MBTI는 무엇인가요? 🤔",
    list(mbti_description.keys())
)

# 애니메이션 효과를 위한 텍스트
st.write("선택한 MBTI에 맞는 성격과 직업을 추천합니다... 🚀")

# 잠깐 대기 후 성격 설명과 직업 추천 표시
time.sleep(2)

# 성격 설명 및 직업 추천
if mbti_choice in mbti_description:
    personality = mbti_description[mbti_choice]["personality"]
    jobs = mbti_description[mbti_choice]["jobs"]
    
    st.subheader(f"성격 설명 🧠")
    st.write(personality)
    
    st.subheader(f"추천 직업 💼")
    st.write(jobs)
    
    st.balloons()  # 풍선 효과
else:
    st.write("잘못된 MBTI입니다. 다시 시도해주세요! 🎈")
