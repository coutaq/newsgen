from database import QueryGenerator
from database.models.BaseModel import BaseModel
from database.utils import hash

class User(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'users'

    @staticmethod
    def fields() -> list:
        return ["id", "login", "password"]

    @staticmethod
    def foreign_fields() -> list:
        return ["role_id"]

    @staticmethod
    def create(values) -> str:
        values[1] = hash(values[1])
        return QueryGenerator.create_insert(User.table_name(), User.fields() + User.foreign_fields())(values)

    @staticmethod
    def update(where, values) -> str:
        values[1] = hash(values[1])
        return QueryGenerator.create_update(User.table_name(), User.fields() + User.foreign_fields())(where, values)
