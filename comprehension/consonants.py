text = "a man a canal a panama "
consonants = {ch for ch in text if ch not in "aeiou" and ch.isalpha()}
print(consonants)