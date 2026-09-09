from mysql import connector

connection = connector.connect(
    user = "root",
    password = "Password@123",
    host = "localhost",
    database = "song_db"
)

cursor = connection.cursor()
query = """
    insert into song(title,track_number,movie,singers) values(%s,%s,%s,%s)
"""

values = ("tum hi ho","02","aashiqui 2","arjith singh")
cursor.execute(query,values)
connection.commit()
connection.close()
print("record added")



