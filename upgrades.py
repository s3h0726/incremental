# upgrades.py

BUILDINGS = {

    "copper_generator": {
        "name": "🔋 구리 발전기",
        "base_cost": 10,
        "production": 1
    },

    "iron_generator": {
        "name": "⚙ 철 발전기",
        "base_cost": 100,
        "production": 10
    },

    "reactor": {
        "name": "☢ 원자로",
        "base_cost": 1000,
        "production": 100
    },

    "factory": {
        "name": "🏭 자동 공장",
        "base_cost": 10000,
        "production": 500
    },

    "ai_factory": {
        "name": "🤖 AI 공장",
        "base_cost": 100000,
        "production": 2500
    },

    "quantum_miner": {
        "name": "🌌 양자 채굴기",
        "base_cost": 1000000,
        "production": 10000
    },

    "nano_complex": {
        "name": "🔬 나노 콤플렉스",
        "base_cost": 10000000,
        "production": 50000
    },

    "dimension_extractor": {
        "name": "🌀 차원 추출기",
        "base_cost": 100000000,
        "production": 250000
    },

    "reality_breaker": {
        "name": "💥 현실 분해기",
        "base_cost": 1000000000,
        "production": 1000000
    },

    "stellar_harvester": {
        "name": "⭐ 항성 수확기",
        "base_cost": 10000000000,
        "production": 5000000
    },

    "galaxy_core": {
        "name": "🌠 은하 코어",
        "base_cost": 100000000000,
        "production": 25000000
    },

    "universe_engine": {
        "name": "🌌 우주 엔진",
        "base_cost": 1000000000000,
        "production": 100000000
    }

}


def get_building_cost(base_cost, owned):

    return base_cost * (1.15 ** owned)


def get_total_production(owned_buildings):

    total = 0

    for building_id, amount in owned_buildings.items():

        if building_id in BUILDINGS:

            production = BUILDINGS[building_id]["production"]

            total += production * amount

    return total
