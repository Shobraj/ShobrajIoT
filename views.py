from shobrajiot import app, mqtt
from models import *
from forms import LoginForm, RegisterForm
from flask import render_template, request, redirect, url_for, flash
from passlib.hash import sha256_crypt

@app.route("/")
def home():
    return render_template('home.html')


@app.route('/Login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/client')
def client():
    mqtt.publish('ws/world', 'hello world')
    return render_template('client.html')

@app.route('/Register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        flash("Registration success!", "success")

        return redirect(url_for('login'))
    return render_template('register.html', form=form)