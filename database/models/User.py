from .BaseModel import BaseModel


class User(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'users'

    @staticmethod
    def fields():
        return ["id", "login", "password"]

    @staticmethod
    def foreign_fields():
        return ["role_id"]
