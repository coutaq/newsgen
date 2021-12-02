from .utils import arr_to_str, fields_with_values


def create_select(table_name: str, fields):
    if fields == ["*"]:
        fields = "*"
    else:
        fields = arr_to_str(fields, '`')

    def select(where):
        if where == "wildcard":
            return f"SELECT {fields} from `{table_name}`"
        else:

            return f"SELECT {fields} from `{table_name}` WHERE id = {where}"

    return select


def create_insert(table_name: str, fields: []):
    quote = "'"

    def insert(values: []):
        return f"INSERT into `{table_name}` ({arr_to_str(fields, '`')}) VALUES (NULL,{arr_to_str(values, quote)})"

    return insert


def create_update(table_name: str, fields: []):
    def update(where, values: []):
        return f"UPDATE `{table_name}` SET {fields_with_values(fields, values)} WHERE id = {where}"

    return update


def create_delete(table_name: str):
    def update(where):
        return f"DELETE from `{table_name}` WHERE id = {where}"

    return update
