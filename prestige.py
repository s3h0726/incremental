# prestige.py

import math

# =========================
# 1차 프레스티지
# 에너지 -> 부품
# =========================

def calculate_parts(energy):

    if energy < 1_000_000:
        return 0

    return int(
        math.sqrt(
            energy / 1_000_000
        )
    )


# =========================
# 2차 프레스티지
# 부품 -> 드론
# =========================

def calculate_drones(parts):

    if parts < 1000:
        return 0

    return int(
        math.sqrt(
            parts / 1000
        )
    )


# =========================
# 3차 프레스티지
# 드론 -> 양자코어
# =========================

def calculate_quantum_cores(drones):

    if drones < 500:
        return 0

    return int(
        math.sqrt(
            drones / 500
        )
    )


# =========================
# 4차 프레스티지
# 양자코어 -> 초월점수
# =========================

def calculate_transcendence(
    quantum_cores
):

    if quantum_cores < 100:
        return 0

    return int(
        math.sqrt(
            quantum_cores / 100
        )
    )


# =========================
# 5차 프레스티지
# 초월점수 -> 현실붕괴
# =========================

def calculate_reality_breaks(
    transcendence
):

    if transcendence < 10:
        return 0

    return int(
        math.sqrt(
            transcendence / 10
        )
    )


# =========================
# 생산 배율
# =========================

def production_multiplier(
    parts,
    drones,
    quantum_cores,
    transcendence,
    reality_breaks
):

    multiplier = 1.0

    multiplier *= (
        1 + parts * 0.05
    )

    multiplier *= (
        1 + drones * 0.15
    )

    multiplier *= (
        1 + quantum_cores * 0.50
    )

    multiplier *= (
        1 + transcendence * 2.0
    )

    multiplier *= (
        1 + reality_breaks * 10.0
    )

    return multiplier


# =========================
# 현재 main.py 호환용
# =========================

def calculate_prestige_gain(
    energy
):

    return calculate_parts(
        energy
    )


# =========================
# 프레스티지 실행 함수
# =========================

def do_parts_prestige(
    session
):

    gain = calculate_parts(
        session.energy
    )

    if gain <= 0:
        return False

    session.parts += gain

    session.energy = 0
    session.energy_per_second = 0
    session.owned_buildings = {}

    return True


def do_drones_prestige(
    session
):

    gain = calculate_drones(
        session.parts
    )

    if gain <= 0:
        return False

    session.drones += gain

    session.parts = 0

    return True


def do_quantum_prestige(
    session
):

    gain = calculate_quantum_cores(
        session.drones
    )

    if gain <= 0:
        return False

    session.quantum_cores += gain

    session.drones = 0

    return True


def do_transcendence_prestige(
    session
):

    gain = calculate_transcendence(
        session.quantum_cores
    )

    if gain <= 0:
        return False

    session.transcendence += gain

    session.quantum_cores = 0

    return True


def do_reality_break(
    session
):

    gain = calculate_reality_breaks(
        session.transcendence
    )

    if gain <= 0:
        return False

    if "reality_breaks" not in session:
        session.reality_breaks = 0

    session.reality_breaks += gain

    session.transcendence = 0

    return True
