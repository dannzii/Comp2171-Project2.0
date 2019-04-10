import os
from app import app
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user, current_user, login_required, login_manager, user_loader
from app.forms import Customer, Users
from app.models import UserProfile


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')
    
@app.route('/login', methods=['POST', 'GET'])
def login():

    my_login_form = Users()
    if request.method == 'POST':
        if my_login_form.validate_on_submit():
            
            username = my_login_form.username.data
            password = my_login_form.password.data
            
            user = UserProfile.query.filter_by(username=username).first()
            
            if user is not None and user.password == password:
                # get user id, load into session
                login_user(user)
            
            flash('You were logged in', 'success')
            return redirect(url_for('signedIn'))
            
            
    flash('An error occurred while you tried to log in', 'Please try again')
    return render_template('login.html', form=my_login_form)
    
    
    
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
        
       
@app.route('/Register Client')
def registration():
     if not session.get('logged_in'):
        abort(401)
        
        myform = Customer()
        
        if request.method == 'POST':
            if myform.validate_on_submit():
                firstname = myform.firstname.data
                lastname = myform.lastname.data
                address = myform.address.data
                email = myform.email.data
                appointment = myform.appointment.data
                
                flash('registion Complete', 'Success')
                return redirect(url_for('signedIn'))
                
        flash_errors(myform)
        return render_template('registration.html', form=myform)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out', 'success')
    return render_template(logout.html)



def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')  


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
