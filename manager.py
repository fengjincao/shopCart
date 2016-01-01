# manage.py

from flask.ext.script import Manager, prompt_bool

from core import app, db

manager = Manager(app)


@manager.command
def hello():
    print "hello"


@manager.command
def drop():
    """Drops database tables"""
    if prompt_bool("Are you sure you want to lose all your data"):
        db.drop_all()


@manager.command
def create():
    """Creates database tables from sqlalchemy models"""
    db.create_all()


@manager.command
def recreate():
    """Recreates database tables (same as issuing 'drop' and then 'create')"""
    drop()
    create()

if __name__ == "__main__":
    manager.run()
