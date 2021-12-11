from database.models.BaseModel import BaseModel


class User(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'users'

    @staticmethod
    def fields() -> list:
        return ["id", "name", "gender", "age"]

    @staticmethod
    def foreign_fields() -> list:
        return []
