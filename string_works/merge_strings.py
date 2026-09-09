# merge strings
"""
word1 ="PQR"
WORD2 = "ABC"
MERGED_STRING = "PAQBRC"

"""

word1 = "PQRST"
word2 = "ABCDE"

merged_str = " "
for i in range(0,len(word1)):
    merged_str += word1[i] + word2[i]
print(merged_str)

