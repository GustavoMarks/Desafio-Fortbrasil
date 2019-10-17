from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    name = db.Column(db.String)


    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


    def __repr__ (self):
        return "<User %r>" % self.email


class Estab(db.Model):
    __tablename__ = "estabs"

    id = db.Column(db.Integer, primary_key = True)
    phone = db.Column(db.String, unique = True)
    name = db.Column(db.String)
    adress = db.Column(db.String)
    owner = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=owner)


    def __init__(self, phone, name, adress, owner):
        self.phone = phone
        self.name = name
        self.adress = adress
        self.owner = owner


    def __repr__ (self):
        return "<Estab %r>" % self.phone