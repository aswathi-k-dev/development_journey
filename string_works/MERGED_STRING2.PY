word1 = "PQRST"
word2 = "ABC"

small_string = " "
large_string = " "
merged_string = " "

if len(word1)<len(word2):
    small_string = word1
    large_string = word2
else:
    small_string = word2
    large_string = word1

for i in range(0,len(small_string)):
    merged_string += word1[i]+word2[i]
balance = large_string[len(small_string):]
merged_string += balance
print(merged_string)


