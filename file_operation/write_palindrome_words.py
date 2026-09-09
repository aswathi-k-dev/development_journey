words = ["madam","aba","tan","sin","malayalam"]
fw = open("file_operation\\palindromes.txt","w")
for w in words:
    reversed_word = w[::-1]
    if reversed_word == w:
        fw.write(w+"\n")

print("cmpltd")
