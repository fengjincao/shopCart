from server import app, lm
from flask import render_template, g, url_for, session,redirect, flash, request
from server.forms import LoginForm
from server.models import User, GoodsList
from flask.ext.login import current_user, login_required, login_user , logout_user
from server.controler import check_login


@app.route('/home')
def home():
    user = {'nickname': 'Allen'}  # fake user
    if g.user is not None:
        return render_template("index.html",
            title='Home',
            user=user)


@app.route('/shopping', methods=['POST','GET'])
def shopping():
    goods = GoodsList.get_all()
    return render_template('shopping.html',
                           goods=goods)


@app.route('/add_shopcart',methods=['POST'])
def add_shopcart():
    return None


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


@app.before_request
def before_request():
    g.user = current_user


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


