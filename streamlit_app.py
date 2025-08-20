
import streamlit as st
# 앱 제목 설정
st.title("📚 MBTI 학습 유형 진단")
st.markdown("나에게 맞는 학습 유형은 무엇일까요? 간단한 설문에 답해보세요.")

# MBTI 학습 유형 결과 데이터
learning_types = {
    "ISTJ": {
        "title": "논리적이고 체계적인 학습자 (ISTJ)",
        "description": "세부적인 정보와 사실을 바탕으로 단계적으로 학습하는 것을 선호합니다. 정해진 규칙과 절차를 따를 때 가장 편안함을 느낍니다.",
        "strategies": "- **정리:** 깔끔하게 정리된 교재나 노트 필기를 좋아합니다.\n- **반복:** 규칙적인 반복 학습을 통해 지식을 확고히 합니다.\n- **명확성:** 불명확한 개념보다는 구체적인 사실을 배우는 것을 선호합니다."
    },
    "ISFJ": {
        "title": "경험을 중시하는 협력적 학습자 (ISFJ)",
        "description": "실제 경험과 개인적인 관계를 통해 배우는 것을 선호합니다. 타인을 도우면서 배우는 것에 보람을 느낍니다.",
        "strategies": "- **실습:** 직접 해보는 실습을 통해 더 잘 기억합니다.\n- **협업:** 그룹 스터디나 팀 프로젝트를 통해 학습 효율을 높일 수 있습니다.\n- **예시:** 추상적인 이론보다는 구체적인 사례를 통해 이해합니다."
    },
    "INFJ": {
        "title": "통찰력이 뛰어난 이상주의적 학습자 (INFJ)",
        "description": "새로운 아이디어나 깊은 의미를 탐구하며 학습합니다. 전체적인 맥락을 파악하고 미래의 가능성을 상상하는 것을 좋아합니다.",
        "strategies": "- **토론:** 깊이 있는 주제에 대해 토론하며 생각을 정리합니다.\n- **연결:** 서로 다른 개념을 연결하고 의미를 찾는 것을 좋아합니다.\n- **자기성찰:** 학습 내용을 자신의 가치관과 연결하며 배웁니다."
    },
    "INTJ": {
        "title": "전략적이고 분석적인 학습자 (INTJ)",
        "description": "전체적인 시스템을 이해하고 가장 효율적인 방법을 찾아 학습합니다. 논리적 분석과 비판적 사고를 통해 지식을 습득합니다.",
        "strategies": "- **계획:** 학습 목표와 계획을 스스로 세우고 달성합니다.\n- **탐구:** 관심 있는 주제를 깊이 파고들어 전문가 수준의 지식을 얻으려 합니다.\n- **문제 해결:** 복잡한 문제를 해결하는 과정에서 학습합니다."
    },
    "ISTP": {
        "title": "실용적이고 현실적인 학습자 (ISTP)",
        "description": "직접 해보면서 배우는 것을 가장 즐깁니다. 손으로 만지고 조작하며 지식을 습득하고, 문제가 생기면 즉시 해결하는 능력이 뛰어납니다.",
        "strategies": "- **실습:** 이론보다는 직접적인 실습을 통해 배웁니다.\n- **자기 주도:** 자신의 속도와 방식으로 자유롭게 학습하는 것을 선호합니다.\n- **호기심:** 새로운 도구와 기술을 배우는 것을 좋아합니다."
    },
    "ISFP": {
        "title": "유연하고 감각적인 학습자 (ISFP)",
        "description": "자유롭고 유연한 환경에서 학습합니다. 예술적 감각이 뛰어나며, 학습 내용이 개인적인 가치나 흥미와 연결될 때 집중력이 높아집니다.",
        "strategies": "- **경험:** 오감을 활용한 경험 중심 학습을 선호합니다.\n- **창의성:** 학습 내용을 자신만의 방식으로 표현하고 응용하는 것을 좋아합니다.\n- **흥미:** 관심 있는 주제부터 먼저 배우는 것이 효과적입니다."
    },
    "INFP": {
        "title": "창의적이고 사색적인 학습자 (INFP)",
        "description": "자신만의 가치와 의미를 찾으며 학습합니다. 새로운 아이디어를 탐구하고, 자신의 내면과 연결된 주제에 깊이 몰입합니다.",
        "strategies": "- **사색:** 조용한 환경에서 혼자 생각하며 학습하는 것을 선호합니다.\n- **글쓰기:** 자신의 생각과 감정을 글로 표현하며 학습 내용을 정리합니다.\n- **심층적 이해:** 표면적인 지식보다 근본적인 의미를 파고드는 것을 좋아합니다."
    },
    "INTP": {
        "title": "지적 호기심이 많은 분석적 학습자 (INTP)",
        "description": "논리적이고 분석적인 사고를 통해 학습합니다. 세상의 모든 원리와 시스템을 이해하려 하며, 복잡한 이론을 탐구하는 것을 즐깁니다.",
        "strategies": "- **이론:** 새로운 이론과 개념을 배우는 것을 즐깁니다.\n- **논리:** 불일치하는 논리를 찾아내고 비판적으로 사고합니다.\n- **독학:** 혼자서 깊이 있는 주제를 탐구하는 데 능숙합니다."
    },
    "ESTP": {
        "title": "활동적이고 실용적인 학습자 (ESTP)",
        "description": "새로운 경험을 통해 즉흥적으로 배우는 것을 좋아합니다. 직접 행동하며 문제를 해결하는 것을 즐기며, 이론보다는 실용적인 지식을 선호합니다.",
        "strategies": "- **실습:** 직접 몸으로 부딪히며 배우는 것이 효과적입니다.\n- **경험:** 현장 학습이나 인턴십을 통해 더 많은 것을 배웁니다.\n- **간결성:** 핵심만 담긴 간결한 정보를 선호합니다."
    },
    "ESFP": {
        "title": "사교적이고 자유로운 학습자 (ESFP)",
        "description": "사람들과 교류하며 즐겁게 학습하는 것을 좋아합니다. 활기찬 분위기에서 배우고, 학습 내용을 공유하며 재미를 느낍니다.",
        "strategies": "- **그룹 스터디:** 친구들과 함께 공부하며 동기부여를 얻습니다.\n- **활동:** 게임, 퀴즈 등 재미있는 활동을 통해 배웁니다.\n- **감각 활용:** 시청각 자료나 흥미로운 예시를 통해 학습합니다."
    },
    "ENFP": {
        "title": "열정적이고 창의적인 학습자 (ENFP)",
        "description": "다양한 가능성과 아이디어를 탐구하며 학습합니다. 새로운 사람들과의 만남이나 자유로운 토론을 통해 영감을 얻습니다.",
        "strategies": "- **브레인스토밍:** 여러 아이디어를 자유롭게 공유하며 학습합니다.\n- **자유로운 환경:** 정해진 틀 없이 자유롭게 학습하는 것을 좋아합니다.\n- **새로운 도전:** 새로운 과목이나 분야에 도전하는 것을 즐깁니다."
    },
    "ENTP": {
        "title": "논쟁을 즐기는 발명가적 학습자 (ENTP)",
        "description": "복잡한 문제에 도전하고 논리적으로 분석하는 것을 좋아합니다. 다양한 관점을 탐색하고 토론하는 과정에서 지식을 습득합니다.",
        "strategies": "- **토론:** 논쟁과 토론을 통해 자신의 논리를 다듬습니다.\n- **가설 설정:** 새로운 가설을 세우고 이를 검증하는 과정을 즐깁니다.\n- **다양한 분야:** 여러 분야의 지식을 연결하여 창의적인 아이디어를 만들어냅니다."
    },
    "ESTJ": {
        "title": "현실적이고 계획적인 학습자 (ESTJ)",
        "description": "체계적이고 현실적인 목표를 세워 학습합니다. 명확한 규칙과 절차를 따르며, 학습 목표를 효율적으로 달성하는 것을 중요하게 생각합니다.",
        "strategies": "- **계획:** 철저한 학습 계획을 세워 그대로 실천합니다.\n- **실용성:** 즉시 적용할 수 있는 실용적인 지식을 선호합니다.\n- **체계적 정리:** 학습 자료를 체계적으로 정리하여 효율을 높입니다."
    },
    "ESFJ": {
        "title": "사교적이고 책임감 있는 학습자 (ESFJ)",
        "description": "사람들과 함께 배우고, 학습 공동체에 기여하는 것을 중요하게 생각합니다. 책임감이 강하고, 다른 사람들과의 관계 속에서 안정감을 느낍니다.",
        "strategies": "- **그룹 스터디:** 함께 공부하는 것을 통해 더 큰 시너지를 냅니다.\n- **선행 학습:** 다른 사람을 돕기 위해 미리 학습하는 것을 좋아합니다.\n- **피드백:** 다른 사람의 피드백을 통해 자신의 학습 방향을 점검합니다."
    },
    "ENFJ": {
        "title": "타인을 성장시키는 공감형 학습자 (ENFJ)",
        "description": "타인의 성장을 돕는 과정에서 보람을 느낍니다. 학습 내용이 다른 사람에게 어떤 영향을 미칠지 고민하며 배우는 것을 좋아합니다.",
        "strategies": "- **멘토링:** 다른 사람을 가르치며 자신의 지식을 다집니다.\n- **협력:** 팀 프로젝트나 그룹 활동에서 리더 역할을 맡아 학습을 이끕니다.\n- **피드백:** 긍정적인 피드백을 통해 학습 동기를 얻습니다."
    },
    "ENTJ": {
        "title": "비전이 있는 카리스마적 학습자 (ENTJ)",
        "description": "장기적인 목표와 큰 그림을 그리며 학습합니다. 효율성과 리더십을 발휘하여 학습 과정을 주도하고 관리하는 것을 즐깁니다.",
        "strategies": "- **목표 설정:** 명확한 학습 목표와 비전을 설정합니다.\n- **리소스 관리:** 학습 자료와 시간을 효율적으로 관리합니다.\n- **주도적 역할:** 그룹 스터디에서 리더 역할을 맡아 학습을 조직합니다."
    }
}

# 설문 문항 및 답변
questions = {
    "question_E_I": {
        "text": "1. 친구들과 대화하거나 함께 공부할 때, 당신은 주로:",
        "options": {"E": "자신의 생각을 먼저 말하며 대화를 주도하는 편이다.", "I": "상대방의 이야기를 먼저 듣고, 깊이 생각한 후 말하는 편이다."}
    },
    "question_S_N": {
        "text": "2. 새로운 지식을 배울 때, 당신은:",
        "options": {"S": "구체적인 사실과 실용적인 정보를 먼저 확인한다.", "N": "전체적인 개념이나 이론, 숨겨진 의미를 먼저 파악한다."}
    },
    "question_T_F": {
        "text": "3. 학습 방법을 선택할 때, 당신은:",
        "options": {"T": "가장 효율적이고 논리적인 방법을 찾는다.", "F": "나에게 흥미롭고 재미있는 방법을 찾는다."}
    },
    "question_J_P": {
        "text": "4. 시험 공부를 할 때, 당신은:",
        "options": {"J": "꼼꼼하게 계획을 세우고, 계획대로 실천하는 편이다.", "P": "계획 없이 자유롭게, 그때그때 끌리는 대로 공부하는 편이다."}
    },
    "question_E_I_2": {
        "text": "5. 새로운 분야를 공부할 때, 당신은:",
        "options": {"E": "여러 사람과 함께 배우며 궁금한 점을 공유하는 것을 좋아한다.", "I": "혼자 조용히 자료를 찾아보며 깊이 파고드는 것을 선호한다."}
    },
    "question_S_N_2": {
        "text": "6. 학습 내용이 이해가 안 될 때, 당신은:",
        "options": {"S": "예시나 실제 적용 사례를 찾아본다.", "N": "관련된 다른 이론이나 개념과의 연결 고리를 찾아보려 노력한다."}
    },
    "question_T_F_2": {
        "text": "7. 프로젝트를 진행할 때, 당신은:",
        "options": {"T": "논리적인 결과와 목표 달성에 집중한다.", "F": "팀원들의 협력과 조화로운 분위기를 중요하게 생각한다."}
    },
    "question_J_P_2": {
        "text": "8. 학습 일정을 관리할 때, 당신은:",
        "options": {"J": "정해진 마감 기한을 철저히 지키려 노력한다.", "P": "유연하게 일정을 조정하고, 자유롭게 진행하는 것을 선호한다."}
    }
}

# 세션 상태 초기화 (결과를 저장하기 위해 사용)
# st.session_state를 사용하면 페이지가 새로고침되어도 변수값이 유지됩니다.
if 'mbti_result' not in st.session_state:
    st.session_state['mbti_result'] = None

# 사용자 입력 받기
if st.session_state['mbti_result'] is None:
    st.subheader("아래 질문에 답하고 '제출하기' 버튼을 눌러주세요.")

    answers = {}
    for key, q in questions.items():
        # 라디오 버튼을 사용하여 질문에 대한 답변을 받습니다.
        answers[key] = st.radio(q["text"], options=list(q["options"].values()), key=key, index=None)

    # 제출 버튼
    submit_button = st.button("제출하기")

    if submit_button:
        # 모든 질문에 응답했는지 확인
        if None in answers.values():
            st.error("모든 질문에 답해주세요!")
        else:
            # MBTI 유형 계산
            # 각 지표별 응답을 기반으로 유형을 결정합니다.
            # E vs I
            e_count = sum(1 for q in ["question_E_I", "question_E_I_2"] if answers[q] == questions[q]["options"]["E"])
            i_count = sum(1 for q in ["question_E_I", "question_E_I_2"] if answers[q] == questions[q]["options"]["I"])
            ei_result = "E" if e_count > i_count else "I"

            # S vs N
            s_count = sum(1 for q in ["question_S_N", "question_S_N_2"] if answers[q] == questions[q]["options"]["S"])
            n_count = sum(1 for q in ["question_S_N", "question_S_N_2"] if answers[q] == questions[q]["options"]["N"])
            sn_result = "S" if s_count > n_count else "N"

            # T vs F
            t_count = sum(1 for q in ["question_T_F", "question_T_F_2"] if answers[q] == questions[q]["options"]["T"])
            f_count = sum(1 for q in ["question_T_F", "question_T_F_2"] if answers[q] == questions[q]["options"]["F"])
            tf_result = "T" if t_count > f_count else "F"

            # J vs P
            j_count = sum(1 for q in ["question_J_P", "question_J_P_2"] if answers[q] == questions[q]["options"]["J"])
            p_count = sum(1 for q in ["question_J_P", "question_J_P_2"] if answers[q] == questions[q]["options"]["P"])
            jp_result = "J" if j_count > p_count else "P"
            
            # 최종 MBTI 유형 조합
            mbti_type = ei_result + sn_result + tf_result + jp_result
            st.session_state['mbti_result'] = mbti_type
            # 결과를 세션 상태에 저장 후 페이지를 다시 실행합니다.
            # 이렇게 하면 제출 버튼을 누른 후에만 결과가 표시됩니다.
            st.rerun()

# 결과 표시
if st.session_state['mbti_result'] is not None:
    result_type = st.session_state['mbti_result']
    result_data = learning_types.get(result_type, {})
    
    st.subheader("🎉 당신의 학습 유형은...")
    st.header(f"{result_type} 입니다!")
    
    if result_data:
        st.info(f"**{result_data['title']}**")
        st.write(result_data['description'])
        
        st.markdown("---")
        st.subheader("📝 추천 학습 전략")
        st.markdown(result_data['strategies'])

    # 다시 하기 버튼
    if st.button("다시 진단하기"):
        st.session_state['mbti_result'] = None
        st.rerun()
    
    
    