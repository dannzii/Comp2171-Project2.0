from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
app.config['SECRET_KEY'] = "Xyuilo134dRTy"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:admin101@localhost/froste_byte"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # necessary to tell Flask-Login what the default route is for the login page


app.config.from_object(__name__)

from app import views
