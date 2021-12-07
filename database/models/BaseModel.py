from abc import ABC

import database.QueryGenerator as QueryGenerator


class BaseModel(ABC):

    @classmethod
    def table_name(cls) -> str:
        pass

    @classmethod
    def fields(cls) -> list:
        pass

    @classmethod
    def foreign_fields(cls) -> list:
        pass

    @classmethod
    def create(cls, values) -> str:
        return QueryGenerator.create_insert(cls.table_name(), cls.fields() + cls.foreign_fields())(values)

    @classmethod
    def read(cls, where=None, fields=None) -> str:
        if fields is None:
            fields = ["*"]
        return QueryGenerator.create_select(cls.table_name(), fields)(where)

    @classmethod
    def update(cls, where, values) -> str:
        return QueryGenerator.create_update(cls.table_name(), cls.fields() + cls.foreign_fields())(where, values)

    @classmethod
    def delete(cls, where) -> str:
        return QueryGenerator.create_delete(cls.table_name())(where)
