employee = {"id":121,"name":"aswathi","dept":"hr"}

key = input("enter key: ")

try:
    print(employee[key])

except Exception as e:
    print(e)
finally:
    print("db commit....")
