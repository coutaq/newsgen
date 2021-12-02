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


@app.route("/db/<model>", methods=["GET", "POST"])
def api_routes(model):
    return model_to_route(exposed_models[model], conn)()


@app.route("/db/<model>/<id>", methods=["GET", "PUT", "DELETE"])
def api_routes_id(model, id):
    return model_to_route_id(exposed_models[model], conn)(id)
