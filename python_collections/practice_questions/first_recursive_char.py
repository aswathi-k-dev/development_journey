# USING LIST

text = "ABCABAC"
unique_words = []
for ch in text:
    if ch in unique_words:
        print(ch)
        break
    else:
        unique_words.append(ch)



