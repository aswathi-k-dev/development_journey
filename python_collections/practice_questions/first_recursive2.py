text = "ABCBCA"
char_count = {}
for ch in text:
    if ch in char_count:
        print(ch)
        break
    else:
        char_count[ch] =1