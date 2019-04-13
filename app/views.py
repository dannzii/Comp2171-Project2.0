import os
import datetime
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import Customer, User, Appointment
from app.models import UserProfile, Customers


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/mission_statemement')
def Mission_Statemement():
    """Render website's Mission Statment page."""
    return render_template('mission_statement.html')
    
    

@app.route('/vission_statemement')
def Vission_Statemement():
    """Render website's Vission Statment page."""
    return render_template('vission_statement.html')

@app.route('/Manager/')
def manager():
    """Render website's Manager Page"""
    return render_template('Manager.html')


@app.route('/addemployee/', methods=['POST', 'GET'])
def addemployee():
    if not session.get('logged_in'):
        abort(401)
        
    form = User()
    if request.method == "POST":
        
        if form.validate_on_submit():
            
            firstname = form.firstname.data
            lastname = form.lastname.data
            email = form.email.data
            address = form.address.data
            username = form.username.data
            password = form.password.data
            User_type = form.User_type.data
        
        flash('Completed', 'Success')
        return redirect(url_for('manager'))
    
    flash('An error occured', 'OOPS') 
    return render_template('addemployee.html',form=form)
    
@app.route('/createAppointment/', methods=['POST', 'GET'])
def Create_appointment():
    this_form = Appointment()
    
    if request.methods == "POST":
        if this_form.validate_on_submit():
            
            appointment= this_form.appointment.data
            
            flash('Your appointment has been set')
            return redirect(url_for('manager'))
        else:
            flash('OOPs an error has occured, please try again')
            return render_template('createappointment.html', form=this_form)

@app.route("/customerProfiles")
def customerprofiles():
    users = Customers.query.all()
    profiles = []
    
    for user in users:
        profiles.append({"firstname":user.first_name, "lastname": user.last_name, "gender": user.gender, "location":user.location, "created_on":user.created_on, "id":user.id})
    
    return render_template("list-of-customer.html", profiles = profiles)
    
@app.route('/profile/<userid>')
def inidi_customer_profile(userid):
    user = Customers.query.filter_by(id=userid).first()
    
    if user is None:
        return redirect(url_for('home'))
        
    c_y = int(user.created_on.split("-")[0])
    c_m = int(user.created_on.split("-")[1])
    c_d = int(user.created_on.split("-")[2])
    
    user.created_on = format_date_joined(c_y, c_m, c_d)
    
    return render_template("inidi_customer_profile.html", user = user)

def format_date_joined(yy,mm,dd):
    return datetime.date(yy,mm,dd).strftime("%B, %d,%Y")
   
@app.route('/login', methods=['POST', 'GET'])
def login():

    my_login_form = User()
    error = None
    if request.method == 'POST':
        
        username = my_login_form.username.data
        password = my_login_form.password.data
         
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            
            flash('You were logged in', 'success')
            return redirect(url_for('manager'))
            
    flash('An error occurred while you tried to log in', 'Please try again')
    return render_template('login.html', form=my_login_form)
"""
        my_login_form = User()
        if my_login_form.validate_on_submit():
            
            username = my_login_form.username.data
            password = my_login_form.password.data
            
            user = UserProfile.query.filter_by(username=username).first()
            
            if user is not None and user.password == password:
                # get user id, load into session
                login_user(user)
"""
           
    
    
    
@app.route('/signedIn')   
def signedIn():
     if not session.get('logged_in'):
        abort(401)
        
        
        user = UserProfile.query.filter_by(username=username).first()
        if user is user.username == "Hyatt":
            flash('Welcome Mr.Hyatt')
            return render_template('Manager.html')
            
            
        elif user is user.username == "Emplo":
            flash('Welcome')
            return render_template('Employee.html')
        
       
@app.route('/registerClient', methods=['POST', 'GET'])
def registration():
    if not session.get('logged_in'):
        abort(401)
        
        myform = Customer()
        if request.method == "POST":
            if myform.validate_on_submit():
                
                firstname = myform.firstname.data
                lastname = myform.lastname.data
                address = myform.address.data
                gender = myform.gender.data
                email = myform.email.data
                
                flash('registion Complete', 'Success')
                return redirect(url_for('customerprofiles'))
                
        flash_errors(myform)
        return render_template('registration.html', form=myform)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    logout_user()
    flash('You were logged out', 'success')
    return render_template('logout.html')



def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')  

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
