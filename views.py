from shobrajiot import app, mqtt, db
from models import User
from forms import LoginForm, RegisterForm
from flask import render_template, request, redirect, url_for, flash, session
from passlib.hash import sha256_crypt
from sqlalchemy import exc
from functools import wraps


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Unauthorized, Please log in", 'danger')
            return redirect(url_for('login'))
    return wrap


@app.route("/")
def home():
    return render_template('home.html')

#user login
@app.route('/Login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        email = form.email.data
        password_cadidate = form.password.data
        try:
            user = User.query.filter_by(email=email).first()
            if user:
                if (user.email == email) and sha256_crypt.verify(password_cadidate, user.password):
                    #app.logger.info('user '+user.name+' log in')
                    session['logged_in'] = True
                    session['username'] = user.username                    
                    print('user '+user.name+' log in')
                    flash('Welcome '+user.username+' ☻', 'success')
                    return redirect(url_for('home'))
                else:
                    #app.logger.info('log failed for '+user.name)
                    print('log failed for '+user.name)
                    flash("Log In failed", "danger")
                    return render_template('login.html', form=form)
            else:
                flash("No user with email "+email, "danger")
                return render_template('login.html', form=form)
        except exc.SQLAlchemyError:
            #app.logger.info(exc)            
            flash("Couldn't log in!", "danger")
        except AttributeError:
            flash("Some thing went wrong!", "warning")
            return redirect(url_for('home'))

    return render_template('login.html', form=form)


#Logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logout.', 'success')
    return redirect(url_for('login'))
    

#user register
@app.route('/Register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        user = User(name, username, email, password)
        try:
            db.session.add(user)
            db.session.commit()
            flash("Registration success!", "success")
            return redirect(url_for('login'))
        except exc.IntegrityError:
            flash("User with same detials is already exist!", "warning")
            return redirect(url_for('register'))
        except AttributeError:
            flash("Some thing went wrong!", "warning")
            return redirect(url_for('home'))
    
    return render_template('register.html', form=form)


@app.route('/client')
@is_logged_in
def client():
    mqtt.publish('ws/world', 'hello world')
    return render_template('client.html')

@app.route('/UI')
@is_logged_in
def UI():
    return render_template('ui.html')