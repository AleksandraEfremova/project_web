from datetime import timedelta
import os

import os.path
from pathlib import Path

from environs import Env

basedir = os.path.abspath(os.path.dirname(__file__))

env = Env()
env.read_env()


ENV = env.str("FLASK_ENV", default="development")
DEBUG = ENV == "development"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'fkhgfwyegd,gduk,gicw,ufkeb'
SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
REMEMBER_COOKIE_DURATION = timedelta(days=5)
SQLALCHEMY_TRACK_MODIFICATIONS = False
BASE_DIR = Path(__file__).resolve()
MEDIA_DIR = os.path.join(os.path.dirname(BASE_DIR), 'media')