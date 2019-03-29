from flask_wtf import FlaskForm
from wtforms import Form, TextField, PasswordField, StringField, TextAreaField, validators


class LoginForm(FlaskForm):
    username = TextField('username')
    password = PasswordField('password')


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1,max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password do not match')
    ])
    confirm = PasswordField('Confirm Password')