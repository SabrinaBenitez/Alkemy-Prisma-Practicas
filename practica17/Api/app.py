from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api=Api(app)

class saludar(Resource):
    def get(self):
        return {'saludo':'Buenos Dias'}

api.add_resource(saludar,'/')

if __name__ == '__main__':
    app.run (host='localhost', port=5000, debug=True)
