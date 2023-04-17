from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import TicketForm
import requests
import serial
import time
from django.http import JsonResponse
from . import ard_sensor as ard
import subprocess
import json



def index(request):
    return render(request, 'index.html')

def booking(request):
    return render(request, 'booking.html')

def schedule(request):
    vaikom = Vaikom.objects.all()
    context = { 'vaikom': vaikom }
    return render(request, 'schedule.html', context)

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
    weather = get_json()
    sensor = ard.getSensorData()
    print(sensor)
    if sensor != None:
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

        'dht': sensor['Temp_Sensor'],
        'ir': sensor['IR_Sensor'],
    }
    else:
        context = {
        'weather': weather['weather'][0]['main'],
        'description': weather['weather'][0]['description'].capitalize(),
        'visibility': weather['visibility'],
        'temp': round(int(weather['main']['temp'])),

        'pressure': weather['main']['pressure'],
        'humidity': weather['main']['humidity'],
        'sea_level': weather['main']['sea_level'],
        'wind': weather['wind']['speed'],

        'dht': 0,
        'ir': 0,
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
    print("now")
    return render(request, 'tracking.html')


def ajax_data(request):
    sensor_json = ard.getSensorData()
    if sensor_json == None:
        sensor_json = {'IR_Sensor': 0, 'Temp_Sensor': 0}
    else:
        IRsensor_value = sensor_json['IR_Sensor']
        DTHsensor = sensor_json['Temp_Sensor']
        obj1 = IRSensorValue.objects.first()
        obj2 = DHTSensorValue.objects.first()
        if obj1:
            obj1.value += IRsensor_value
            obj1.save()
        else:
            IRSensorValue.objects.create(value=IRsensor_value)

        if obj2:
            obj2.temperature = DTHsensor
            obj2.save()
        else:
            DHTSensorValue.objects.create(temperature=DTHsensor)

    print("DB", obj1.value)
    json_data = {'IRsensor_value': obj1.value, 'DTHsensor_value': obj2.temperature}
    print(json_data)
    return JsonResponse(json_data, safe=False, content_type='application/json')


def reset_value(request):
    my_model = IRSensorValue.objects.first() # Get the first instance of the model
    my_model.value = 0 # Reset the value to zero
    my_model.save() # Save the changes to the database
    return dashboard(request)
