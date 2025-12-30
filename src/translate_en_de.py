# src/translate_en_de.py

from transformers import pipeline

translator = pipeline(
    "translation_en_to_de",
    model="Helsinki-NLP/opus-mt-en-de"
)

def english_to_german(text: str) -> str:
    result = translator(text, max_length=128)
    return result[0]["translation_text"]
