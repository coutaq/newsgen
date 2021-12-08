from api.app import app
import os
basedir = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = "/assets/"
app.config['BASEDIR'] = basedir
app.run(debug=True)
