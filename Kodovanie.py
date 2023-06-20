def zakodovat(text, x):
    zakodovany_text = ""
    for char in text:
        zakodovany_char = chr(ord(char) + x)
        zakodovany_text += zakodovany_char
    return zakodovany_text

def dekodovat(zakodovany_text, x):
    dekodovany_text = ""
    for char in zakodovany_text:
        dekodovany_char = chr(ord(char) - x)
        dekodovany_text += dekodovany_char
    return dekodovany_text


original_text = "Ahoj svet!"
x = 3
zakodovany_text = zakodovat(original_text, x)
print("Zakodovany text:", zakodovany_text)
dekodovany_text = dekodovat(zakodovany_text, x)
print("Dekodovany text:", dekodovany_text)