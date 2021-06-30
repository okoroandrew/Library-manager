from flask import Flask
from flask_restful import Api
from resources import Book, Books


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)

api.add_resource(Book, '/book/<string:name>')
api.add_resource(Books, '/books')


if __name__ == "__main__":
    app.run(port=5000, debug=True)

