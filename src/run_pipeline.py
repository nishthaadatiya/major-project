from translate_en_de import english_to_german
from german_to_gloss import german_to_gloss
from gloss_to_asl_english import gloss_to_asl_english

print("Type an English sentence (or 'exit' to quit):")

while True:
    english_input = input(">> ")

    if english_input.lower() == "exit":
        break

    german = english_to_german(english_input)
    semantic_gloss = german_to_gloss(german)
    asl_gloss = gloss_to_asl_english(semantic_gloss)

    print("German (hidden):", german)
    print("Semantic Gloss :", semantic_gloss)
    print("ASL-English    :", asl_gloss)
    print("-" * 50)
