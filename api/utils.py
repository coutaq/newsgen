from flask import request, jsonify, Response

from database.models.AuthUser import AuthUser
from database.models.BaseModel import BaseModel
from database.MySQLConnection import MySQLConnection
from database.utils import check_hash


def model_to_route(model: BaseModel, conn: MySQLConnection) -> ():
    def model_func() -> Response:
        data = dict()
        if request.method == 'GET':
            query = model.read()
            data = conn.execute_query(query, True)
        if request.method == 'POST':
            fields = model.fields() + model.foreign_fields()
            fields.remove("id")
            values = [request.json.get(x) for x in fields]
            print(values)
            query = model.create(values)
            data = conn.execute_query(query, True)
        return jsonify(data)

    return model_func


def model_to_route_id(model: BaseModel, conn: MySQLConnection) -> ():
    def model_id(id: str) -> Response:
        data = dict()
        if request.method == 'GET':
            query = model.read(where=id)
            data = conn.execute_query(query, True)
        if request.method == 'PUT':
            values = {k:v for k,v in request.json.items()}
            query = model.update(id, values)
            data = conn.execute_query(query, True)
        if request.method == 'sDELETE':
            query = model.delete(id)
            data = conn.execute_query(query, True)
        return jsonify(data)

    return model_id


def authenticate(conn, login: str, password: str):
    if "@" in login and "." in login:
        query = AuthUser.read(where=f"email = '{login}'")
        user = conn.execute_query(query)
        if len(user) == 0:
            return {"user": None, "errors": {"login": "Пользователя с такой почтой не существует."}}
        else:
            if check_hash(password, user[0]["password"]):
                return user, []
            else:
                return {"user": None, "errors": {"password": "Неверный пароль!"}}
    else:
        query = AuthUser.read(where=f"login = '{login}'")
        user = conn.execute_query(query)
        if len(user) == 0:
            return {"user": None, "errors": {"login": "Пользователя с таким никнеймом не существует."}}
        else:
            if check_hash(password, user[0]["password"]):
                return {"user": user, "errors": None}
            else:
                return {"user": None, "errors": {"password": "Неверный пароль!"}}
    return {}
