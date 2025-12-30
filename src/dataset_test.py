import pandas as pd
from translate_en_de import english_to_german
from german_to_gloss import german_to_gloss

df = pd.read_csv("data/processed/train_clean.csv")

print("COLUMNS:", df.columns)
print("\nPIPELINE TEST (EN → DE → GLOSS)\n")

for i in range(3):
    english = df.iloc[i]["input_text"]

    german = english_to_german(english)
    gloss = german_to_gloss(german)

    print("English:", english)
    print("German :", german)
    print("Gloss  :", gloss)
    print("-" * 40)
