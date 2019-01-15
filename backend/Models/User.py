# libraries
from app import db
import hashlib, uuid

salt = uuid.uuid4().hex

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), unique=False, nullable=False)
    create_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<user %s>' % self.name
    
    def hash_password(self, password):
        self.password = hashlib.sha512((password + salt).encode('utf-8')).hexdigest()