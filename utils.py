# utils.py

SUFFIXES = [
    "",
    "K",
    "M",
    "B",
    "T",
    "Qa",
    "Qi",
    "Sx",
    "Sp",
    "Oc",
    "No",
    "Dc",
    "UDc",
    "DDc",
    "TDc",
    "QaDc",
    "QiDc",
    "SxDc",
    "SpDc",
    "OcDc",
    "NoDc"
]


def format_number(number):

    try:
        number = float(number)

    except:
        return "0"

    if number < 1000:
        return f"{number:,.0f}"

    index = 0

    while number >= 1000 and index < len(SUFFIXES) - 1:

        number /= 1000

        index += 1

    return f"{number:.2f}{SUFFIXES[index]}"


def format_production(value):

    return f"{format_number(value)}/s"


def format_percent(value):

    return f"{value:.1f}%"


def scientific(number):

    try:

        return "{:.3e}".format(number)

    except:

        return "0"


def clamp(value, minimum, maximum):

    return max(
        minimum,
        min(value, maximum)
    )


def calculate_multiplier(level):

    return 1.10 ** level


def building_cost(base_cost, owned):

    return base_cost * (
        1.15 ** owned
    )


def research_cost(base_cost, level):

    return base_cost * (
        2 ** level
    )
