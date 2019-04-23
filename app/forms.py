from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, InputRequired
from wtforms import TextAreaField, StringField, SelectField, PasswordField, SelectField


class  Customer(FlaskForm):
    title =  SelectField('Title', choices = [('','Select One'),('Miss','Miss'),('Mrs','Mrs'), ('Mr','Mr')]) 
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    address = StringField ('Address', validators=[InputRequired()])
    email = StringField ('Email', validators=[InputRequired()])
    phoneNum = StringField ('Phone Number', validators=[InputRequired()])
    Company_name = StringField ('Company Name', validators=[InputRequired()])
    gender = SelectField('Gender', choices = [('','Select One'),('Male','Male'),('Female','Female')]) 
    

class User(FlaskForm):    
    username = StringField ('Username', validators=[InputRequired()])
    password = PasswordField ('Password',  validators=[InputRequired()])
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    gender = SelectField('Gender', choices = [('','Please choose one'),('Male','Male'),('Female','Female')], validators=[InputRequired()]) 
    address = StringField ('Address', validators=[InputRequired()])
    email = StringField ('Email', validators=[InputRequired()])
    usertype = SelectField('Type of User', choices = [('','Please choose one'),('E','Employee'),('M','Manager')], validators=[InputRequired()])
    
    
    
class Appointment(FlaskForm):
    appointmentname = StringField ('Appointment name', validators=[InputRequired()])
    appointmentdate = StringField ('Apointment Date', validators=[InputRequired()])


class LoginUser(FlaskForm):
    username = StringField ('Username', validators=[InputRequired()])
    password = PasswordField ('Password',  validators=[InputRequired()])
    
class AC(FlaskForm):
    actype = StringField ('Air Condition Unit', validators=[InputRequired()])
    acissue = StringField ('Air Condition Issue', validators=[InputRequired()])
    service = SelectField ('Type of service to be done to the unit', choices = [('Types','Types'), ('Installation','Installation'), ('Repair','Repair'), ('Gas Refile','Gas Refile'), ('General Service','General Service')])
    
    
    