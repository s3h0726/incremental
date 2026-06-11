# achievements.py

ACHIEVEMENTS = {

    # =====================
    # 에너지 업적
    # =====================

    "energy_100": {
        "name": "첫 번째 전력",
        "description": "에너지 100 달성",
        "reward": 1.05
    },

    "energy_1000": {
        "name": "소형 발전소",
        "description": "에너지 1,000 달성",
        "reward": 1.05
    },

    "energy_10000": {
        "name": "산업 혁명",
        "description": "에너지 10,000 달성",
        "reward": 1.10
    },

    "energy_1m": {
        "name": "메가와트",
        "description": "에너지 1,000,000 달성",
        "reward": 1.15
    },

    "energy_1b": {
        "name": "기가와트",
        "description": "에너지 1,000,000,000 달성",
        "reward": 1.25
    },

    # =====================
    # 건물 업적
    # =====================

    "build_10": {
        "name": "건설 시작",
        "description": "건물 10개 보유",
        "reward": 1.05
    },

    "build_50": {
        "name": "공장 지구",
        "description": "건물 50개 보유",
        "reward": 1.10
    },

    "build_100": {
        "name": "산업 도시",
        "description": "건물 100개 보유",
        "reward": 1.20
    },

    "build_500": {
        "name": "메가시티",
        "description": "건물 500개 보유",
        "reward": 1.35
    },

    # =====================
    # 부품 업적
    # =====================

    "parts_10": {
        "name": "부품 생산",
        "description": "부품 10개 획득",
        "reward": 1.10
    },

    "parts_100": {
        "name": "기계 제작",
        "description": "부품 100개 획득",
        "reward": 1.15
    },

    "parts_1000": {
        "name": "대량 생산",
        "description": "부품 1,000개 획득",
        "reward": 1.25
    },

    # =====================
    # 드론 업적
    # =====================

    "drones_10": {
        "name": "드론 군단",
        "description": "드론 10개 획득",
        "reward": 1.20
    },

    "drones_100": {
        "name": "기계 제국",
        "description": "드론 100개 획득",
        "reward": 1.30
    },

    # =====================
    # 양자코어 업적
    # =====================

    "quantum_1": {
        "name": "양자 시대",
        "description": "양자코어 1개 획득",
        "reward": 1.50
    },

    "quantum_10": {
        "name": "양자 문명",
        "description": "양자코어 10개 획득",
        "reward": 2.00
    },

    # =====================
    # 초월 업적
    # =====================

    "trans_1": {
        "name": "초월자",
        "description": "초월점수 1 획득",
        "reward": 2.00
    },

    "trans_10": {
        "name": "차원 여행자",
        "description": "초월점수 10 획득",
        "reward": 3.00
    },

    # =====================
    # 현실붕괴 업적
    # =====================

    "reality_1": {
        "name": "현실 균열",
        "description": "현실붕괴 1회",
        "reward": 5.00
    },

    "reality_10": {
        "name": "창조자",
        "description": "현실붕괴 10회",
        "reward": 10.00
    }

}
def total_buildings(session):

    return sum(
        session.owned_buildings.values()
    )


def check_achievements(session):

    unlocked = []

    energy = session.energy
    parts = session.parts
    drones = session.drones
    quantum = session.quantum_cores

    transcendence = (
        session.transcendence
    )

    reality = getattr(
        session,
        "reality_breaks",
        0
    )

    buildings = total_buildings(
        session
    )

    checks = {

        "energy_100":
            energy >= 100,

        "energy_1000":
            energy >= 1000,

        "energy_10000":
            energy >= 10000,

        "energy_1m":
            energy >= 1_000_000,

        "energy_1b":
            energy >= 1_000_000_000,

        "build_10":
            buildings >= 10,

        "build_50":
            buildings >= 50,

        "build_100":
            buildings >= 100,

        "build_500":
            buildings >= 500,

        "parts_10":
            parts >= 10,

        "parts_100":
            parts >= 100,

        "parts_1000":
            parts >= 1000,

        "drones_10":
            drones >= 10,

        "drones_100":
            drones >= 100,

        "quantum_1":
            quantum >= 1,

        "quantum_10":
            quantum >= 10,

        "trans_1":
            transcendence >= 1,

        "trans_10":
            transcendence >= 10,

        "reality_1":
            reality >= 1,

        "reality_10":
            reality >= 10

    }

    for achievement_id, passed in checks.items():

        if passed:

            if (
                achievement_id
                not in session.achievements
            ):

                session.achievements.append(
                    achievement_id
                )

                unlocked.append(
                    achievement_id
                )

    return unlocked
    def achievement_multiplier(
    session
):

    multiplier = 1.0

    for achievement_id in (
        session.achievements
    ):

        multiplier *= (
            ACHIEVEMENTS[
                achievement_id
            ]["reward"]
        )

    return multiplier
