"""
URL configuration for Bus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from traffic.views import index, search, login, booking,lover,systemLogin,system,person,route,schedule,station,bus,properson,probus,proschedule,prohistory,system2,system3,system1,bookingHistory,bookingBus,bookingStation,delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('search/', search, name='search'),
    path('login/', login, name='login'),
    path('booking/', booking, name='booking'),
    path('bookingHistory/', bookingHistory, name='bookingHistory'),
    path('bookingBus/', bookingBus, name='bookingBus'),
    path('bookingStation/', bookingStation, name='bookingStation'),
    path('lover/', lover, name='lover'),
    path('systemLogin/', systemLogin, name='systemLogin'),
    path('system/', system, name='system'),
    path('system1/', system1, name='system1'),
    path('system2/', system2, name='system2'),
    path('system3/', system3, name='system3'),
    path('person/', person, name='person'),
    path('route/', route, name='route'),
    path('schedule/', schedule, name='schedule'),
    path('station/', station, name='station'),
    path('bus/', bus, name='bus'),
    path('properson/', properson, name='properson'),
    path('probus/', probus, name='probus'),
    path('proschedule/', proschedule, name='proschedule'),
    path('prohistory/', prohistory, name='prohistory'),
    path('delete/<int:appointment_id>/', delete, name='delete'),

]