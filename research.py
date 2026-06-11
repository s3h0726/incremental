# research.py

RESEARCH_TREE = {

    # =====================
    # 기초 기술
    # =====================

    "efficiency_1": {
        "name": "발전 효율 I",
        "cost": 10,
        "effect": 1.25,
        "category": "기초 기술",
        "requires": []
    },

    "efficiency_2": {
        "name": "발전 효율 II",
        "cost": 50,
        "effect": 1.50,
        "category": "기초 기술",
        "requires": ["efficiency_1"]
    },

    "efficiency_3": {
        "name": "발전 효율 III",
        "cost": 200,
        "effect": 2.00,
        "category": "기초 기술",
        "requires": ["efficiency_2"]
    },

    "production_1": {
        "name": "생산 최적화 I",
        "cost": 25,
        "effect": 1.20,
        "category": "기초 기술",
        "requires": []
    },

    "production_2": {
        "name": "생산 최적화 II",
        "cost": 100,
        "effect": 1.40,
        "category": "기초 기술",
        "requires": ["production_1"]
    },

    "automation_1": {
        "name": "자동화 I",
        "cost": 75,
        "effect": 1,
        "category": "기초 기술",
        "requires": []
    },

    "automation_2": {
        "name": "자동화 II",
        "cost": 250,
        "effect": 1,
        "category": "기초 기술",
        "requires": ["automation_1"]
    },

    # =====================
    # 산업 기술
    # =====================

    "factory_1": {
        "name": "고효율 공장",
        "cost": 500,
        "effect": 1.5,
        "category": "산업 기술",
        "requires": ["production_2"]
    },

    "factory_2": {
        "name": "대형 공장",
        "cost": 1500,
        "effect": 2.0,
        "category": "산업 기술",
        "requires": ["factory_1"]
    },

    "logistics_1": {
        "name": "컨베이어 벨트",
        "cost": 300,
        "effect": 0.98,
        "category": "산업 기술",
        "requires": []
    },

    "logistics_2": {
        "name": "자동 운송",
        "cost": 1200,
        "effect": 0.96,
        "category": "산업 기술",
        "requires": ["logistics_1"]
    },

    "ai_1": {
        "name": "기초 AI",
        "cost": 1000,
        "effect": 1.5,
        "category": "산업 기술",
        "requires": []
    },

    "ai_2": {
        "name": "학습 AI",
        "cost": 5000,
        "effect": 2.0,
        "category": "산업 기술",
        "requires": ["ai_1"]
    },

    # =====================
    # 미래 기술
    # =====================

    "quantum_1": {
        "name": "양자 회로",
        "cost": 10000,
        "effect": 2,
        "category": "미래 기술",
        "requires": ["ai_2"]
    },

    "quantum_2": {
        "name": "양자 연산",
        "cost": 25000,
        "effect": 3,
        "category": "미래 기술",
        "requires": ["quantum_1"]
    },

    "nano_1": {
        "name": "나노 조립",
        "cost": 12000,
        "effect": 0.95,
        "category": "미래 기술",
        "requires": []
    },

    "nano_2": {
        "name": "나노 생산",
        "cost": 35000,
        "effect": 0.90,
        "category": "미래 기술",
        "requires": ["nano_1"]
    },

    "dimension_1": {
        "name": "차원 탐사",
        "cost": 50000,
        "effect": 2,
        "category": "미래 기술",
        "requires": []
    },

    # =====================
    # 초월 기술
    # =====================

    "singularity_1": {
        "name": "특이점 이론",
        "cost": 100000,
        "effect": 2,
        "category": "초월 기술",
        "requires": ["quantum_2"]
    },

    "singularity_2": {
        "name": "특이점 구현",
        "cost": 250000,
        "effect": 3,
        "category": "초월 기술",
        "requires": ["singularity_1"]
    },

    "reality_1": {
        "name": "현실 균열",
        "cost": 500000,
        "effect": 5,
        "category": "초월 기술",
        "requires": []
    },

    "reality_2": {
        "name": "현실 붕괴",
        "cost": 1000000,
        "effect": 10,
        "category": "초월 기술",
        "requires": ["reality_1"]
    },

    "universe_1": {
        "name": "행성 개발",
        "cost": 2500000,
        "effect": 10,
        "category": "초월 기술",
        "requires": []
    },

    "universe_2": {
        "name": "항성 개발",
        "cost": 10000000,
        "effect": 50,
        "category": "초월 기술",
        "requires": ["universe_1"]
    }
}
def can_unlock(research_id, owned_research):

    research = RESEARCH_TREE[research_id]

    for requirement in research["requires"]:

        if requirement not in owned_research:
            return False

    return True


def buy_research(
    research_id,
    session
):

    research = RESEARCH_TREE[research_id]

    if research_id in session.research:
        return False

    if session.parts < research["cost"]:
        return False

    if not can_unlock(
        research_id,
        session.research
    ):
        return False

    session.parts -= research["cost"]

    session.research.append(
        research_id
    )

    return True
