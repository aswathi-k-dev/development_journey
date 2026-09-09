words = ["jhon",'alice',"bob","emma"]
result = [w[0].upper() + w[1:] for w in words]
print(result)