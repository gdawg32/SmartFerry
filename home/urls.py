from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.ticket, name='booking'),
    path('schedule/', views.schedule, name='schedule'),
    path('login/', views.login, name='login'),
    path('ticket/', views.ticket, name='ticket'),
    path('dashboard/', views.dashboard, name='dashboard'),
]