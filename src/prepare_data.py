import pandas as pd
import re
import os

RAW_PATH = "data/raw/PHOENIX-2014-T.train.corpus.csv"
OUT_PATH = "data/processed/train_clean.csv"

def clean_english(text):
    text = str(text).lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip()

def clean_gloss(text):
    text = str(text).upper()
    text = re.sub(r"[^\w\s\-]", "", text)
    return text.strip()

def main():
    df = pd.read_csv(RAW_PATH, sep="|")

    df["input_text"] = df["translation"].apply(clean_english)
    df["target_gloss"] = df["orth"].apply(clean_gloss)

    final_df = df[["input_text", "target_gloss"]]

    os.makedirs("data/processed", exist_ok=True)
    final_df.to_csv(OUT_PATH, index=False)

    print("✅ Cleaned data saved to:", OUT_PATH)
    print(final_df.head())

if __name__ == "__main__":
    main()

