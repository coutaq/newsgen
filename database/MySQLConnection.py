import pymysql

from log.LogManager import LogManager


class MySQLConnection:

    @staticmethod
    def connection():
        connection = pymysql.connect(
            host='localhost',
            user='coutaq',
            password='qwed',
            db='newsgen',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection

    def execute_query(self, query: str, verbose=False) -> dict:
        if verbose:
            lg = LogManager()
            lg.notify(query)
        conn = self.connection()
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        conn.commit()
        conn.close()
        if verbose:
            lg.notify(row)
        if len(row) == 1:
            return row[0]
        return row

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MySQLConnection, cls).__new__(cls)
        return cls.instance
