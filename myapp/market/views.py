#from myapp.market.models import Vitamins
from flask import Blueprint, current_app, render_template, send_from_directory, request
from sqlalchemy import func
#from db import db
from flask_sqlalchemy import SQLAlchemy

from myapp.market.models import Vitamins


db = SQLAlchemy()

blueprint = Blueprint('market', __name__)

@blueprint.route("/")
def index():
    page_title = 'Витамины и БАДы NOW'
    title = 'Введите название и дозировку:'
    return render_template('market/index.html', page_title=page_title, title = title)

def search():
    name = request.args.get('name', None)
    query = db.select(Vitamins.name)
    query = query.filter(func.lower(Vitamins.name).contains(name.lower()))
    product_list = db.session.execute(query).scalars()
    product_list = Vitamins.query.order_by(Vitamins.price.desc()).all()
    return render_template('market/index.html', product_list=product_list)
