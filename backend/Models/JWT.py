# libraries
from app import db

class JWT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    expiry_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<token %s>' % self.token