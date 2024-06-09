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
    bus_list = Bus.objects.all()
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


# # views.py
# from django.shortcuts import render
# from .models import ActualFrequency, Route
# from .forms import SearchForm
#
#
# def search(request):
#     form = SearchForm(request.GET or None)
#     results = []
#
#     if form.is_valid():
#         driving_date = form.cleaned_data.get('driving_date')
#         jurisdiction_unit = form.cleaned_data.get('jurisdiction_unit')
#         route_number = form.cleaned_data.get('route_number')
#         outbound_return = form.cleaned_data.get('outbound_return')
#
#         # Query the ActualFrequency model
#         frequencies = ActualFrequency.objects.all()
#
#         if driving_date:
#             frequencies = frequencies.filter(driving_date=driving_date)
#         if jurisdiction_unit:
#             frequencies = frequencies.filter(jurisdiction_unit=jurisdiction_unit)
#         if route_number:
#             frequencies = frequencies.filter(route_number=route_number)
#         if outbound_return:
#             frequencies = frequencies.filter(outbound_return=outbound_return)
#
#         # Combine data from Route model
#         for freq in frequencies:
#             route = Route.objects.filter(
#                 jurisdiction_unit=freq.jurisdiction_unit,
#                 route_number=freq.route_number,
#                 outbound_return=freq.outbound_return
#             ).first()
#
#             if route:
#                 results.append({
#                     'driving_date': freq.driving_date,
#                     'departure_time': freq.departure_time,
#                     'driving_week': freq.driving_week,
#                     'jurisdiction_unit': freq.jurisdiction_unit,
#                     'route_number': freq.route_number,
#                     'outbound_return': freq.outbound_return,
#                     'starting_point_x': route.starting_point_x,
#                     'starting_point_y': route.starting_point_y,
#                     'destination_x': route.destination_x,
#                     'destination_y': route.destination_y,
#                     'driver_id': freq.driver_id,
#                     'vehicle_license_plate': freq.vehicle_license_plate,
#                 })
#
#     context = {
#         'form': form,
#         'results': results
#     }
#
#     return render(request, 'search.html', context)


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