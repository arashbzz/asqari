#!/bin/bash
flask db stamp
python app.py db upgrade
flask db init
flask db migrate
flask db upgrade
gunicorn -b 0.0.0.0:80 -w 2 app:app