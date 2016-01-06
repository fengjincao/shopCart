from server import app, lm
from flask import render_template, g, url_for, session,redirect, flash, request
from server.forms import LoginForm
from server.models import User, GoodsList ,Shopping
from flask.ext.login import current_user, login_required, login_user , logout_user
from server.controler import check_login


@app.route('/home')
def home():

    user = User.get_user_by_name(session['nickname'])
    user = {'nickname': user.nickname}  # fake user
    if g.user is not None:
        return render_template("index.html",
            title='Home',
            user=user)


@app.route('/shopping', methods=['POST', 'GET'])
def shopping():
    goods = GoodsList.get_all()
    return render_template('shopping.html',
                           goods=goods)


@app.route('/goodspage/<int:good_id>', methods=['POST', "GET"])
def goodspage(good_id):
    goods = GoodsList.get_id(good_id)
    user = User.get_user_by_name(session['nickname'])
    userid = user.id
    return render_template('goodspage.html', goods=goods, userid=userid)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    # if g.user is not None:
    #     return redirect(url_for('home'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit() and check_login(form.nick.data):
            session['nickname'] = form.nick.data
            flash(form.nick.data+"login successfuly")
            return redirect('/home')
    return render_template('login.html',
                           title='Login',
                           error='Please input an unused nickname!',
                           form=form)


@app.route('/add_shop_cart', methods=['POST'])
def add_shop():
    goods_id = request.form['goods_id']
    user_id = request.form['user_id']
    quantity = request.form['quantity']
    user_id2 = current_user
    Shopping.insert_shopcart(goods_id, user_id, quantity)

    shop_items = Shopping.get_all(user_id)
    view_lists = []
    for shop_item in shop_items:
        goodsitem = GoodsList.get_id(shop_item.goodsid)
        view_item = {'quantity': shop_item.quantity,
                    'goods_id': goodsitem.id,
                    'goods_price':goodsitem.price,
                    'goods_name': goodsitem.name,
                    'total_money': int(shop_item.quantity)*int(goodsitem.price)}
        view_lists.append(view_item)
    return render_template('shopcart.html', shopitems=view_lists, username=session['nickname'])


@app.before_request
def before_request():
    g.user = current_user


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


