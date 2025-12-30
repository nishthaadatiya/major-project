import re

# German function words that are usually dropped in sign language gloss
STOPWORDS = {
    "und", "oder", "aber",
    "der", "die", "das", "den", "dem", "des",
    "ein", "eine", "einen", "einem", "einer",
    "ist", "sind", "war", "waren",
    "wird", "werden", "bleibt",
    "es", "im", "am", "an", "auf", "zu", "für", "von",
    "mit", "noch", "auch", "nur", "nun", "dann", "wie"
}

# Optional normalization (keeps gloss consistent)
NORMALIZATION = {
    "heute": "HEUTE",
    "morgen": "MORGEN",
    "nacht": "NACHT",
    "wetter": "WETTER",
    "wettervorhersage": "WETTERVORHERSAGE",
    "temperaturen": "TEMPERATUREN",
    "norden": "NORD",
    "süden": "SUED",
    "osten": "OST",
    "westen": "WEST",
}

def apply_gloss_rules(sentence: str) -> str:
    """
    Apply rule-based German → Gloss conversion.
    """

    if not isinstance(sentence, str):
        return ""

    # lowercase
    sentence = sentence.lower()

    # remove punctuation (keep umlauts)
    sentence = re.sub(r"[^\w\säöüß]", "", sentence)

    words = sentence.split()
    gloss_words = []

    for word in words:
        if word in STOPWORDS:
            continue

        if word in NORMALIZATION:
            gloss_words.append(NORMALIZATION[word])
        else:
            gloss_words.append(word.upper())

    return " ".join(gloss_words)
