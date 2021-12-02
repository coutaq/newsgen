from database.models.BaseModel import BaseModel


class Group(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'groups'

    @staticmethod
    def fields() -> list:
        return ["id", "title"]

    @staticmethod
    def foreign_fields() -> list:
        return []
