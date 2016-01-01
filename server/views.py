from core import app,db,jwt
from flask import render_template, g, url_for, session,redirect, flash, request ,jsonify
from flask_jwt import current_identity, jwt_required
from server.forms import LoginForm
from server.models import User, GoodsList
from server.controler import check_login


@app.route('/home')
@jwt_required()
def home():
    user = {'nickname': 'Allen'}  # fake user
    if g.user is not None:
        return render_template("index.html",
            title='Home',
            user=user)


@app.route('/shopping')
@jwt_required()
def shopping():
    goods = GoodsList.get_all()
    return render_template('shopping.html',
                           goods=goods)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    # if g.user is not None:
    #     return redirect(url_for('home'))
    form = LoginForm()
    if request.method == 'POST':
        if check_login(form.nick.data):
            session['nickname'] = form.nick.data
            flash(form.nick.data+"login successfuly")
            return redirect('/home')
    return render_template('login.html',
                           title='Login',
                           error='Please input an unused nickname!',
                           form=form)


@app.before_request
def before_request():
    g.user = current_identity


def auth_request_handler():
    username = request.form['name']
    user = User.query.filter(User.username == username).first()
    if not user:
        return ''
    access_token = jwt.jwt_encode_callback(user)
    data = {
        'access_token': access_token.encode('utf-8'),
    }
    return jsonify(**data)
