import os

basedir = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:root@127.0.0.1:3306/shopcarttest?charset=utf8&use_unicode=0'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

JWT_AUTH_URL_RULE = '/account/auth'

