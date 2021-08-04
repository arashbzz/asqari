from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config  import Development
from flask_migrate import Migrate



app = Flask(__name__)
app.config.from_object(Development)
db = SQLAlchemy(app)
migrate = Migrate(app,db)


from viwes import index

from mod_photo import photo
from mod_admin import admin
from mod_users import users


app.register_blueprint(photo)
app.register_blueprint(admin)
app. register_blueprint(users)