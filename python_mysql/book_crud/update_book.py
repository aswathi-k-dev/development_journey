from mysql import connector

connection = connector.connect(
    user = "root",
    password = "Password@123",
    host = "localhost",
    database = "book_db"
)

cursor = connection.cursor()

query = """ 
    update book set title = %s,price = %s where id = %s
"""

values = ("balyakalasakhi",399.00,3)

cursor.execute(query,values)
connection.commit()

print("record updated")