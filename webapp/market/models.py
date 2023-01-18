from webapp.db import db

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

