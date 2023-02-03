from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from webapp.db import db

favorite = db.Table(
    'favorite',
    db.Column('product_id', db.Integer, db.ForeignKey('vitamins.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
    email = db.Column(db.String(50))
    favorite = db.relationship(
        'Vitamins',
        secondary=favorite,
        lazy='subquery',
        backref=db.backref('users', lazy=True)
    )

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @property
    def is_user(self):
        return self.role == 'user'
