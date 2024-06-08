from django.shortcuts import render
from traffic.models import Bus
import json

# Create your views here.

from .models import Bus
from .models import HistoricalArrivals
from .models import AppointmentForm
from django.shortcuts import render,redirect
from django.http import HttpResponse





def index(request):
    # 从数据库中获取所有 Bus 对象的列表
    bus_list = Bus.objects.all()
    # 将 bus_list 传递给模板
    return render(request, "index.html", {"bus_list": bus_list})

def search(request):
    filters = {}
    possible_filters = ['arrival_time', 'departure_time', 'driving_week', 'outbound_return', 'route_number']

    for filter in possible_filters:
        value = request.GET.get(filter)
        if value:
            filters[filter] = value

    HistoricalArrivals_list = HistoricalArrivals.objects.filter(**filters)

    return render(request, 'search.html', {
        'HistoricalArrivals_list': HistoricalArrivals_list,
        'arrival_times': HistoricalArrivals.objects.values_list('arrival_time', flat=True).distinct(),
        'departure_times': HistoricalArrivals.objects.values_list('departure_time', flat=True).distinct(),
        'driving_weeks': HistoricalArrivals.objects.values_list('driving_week', flat=True).distinct(),
        'outbound_returns': HistoricalArrivals.objects.values_list('outbound_return', flat=True).distinct(),
        'route_numbers': HistoricalArrivals.objects.values_list('route_number', flat=True).distinct(),
    })

def lover(request):
    filters = {}
    possible_filters = ['arrival_time', 'departure_time', 'driving_week', 'outbound_return', 'route_number']

    for filter in possible_filters:
        value = request.GET.get(filter)
        if value:
            filters[filter] = value

    HistoricalArrivals_list = HistoricalArrivals.objects.filter(**filters)

    return render(request, 'lover.html', {
        'HistoricalArrivals_list': HistoricalArrivals_list,
        'arrival_times': HistoricalArrivals.objects.values_list('arrival_time', flat=True).distinct(),
        'departure_times': HistoricalArrivals.objects.values_list('departure_time', flat=True).distinct(),
        'driving_weeks': HistoricalArrivals.objects.values_list('driving_week', flat=True).distinct(),
        'outbound_returns': HistoricalArrivals.objects.values_list('outbound_return', flat=True).distinct(),
        'route_numbers': HistoricalArrivals.objects.values_list('route_number', flat=True).distinct(),
    })


def login(request):
    if request.method == 'POST':
            return redirect('booking')
    else:
        form = AppointmentForm()
    return render(request, 'login.html')

def booking(request):
    return render(request, 'booking.html')

def systemLogin (request):
        return render(request, 'systemLogin.html')


def system(request):
    return render(request, 'system.html')