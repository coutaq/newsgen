from .BaseModel import BaseModel


class Role(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'roles'

    @staticmethod
    def fields():
        return ["id","slug", "admin"]

    @staticmethod
    def foreign_fields():
        return []
