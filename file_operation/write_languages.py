languages = ["python","java","c++","css","nlp"]

fw = open("file_operation\\languages.txt","w")
for l in languages:
    fw.write(l+"\n")


print("write completed")


