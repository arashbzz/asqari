import re
from flask import render_template, redirect, url_for, request, flash
from . import admin
from werkzeug.utils import secure_filename
import uuid

from mod_photo.forms import PhotoUploadingForm, TempForm
from mod_photo.models import PhotoDb, Temp
from app import db


@admin.route('/')
def index():

    return render_template('admin/index.html')


@admin.route('/uploading_photo', methods=['POST', 'GET'])
def upload_photo():
    '''for uploadin a photo to the database, this method also add the kind of photo    '''

    form = PhotoUploadingForm()
    photoes = PhotoDb.query.all()
    choices = Temp.query.all()
    choices = [(choice.id, choice.name)for choice in choices]
    form.temp.choices = choices

    if request.method == 'POST':
        if not form.validate_on_submit:
            flash('form is mot validate')

        file_name = f'{uuid.uuid1()}_{secure_filename(form.file.data.filename)}'
        photo = PhotoDb()

        # photo.temp =  [Temp.query.get(temp_id) for temp_id in form.temp.data]

        photo.temp.append(Temp.query.get(form.temp.data))

        photo.filename = file_name

        db.session.add(photo)
        db.session.commit()
        form.file.data.save(f'static/photos/{file_name}')

    return render_template('admin/photo_uploading.html', form=form, photoes=photoes)


@admin.route('/config_temp', methods=['GET', 'POST'])
def config_temp():
    temps = Temp.query.all()
    form = TempForm()
    if request.method == 'POST':
        if not form.validate_on_submit:
            flash('form is not validate')
        temp = Temp()
        temp.name = form.name.data
        temp.slug = form.slug.data
        temp.maxtemp = form.maxtemp.data
        temp.mintemp = form.mintemp.data

        db.session.add(temp)
        db.session.commit()
        return redirect(url_for('admin.config_temp'))
    return render_template('admin/config_temp.html', form=form, temps=temps)


@admin.route('/config_temp/delete_item/<int:temp_id>', methods=['GET', 'POST'])
def delete_temp(temp_id):
    selected_temp = Temp.query.filter(Temp.id == temp_id).first()
    db.session.delete(selected_temp)
    db.session.commit()
    return redirect(url_for('admin.config_temp'))


@admin.route('/config_temp/edit_item/<int:temp_id>', methods=['GET', 'POST'])
def edit_temp(temp_id):
    temps = Temp.query.all()
    selected_temp = Temp.query.get_or_404(temp_id)
    form = TempForm(obj=selected_temp)
    if request.method == 'POST':
        if not form.validate_on_submit:
            return render_template('admin/edit_temp.html', form=form, temps=temps)

        selected_temp.name = form.name.data
        selected_temp.slug = form.slug .data
        selected_temp.maxtemp = form.maxtemp.data
        selected_temp.mintemp = form.mintemp.data

        db.session.commit()
        # return redirect(url_for('admin.config_temp'))

    return render_template('admin/edit_temp.html', form=form, temps=temps, temp=selected_temp)


@admin.route('/uploading_photo/search', methods=['GET'])
def photo_search():
    form = PhotoUploadingForm()
    form.temp.choices = [(choice.id, choice.name)for choice in Temp.query.all()]    
    search = request.args.get('chara')
    search = "%{}%".format(search)
    print(search)
    photoes = PhotoDb.query.filter(PhotoDb.filename.like(search)).all()

    return render_template('admin/photo_uploading.html', photoes=photoes, form=form)


@admin.route('/uploading_photo/filtering', methods=['GET'])
def photo_filtering():
    form = PhotoUploadingForm()
    form.temp.choices = [(choice.id, choice.name)for choice in Temp.query.all()]
    
    search = request.args.get('temp')
    photoes=[]
    for photo in PhotoDb.query.all():
        if photo.temp[0].id == int(search):
            print(photo.temp[0].id,search)
            photoes.append(photo)

    # print(search, PhotoDb.query.all())
    # photoes = PhotoDb.query.filter(
    #     (photo.temp[0].id for photo in PhotoDb.query.all()) == search).all()
    print(photoes)
    return render_template('admin/photo_uploading.html', photoes=photoes, form=form)
