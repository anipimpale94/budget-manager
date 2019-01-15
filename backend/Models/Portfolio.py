# libraries
from app import db

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(80), unique=False, nullable=False)
    estimate = db.Column(db.Float, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    create_date = db.Column(db.DateTime)
    modify_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<user %s>' % self.subject
