from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user
from webapp.model import db, Vitamins, User
from webapp.forms import LoginForm

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


    @app.route("/")
    def index():
        page_title = 'Витамины и БАДы NOW'
        title = 'Введите название и дозировку'
        return render_template('index.html', page_title=page_title, title = title)


    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', title=title, form=login_form)
    

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Вы успешно авторизовались')
            return redirect(url_for('index'))

        flash('Неправильное имя пользователя или пароль')
        return redirect(url_for('login'))


    @app.route('/logout')
    def logout():
        flash('Вы вышли изучетной записи')
        logout_user()
        return redirect(url_for('index'))


    return app
    