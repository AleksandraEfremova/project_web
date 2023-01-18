
from getpass import getpass
import sys

from webapp import create_app
from webapp.db import User, db

app = create_app()

with app.app_context():
    username = input('Введите логин: ')

    if User.query.filter(User.username == username).count():
        print('Такой пользователь уже есть')
        sys.exit(0)

    password = getpass('Введите пароль: ')
    password2 = getpass('Повторите пароль: ')
    if not password == password2:
        sys.exit(0)
    
    new_user = User(username=username, role='user')
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print('Создан ползователя с id {}'.format(new_user.id))