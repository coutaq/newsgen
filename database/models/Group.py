from .BaseModel import BaseModel


class Group(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'groups'

    @staticmethod
    def fields():
        return ["id","title"]

    @staticmethod
    def foreign_fields():
        return []
