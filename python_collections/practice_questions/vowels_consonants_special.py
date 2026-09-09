text = "hello$world#"
vowels = []
consonants = []
specials = []

for char in text:
    if char.lower() in "aeiou":
        vowels.append(char)
    elif char.isalpha():
        consonants.append(char)
    else:
        specials.append(char)
print("vowels =",vowels)
print("consonants =",consonants)
print("special charactrs =",specials)
        