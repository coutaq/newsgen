from abc import ABC, abstractmethod
from database.MySQLConnection import MySQLConnection
import database.QueryGenerator as qg


class BaseModel(ABC):

    @classmethod
    def table_name(cls) -> str:
        pass

    @classmethod
    def fields(cls):
        pass

    @classmethod
    def foreign_fields(cls):
        pass

    @classmethod
    def create(cls, values) -> str:
        return qg.create_insert(cls.table_name(), cls.fields() + cls.foreign_fields())(values)

    @classmethod
    def read(cls, fields=["*"], where="wildcard") -> str:
        return qg.create_select(cls.table_name(), fields)(where)

    @classmethod
    def update(cls, where, values) -> str:
        return qg.create_update(cls.table_name(), cls.fields() + cls.foreign_fields())(where, values)

    @classmethod
    def delete(cls, where) -> MySQLConnection:
        return qg.create_delete(cls.table_name())(where)
