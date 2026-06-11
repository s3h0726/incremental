import streamlit as st


def load_css():

    st.markdown(
        """
<style>

/* ==========================
   전체 배경
========================== */

.stApp {

    background:
    linear-gradient(
        135deg,
        #020617,
        #0f172a,
        #1e293b
    );

    color: white;
}


/* ==========================
   제목
========================== */

h1 {

    color: #60a5fa;

    text-shadow:
        0px 0px 10px #3b82f6,
        0px 0px 25px #3b82f6;

    font-weight: 800;
}


/* ==========================
   카드
========================== */

div[data-testid="metric-container"] {

    background: rgba(
        15,
        23,
        42,
        0.95
    );

    border: 1px solid #2563eb;

    border-radius: 16px;

    padding: 18px;

    box-shadow:
        0 0 10px rgba(
            59,
            130,
            246,
            0.3
        );

    transition: 0.3s;
}


div[data-testid="metric-container"]:hover {

    transform: translateY(-4px);

    box-shadow:
        0 0 20px rgba(
            96,
            165,
            250,
            0.8
        );
}


/* ==========================
   버튼
========================== */

.stButton > button {

    width: 100%;

    border-radius: 14px;

    height: 55px;

    font-size: 18px;

    font-weight: 700;

    border: none;

    color: white;

    background:
    linear-gradient(
        90deg,
        #2563eb,
        #3b82f6
    );

    box-shadow:
        0 0 10px rgba(
            59,
            130,
            246,
            0.5
        );

    transition: 0.2s;
}


.stButton > button:hover {

    transform: scale(1.03);

    box-shadow:
        0 0 25px rgba(
            96,
            165,
            250,
            0.8
        );
}


/* ==========================
   탭
========================== */

.stTabs [data-baseweb="tab"] {

    font-size: 18px;

    font-weight: 700;

    color: white;
}


.stTabs [aria-selected="true"] {

    color: #60a5fa !important;

    text-shadow:
        0px 0px 10px #60a5fa;
}


/* ==========================
   구분선
========================== */

hr {

    border-color:
    rgba(
        59,
        130,
        246,
        0.4
    );
}


/* ==========================
   스크롤바
========================== */

::-webkit-scrollbar {

    width: 10px;
}


::-webkit-scrollbar-track {

    background: #0f172a;
}


::-webkit-scrollbar-thumb {

    background: #2563eb;

    border-radius: 20px;
}


/* ==========================
   정보 박스
========================== */

.stAlert {

    border-radius: 14px;
}


/* ==========================
   사이드바
========================== */

section[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #0f172a,
        #020617
    );

    border-right:
    1px solid #2563eb;
}


/* ==========================
   푸터 제거
========================== */

footer {

    visibility: hidden;
}


/* ==========================
   메인 Generate 버튼
========================== */

.generate-button button {

    height: 90px;

    font-size: 32px;

    border-radius: 20px;

    background:
    linear-gradient(
        90deg,
        #2563eb,
        #60a5fa
    );

    animation:
        pulse 2s infinite;
}


/* ==========================
   애니메이션
========================== */

@keyframes pulse {

    0% {

        box-shadow:
        0 0 0px
        rgba(
            96,
            165,
            250,
            0.4
        );
    }

    50% {

        box-shadow:
        0 0 30px
        rgba(
            96,
            165,
            250,
            0.8
        );
    }

    100% {

        box-shadow:
        0 0 0px
        rgba(
            96,
            165,
            250,
            0.4
        );
    }
}

</style>
        """,
        unsafe_allow_html=True
    )
