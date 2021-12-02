from database.models.BaseModel import BaseModel


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
