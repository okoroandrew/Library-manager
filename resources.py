import sqlite3
from flask_restful import Resource, reqparse


class Book(Resource):
    """Resource for post, get, put, and deletion of book by its unique name."""
    TABLE_NAME = "books"

    parser = reqparse.RequestParser()
    parser.add_argument('quantity',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, name):
        book1 = self.find_by_name(name)
        if book1:
            return book1, 200
        return {"message": f"no record of {name} found"}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect("library.db")
        cursor = connection.cursor()
        sqlite_query = "SELECT * FROM {table} WHERE book_name = ?;".format(table=cls.TABLE_NAME)

        cursor.execute(sqlite_query, (name,))
        record = cursor.fetchone()
        connection.close()

        if record:
            return {"book": {"id": record[0], "book name": record[1], "quantity": record[2]}}

    def post(self, name):
        if self.find_by_name(name):
            return {"message": f"book {name} already exist"}

        data = Book.parser.parse_args()

        book= {"name": name, "quantity": data["quantity"]}

        try:
            Book.insert_into_table(book)
        except:
            return {"message": "An error occurred"}, 400

        return book, 200

    @classmethod
    def insert_into_table(cls, book):
        connection = sqlite3.connect("library.db")
        cursor = connection.cursor()
        sqlite_query = "INSERT INTO {table} VALUES (?, ?, ?);".format(table=cls.TABLE_NAME)

        cursor.execute(sqlite_query, (None, book["name"], book["quantity"]))
        connection.commit()
        connection.close()

    def put(self, name):
        data = Book.parser.parse_args()
        book = {"name": name, "quantity": data["quantity"]}

        if self.find_by_name(name):
            try:
                Book.update_table(book)
            except:
                return {"message": "An error occurred"}, 400

        else:
            try:
                Book.insert_into_table(book)
            except:
                return {"message": "An error occurred"}, 400

        return book, 200

    @classmethod
    def update_table(cls, book):
        connection = sqlite3.connect("library.db")
        cursor = connection.cursor()
        sqlite_query = "UPDATE {table} SET quantity =? WHERE book_name = ?;".format(table=cls.TABLE_NAME)
        cursor.execute(sqlite_query, (book["quantity"], book["name"]))
        connection.commit()
        connection.close()

    @classmethod
    def delete(cls, name):
        connection = sqlite3.connect("library.db")
        cursor = connection.cursor()
        sqlite_query = "DELETE FROM {table} WHERE book_name =?".format(table=cls.TABLE_NAME)

        delete = cursor.execute(sqlite_query, (name,))
        connection.commit()
        connection.close()

        if delete:
            return {"message": f"{name} deleted successfully"}, 200
        return{"message": "An error occurred"}, 400


class Books(Resource):
    """get the entire book in the library"""
    TABLE_NAME = "books"

    def get(self):
        connection = sqlite3.connect("library.db")
        cursor = connection.cursor()
        sqlite_query = "SELECT * FROM {table}".format(table=Books.TABLE_NAME)

        cursor.execute(sqlite_query)
        records= cursor.fetchall()
        books= []
        for record in records:
            books.append({"id": record[0], "book_name": record[1], "quantity": record[2]})
        connection.close()
        return {"books": books}




