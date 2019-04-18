import os
import datetime
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import Customer, User, Appointment, LoginUser
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
            firstname = Customers(first_name = form.get("firstname"))
            lastname = Customers(last_name = form.get("lastname"))
            gender = Customers(gender = form.get("gender"))
            email = Customers(email = form.get("email"))
            address = Customers(address = form.get("address"))
            username = Customers(username = form.get("username"))
            password = Customers(password = form.get("password"))
            user_type = Customers(user_type = form.get("User_type"))
            
            db.session.add(firstname)
            db.session.add(lastname)
            db.session.add(gender)
            db.session.add(email)
            db.session.add(address)
            db.session.add(username)
            db.session.add(password)
            db.session.add(user_type)
            
            db.session.commit()
        flash('Registration Completed', 'Success')
        return redirect(url_for('manager'))
    
    flash_errors (form)  
    return render_template('addemployee.html',form=form)


@app.route('/registerClient', methods=['POST', 'GET'])
def registration():
    if not session.get('logged_in'):
        abort(401)
    
    thisform = Customer()
    if request.method == "POST":
        
        if thisform.validate_on_submit():
            firstname = thisform.firstname.data
            lastname = thisform.lastname.data
            gender = thisform.gender.data
            address = thisform.address.data
            email = thisform.email.data
            
        flash('Registration Completed', 'Success')
        return redirect(url_for('manager'))
        
    flash_errors (thisform) 
    return render_template('registration.html' , form=thisform)
        
@app.route('/createAppointment/', methods=['POST', 'GET'])
def Create_appointment():
    this_form = Appointment()
    
    if request.method == "POST":
        if this_form.validate_on_submit():
            
            appointment= this_form.appointment.data
            
            flash('Your appointment has been set')
            return redirect(url_for('manager'))
            
    flash_errors (this_form) 
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

    my_login_form = LoginUser()
    if request.method == 'POST':
        if my_login_form.validate_on_submit():
            
            username = my_login_form.username.data
            password = my_login_form.password.data
            
            user = UserProfile.query.filter_by(username=username).first()
            
            if user is not None and check_password_hash(user.password, password ):
                remember_me = False
                
                if 'remember_me' in request.form:
                    remember_me = True
                # get user id, load into session
                login_user(user, remember=remember_me)
                
            next_page = request.args.get('next')
            # remember to flash a message to the user
            flash("Login Successful", "success")
            print (next_page)
            return redirect(url_for("manager") )
            
    flash_errors (my_login_form) 
    return render_template('login.html', form=my_login_form)

@app.route('/<file_name>.txt')
@login_required
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)
    
@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))    
    
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
        
        
        
@app.route('/logout')
def logout():
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
