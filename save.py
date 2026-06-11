# save.py

import json
import os
import time

SAVE_FILE = "save.json"

# 자동 저장 시간 기록
LAST_AUTO_SAVE = 0


def save_game(session):
    """
    게임 저장
    """

    data = {
        "energy": session.get("energy", 0),
        "parts": session.get("parts", 0),
        "drones": session.get("drones", 0),
        "quantum_cores": session.get("quantum_cores", 0),
        "transcendence": session.get("transcendence", 0),
        "reality_breaks": session.get("reality_breaks", 0),

        "click_power": session.get("click_power", 1),
        "energy_per_second": session.get("energy_per_second", 0),

        "owned_buildings": session.get(
            "owned_buildings",
            {}
        ),

        "achievements": session.get(
            "achievements",
            []
        ),

        "research": session.get(
            "research",
            []
        ),

        "last_save_time": time.time()
    }

    try:

        with open(
            SAVE_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

        return True

    except Exception as e:

        print(
            f"저장 실패: {e}"
        )

        return False


def load_game(session):
    """
    저장 불러오기
    """

    if not os.path.exists(
        SAVE_FILE
    ):
        return False

    try:

        with open(
            SAVE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(
                file
            )

        session.energy = data.get(
            "energy",
            0
        )

        session.parts = data.get(
            "parts",
            0
        )

        session.drones = data.get(
            "drones",
            0
        )

        session.quantum_cores = data.get(
            "quantum_cores",
            0
        )

        session.transcendence = data.get(
            "transcendence",
            0
        )

        session.reality_breaks = data.get(
            "reality_breaks",
            0
        )

        session.click_power = data.get(
            "click_power",
            1
        )

        session.energy_per_second = data.get(
            "energy_per_second",
            0
        )

        session.owned_buildings = data.get(
            "owned_buildings",
            {}
        )

        session.achievements = data.get(
            "achievements",
            []
        )

        session.research = data.get(
            "research",
            []
        )

        return True

    except Exception as e:

        print(
            f"불러오기 실패: {e}"
        )

        return False


def delete_save():
    """
    저장 삭제
    """

    try:

        if os.path.exists(
            SAVE_FILE
        ):

            os.remove(
                SAVE_FILE
            )

        return True

    except Exception as e:

        print(
            f"삭제 실패: {e}"
        )

        return False


def save_exists():
    """
    저장 존재 여부
    """

    return os.path.exists(
        SAVE_FILE
    )


def auto_save(
    session,
    interval=30
):
    """
    interval 초마다 자동 저장
    """

    global LAST_AUTO_SAVE

    current_time = time.time()

    if (
        current_time
        - LAST_AUTO_SAVE
        >= interval
    ):

        save_game(
            session
        )

        LAST_AUTO_SAVE = (
            current_time
        )


def export_save():
    """
    저장 데이터 반환
    (백업 기능용)
    """

    if not os.path.exists(
        SAVE_FILE
    ):
        return None

    with open(
        SAVE_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(
            file
        )


def import_save(
    data
):
    """
    저장 데이터 가져오기
    """

    try:

        with open(
            SAVE_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

        return True

    except Exception as e:

        print(
            f"가져오기 실패: {e}"
        )

        return False
