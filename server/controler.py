from models import User
from core import db


def check_login(nickname):
    if nickname is None:
        return False
    user = User(nickname=nickname,)
    db.session.add(user)
    try:
        db.session.commit()
    except Exception as e:
        return False
    return True

