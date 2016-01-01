from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CsrfProtect
from flask.ext.login import LoginManager


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
csrf = CsrfProtect(app)
lm = LoginManager()
lm.init_app(app)
from server import views, models


