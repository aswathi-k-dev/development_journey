text = "the quick brown fox jumps over lazy dog"
alphabets = "abcdefghijklmnopqrstuvwxyz"
for char in alphabets:
    if char not in text:
        print("not a pangram")
        break
else:
    print("pangram")