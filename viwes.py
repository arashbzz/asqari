from threading import Condition
from flask.templating import render_template
from app import app
import requests
from mod_photo.models import PhotoDb,Temp


@app.route('/')
def index():
    """Python Program to Get IP Address"""

    ip = requests.get('https://api.ipify.org').text

    # query = '103.194.67.94'
    # query = ip
    # url = f"http://ip-api.com/json/{query}"
    # payload = "{\"ips\": [\"1.1.1.1\", \"1.2.3.4\"]}"
    # response_ip = requests.request("POST", url, data=payload)
    # y=response_ip.json()

    """get weathrer condition  """

    key = '53d7f1dde8564a69838135859212907'
    q = ip
    url = f'http://api.weatherapi.com/v1/current.json?key={key}&q={q}&aqi=no'
    response = requests.request("POST", url)

    weather_json=response.json()
    current_temp= weather_json["current"]["temp_c"]

    temps = Temp.query.all()
    for temp in temps:
        if temp.mintemp<current_temp<temp.maxtemp :
            condition = temp
        
    # print (condition.id, condition.photo[0])
    
    # photo =PhotoDb.query.filter((PhotoDb.temp ==8)).first()
    
   
  
   
    return render_template('main.html',weather_json=weather_json, photo= condition.photo[0])

