import sqlite3

# connection = sqlite3.connect("library.db")
# cursor = connection.cursor()
# sqlite_query = "INSERT INTO books VALUES (?, ?, ?);"
#
# tuples = [(None, "good", 2), (None, "bad", 3), (None, "worse", 10)]
#
# cursor.executemany(sqlite_query, tuples)
# connection.commit()
# connection.close()


connection = sqlite3.connect("library.db")
cursor = connection.cursor()
sqlite_query = "SELECT * FROM books;"

cursor.execute(sqlite_query)
record = cursor.fetchall()
print(*record)

if record:
    print({"book": {"id": record[0], "book name": record[1]}})
connection.close()

# connection = sqlite3.connect("library.db")
# cursor = connection.cursor()
# sqlite_query = "UPDATE books SET quantity =? WHERE book_name = ?;"
# cursor.executemany(sqlite_query, [(10, "Andrew"), (22, "grammy")])
# connection.commit()
# connection.close()
