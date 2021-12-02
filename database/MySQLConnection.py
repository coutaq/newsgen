import pymysql

from log.LogManager import LogManager


class MySQLConnection:

    @staticmethod
    def connection():
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='vk-parser',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection

    def execute_query(self, query, verbose=False):

        conn = self.connection()
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        conn.commit()
        conn.close()
        if verbose:
            lg = LogManager()
            lg.notify(query)
        return row

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MySQLConnection, cls).__new__(cls)
        return cls.instance
