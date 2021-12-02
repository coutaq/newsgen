from database.models.BaseModel import BaseModel


class VkUserInGroups(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'vk_users_interests'

    @staticmethod
    def fields() -> list:
        return ["id"]

    @staticmethod
    def foreign_fields() -> list:
        return ["vk_user_id", "interest_id"]
