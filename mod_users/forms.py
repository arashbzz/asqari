from flask_wtf.form import FlaskForm
from wtforms import FileField, StringField
from wtforms import validators
from wtforms.validators import DataRequired



class login_form (FlaskForm_):
    user_name= StringField('user_name', validators = [DataRequired()] )
    password  = StringField('password', validators = [DataRequired()] )