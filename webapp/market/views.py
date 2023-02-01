from flask import Blueprint, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

from webapp.market.models import Vitamins
from webapp import db
#db = SQLAlchemy()

blueprint = Blueprint('market', __name__)


@blueprint.route("/")
def index():
    page_title = 'Витамины и БАДы NOW'
    title = 'Введите название и дозировку:'
    name = request.args.get('name', None)
    
    query = db.select(Vitamins)
    if name:
        query = query.filter(func.lower(Vitamins.name).contains(name.lower()))
    vitamins = db.session.execute(query.order_by(Vitamins.price)).scalars()
    
    return render_template('market/index.html', page_title=page_title, title=title, vitamins=vitamins)


