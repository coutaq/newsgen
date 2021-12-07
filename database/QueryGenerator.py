from .utils import arr_to_str

sep = '\''


def create_select(table_name: str, fields):
    def select(where="*"):
        return f"SELECT {arr_to_str(fields, '')} from {table_name} WHERE {where}"

    return select


def create_insert(table_name: str, fields: []):
    def insert(values: []):
        if len(values) != len(fields):
            return f"INSERT into {table_name} ({arr_to_str(fields, '`')}) VALUES (NULL,{arr_to_str(values, sep)})"

    return insert
