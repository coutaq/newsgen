from database import QueryGenerator
from database.models.BaseModel import BaseModel
from database.utils import hash


class AuthUser(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'auth_users'

    @staticmethod
    def fields() -> list:
        return ["id", "name", "login", "email", "password", "image"]

    @staticmethod
    def foreign_fields() -> list:
        return []

    @staticmethod
    def create(values) -> str:
        values[4] = hash(values[4])
        return QueryGenerator.create_insert(AuthUser.table_name(), AuthUser.fields() + AuthUser.foreign_fields())(values)

    @staticmethod
    def update(where, values) -> str:
        values[4] = hash(values[4])
        return QueryGenerator.create_update(AuthUser.table_name(), AuthUser.fields() + AuthUser.foreign_fields())(where, values)
