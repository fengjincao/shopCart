from datetime import datetime

from flask import Flask,current_app
from flask.ext.sqlalchemy import SQLAlchemy
from flask_jwt import JWT


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db = SQLAlchemy(app)
    jwt = JWT()

    import core
    core.app = app
    core.db = db
    from server.models import User
    from server.views import auth_request_handler

    def jwt_payload_handler(user):
        iat = datetime.utcnow()
        exp = iat + current_app.config.get('JWT_EXPIRATION_DELTA')
        nbf = iat + current_app.config.get('JWT_NOT_BEFORE_DELTA')
        return {'exp': exp, 'iat': iat, 'nbf': nbf, 'identity': user.id}

    def identity(payload):
        user = User.query.get(payload['identity'])
        return user

    jwt.identity_callback = identity
    jwt.auth_request_callback = auth_request_handler
    jwt.jwt_payload_callback = jwt_payload_handler

    jwt.init_app(app)
    core.jwt = jwt

    from server import views, models
    return app



