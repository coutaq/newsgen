from flask import Flask, request, jsonify
from werkzeug.utils import  secure_filename
from api.utils import model_to_route, model_to_route_id, authenticate
from database.MySQLConnection import MySQLConnection
from database.models.Category import Category
from database.models.AuthUser import AuthUser
from log.ConsoleLogger import ConsoleLogger
from log.LogManager import LogManager
from flask_cors import CORS
import os
lg = LogManager()
lg.attach(ConsoleLogger())
conn = MySQLConnection()
app = Flask(__name__)

CORS(app)




@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/upload-file", methods=["POST"])
def upload_file():
    file = request.files.get('file')
    filename = secure_filename(file.filename)
    file_location = os.path.join(app.config['BASEDIR'], app.config['UPLOAD_FOLDER'], filename)
    with open(file_location, 'wb+') as localfile:
        file.save(localfile)
    return jsonify(file_location)


@app.route("/auth", methods=["POST"])
def auth():
    # lg.notify(request)
    login = request.json["login"]
    pwd = request.json["password"]
    return jsonify(authenticate(conn, login, pwd))


exposed_models = {"users": AuthUser, "category": Category}


@app.route("/db/<model>", methods=["GET", "POST"])
def api_routes(model):
    return model_to_route(exposed_models[model], conn)()


@app.route("/db/<model>/<id>", methods=["GET", "PUT", "DELETE"])
def api_routes_id(model, id):
    return model_to_route_id(exposed_models[model], conn)(id)
