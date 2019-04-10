from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, InputRequired
from wtforms import TextAreaField, StringField, SelectField, PasswordField


class  Customer(FlaskForm):
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    address = StringField ('Address', validators=[InputRequired()])
    email = StringField ('Email', validators=[InputRequired()])
    appointment = StringField ('Appointment', validators=[InputRequired()])
    ac_type = StringField ('Air Condition Unit', validators=[InputRequired()])
    unit_service = SelectField ('Type of service to be done to the unit', choices = ['Types', 'Installation', 'Repair', 'Gas Refile', 'General Service'])





class Users(FlaskForm):    
    username = StringField ('Username', validators=[InputRequired()])
    password = PasswordField ('Password',  validators=[InputRequired()])


    
class AddEmployee(FlaskForm):
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    address = StringField ('Address', validators=[InputRequired()])
    email = StringField ('Email', validators=[InputRequired()])
    username = StringField ('Username', validators=[InputRequired()])
    password = PasswordField ('Password',  validators=[InputRequired()])