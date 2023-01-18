#from webapp.market.models import Vitamins
from flask import Blueprint, current_app, render_template

blueprint = Blueprint('market', __name__)

@blueprint.route("/")
def index():
    page_title = 'Витамины и БАДы NOW'
    title = 'Введите название и дозировку'
    return render_template('market/index.html', page_title=page_title, title = title)
