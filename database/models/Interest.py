from database import QueryGenerator
from database.models.BaseModel import BaseModel


class Interest(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'interests'

    @staticmethod
    def fields() -> list:
        return ["id", "title"]

    @staticmethod
    def foreign_fields() -> list:
        return ["category_id"]

    @staticmethod
    def read(where=None, fields=None) -> str:
        if fields is None:
            fields = ["*"]
        return QueryGenerator.create_select(Interest.table_name(), fields)(where)+"LEFT JOIN `categories` on category_id = categories.id"
