word = "pneumonoultramicroscopicsilicovolcanoconiosis"
vowels = " a,e,i,o,u"
consonants = 0
vowel_count = 0
for ch in word:
    if ch in vowels:
        vowel_count = vowel_count + 1
    else:
        consonants = consonants + 1
print("vowelcount = ",vowel_count)
print("consonants = ",consonants)
