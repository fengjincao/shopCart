from server import db
from sqlalchemy.exc import IntegrityError
from flask.ext.login import current_user


class GoodsList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    price = db.Column(db.String(120), index=True, unique=False)

    @staticmethod
    def get_all():
        return GoodsList.query.all()

    @staticmethod
    def get_id(id):
        return GoodsList.query.get(id)

    def __repr__(self):
        return '<GoodsList %s>' % (self.name)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)

    @staticmethod
    def get_user_by_id(rid):
        user = User.query.get(rid)
        return user

    @staticmethod
    def get_user_by_name(username):
        user = User.query.filter(db.text("nickname=:name")).params(name=username).first()
        return user


    def get_id(self):
        return unicode(self.id)


class Shopping(db.Model):
    goodsid = db.Column(db.Integer, db.ForeignKey(GoodsList.id), primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey(User.id), primary_key=True)
    quantity = db.Column(db.Integer)

    @staticmethod
    def insert_shopcart(goods_id, user_id, quantity):
        shop_item = Shopping(goodsid=goods_id, userid=user_id , quantity=quantity)
        db.session.add(shop_item)
        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            old_shop_item = db.session.query(Shopping).filter('goodsid =:goods_id and userid=:user_id').params(goods_id=int(goods_id), user_id=int(user_id)).first()
            old_shop_item.quantity += int(quantity)
            db.session.commit()

    @staticmethod
    def get_all(user_id):
        all_shopping = db.session.query(Shopping).filter(db.text(" userid=:user_id")).params(user_id=int(user_id)).all()
        return all_shopping

