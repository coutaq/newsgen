from log.ConsoleLogger import ConsoleLogger
from log.LogManager import LogManager
from database.models.User import User
from database.MySQLConnection import MySQLConnection
from api.app import app
app.run(debug=True)
lg = LogManager()
lg.attach(ConsoleLogger())

conn = MySQLConnection()

query = User.create(['coutaq', '12345678'])
