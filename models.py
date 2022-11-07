from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwd = db.Column(db.String(300), nullable=False, unique=True)
    is_admin = db.Column(db.Boolean, default=False)
    wish = db.Column(db.String)

    def __repr__(self):
        return '<User %r>' % self.username

class Car(db.Model):
    __tablename__ = "car"

    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, unique=True, nullable=False)
    car_name = db.Column(db.CHAR(120), unique=True, nullable=True)
    description = db.Column(db.Text(300), nullable=True, unique=False)
    model = db.Column(db.CHAR(120), nullable = True, unique=False)
    img = db.Column(db.BLOB, nullable = True, unique = False)

    def __repr__(self):
        return '<Car %r>' % self.car_name