from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class LoginForm(Form):
    nick = StringField('nickname', validators=[DataRequired()])



