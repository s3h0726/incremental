# main.py

import time
import streamlit as st

from styles import load_css
from upgrades import BUILDINGS, get_building_cost, get_total_production
from prestige import (
    calculate_parts,
    calculate_drones,
    calculate_quantum_cores,
    calculate_transcendence,
    calculate_reality_breaks
)
from research import RESEARCH_TREE, buy_research, can_unlock
from achievements import (
    ACHIEVEMENTS,
    check_achievements,
    achievement_multiplier
)
from save import (
    save_game,
    load_game,
    delete_save,
    auto_save
)
from events import (
    initialize_event_data,
    update_event_effects,
    random_event
)
from utils import format_number


# =====================================
# 페이지 설정
# =====================================

st.set_page_config(
    page_title="Quantum Factory",
    page_icon="⚡",
    layout="wide"
)

load_css()


# =====================================
# 세션 초기화
# =====================================

DEFAULTS = {
    "energy": 0.0,
    "parts": 0,
    "drones": 0,
    "quantum_cores": 0,
    "transcendence": 0,
    "reality_breaks": 0,

    "click_power": 1,
    "energy_per_second": 0,

    "owned_buildings": {},
    "research": [],
    "achievements": [],

    "last_update": time.time()
}

for key, value in DEFAULTS.items():

    if key not in st.session_state:
        st.session_state[key] = value


initialize_event_data(
    st.session_state
)


# =====================================
# 저장 불러오기
# =====================================

if "loaded" not in st.session_state:

    load_game(st.session_state)

    st.session_state.loaded = True


# =====================================
# 오프라인 생산
# =====================================

current_time = time.time()

elapsed = (
    current_time
    - st.session_state.last_update
)

multiplier = achievement_multiplier(
    st.session_state
)

event_multiplier = (
    st.session_state.event_multiplier
)

st.session_state.energy += (
    st.session_state.energy_per_second
    * elapsed
    * multiplier
    * event_multiplier
)

st.session_state.last_update = (
    current_time
)


# =====================================
# 이벤트
# =====================================

update_event_effects(
    st.session_state
)

event_message = random_event(
    st.session_state
)

if event_message:
    st.toast(event_message)


# =====================================
# 업적 검사
# =====================================

new_achievements = (
    check_achievements(
        st.session_state
    )
)

for achievement_id in new_achievements:

    st.toast(
        f"🏆 업적 달성: "
        f"{ACHIEVEMENTS[achievement_id]['name']}"
    )


# =====================================
# 제목
# =====================================

st.title("⚡ Quantum Factory")


# =====================================
# 자원 표시
# =====================================

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "⚡ 에너지",
        format_number(
            st.session_state.energy
        )
    )

with c2:
    st.metric(
        "🔩 부품",
        format_number(
            st.session_state.parts
        )
    )

with c3:
    st.metric(
        "🤖 드론",
        format_number(
            st.session_state.drones
        )
    )


# =====================================
# 탭
# =====================================

tabs = st.tabs([
    "⚡ 생산",
    "🏭 건물",
    "🧪 연구",
    "🏆 업적",
    "♾ 프레스티지",
    "⚙ 설정"
])


# =====================================
# 생산
# =====================================

with tabs[0]:

    st.subheader("수동 생산")

    if st.button(
        "⚡ 에너지 생산"
    ):

        st.session_state.energy += (
            st.session_state.click_power
        )

        st.rerun()


# =====================================
# 건물
# =====================================

with tabs[1]:

    st.subheader("건물 구매")

    for building_id, data in BUILDINGS.items():

        owned = (
            st.session_state
            .owned_buildings
            .get(
                building_id,
                0
            )
        )

        cost = get_building_cost(
            data["cost"],
            owned
        )

        col1, col2 = st.columns([3,1])

        with col1:

            st.write(
                f"{data['name']} "
                f"(보유 {owned})"
            )

        with col2:

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

                    st.session_state.energy_per_second = (
                        get_total_production(
                            st.session_state
                            .owned_buildings
                        )
                    )

                    st.rerun()


# =====================================
# 연구
# =====================================

with tabs[2]:

    st.subheader("연구")

    for research_id, research in RESEARCH_TREE.items():

        unlocked = can_unlock(
            research_id,
            st.session_state.research
        )

        owned = (
            research_id
            in st.session_state.research
        )

        if owned:

            st.success(
                research["name"]
            )

        elif unlocked:

            if st.button(
                f"{research['name']} "
                f"({research['cost']})"
            ):

                buy_research(
                    research_id,
                    st.session_state
                )

                st.rerun()


# =====================================
# 업적
# =====================================

with tabs[3]:

    for achievement_id in (
        st.session_state.achievements
    ):

        achievement = (
            ACHIEVEMENTS[
                achievement_id
            ]
        )

        st.success(
            achievement["name"]
        )


# =====================================
# 프레스티지
# =====================================

with tabs[4]:

    st.subheader("프레스티지")

    st.write(
        f"획득 가능 부품: "
        f"{calculate_parts(st.session_state.energy)}"
    )

    if st.button(
        "🔩 부품 프레스티지"
    ):

        gain = calculate_parts(
            st.session_state.energy
        )

        if gain > 0:

            st.session_state.parts += gain
            st.session_state.energy = 0

            st.rerun()


# =====================================
# 설정
# =====================================

with tabs[5]:

    if st.button("💾 저장"):
        save_game(st.session_state)

    if st.button("📂 불러오기"):
        load_game(st.session_state)
        st.rerun()

    if st.button("🗑 저장 삭제"):
        delete_save()


# =====================================
# 자동 저장
# =====================================

auto_save(st.session_state)
