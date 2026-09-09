try:
    fr = open("error_handling\\ey_words.txt","r")
    for line in fr:
        print(line)
except Exception as e:
    print(e)
finally:
    print("db commit")