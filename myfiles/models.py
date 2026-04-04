from myfiles import db
from datetime import datetime

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    files = db.relationship("File", backref="user", lazy=True)

    pass

class File(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, default="default.txt")
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False )
    pass
