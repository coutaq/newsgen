from .BaseModel import BaseModel


class VkUser(BaseModel):
    @staticmethod
    def table_name() -> str:
        return 'vk_users'

    @staticmethod
    def fields():
        return ["id", "name", "vk_id"]

    @staticmethod
    def foreign_fields():
        return []
