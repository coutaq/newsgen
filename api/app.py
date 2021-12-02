from flask import Flask

from api.utils import model_to_route, model_to_route_id
from database.MySQLConnection import MySQLConnection
from database.models.Category import Category
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


exposed_models = {"user": User, "category": Category}
for name, model in exposed_models.items():
    def f1():
        return model_to_route(model, conn)()()
    f1.__name__ = name

    def f2(id):
        return model_to_route_id(model, conn)()(id)
    f2.__name__ = name + "_id"
    app.add_url_rule(f'/{name}', view_func=f1, methods=['POST', 'GET'])
    app.add_url_rule(f'/{name}/<int:id>', view_func=f2, methods=['GET', 'DELETE', 'PUT'])
