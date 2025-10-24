import streamlit as st

st.set_page_config(page_title="タスクフロー診断", layout="centered")

# --- セッション状態初期化 ---
if 'step' not in st.session_state:
    st.session_state.step = 'B'
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# --- 質問関数 ---
def question_B():
    st.markdown("<h2 style='text-align:center;'>机・椅子・Wi-Fi・電源はある？</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:80px; text-align:center;'>💻</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([0.3, 1, 1])
    with col2:
        if st.button("ある"):
            st.session_state.answers['B'] = 'ある'
            st.session_state.step = 'C'
    with col3:
        if st.button("ない"):
            st.session_state.answers['B'] = 'ない'
            st.session_state.step = 'D'

def question_C():
    st.markdown("<h2 style='text-align:center;'>時間はどれくらいある？</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:80px; text-align:center;'>⏰</p>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns([0.3, 1, 1, 1])
    with col2:
        if st.button("1時間以上"):
            st.session_state.answers['C'] = '1時間以上'
            st.session_state.step = 'E'
    with col3:
        if st.button("30分前後"):
            st.session_state.answers['C'] = '30分前後'
            st.session_state.step = 'D'
    with col4:
        if st.button("10分以下"):
            st.session_state.answers['C'] = '10分以下'
            st.session_state.step = 'G'

def question_E():
    st.markdown("<h2 style='text-align:center;'>集中できる時間帯か？</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:80px; text-align:center;'>🧠</p>", unsafe_allow_html=True)
    col1, col2, col3= st.columns([0.3, 1, 1])
    with col2:
        if st.button("はい"):
            st.session_state.answers['E'] = 'はい'
            st.session_state.step = 'H'
    with col3:
        if st.button("いいえ"):
            st.session_state.answers['E'] = 'いいえ'
            st.session_state.step = 'I'

def question_H():
    st.markdown("<h2 style='text-align:center;'>身体・精神的エネルギーはある？</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:80px; text-align:center;'>⚡</p>", unsafe_allow_html=True)
    col1, col2, col3= st.columns([0.3, 1, 1])
    with col2:
        if st.button("ある"):
            st.session_state.answers['H'] = 'ある'
            st.session_state.step = 'J'
    with col3:
        if st.button("ない"):
            st.session_state.answers['H'] = 'ない…'
            st.session_state.step = 'K'

# --- 結果表示 ---
def result(mode):
    st.markdown(f"<h2 style='text-align:center;'>おすすめモード: {mode}</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>フロー終了</p>", unsafe_allow_html=True)

    st.markdown(
        "<p style='text-align:center; font-size:20px;'>タイマーをセットしてタスクを開始： "
        "<a href='https://accounts.toggl.com/track/login/?returnTo=https%3A%2F%2Ftrack.toggl.com%2Ftimer' target='_blank'>Toggle</a></p>",
        unsafe_allow_html=True
    )

# --- ステップ制御 ---
step = st.session_state.step

if step == 'B':
    question_B()
elif step == 'C':
    question_C()
elif step == 'D':
    result("読書・スマホでできる軽作業モード📖")
elif step in ['G','I','K']:
    result("家事・事務処理・休憩・セルフケア☘️")
elif step == 'E':
    question_E()
elif step == 'H':
    question_H()
elif step == 'J':
    result("PCでタスク実行モード💻")
