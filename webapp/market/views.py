from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy

from webapp.market.models import Vitamins

db = SQLAlchemy()

blueprint = Blueprint('market', __name__)


@blueprint.route("/")
def index():
    page_title = 'Витамины и БАДы NOW'
    title = 'Введите название и дозировку:'
    return render_template('market/index.html', page_title=page_title, title=title)


def search():
    product_list = Vitamins.query.order_by(Vitamins.price.desc()).all()
    return render_template('market/index.html', product_list=product_list)
