from database.models.BaseModel import BaseModel


class Role(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'posts'

    @staticmethod
    def fields() -> list:
        return ["id", "title", "link", "created_at"]

    @staticmethod
    def foreign_fields() -> list:
        return ['interest_id']
