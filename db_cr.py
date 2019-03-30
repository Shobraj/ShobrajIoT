from shobrajiot import db
from models import User
from passlib.hash import sha256_crypt

db.create_all()


db.session.add('shobharaj', 'shobraj', 'shobharajsk@gmail.com',sha256_crypt.encrypt('asdf'))

db.session.commit()