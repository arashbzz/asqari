from sqlalchemy import Column, Integer, String, Table, ForeignKey
from app import db

photo_temp = Table('photo_temp', db.metadata,
                          Column('photo_id', ForeignKey('photo.id', ondelete='cascade')),
                          Column('temp_id', ForeignKey('temp.id', ondelete='cascade'))
                          )


class PhotoDb (db.Model):
    __tablename__ = 'photo'
    id = Column(Integer(), primary_key=True)
    description = Column(String(128), nullable=True)
    filename = Column(String(128), nullable=False, unique=False)
    temp = db.relationship("Temp",
                    secondary=photo_temp, back_populates='photo')


class Temp (db.Model):
    __tablename__ = 'temp'
    id = Column(Integer(), primary_key=True)
    name = Column(String(32), nullable=False, unique=False)
    slug = Column(String(32), nullable=False, unique=False)
    maxtemp = Column(Integer(), nullable=False, unique=False)
    mintemp = Column(Integer(), nullable=False, unique=False)
    photo = db.relationship("PhotoDb",
                    secondary=photo_temp, back_populates='temp')
