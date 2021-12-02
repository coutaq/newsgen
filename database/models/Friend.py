from database.models.BaseModel import BaseModel


class Category(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'friends'

    @staticmethod
    def fields() -> list:
        return ["id"]

    @staticmethod
    def foreign_fields() -> list:
        return ["from_id", "to_id"]
