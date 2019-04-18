from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, InputRequired
from wtforms import TextAreaField, StringField, SelectField, PasswordField, SelectField


class  Customer(FlaskForm):
    title =  SelectField('Title', choices = [('','Select One'),('M','Miss'),('Mrs','Mrs'), ('Mr','Mr')]) 
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    address = StringField ('Address', validators=[InputRequired()])
    email = StringField ('Email', validators=[InputRequired()])
    phoneNum = StringField ('Phone Number', validators=[InputRequired()])
    Company_name = StringField ('Company Name', validators=[InputRequired()])
    gender = SelectField('Gender', choices = [('','Select One'),('M','Male'),('F','Female')]) 
    





class User(FlaskForm):    
    username = StringField ('Username', validators=[InputRequired()])
    password = PasswordField ('Password',  validators=[InputRequired()])
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    gender = SelectField('Gender', choices = [('','Please choose one'),('M','Male'),('F','Female')], validators=[InputRequired()]) 
    address = StringField ('Address', validators=[InputRequired()])
    email = StringField ('Email', validators=[InputRequired()])
    User_type = SelectField('Type of User', choices = [('','Please choose one'),('E','Emplpoyee'),('M','Manager')], validators=[InputRequired()])
    
    
    
class Appointment(FlaskForm):
    appointment = StringField ('Appointment Date', validators=[InputRequired()])
    app


class LoginUser(FlaskForm):
    username = StringField ('Username', validators=[InputRequired()])
    password = PasswordField ('Password',  validators=[InputRequired()])
    
class AC(FlaskForm):
    ac_type = StringField ('Air Condition Unit', validators=[InputRequired()])
    ac_issue = StringField ('Air Condition I', validators=[InputRequired()])
    unit_service = SelectField ('Type of service to be done to the unit', choices = ['Types', 'Installation', 'Repair', 'Gas Refile', 'General Service'])