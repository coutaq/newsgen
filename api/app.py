from flask import Flask

from api.utils import model_to_route, model_to_route_id
from database.MySQLConnection import MySQLConnection
from database.models.User import User
from log.ConsoleLogger import ConsoleLogger
from log.LogManager import LogManager

lg = LogManager()
lg.attach(ConsoleLogger())
conn = MySQLConnection()
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


exposed_models = {"user": User}
for name, model in exposed_models:
    @app.route(f'/{name}', methods=['POST', 'GET'])
    def user():
        return model_to_route(model, conn)()


    @app.route(f'/{name}/<int:id>', methods=['GET', 'DELETE', 'PUT'])
    def user_id(id):
        return model_to_route_id(model, conn)(id)
