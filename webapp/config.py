import os.path
from datetime import timedelta
from pathlib import Path

from environs import Env

basedir = os.path.abspath(os.path.dirname(__file__))

env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve()
ENV = env.str("FLASK_ENV", default="development")
DEBUG = ENV == "development"
MEDIA_DIR = os.path.join(os.path.dirname(BASE_DIR), 'media')
REMEMBER_COOKIE_DURATION = timedelta(days=5)
SECRET_KEY = 'fkhgfwyegd,gduk,gicw,ufkeb'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
