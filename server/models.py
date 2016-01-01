from core import db


class GoodsList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    price = db.Column(db.String(120), index=True, unique=False)

    @staticmethod
    def get_all():
        return GoodsList.query.all()

    def __repr__(self):
        return '<GoodsList %s>' % self.name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)

    def get_id(self):
        return unicode(self.id)


class Shopping(db.Model):
    goodsid = db.Column(db.Integer, db.ForeignKey(GoodsList.id))
    userid = db.Column(db.Integer, db.ForeignKey(User.id))
    quantity = db.Column(db.Integer, primary_key=True)
