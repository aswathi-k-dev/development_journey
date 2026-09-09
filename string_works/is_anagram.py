def is_anagram(word1,word2):
    for char in word1:
        if char not in word2 or word1.count(char)!= word2.count(char):
            print(False)
            break
    else:
        print(True)
is_anagram("fried","fired")
is_anagram("silents","listen")
is_anagram("act","cat")

