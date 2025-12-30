from translate_en_de import english_to_german

tests = [
    "Tomorrow the weather will be cold",
    "It will rain in the north",
    "Tonight it will stay dry"
]

for t in tests:
    print("English:", t)
    print("German :", english_to_german(t))
    print("-" * 40)
