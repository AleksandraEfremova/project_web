from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user,login_required, login_user, logout_user

from webapp.db import db
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User
from webapp.user.decorators import user_required

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('market.index'))

    title = "Авторизация"
    login_form = LoginForm()
    return render_template('user/login.html', title=title, form=login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
    if user and user.check_password(form.password.data):
        login_user(user, remember=form.remember_me.data)
        flash('Вы успешно авторизовались')
        return redirect(url_for('market.index'))

    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    flash('Вы вышли изучетной записи')
    logout_user()
    return redirect(url_for('market.index'))

@blueprint.route('/user')
@user_required
def user_index():
    page_title = 'Витамины и БАДы NOW. Избранное.'
    if current_user.is_user:
        return render_template('user/user.html', page_title=page_title)
    

@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('market.index'))
    form = RegistrationForm()
    title = "Регистрация"
    return render_template('user/registration.html', title=title, form=form)


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(getattr(form, field).label.text, error))
        return redirect(url_for('user.register'))