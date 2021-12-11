from api.app import app
import os
from database.models.User import User
from database.models.Post import Post
from database.MySQLConnection import MySQLConnection
basedir = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = "/assets/"
app.config['BASEDIR'] = basedir
#app.run(debug=True)

conn = MySQLConnection()
query = User.read(fields=['users.id'])
users = conn.execute_query(query, True)
query = Post.read(fields=['posts.id'])
posts = conn.execute_query(query, True)
users = map(lambda d: d['id'], users)
posts = map(lambda d: d['id'], posts)
print(users)
print(posts)
