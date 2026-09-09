temperature =[18,22,35,28,15]
result = ["cold" if t < 20 else "warm" if t <=30 else "hot"for t in temperature ]
print(result)