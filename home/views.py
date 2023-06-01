from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import TicketForm
import requests
from . import sms
from django.http import JsonResponse
import time




def index(request):
    return render(request, 'index.html')

def booking(request):
    return render(request, 'booking.html')

def schedule(request):
    vaikom = Vaikom.objects.all()
    context = { 'vaikom': vaikom }
    return render(request, 'schedule.html', context)

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form': TicketForm(),
                'success_message': 'Your booking has been successful!'
            }
        else:
            print(form.errors)
            context = {
                'form': form,
            }
            
    else:
        context = {
            'form': TicketForm(),
        }

    return render(request, 'ticket.html', context)

def dashboard(request):
    weather = get_json() # Get the data from OpenWeatherMap API
    #sensor = ard.getSensorData() # Get the data from Arduino
    
    #ir = ard.getIRSensorData()
    context = {
    'weather': weather['weather'][0]['main'],
    'description': weather['weather'][0]['description'].capitalize(),
    'visibility': weather['visibility'],
    'temp': round(int(weather['main']['temp'])),

    'pressure': weather['main']['pressure'],
    'humidity': weather['main']['humidity'],
    'sea_level': weather['main']['sea_level'],
    'wind': weather['wind']['speed'],

}
    return render(request, 'dashboard.html', context)


def get_json():
    API_KEY = "cd73fce3c747985dfb804f5efab52268"
    ZIP = 686141
    COUNTRY = "IN"
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={ZIP},{COUNTRY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    # Store the data from API
    json_data = response.json()
    return json_data

def tracking(request):
    return render(request, 'tracking.html')


def ajax_data(request):
    sensor_json = get_sensor_value()
    print(sensor_json)
    if sensor_json == None:
        json_data = {'IRsensor_value': 0, 'DTHsensor_value': 0}
        print(json_data)
        return JsonResponse(json_data, safe=False, content_type='application/json')
    else:
        DTHsensor = int(sensor_json['V1'])
        IRsensor_value = int(sensor_json['V2'])
        
        if int(DTHsensor) > 25:
            last_sms_time = request.session.get('last_sms_time', 0)
            cooldown_time = 2 * 60  # 2 minutes in seconds
            current_time = time.time()
            if current_time - last_sms_time > cooldown_time:
                sms.send_sms()
                print("SMS sent")
                request.session['last_sms_time'] = current_time
                request.session.save()  # Save the session after modifying it


        json_data = {'IRsensor_value': IRsensor_value, 'DTHsensor_value': DTHsensor}
        print(json_data)
        return JsonResponse(json_data, safe=False, content_type='application/json')


def reset_value(request):
    url = 'https://blr1.blynk.cloud/external/api/update?token=91WF7MrryhttcaAhOKW62ylGe9o-40cb&V2=0'
    response = requests.get(url)
    if response.status_code == 200:
        print('reset successful')
    return dashboard(request)


def get_sensor_value():
    url = 'https://blr1.blynk.cloud/external/api/get?token=91WF7MrryhttcaAhOKW62ylGe9o-40cb&V1&V2&V3&V4'
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        print('Error:', response.status_code)
        return None