from wtforms import FileField, IntegerField, StringField, SelectField
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class PhotoUploadingForm (FlaskForm) :
    file = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    temp = SelectField()

class TempForm(FlaskForm):
    name = StringField( validators=[DataRequired()])
    slug = StringField( validators=[DataRequired()])
    maxtemp = IntegerField(validators=[DataRequired()])
    mintemp = IntegerField(validators=[DataRequired()])
