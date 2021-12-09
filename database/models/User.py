from database.models.BaseModel import BaseModel


class User(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'users'

    @staticmethod
    def fields() -> list:
        return ["id", "name"]

    @staticmethod
    def foreign_fields() -> list:
        return []
