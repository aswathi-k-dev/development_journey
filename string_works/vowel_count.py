word = "supErcalifragilistiexpialidocious"
vowels = " a,e,i,o,u"
vowel_count = 0
for ch in word:
    if ch.lower() in vowels:
        vowel_count = vowel_count + 1
        
print("vowelcount = ",vowel_count)
