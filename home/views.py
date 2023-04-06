from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import TicketForm
import requests




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