import streamlit as st
import time

st.set_page_config(page_title="증분 게임", page_icon="⚡")

if "points" not in st.session_state:
    st.session_state.points = 0

if "power" not in st.session_state:
    st.session_state.power = 1

if "auto" not in st.session_state:
    st.session_state.auto = 0

st.title("⚡ 에너지 증분 게임")

# 자동 생산
current_time = time.time()

if "last_time" not in st.session_state:
    st.session_state.last_time = current_time

elapsed = current_time - st.session_state.last_time
st.session_state.points += elapsed * st.session_state.auto
st.session_state.last_time = current_time

st.metric("에너지", f"{int(st.session_state.points):,}")
st.metric("클릭 파워", st.session_state.power)
st.metric("자동 생산", st.session_state.auto)

if st.button("⚡ 클릭"):
    st.session_state.points += st.session_state.power
    st.rerun()

st.divider()

st.subheader("업그레이드")

if st.button("🔨 클릭 파워 업그레이드 (10 에너지)"):
    if st.session_state.points >= 10:
        st.session_state.points -= 10
        st.session_state.power += 1
        st.rerun()

if st.button("🤖 자동 생산기 구매 (50 에너지)"):
    if st.session_state.points >= 50:
        st.session_state.points -= 50
        st.session_state.auto += 1
        st.rerun()

st.divider()

st.write("목표: 10,000 에너지 달성")

if st.session_state.points >= 10000:
    st.success("🎉 승리!")
