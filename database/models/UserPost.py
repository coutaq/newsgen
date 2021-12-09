from database.models.BaseModel import BaseModel


class UserPost(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'user_posts'

    @staticmethod
    def fields() -> list:
        return ["id", "opened", "created_at"]

    @staticmethod
    def foreign_fields() -> list:
        return ['user_id', 'post_id']
