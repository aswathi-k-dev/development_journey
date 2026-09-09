words = ["silent","listen","race","care","trap","night","tight"]

fw = open("file_operation\\anagrams.txt","w")
for wi in words:
    for wj in words:
        if sorted(wi)==sorted(wj) and wi != wj:
            fw.write(wi + "\n")


 