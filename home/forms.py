from django import forms
from .models import Ticket
import re
from datetime import date, time, datetime



class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['name', 'email', 'phone', 'departure_port', 'arrival_port', 'date', 'time', 'num_passengers', 'comments']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'border rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Email', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'border rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Phone', 'type': 'tel', 'required': True}),
            'departure_port': forms.Select(attrs={'class': 'border rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Departure Port', 'required': True}, choices=[('Vaikom', 'Vaikom'), ('Thavanakadavu', 'Thavanakadavu')]),
            'arrival_port': forms.Select(attrs={'class': 'border rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Arrival Port', 'required': True}, choices=[('Vaikom', 'Vaikom'), ('Thavanakadavu', 'Thavanakadavu')]),
            'date': forms.DateInput(attrs={'class': 'border rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Date', 'type': 'date', 'min': date.today().strftime('%Y-%m-%d'), 'required': True}),
            'time': forms.TimeInput(attrs={'class': 'border rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Time', 'type': 'time', 'min': datetime.now().strftime('%H:%M'), 'required': True}),
            'num_passengers': forms.NumberInput(attrs={'class': 'border rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'No. of Passengers', 'required': True}),
            'comments': forms.Textarea(attrs={'class': 'border rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent', 'placeholder': 'Comments', 'rows': 4, 'required': False}),
        }

    def clean(self):
        cleaned_data = super().clean()
        departure_port = cleaned_data.get('departure_port')
        arrival_port = cleaned_data.get('arrival_port')
        phone = cleaned_data.get('phone')

        if departure_port == arrival_port:
            self.add_error('departure_port', 'The departure and arrival ports cannot be the same.')
        
        if phone and not re.match(r'^\+?\d{10,12}$', phone):
            self.add_error('phone', 'Please enter a valid phone number')

        

        return cleaned_data
