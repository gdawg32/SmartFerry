from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import TicketForm




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
    return render(request, 'dashboard.html')