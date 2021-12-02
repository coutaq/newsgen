from .BaseModel import BaseModel


class Interest(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'interests'

    @staticmethod
    def fields():
        return ["id","title"]

    @staticmethod
    def foreign_fields():
        return ["category_id"]
