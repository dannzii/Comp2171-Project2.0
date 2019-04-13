from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, InputRequired
from wtforms import TextAreaField, StringField, SelectField, PasswordField, SelectField


class  Customer(FlaskForm):
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    address = StringField ('Address', validators=[InputRequired()])
    email = StringField ('Email', validators=[InputRequired()])
    appointment = StringField ('Appointment', validators=[InputRequired()])
    gender = SelectField('Gender', choices = [('','Select One'),('M','Male'),('F','Female')]) 
    ac_type = StringField ('Air Condition Unit', validators=[InputRequired()])
    unit_service = SelectField ('Type of service to be done to the unit', choices = ['Types', 'Installation', 'Repair', 'Gas Refile', 'General Service'])





class User(FlaskForm):    
    username = StringField ('Username', validators=[InputRequired()])
    password = PasswordField ('Password',  validators=[InputRequired()])
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    gender = SelectField('Gender', choices = [('','Please choose one'),('M','Male'),('F','Female')]) 
    address = StringField ('Address', validators=[InputRequired()])
    email = StringField ('Email', validators=[InputRequired()])
    User_type = StringField ('Type of User', validators=[InputRequired()])
    
    
    
class Appointment(FlaskForm):
    appointment = StringField ('Appointment Date', validators=[InputRequired()])