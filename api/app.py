from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from api.utils import model_to_route, model_to_route_id, authenticate
from database.MySQLConnection import MySQLConnection
from database.models.Category import Category
from database.models.AuthUser import AuthUser
from database.models.Interest import Interest
from database.models.Post import Post
from database.models.UserPost import UserPost
from database.models.User import User
from log.ConsoleLogger import ConsoleLogger
from log.LogManager import LogManager
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
import os

lg = LogManager()
lg.attach(ConsoleLogger())
conn = MySQLConnection()
app = Flask(__name__)
auth = HTTPBasicAuth()
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@auth.verify_password
def verify(username, password):
    return authenticate(conn, username, password)


@app.route("/upload-file", methods=["POST"])
@auth.login_required
def upload_file():
    file = request.files.get('file')
    filename = secure_filename(file.filename)
    file_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    print(app.config['BASEDIR'])
    print(file_location)
    with open(file_location, 'wb+') as localfile:
        file.save(localfile)
    return jsonify(file_location, app.config['BASEDIR'])


@app.route("/auth", methods=["POST"])
def auth_my():
    # lg.notify(request)
    login = request.json["login"]
    pwd = request.json["password"]
    return jsonify(authenticate(conn, login, pwd))


@app.route('/getReport')
@auth.login_required
def report():
    query = "CALL `GetTopPostsOfAllTime`();"
    top_posts = conn.execute_query(query, True)
    query = "CALL `GetViewsOfAllTime`();"
    views = conn.execute_query(query, True)
    query = "CALL `GetViewsByInterest`();"
    views_by_interest = conn.execute_query(query, True)

    return {'top_posts': top_posts, 'views': views, 'views_by_interest': views_by_interest}


exposed_models = {"users": AuthUser, "categories": Category, "dbusers": User, "posts": Post, "seen": UserPost,
                  "interests": Interest}


@app.route("/db/<model>", methods=["GET", "POST"])
@auth.login_required
def api_routes(model):
    return model_to_route(exposed_models[model], conn)()


@app.route("/db/<model>/<id>", methods=["GET", "PUT", "DELETE"])
@auth.login_required
def api_routes_id(model, id):
    return model_to_route_id(exposed_models[model], conn)(id)


@app.route("/interests-filter/<id>")
@auth.login_required
def int_filter(id):
    query = Interest.read(id, 'category_id')
    data = conn.execute_query(query, True)
    if not isinstance(data, list):
        data = [data]
    return jsonify(data)


@app.route("/posts-filter/<id>")
@auth.login_required
def post_filter(id):
    query = Post.read(id, 'interest_id')
    data = conn.execute_query(query, True)
    if not isinstance(data, list):
        data = [data]
    return jsonify(data)
