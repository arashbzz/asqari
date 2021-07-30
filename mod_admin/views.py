import re
from flask import render_template, redirect , url_for, request,flash
from . import admin
from werkzeug.utils import secure_filename
import uuid

from mod_photo.forms import PhotoUploadingForm , TempForm
from mod_photo.models import PhotoDb , Temp
from app import db

@admin.route('/')
def index():

    return render_template('admin/base.html')

@admin.route('/uploading_photo', methods=['POST', 'GET'])
def upload_photo():

    '''for uploadin a photo to the database, this method also add the kind of photo    '''
    
    form = PhotoUploadingForm()

    choices = Temp.query.all()
    choices= [(choice.id, choice.name )for choice in choices ] 
    form.temp.choices = choices
 
    if request.method == 'POST':
        if not form.validate_on_submit:
            flash ('form is mot validate')
      
        print(dir(form.file.data))
        file_name = f'{uuid.uuid1()}_{secure_filename(form.file.data.filename)}'
        photo = PhotoDb()
        photo.temp = [Temp.query.get(temp_id) for temp_id in form.temp.data]
        photo.filename = file_name

        db.session.add(photo)
        db.session.commit()
        form.file.data.save(f'static/photos/{file_name}')
       

    return render_template('admin/photo_uploading.html', form = form)

@admin.route('/config_temp', methods=['GET', 'POST'])
def config_temp ():
    temps = Temp.query.all()
    form = TempForm()
    if request.method == 'POST':
        if not form.validate_on_submit:
            flash ('form is not validate')
        temp = Temp()
        temp.name =form.name.data
        temp.slug =form.slug.data
        temp.maxtemp =form.maxtemp.data
        temp.mintemp =form.mintemp.data

        db.session.add(temp)
        db.session.commit()
        return redirect(url_for('admin.config_temp'))
    return render_template('admin/config_temp.html', form = form, temps= temps)