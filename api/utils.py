from flask import request, jsonify

from database.models.BaseModel import BaseModel


def model_to_route(model: BaseModel, conn):
    def model():
        if request.method == 'GET':
            query = model.read()
            data = conn.execute_query(query, True)
        if request.method == 'POST':
            fields = model.fields() + model.foreign_fields()
            fields.remove("id")
            values = [request.form.get(x) for x in fields]
            query = model.create(values)
            data = conn.execute_query(query, True)
        return jsonify(data)

    return model


def model_to_route_id(model: BaseModel, conn):
    def model_id(id):
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
