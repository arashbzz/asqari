from flask import Blueprint

photo = Blueprint('photo', __name__, url_prefix='/photo/')


from .models import PhotoDb, Temp