from .BaseModel import BaseModel


class Category(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'friends'

    @staticmethod
    def fields():
        return ["id"]

    @staticmethod
    def foreign_fields():
        return ["from_id", "to_id"]
