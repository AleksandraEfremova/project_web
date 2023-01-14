from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Vitamins(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    raiting = db.Column(db.Float, nullable=False)
    brand = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    
    def __repr__(self):
        return '<Vitamins {} {} {} {} {}>'.format(self.name, self.price, self.raiting, self.image, self.url)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return '<User {}>'.format(self.username)