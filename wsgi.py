from api.app import app
import os
basedir = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = "/assets/"
app.config['BASEDIR'] = os.path.realpath("/home/coutaq/public_html/newsletter/assets")
if __name__ == "__main__":
    app.run()
