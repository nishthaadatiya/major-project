# src/phase2_test.py

from translate_en_de import english_to_german
from german_to_gloss import german_to_gloss
from gloss_to_asl_english import gloss_to_asl_english
import pandas as pd

# =================================================
# TEST 1: English → German → Gloss → ASL-English
# =================================================

english_input = "Tomorrow the weather will be cold"

german_text = english_to_german(english_input)
semantic_gloss = german_to_gloss(german_text)
asl_english_gloss = gloss_to_asl_english(semantic_gloss)

print("English Input :", english_input)
print("German (hidden):", german_text)
print("Semantic Gloss :", semantic_gloss)
print("ASL-English    :", asl_english_gloss)
print("-" * 50)

# =================================================
# TEST 2: Direct German → Gloss → ASL-English
# =================================================

examples = [
    "und nun die wettervorhersage für morgen",
    "im norden bleibt es heute nacht trocken",
    "morgen ähnliche temperaturen wie heute"
]

for s in examples:
    gloss = german_to_gloss(s)
    asl_gloss = gloss_to_asl_english(gloss)

    print("German        :", s)
    print("Semantic Gloss:", gloss)
    print("ASL-English   :", asl_gloss)
    print("-" * 40)

# =================================================
# TEST 3: Dataset connection
# =================================================

df = pd.read_csv("data/processed/train_clean.csv")
print("COLUMNS:", df.columns)

print("\nDATASET SAMPLE TEST\n")

for i in range(3):
    sentence = df.iloc[i]["input_text"]

    gloss = german_to_gloss(sentence)
    asl_gloss = gloss_to_asl_english(gloss)

    print("German        :", sentence)
    print("Semantic Gloss:", gloss)
    print("ASL-English   :", asl_gloss)
    print("-" * 40)
