word1 = "silents"
word2 = "listen"
for char in word1:
    if char not  in word2 or word1.count(char)!= word2.count(char):
        print("not anagram")
        break
else:
    print("anagram")