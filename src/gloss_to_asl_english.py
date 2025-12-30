# src/gloss_to_asl_english.py

GLOSS_MAP = {
    # Time
    "MORGEN": "TOMORROW",
    "GESTERN": "YESTERDAY",
    "HEUTE": "TODAY",
    "NACHT": "NIGHT",
    "TAG": "DAY",

    # Weather
    "WETTER": "WEATHER",
    "WETTERVORHERSAGE": "WEATHER FORECAST",
    "REGEN": "RAIN",
    "SCHNEE": "SNOW",
    "KALT": "COLD",
    "WARM": "WARM",
    "HEISS": "HOT",
    "TROCKEN": "DRY",

    # Locations
    "NORD": "NORTH",
    "NORDEN": "NORTH",
    "NORDWESTEN": "NORTH WEST",

    # Common concepts
    "BLEIBT": "STAY",
    "REGNET": "RAIN",
    "BLITZ": "LIGHTNING",
    "DONNER": "THUNDER",
}

def gloss_to_asl_english(gloss: str) -> str:
    tokens = gloss.split()
    mapped = [GLOSS_MAP.get(tok, tok) for tok in tokens]
    return " ".join(mapped)
