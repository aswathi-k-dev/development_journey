names = ["john","","alice","","david",]
result = ["unknown" if n == "" else n for n in names]
print(result)