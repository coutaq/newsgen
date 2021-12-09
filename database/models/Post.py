from database import QueryGenerator
from database.models.BaseModel import BaseModel


class Post(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'posts'

    @staticmethod
    def fields() -> list:
        return ["id", "title", "link", "created_at"]

    @staticmethod
    def foreign_fields() -> list:
        return ['interest_id']

    @staticmethod
    def read(where=None, fields=None) -> str:
        if fields is None:
            fields = ["posts.id, posts.title, interests.title as 'interest' , interests.id as 'interest_id' "]
        return QueryGenerator.create_select(Post.table_name(), fields, "LEFT JOIN `interests` on interest_id = interests.id")(where)
