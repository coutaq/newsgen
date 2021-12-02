from api.app import app
from database.MySQLConnection import MySQLConnection
from database.models.User import User
from log.ConsoleLogger import ConsoleLogger
from log.LogManager import LogManager
from database.utils import  hash, check_hash
app.run(debug=True)
