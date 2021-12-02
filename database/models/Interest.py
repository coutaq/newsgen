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
