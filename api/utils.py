from flask import request, jsonify, Response

from database.models.BaseModel import BaseModel
from database.MySQLConnection import MySQLConnection


def model_to_route(model: BaseModel, conn: MySQLConnection) -> ():
    def model_func() -> Response:
        data = dict()
        if request.method == 'GET':
            query = model.read()
            data = conn.execute_query(query, True)
        if request.method == 'POST':

            fields = model.fields() + model.foreign_fields()
            fields.remove("id")
            values = [request.form.get(x) for x in fields]
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
            fields = model.fields() + model.foreign_fields()
            fields.remove("id")
            values = [request.form.get(x) for x in fields]
            query = model.update(id, values)
            data = conn.execute_query(query, True)
        if request.method == 'DELETE':
            query = model.delete(id)
            data = conn.execute_query(query, True)
        return jsonify(data)

    return model_id
