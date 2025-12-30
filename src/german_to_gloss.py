import re

# Words to drop (German function words not needed in gloss)
STOPWORDS = {
    "und", "oder", "aber", "die", "der", "das", "ein", "eine",
    "im", "in", "am", "an", "auf", "zu", "für", "von",
    "es", "ist", "sind", "wird", "werden", "bleibt",
    "auch", "noch", "nur", "wie", "mit", "sich",
    "nun", "dann"
}

# Simple word normalization (optional, grows over time)
NORMALIZATION = {
    "heute": "HEUTE",
    "morgen": "MORGEN",
    "nacht": "NACHT",
    "temperaturen": "TEMPERATUREN",
    "wettervorhersage": "WETTERVORHERSAGE",
    "norden": "NORD",
    "süden": "SUED",
    "osten": "OST",
    "westen": "WEST",
}

def german_to_gloss(sentence: str) -> str:
    """
    Convert a German sentence into a simplified gloss format.
    """

    if not isinstance(sentence, str):
        return ""

    # lowercase
    sentence = sentence.lower()

    # remove punctuation
    sentence = re.sub(r"[^\w\s]", "", sentence)

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
