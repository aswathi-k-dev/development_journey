word1 = "silents"
word2 = "listen"
for char in word1:
    if char  in word2:
        print("not an anagram")
        break
else:
    print('anagram')