import streamlit as st
import time

from styles import load_css
from upgrades import BUILDINGS
from prestige import calculate_prestige_gain
from utils import format_number

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="Quantum Factory",
    page_icon="⚡",
    layout="wide"
)

load_css()

# -----------------------------
# 세션 데이터 초기화
# -----------------------------
defaults = {
    "energy": 0.0,
    "parts": 0.0,
    "drones": 0.0,
    "quantum_cores": 0.0,
    "transcendence": 0,

    "click_power": 1,
    "energy_per_second": 0,

    "owned_buildings": {},

    "achievements": [],
    "research": [],

    "last_update": time.time()
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -----------------------------
# 오프라인 생산 계산
# -----------------------------
current_time = time.time()

elapsed = current_time - st.session_state.last_update

st.session_state.energy += (
    st.session_state.energy_per_second * elapsed
)

st.session_state.last_update = current_time

# -----------------------------
# 헤더
# -----------------------------
st.markdown(
    """
    <h1 style='text-align:center'>
    ⚡ Quantum Factory
    </h1>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# 자원 표시
# -----------------------------
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "⚡ 에너지",
        format_number(st.session_state.energy)
    )

with col2:
    st.metric(
        "🔩 부품",
        format_number(st.session_state.parts)
    )

with col3:
    st.metric(
        "🤖 드론",
        format_number(st.session_state.drones)
    )

with col4:
    st.metric(
        "🌌 양자코어",
        format_number(st.session_state.quantum_cores)
    )

with col5:
    st.metric(
        "♾ 초월점수",
        format_number(st.session_state.transcendence)
    )

st.divider()

# -----------------------------
# 탭
# -----------------------------
tabs = st.tabs([
    "⚡ 생산",
    "🏭 업그레이드",
    "🧪 연구",
    "🏆 업적",
    "♾ 프레스티지",
    "⚙ 설정"
])

# =====================================================
# 생산 탭
# =====================================================
with tabs[0]:

    st.subheader("에너지 생산")

    if st.button(
        "⚡ GENERATE",
        use_container_width=True
    ):
        st.session_state.energy += (
            st.session_state.click_power
        )
        st.rerun()

    st.write(
        f"클릭 생산량 : "
        f"{format_number(st.session_state.click_power)}"
    )

    st.write(
        f"자동 생산량 : "
        f"{format_number(st.session_state.energy_per_second)}/s"
    )

# =====================================================
# 업그레이드 탭
# =====================================================
with tabs[1]:

    st.subheader("시설")

    for building_id, building in BUILDINGS.items():

        owned = st.session_state.owned_buildings.get(
            building_id,
            0
        )

        cost = building["base_cost"] * (
            1.15 ** owned
        )

        with st.container():

            left, right = st.columns([4,1])

            with left:
                st.markdown(
                    f"""
                    **{building['name']}**

                    생산량:
                    {building['production']}/s

                    보유:
                    {owned}
                    """
                )

            with right:

                if st.button(
                    f"구매 {building_id}"
                ):

                    if (
                        st.session_state.energy
                        >= cost
                    ):
                        st.session_state.energy -= cost

                        st.session_state.owned_buildings[
                            building_id
                        ] = owned + 1

                        st.session_state.energy_per_second += (
                            building["production"]
                        )

                        st.rerun()

            st.caption(
                f"비용: "
                f"{format_number(cost)}"
            )

# =====================================================
# 연구
# =====================================================
with tabs[2]:

    st.subheader("연구소")

    st.info(
        "research.py에서 구현 예정"
    )

# =====================================================
# 업적
# =====================================================
with tabs[3]:

    st.subheader("업적")

    if not st.session_state.achievements:
        st.write("획득한 업적이 없습니다.")

    for achievement in (
        st.session_state.achievements
    ):
        st.success(achievement)

# =====================================================
# 프레스티지
# =====================================================
with tabs[4]:

    st.subheader("초월")

    gain = calculate_prestige_gain(
        st.session_state.energy
    )

    st.write(
        f"획득 가능한 초월점수: "
        f"{gain}"
    )

    if st.button(
        "♾ 프레스티지 실행"
    ):

        if gain > 0:

            st.session_state.transcendence += gain

            st.session_state.energy = 0
            st.session_state.parts = 0
            st.session_state.drones = 0
            st.session_state.quantum_cores = 0

            st.session_state.energy_per_second = 0
            st.session_state.owned_buildings = {}

            st.rerun()

# =====================================================
# 설정
# =====================================================
with tabs[5]:

    st.subheader("설정")

    if st.button(
        "데이터 초기화"
    ):

        for key in list(
            st.session_state.keys()
        ):
            del st.session_state[key]

        st.rerun()

# -----------------------------
# 푸터
# -----------------------------
st.divider()

st.caption(
    "Quantum Factory v0.1"
)
