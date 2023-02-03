from flask_sqlalchemy import SQLAlchemy
from webapp import config

from webapp.db import db


class Vitamins(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    
    @property
    def image_path(self):
        return f'/{config.MEDIA_DIR}/{self.image}'

    def __repr__(self):
        return self.name