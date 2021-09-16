from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        if city != "":
            res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=cd1fd11566de202d496f0f0700892eb9').read()
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data["sys"]["country"]),
                "temp": str(int((int(json_data["main"]["temp"]) - 273.15))) + 'dC',
                "des_temp": str(json_data["weather"][0]["description"]),
                "humidity": str(json_data["main"]["humidity"]),
                "wind_speed": str(json_data["wind"]["speed"]),
            }
        else:
            city = ''
            data = {}
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})