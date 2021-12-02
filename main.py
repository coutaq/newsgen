from api.app import app
from database.MySQLConnection import MySQLConnection
from database.models.User import User
from log.ConsoleLogger import ConsoleLogger
from log.LogManager import LogManager

app.run(debug=True)
lg = LogManager()
lg.attach(ConsoleLogger())

conn = MySQLConnection()

query = User.create(['coutaq', '12345678'])
