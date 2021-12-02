from .BaseModel import BaseModel


class Category(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'categories'

    @staticmethod
    def fields():
        return ["id", "title"]

    @staticmethod
    def foreign_fields():
        return []
