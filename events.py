# events.py

import random
import time

# ==========================================
# 이벤트 목록
# ==========================================

EVENTS = {

    "energy_surge": {
        "name": "⚡ 에너지 폭주",
        "description": "현재 에너지의 25% 획득",
        "chance": 20
    },

    "parts_cache": {
        "name": "🔩 부품 창고 발견",
        "description": "부품 10% 획득",
        "chance": 15
    },

    "drone_discovery": {
        "name": "🤖 드론 발견",
        "description": "드론 1개 획득",
        "chance": 10
    },

    "quantum_storm": {
        "name": "🌌 양자 폭풍",
        "description": "양자코어 1개 획득",
        "chance": 5
    },

    "factory_boost": {
        "name": "🏭 공장 최적화",
        "description": "60초간 생산량 2배",
        "chance": 15
    },

    "research_breakthrough": {
        "name": "🧪 연구 돌파구",
        "description": "연구 비용 20% 감소",
        "chance": 10
    },

    "transcendent_gift": {
        "name": "♾ 초월의 선물",
        "description": "초월점수 획득",
        "chance": 3
    },

    "reality_crack": {
        "name": "💥 현실 균열",
        "description": "현실붕괴 획득",
        "chance": 1
    },

    "nothing": {
        "name": "🌑 조용한 하루",
        "description": "아무 일도 일어나지 않았다",
        "chance": 21
    }
}


# ==========================================
# 이벤트 뽑기
# ==========================================

def roll_event():

    weighted_pool = []

    for event_id, data in EVENTS.items():

        weighted_pool.extend(
            [event_id] * data["chance"]
        )

    return random.choice(
        weighted_pool
    )


# ==========================================
# 이벤트 적용
# ==========================================

def apply_event(
    event_id,
    session
):

    if event_id == "energy_surge":

        gain = max(
            int(session.energy * 0.25),
            100
        )

        session.energy += gain

        return (
            f"⚡ 에너지 폭주! "
            f"+{gain:,} 에너지"
        )

    elif event_id == "parts_cache":

        gain = max(
            int(session.parts * 0.10),
            1
        )

        session.parts += gain

        return (
            f"🔩 부품 창고 발견! "
            f"+{gain:,} 부품"
        )

    elif event_id == "drone_discovery":

        session.drones += 1

        return (
            "🤖 드론 발견! "
            "+1 드론"
        )

    elif event_id == "quantum_storm":

        session.quantum_cores += 1

        return (
            "🌌 양자 폭풍! "
            "+1 양자코어"
        )

    elif event_id == "factory_boost":

        session.event_multiplier = 2
        session.event_end_time = (
            time.time() + 60
        )

        return (
            "🏭 공장 최적화! "
            "60초 동안 생산량 2배"
        )

    elif event_id == "research_breakthrough":

        session.research_discount = 0.8

        return (
            "🧪 연구 돌파구! "
            "연구 비용 20% 감소"
        )

    elif event_id == "transcendent_gift":

        if hasattr(
            session,
            "transcendence"
        ):

            session.transcendence += 1

        return (
            "♾ 초월의 선물! "
            "+1 초월점수"
        )

    elif event_id == "reality_crack":

        if not hasattr(
            session,
            "reality_breaks"
        ):
            session.reality_breaks = 0

        session.reality_breaks += 1

        return (
            "💥 현실 균열! "
            "+1 현실붕괴"
        )

    return (
        "🌑 아무 일도 일어나지 않았다."
    )


# ==========================================
# 이벤트 버프 갱신
# ==========================================

def update_event_effects(
    session
):

    current_time = time.time()

    if (
        hasattr(
            session,
            "event_end_time"
        )
        and session.event_end_time > 0
        and current_time
        >= session.event_end_time
    ):

        session.event_multiplier = 1
        session.event_end_time = 0


# ==========================================
# 이벤트 발생
# ==========================================

LAST_EVENT_TIME = 0


def random_event(
    session,
    interval=120
):

    global LAST_EVENT_TIME

    now = time.time()

    if (
        now - LAST_EVENT_TIME
        >= interval
    ):

        LAST_EVENT_TIME = now

        event_id = roll_event()

        return apply_event(
            event_id,
            session
        )

    return None


# ==========================================
# 세션 기본값 초기화
# ==========================================

def initialize_event_data(
    session
):

    defaults = {

        "event_multiplier": 1,

        "event_end_time": 0,

        "research_discount": 1
    }

    for key, value in defaults.items():

        if key not in session:

            session[key] = value
