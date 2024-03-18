####........Importing required Modules.......#####
#Flask application to write API's
from flask import Flask
#SQLite database for storing data
from flask_sqlalchemy import SQLAlchemy
#Encrypt the password such that the user account is secured
from flask_bcrypt import Bcrypt
#Login manager
from flask_login import LoginManager
#Socket
from flask_sock import Sock
from flask_socketio import SocketIO
import os


####........Initializing the application......#####
app = Flask(__name__)


##This allows the application to identify the database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "users.db")

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SECRET_KEY"] = 'd42595c985f88f823cd2b3c5'
db  = SQLAlchemy(app)
bcrypt = Bcrypt(app)

## This lines are new for versions after 
## SQLAlcemy-3.0 to fix out of context error
#from requirement_chain.models import User
with app.app_context():
    db.create_all()

#socketio = SocketIO(app)
##This allows the application to manage the login pages
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
login_manager.refresh_view = "accounts.reauthenticate"

from requirement_chain import node