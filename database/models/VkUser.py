from database.models.BaseModel import BaseModel


class VkUser(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'vk_users'

    @staticmethod
    def fields() -> list:
        return ["id", "name", "vk_id"]

    @staticmethod
    def foreign_fields() -> list:
        return []
