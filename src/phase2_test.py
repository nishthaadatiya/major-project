# src/phase2_test.py

from translate_en_de import english_to_german
from german_to_gloss import german_to_gloss
import pandas as pd

# -------- TEST 1: English → German → Gloss --------

english_input = "Tomorrow the weather will be cold"

german_text = english_to_german(english_input)
gloss = german_to_gloss(german_text)

print("English:", english_input)
print("German :", german_text)
print("Gloss  :", gloss)
print("-" * 50)

# -------- TEST 2: German examples --------

examples = [
    "und nun die wettervorhersage für morgen",
    "im norden bleibt es heute nacht trocken",
    "morgen ähnliche temperaturen wie heute"
]

for s in examples:
    print("German:", s)
    print("Gloss :", german_to_gloss(s))
    print("-" * 40)

# -------- TEST 3: Dataset connection --------

df = pd.read_csv("data/processed/train_clean.csv")
print("COLUMNS:", df.columns)

print("\nDATASET SAMPLE TEST\n")
for i in range(3):
    sentence = df.iloc[i]["input_text"]
    print("German:", sentence)
    print("Gloss :", german_to_gloss(sentence))
    print("-" * 40)
