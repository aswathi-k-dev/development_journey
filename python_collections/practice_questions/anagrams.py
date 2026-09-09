words = ["silent","listen","act","cat","note","tone","hen","chicken"]
anagrams = set()
for i in range (0,len(words)):
    for j in range(0,len(words)):
        word1 = words[i]
        word2 = words[j]
        if sorted(word1)==sorted(word2) and word1 != word2:
            anagrams.add(word1)
            anagrams.add(word2)
print(anagrams)