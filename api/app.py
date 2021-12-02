from flask import Flask, jsonify, request
from log.ConsoleLogger import ConsoleLogger
from log.LogManager import LogManager
from database.models.User import User
from database.MySQLConnection import MySQLConnection

lg = LogManager()
lg.attach(ConsoleLogger())
conn = MySQLConnection()
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/user', methods=['POST', 'GET'])
def user():
    if request.method == 'GET':
        query = User.read()
        data = conn.execute_query(query, True)
    if request.method == 'POST':
        fields = User.fields() + User.foreign_fields()
        fields.remove("id")
        values = [request.form.get(x) for x in fields]
        query = User.create(values)
        data = conn.execute_query(query, True)
    return jsonify(data)


@app.route('/user/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def user_id(id):
    if request.method == 'GET':
        query = User.read(where=id)
        data = conn.execute_query(query, True)
    if request.method == 'PUT':
        fields = User.fields() + User.foreign_fields()
        fields.remove("id")
        values = [request.form.get(x) for x in fields]
        query = User.update(id, values)
        data = conn.execute_query(query, True)
    if request.method == 'DELETE':
        query = User.delete(id)
        data = conn.execute_query(query, True)
    return jsonify(data)
