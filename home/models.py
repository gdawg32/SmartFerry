from django.db import models

# Create your models here.

class Vaikom(models.Model):
    time = models.CharField(max_length=100)
    departure = models.CharField(max_length=100)
    arrival = models.CharField(max_length=100)
    time_format = models.CharField(max_length=100)

    def __str__(self):
        return self.time

class Ticket(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    departure_port = models.CharField(max_length=255)
    arrival_port = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    num_passengers = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return self.name
    
class IRSensorValue(models.Model):
    value = models.IntegerField()

class DHTSensorValue(models.Model):
    temperature = models.IntegerField()