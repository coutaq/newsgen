from functools import reduce

from .utils import arr_to_str

sep = '\''


def create_select(table_name: str, fields, *args):
    def select(where):
        return f"SELECT {arr_to_str(fields, '')} from {table_name} {' '.join(args)} {'WHERE id = ' + where if where else ''} ORDER BY `{table_name}`.id;"

    return select


def create_insert(table_name: str, fields: []):
    def insert(values: []):
        if len(values) != len(fields):
            return f"INSERT into {table_name} ({arr_to_str(fields, '`')}) VALUES (NULL,{arr_to_str(values, sep)})"

    return insert


def create_update(table_name: str):
    def value_to_string(key, value):
        return f"`{key}`={sep}{value}{sep}"

    def update(where: str, values: dict):
        return f"UPDATE {table_name} SET {','.join([value_to_string(k, v) for k, v in values.items()])} WHERE id = {where}"

    return update


def create_delete(table_name: str):
    def delete(where):
        return f"DELETE from {table_name} WHERE id = {where}"

    return delete
