from api.app import app
from database.models.AuthUser import AuthUser
print(AuthUser.update("10", {"login":"test", "email":'ttt', 'hui':'dd'}))