from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vitamins(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    raiting = db.Column(db.Float, nullable=False)
    brand = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return ''