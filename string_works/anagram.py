word1 = "fried"
word2 = "fired"
for char in word1:
    if char not in word2:
        print("not an anagram")
        break
else:
    print("anagram")