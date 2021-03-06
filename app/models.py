from . import db
import datetime
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

class UserProfile(db.Model, UserMixin):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
  
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255), unique=True)
    
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
  
  
class Customers(db.Model):
    __tablename__ = 'customer_information'

    id = db.Column(db.Integer, primary_key=True)
    
    title = db.Column(db.String(80))
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    address = db.Column(db.String(120))
    gender = db.Column(db.String(100))
    phoneNum = db.Column(db.String(80))
    email = db.Column(db.String(80))
    created_on = db.Column(db.String(120))
    
    def __init__(self,title, first_name, last_name,gender,address,email,phoneNum,created_on):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.gender = gender
        self.phoneNum = phoneNum
        self.email = email
        self.created_on = created_on
        
class CreateUser(db.Model):
    __tablename__ = 'employee_information'
    
    id = db.Column(db.Integer, primary_key=True)
    
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    address = db.Column(db.String(120))
    gender = db.Column(db.String(100))
    email = db.Column(db.String(80))
    username = db.Column(db.String(80))
    password = db.Column(db.String(257))
    usertype = db.Column(db.String(100))
    created_on = db.Column(db.String(120))
    
    
    def __init__(self, first_name, last_name,gender,email,username,password,address,usertype):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.address = address
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.created_on = str(datetime.datetime.now())[:-16]
        self.usertype = usertype
        
class appointment(db.Model):
    __tablename__ = 'appointment'
    
    id = db.Column(db.Integer, primary_key=True)
    
    appointment = db.Column(db.String(120))
    appointmentdate = db.Column(db.String(120))
    
    
    def __init__(self,appointment,appointmentdate):
        self.appointment = appointment
        self.appointmentdate = appointmentdate

class ac(db.Model):
    __tablename__ = 'ac_units'
    
    id = db.Column(db.Integer, primary_key=True)
    
    actype = db.Column(db.String(257))
    acissue = db.Column(db.String(257))
    service =db.Column(db.String(200))
    
    
    def __init__(self,actype,acissue, service):
        self.actype = actype
        self.acissue = acissue
        self.service = service
        
        

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)