from .BaseModel import BaseModel


class VkUserInGroups(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'vk_users_interests'

    @staticmethod
    def fields():
        return ["id"]

    @staticmethod
    def foreign_fields():
        return ["vk_user_id", "interest_id"]
