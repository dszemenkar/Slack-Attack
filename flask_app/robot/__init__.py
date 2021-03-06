import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '03856807-e819-4a58-84c8-0c1c1f7e6275'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///robot.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

from robot.core.views import core
from robot.messages.views import messages
from robot.users.views import users
from robot.error_pages.handlers import error_pages


app.register_blueprint(core)
app.register_blueprint(messages)
app.register_blueprint(users)
app.register_blueprint(error_pages)