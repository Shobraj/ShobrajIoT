from shobrajiot import db

#databse table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), unique=True)

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.String(500))

    def __init__(self, title, body):
        self.title = title
        self.body = body
    
    def __repr__(self):
        return '<User {}>'.format(self.title)