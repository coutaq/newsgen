from flask import Flask, jsonify, request
from log.ConsoleLogger import ConsoleLogger
from log.LogManager import LogManager
from database.models.User import User
from database.MySQLConnection import MySQLConnection
from api.utils import model_to_route, model_to_route_id

lg = LogManager()
lg.attach(ConsoleLogger())
conn = MySQLConnection()
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/user', methods=['POST', 'GET'])
def user():
    return model_to_route(User, conn)()


@app.route('/user/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def user_id(id):
    return model_to_route_id(User, conn)(id)
