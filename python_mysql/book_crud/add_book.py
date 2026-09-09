from mysql import connector

connection = connector.connect(
    user = "root",
    password = "Password@123",
    host = "localhost",
    database = "book_db"
)

cursor = connection.cursor()
query = """
    insert into book(title,author,genre,price) values(%s,%s,%s,%s)
"""

values = ("mathilukal","basheer","romance",199.00)
cursor.execute(query,values)
connection.commit()
connection.close()
print("record added")
