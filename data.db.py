import sqlite3


try:
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_Query = """CREATE TABLE IF NOT EXISTS books
                        (id integer primary key,
                        book_name text not null,
                        quantity int not null);"""
    cursor.execute(sqlite_Query)
    connection.commit()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

finally:
    if connection:
        connection.close()
        print("The SQLite connection is closed")


