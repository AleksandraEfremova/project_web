from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_required
from flask_migrate import Migrate

from webapp.db import db
#from webapp.market.models import Vitamins
from webapp.user.models import User
from webapp.market.views import blueprint as market_blueprint
from webapp.user.views import blueprint as user_blueprint
from . import commands



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(market_blueprint)
    app.register_blueprint(user_blueprint)

    register_commands(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


    return app

def register_commands(app):
    app.cli.add_command(commands.save_products)
   