from database import QueryGenerator
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

    @staticmethod
    def read(where=None, fields=None) -> str:
        if fields is None:
            fields = ["user_posts.id, user_posts.opened, posts.title as 'post', users.name as 'user' "]
        return QueryGenerator.create_select(UserPost.table_name(), fields, "LEFT JOIN `posts` on post_id = posts.id", "LEFT JOIN `users` on user_id = users.id")(where)

    @staticmethod
    def create(values: list) -> str:
        print("VAL:")
        print(values)
        return QueryGenerator.create_insert(UserPost.table_name(), UserPost.fields()[0:2] + UserPost.foreign_fields())(values[0:1]+values[2:])
