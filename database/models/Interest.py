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
    def select(values) -> str:
        values[3] = hash(values[3])
        return QueryGenerator.create_insert(Interest.table_name(), Interest.fields()+", categories.title")+"LEFT JOIN `categories` on category_id = categories.id"(
            values)
