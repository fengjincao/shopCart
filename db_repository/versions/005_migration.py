from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
goods_list = Table('goods_list', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('price', String(length=120)),
    Column('total', Integer),
)

shopping = Table('shopping', post_meta,
    Column('goodsid', Integer),
    Column('userid', Integer),
    Column('quantity', Integer, primary_key=True, nullable=False),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['goods_list'].create()
    post_meta.tables['shopping'].create()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['goods_list'].drop()
    post_meta.tables['shopping'].drop()
    post_meta.tables['user'].drop()
