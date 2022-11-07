from models import User, Car, db


def add_user(user:User)->None:
    db.session.add(user)
    db.session.commit()

def delete_user(user:User)->None:
    db.session.delete(user)
    db.session.commit()

def get_all_users()->db.Query:
    return User.query.all()

def get_all_car()->db.Query:
    return Car.query.all()

def delete_car(car:Car)->None:
    db.session.delete(car)
    db.session.commit()

def add_car(car:Car)->None:
    db.session.add(car)
    db.session.commit()