from sqlalchemy.exc import IntegrityError
from models import User
from server import db


def check_login(nickname):
    if nickname is None:
        return False
    user = User(nickname=nickname,)
    db.session.add(user)
    try:
        db.session.commit()
    except:
        db.session.rollback()
        return False
    return True

