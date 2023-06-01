from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.ticket, name='booking'),
    path('schedule/', views.schedule, name='schedule'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('ticket/', views.ticket, name='ticket'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tracking/', views.tracking, name='tracking'),
    path('ajax_data/', views.ajax_data, name='ajax_data'),
    path('reset_value/', views.reset_value, name='reset_value'),
]