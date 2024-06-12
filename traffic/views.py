
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import requests
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Passenger

from urllib.parse import quote
from urllib.parse import unquote



def replace_percent_sign(value):
    return ''.join('%25' if char == '%' else char for char in value)

def index(request):
    return render(request, "index.html")
def route(request):
    if request.method == 'GET':
        # 獲取查詢參數
        route_number = request.GET.get('routeNumber')
        start_station = request.GET.get('startStation')
        via_station = request.GET.get('dockStation')
        end_station = request.GET.get('endStation')

        # 設置請求參數，過濾掉空值
        from urllib.parse import quote

        params = {}
        if route_number:
            params['routeNumber'] = route_number
        if start_station:
            # start_station = quote(start_station)
            # start_station = '%25'+start_station+'%25'
            params['startStation'] = start_station
        if via_station:
            params['dockStation'] = via_station
        if end_station:
            params['endStation'] = end_station

        print(f"Params: {params}")

        try:
            # 如果沒有任何查詢參數，則不傳遞任何參數，獲取所有數據
            if not params:
                response = requests.get('http://0.0.0.0:8080/route')
            else:
                response = requests.get('http://0.0.0.0:8080/route', params=params)

            response.raise_for_status()  # 檢查HTTP響應是否返回錯誤

            # 解析Ktor API返回的JSON數據
            routes = response.json()

            # 打印解析後的JSON數據以便調試
            print(f"Parsed Routes: {routes}")

            # 準備要傳遞到模板的數據
            processed_routes = []
            for route in routes:
                processed_route = {
                    'jurisdiction': route.get('jurisdictionUnit'),
                    'route_number': route.get('routeNumber'),
                    'direction': route.get('outboundReturn'),
                    'start_station': route.get('startStation'),
                    'end_station': route.get('endStation')
                }
                processed_routes.append(processed_route)

            # 將數據傳遞到模板並渲染
            return render(request, 'route.html', {'routes': processed_routes})

        except requests.RequestException as e:
            # 打印異常以便調試
            print(f"Failed to fetch data from Ktor API: {str(e)}")
            return JsonResponse({'error': f'Failed to fetch data from Ktor API: {str(e)}'}, status=500)
    else:
        return render(request, 'search.html')

def schedule(request):
    if request.method == 'GET':
        # 獲取查詢參數
        routeNumber = request.GET.get('route_number')
        outboundReturn = request.GET.get('outbound_return')
        drivingWeek = request.GET.get('driving_week')

        print(f"Route Number: {routeNumber}")
        # 設置請求參數
        params = {}
        if routeNumber:
            params['routeNumber'] = routeNumber
        if outboundReturn:
            params['outboundReturn'] = outboundReturn
        if drivingWeek:
            params['drivingWeek'] = drivingWeek

        print(f"Params: {params}")

        try:
            if not params:
                response = requests.get('http://0.0.0.0:8080/schedule')
            else:
                response = requests.get('http://0.0.0.0:8080/schedule', params=params)

            response.raise_for_status()  # 檢查HTTP響應是否返回錯誤

            # 解析 Ktor API 返回的 JSON 數據
            actual_frequencies = response.json()
            print(f"Parsed Actual Frequencies: {actual_frequencies}")

            # 準備要傳遞到模板的數據


            # 將數據傳遞到模板並渲染
            return render(request, 'schedule.html', {'actual_frequencies': actual_frequencies})

        except requests.RequestException as e:
            # 打印異常以便調試
            print(f"Failed to fetch data from Ktor API: {str(e)}")
            return JsonResponse({'error': f'Failed to fetch data from Ktor API: {str(e)}'}, status=500)
    else:
        return render(request, 'search.html')

def station(request):
    if request.method == 'GET':
        # 獲取查詢參數
        routeNumber = request.GET.get('routeNumber')
        stationName = request.GET.get('stationName')
        outboundReturn = request.GET.get('outboundReturn')

        # 設置請求參數
        params = {}
        if routeNumber:
            params['routeNumber'] = routeNumber
        if stationName:
            params['stationName'] = stationName
        if outboundReturn:
            params['outboundReturn'] = outboundReturn

        print(f"Params: {params}")

        try:
            if not params:
                response = requests.get('http://0.0.0.0:8080/station')
            else:
                response = requests.get('http://0.0.0.0:8080/station', params=params)

            response.raise_for_status()  # 檢查HTTP響應是否返回錯誤

            # 解析 Ktor API 返回的 JSON 數據
            stations = response.json()
            print(f"Parsed Stations: {stations}")

            # 準備要傳遞到模板的數據
            processed_stations = []
            for station in stations:
                processed_station = {
                    'station_name': station.get('stationName'),
                    'road_name': station.get('roadName')
                }
                processed_stations.append(processed_station)

            # 將數據傳遞到模板並渲染
            return render(request, 'station.html', {'stations': processed_stations})

        except requests.RequestException as e:
            # 打印異常以便調試
            print(f"Failed to fetch data from Ktor API: {str(e)}")
            return JsonResponse({'error': f'Failed to fetch data from Ktor API: {str(e)}'}, status=500)
    else:
        return render(request, 'search.html')

def bus(request):
    if request.method == 'GET':
        # 獲取查詢參數
        route_number = request.GET.get('route_number')
        start_date = request.GET.get('start_station')
        start_time = request.GET.get('via_station')
        if start_time is not None:
            start_time = start_time.replace('%3A', ':')
            start_time = start_time + ":00"
        outbound_return = request.GET.get('outbound_return')
        # 設置請求參數
        params = {}
        if route_number:
            params['routeNumber'] = route_number
        if start_date:
            params['drivingDate'] = start_date
        if start_time:
            params['departureTime'] = start_time
        if outbound_return:
            params['outboundReturn'] = outbound_return

        print(f"Params: {params}")

        try:
            if not params:
                response = requests.get('http://0.0.0.0:8080/simple_bus')
            else:
                response = requests.get('http://0.0.0.0:8080/simple_bus', params=params)

            response.raise_for_status()  # 檢查HTTP響應是否返回錯誤

            # 解析 Ktor API 返回的 JSON 數據
            buses = response.json()
            print(f"Parsed Buses: {buses}")

            # 準備要傳遞到模板的數據
            processed_buses = []
            for bus in buses:
                processed_bus = {
                    'license': bus.get('licensePlate')
                }
                processed_buses.append(processed_bus)

            # 將數據傳遞到模板並渲染
            return render(request, 'bus.html', {'buses': processed_buses})

        except requests.RequestException as e:
            # 打印異常以便調試
            print(f"Failed to fetch data from Ktor API: {str(e)}")
            return JsonResponse({'error': f'Failed to fetch data from Ktor API: {str(e)}'}, status=500)
    else:
        return render(request, 'search.html')

def probus(request):
    if request.method == 'GET':
        # 獲取查詢參數
        license_plate = request.GET.get('route_number')  # route_number here is used to capture the license plate number


        # 設置請求參數
        params = {}
        if license_plate:
            params['license'] = license_plate


        print(f"Params: {params}")

        try:
            if not params:
                response = requests.get('http://0.0.0.0:8080/bus')
            else:
                response = requests.get('http://0.0.0.0:8080/bus', params=params)

            response.raise_for_status()  # 檢查HTTP響應是否返回錯誤

            # 解析 Ktor API 返回的 JSON 數據
            buses = response.json()
            print(f"Parsed Buses: {buses}")

            # 準備要傳遞到模板的數據
            processed_buses = []
            for bus in buses:
                processed_bus = {
                    'license': bus.get('license'),
                    'brand': bus.get('brand'),
                    'carLength': bus.get('carLength'),
                    'lowFloor': bus.get('lowFloor'),
                    'wheelChairUse': bus.get('wheelChairUse'),
                    'numberOfSeats': bus.get('numberOfSeats'),
                    'typeAorTypeB': bus.get('typeAorTypeB'),
                    'manualGearBox': bus.get('manualGearBox'),
                    'displacement': bus.get('displacement'),
                    'maxHorsePower': bus.get('maxHorsePower'),
                    'maxTorque': bus.get('maxTorque')

                }
                processed_buses.append(processed_bus)

            # 將數據傳遞到模板並渲染
            return render(request, 'probus.html', {'buses': processed_buses})

        except requests.RequestException as e:
            # 打印異常以便調試
            print(f"Failed to fetch data from Ktor API: {str(e)}")
            return JsonResponse({'error': f'Failed to fetch data from Ktor API: {str(e)}'}, status=500)
    else:
        return render(request, 'search.html')

def prohistory(request):
    if request.method == 'GET':
        # 獲取查詢參數
        route_number = request.GET.get('route_number')
        driving_date = request.GET.get('start_station')
        outbound_return = request.GET.get('outbound_return')

        # 設置請求參數
        params = {}
        if route_number:
            params['routeNumber'] = route_number
        if driving_date:
            params['drivingDate'] = driving_date
        if outbound_return:
            params['outboundReturn'] = outbound_return

        print(f"Params: {params}")

        try:
            response = requests.get('http://0.0.0.0:8080/historical_arrival', params=params)
            response.raise_for_status()  # 檢查HTTP響應是否返回錯誤

            # 解析 Ktor API 返回的 JSON 數據
            historical_arrivals = response.json()

            # 準備要傳遞到模板的數據
            processed_arrivals = []
            for arrival in historical_arrivals:
                processed_arrival = {
                    'driving_date': arrival.get('drivingDate'),
                    'station_name': arrival.get('stationName'),
                    'arrival_time': arrival.get('arrivalTime'),
                }
                processed_arrivals.append(processed_arrival)

            # 將數據傳遞到模板並渲染
            return render(request, 'prohistory.html', {'arrivals': processed_arrivals})

        except requests.RequestException as e:
            # 打印異常以便調試
            print(f"Failed to fetch data from Ktor API: {str(e)}")
            return JsonResponse({'error': f'Failed to fetch data from Ktor API: {str(e)}'}, status=500)
    else:
        return render(request, 'search.html')

def proschedule(request):
    if request.method == 'GET':
        # 獲取查詢參數
        route_number = request.GET.get('route_number')
        driving_date = request.GET.get('start_station')
        departure_time = request.GET.get('via_station')
        if departure_time is not None:
            departure_time = departure_time.replace('%3A', ':')
            departure_time = departure_time + ":00"
        outbound_return = request.GET.get('outbound_return')

        # 設置請求參數
        params = {}
        if route_number:
            params['routeNumber'] = route_number
        if driving_date:
            params['drivingDate'] = driving_date
        if departure_time:
            params['departureTime'] = departure_time
        if outbound_return:
            params['outboundReturn'] = outbound_return

        print(f"Params: {params}")

        try:
            if not params:
                response = requests.get('http://0.0.0.0:8080/full_bus')
            else:
                response = requests.get('http://0.0.0.0:8080/full_bus', params=params)

            response.raise_for_status()  # 檢查HTTP響應是否返回錯誤

            # 解析 Ktor API 返回的 JSON 數據
            buses = response.json()
            print(f"Parsed Buses: {buses}")

            # 準備要傳遞到模板的數據
            processed_buses = []
            for bus in buses:
                processed_bus = {
                    'license': bus.get('license'),
                    'brand': bus.get('brand'),
                    'carLength': bus.get('carLength'),
                    'lowFloor': bus.get('lowFloor'),
                    'wheelChairUse': bus.get('wheelChairUse'),
                    'numberOfSeats': bus.get('numberOfSeats'),
                    'typeAorTypeB': bus.get('typeAorTypeB'),
                    'manualGearBox': bus.get('manualGearBox'),
                    'displacement': bus.get('displacement'),
                    'maxHorsePower': bus.get('maxHorsePower'),
                    'maxTorque': bus.get('maxTorque'),
                }
                processed_buses.append(processed_bus)

            # 將數據傳遞到模板並渲染
            return render(request, 'proschedule.html', {'buses': processed_buses})

        except requests.RequestException as e:
            # 打印異常以便調試
            print(f"Failed to fetch data from Ktor API: {str(e)}")
            return JsonResponse({'error': f'Failed to fetch data from Ktor API: {str(e)}'}, status=500)
    else:
        return render(request, 'search.html')

def system(request):
    if request.method == 'GET':
        # 獲取查詢參數
        drivingDate = request.GET.get('drivingDate')
        route_number = request.GET.get('route_number')

        # 設置請求參數
        params = {}
        if drivingDate:
            params['drivingDate'] = drivingDate
        if route_number:
            params['routeNumber'] = route_number
        print(f"Params: {params}")

        try:
            if not params:
                response = requests.get('http://0.0.0.0:8080/vmrs')
            else:
                response = requests.get('http://0.0.0.0:8080/vmrs', params=params)

            response.raise_for_status()  # 檢查HTTP響應是否返回錯誤

            # 解析 Ktor API 返回的 JSON 數據
            buses = response.json()
            print(f"Parsed Buses: {buses}")

            # 準備要傳遞到模板的數據
            processed_buses = []
            for bus in buses:
                processed_bus = {
                    'maintenanceDate': bus.get('maintenanceDate'),
                    'shop': bus.get('shop'),
                    'maintenanceLevel': bus.get('maintenanceLevel'),
                    'personnel': bus.get('personnel'),
                    'license': bus.get('license'),
                }
                processed_buses.append(processed_bus)

            # 將數據傳遞到模板並渲染
            return render(request, 'system.html', {'buses': processed_buses})

        except requests.RequestException as e:
            # 打印異常以便調試
            print(f"Failed to fetch data from Ktor API: {str(e)}")
            return JsonResponse({'error': f'Failed to fetch data from Ktor API: {str(e)}'}, status=500)
    else:
        return render(request, 'search.html')


def system1(request):
    if request.method == 'GET':
        # 獲取查詢參數
        drivingDate = request.GET.get('drivingDate')
        # 設置請求參數
        params = {}
        if drivingDate:
            params['drivingDate'] = drivingDate

        print(f"Params: {params}")

        try:
            if not params:
                response = requests.get('http://0.0.0.0:8080/unused_bus')
            else:
                response = requests.get('http://0.0.0.0:8080/unused_bus', params=params)
            response.raise_for_status()  # 檢查HTTP響應是否返回錯誤

            # 解析 Ktor API 返回的 JSON 數據
            buses = response.json()
            print(f"Parsed Buses: {buses}")
            processed_buses = []
            for bus in buses:
                processed_bus = {
                    'licensePlate': bus.get('licensePlate'),
                }
                processed_buses.append(processed_bus)
            return render(request, 'system1.html', {'buses': processed_buses})
        except requests.RequestException as e:
            # 打印異常以便調試
            print(f"Failed to fetch data from Ktor API: {str(e)}")
            return JsonResponse({'error': f'Failed to fetch data from Ktor API: {str(e)}'}, status=500)
        else:
            return render(request, 'search.html')


def system2(request):
    if request.method == 'GET':
        # 獲取查詢參數
        drivingDate = request.GET.get('drivingDate')
        routeNumber = request.GET.get('routeNumber')
        departureDate = request.GET.get('driving_time')
        if departureDate is not None:
            departureDate = departureDate.replace('%3A', ':')
            departureDate = departureDate + ":00"
        licensePlate = request.GET.get('licensePlate')
        # 設置請求參數
        params = {}
        if drivingDate:
            params['drivingDate'] = drivingDate
        if routeNumber:
            params['routeNumber'] = routeNumber
        if departureDate:
            params['departureDate'] = departureDate
        if licensePlate:
            params['licensePlate'] = licensePlate

        print(f"Params: {params}")

        try:
            if not params:
                response = requests.get('http://0.0.0.0:8080/driver')
            else:
                response = requests.get('http://0.0.0.0:8080/driver', params=params)

            response.raise_for_status()  # 檢查HTTP響應是否返回錯誤

            # 解析 Ktor API 返回的 JSON 數據
            drivers = response.json()
            print(f"Parsed Buses: {drivers}")

            # 準備要傳遞到模板的數據
            processed_buses = []
            for driver in drivers:
                processed_bus = {
                    'driverId': driver.get('driverId'),
                    'birthDay': driver.get('birthDay'),
                    'gender': driver.get('gender'),
                    'violationRecord': driver.get('violationRecord'),
                    'driverLicense': driver.get('driverLicense'),
                    'driverLicenseEd': driver.get('driverLicenseEd'),
                }
                processed_buses.append(processed_bus)

            # 將數據傳遞到模板並渲染
            return render(request, 'system2.html', {'drivers': processed_buses})

        except requests.RequestException as e:
            # 打印異常以便調試
            print(f"Failed to fetch data from Ktor API: {str(e)}")
            return JsonResponse({'error': f'Failed to fetch data from Ktor API: {str(e)}'}, status=500)
    else:
        return render(request, 'search.html')

def system3(request):
    if request.method == 'GET':
        # 獲取查詢參數
        drivingDate = request.GET.get('drivingDate')
        routeNumber = request.GET.get('routeNumber')
        outboundReturn = request.GET.get('outboundReturn')
        departureDate = request.GET.get('departureDate')
        if departureDate is not None:
            departureDate = departureDate.replace('%3A', ':')
            departureDate = departureDate + ":00"

        params = {}
        if drivingDate:
            params['drivingDate'] = drivingDate
        if routeNumber:
            params['routeNumber'] = routeNumber
        if departureDate:
            params['departureDate'] = departureDate
        if outboundReturn:
            params['outboundReturn'] = outboundReturn

        print(f"Params: {params}")

        try:
            if not params:
                response = requests.get('http://0.0.0.0:8080/passenger_phone')
            else:
                response = requests.get('http://0.0.0.0:8080/passenger_phone', params=params)

            response.raise_for_status()  # 檢查HTTP響應是否返回錯誤

            # 解析 Ktor API 返回的 JSON 數據
            drivers = response.json()
            print(f"Parsed Buses: {drivers}")

            # 準備要傳遞到模板的數據
            processed_buses = []
            for driver in drivers:
                processed_bus = {
                    'phone': driver.get('phone'),
                }
                processed_buses.append(processed_bus)

            # 將數據傳遞到模板並渲染
            return render(request, 'system3.html', {'buses': processed_buses})

        except requests.RequestException as e:
            # 打印異常以便調試
            print(f"Failed to fetch data from Ktor API: {str(e)}")
            return JsonResponse({'error': f'Failed to fetch data from Ktor API: {str(e)}'}, status=500)
    else:
        return render(request, 'search.html')



@csrf_exempt
def login(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'login' and all(field in request.POST for field in ['login-uid']):
            login_uid = request.POST['login-uid']

            # 查詢資料庫中是否有乘客資料
            passenger = Passenger.objects.filter(passenger_id=login_uid).first()

            if passenger:
                request.session['passenger_id'] = passenger.passenger_id
                request.session['passenger_name'] = passenger.passenger_name

                return redirect('booking')


        elif action == 'register' and all(field in request.POST for field in ['register-uid', 'register-name', 'register-gender', 'register-phone', 'register-email', 'register-disability']):
            register_uid = request.POST['register-uid']
            register_name = request.POST['register-name']
            register_gender = request.POST['register-gender']
            register_phone = request.POST['register-phone']
            register_email = request.POST['register-email']
            register_disability = request.POST['register-disability']

            # 新增乘客資料到資料庫
            Passenger.objects.create(
                passenger_id=register_uid,
                passenger_name=register_name,
                gender=register_gender,
                phone=register_phone,
                mail=register_email,
                disability_category=register_disability
            )

            return redirect('booking')

    return render(request, 'login.html')

from .models import AppointmentForm



def bookingStation(request):
    if request.method == 'GET':
        # 獲取查詢參數
        stationName = request.GET.get('stationName')
        routeNumber = request.GET.get('routeNumber')
        outboundReturn = request.GET.get('outboundReturn')
        accessibility = request.GET.get('accessibility')
        waitingAreaSeats = request.GET.get('waitingAreaSeats')

        # 設置請求參數
        params = {}
        if stationName:
            params['stationName'] = stationName
        if routeNumber:
            params['routeNumber'] = routeNumber
        if outboundReturn:
            params['outboundReturn'] = outboundReturn
        if accessibility:
            params['accessibility'] = accessibility
        if waitingAreaSeats:
            params['waitingAreaSeats'] = waitingAreaSeats

        print(f"Params: {params}")

        try:
            if not params:
                response = requests.get('http://0.0.0.0:8080/station_disability')
            else:
                response = requests.get('http://0.0.0.0:8080/station_disability', params=params)

            response.raise_for_status()  # 檢查HTTP響應是否返回錯誤

            # 解析 Ktor API 返回的 JSON 數據
            buses = response.json()
            print(f"Parsed Buses: {buses}")

            # 準備要傳遞到模板的數據
            processed_buses = []
            for bus in buses:
                processed_bus = {
                    'stationName': bus.get('stationName'),
                    'roadName': bus.get('roadName'),
                }
                processed_buses.append(processed_bus)

            # 將數據傳遞到模板並渲染
            return render(request, 'bookingStation.html', {'buses': processed_buses})

        except requests.RequestException as e:
            # 打印異常以便調試
            print(f"Failed to fetch data from Ktor API: {str(e)}")
            return JsonResponse({'error': f'Failed to fetch data from Ktor API: {str(e)}'}, status=500)
    else:
        return render(request, 'search.html')

def lover(request):
    return render(request, 'lover.html')


def systemLogin (request):
        return render(request, 'systemLogin.html')


from django.shortcuts import render, redirect
from .models import AppointmentForm
from .forms import AppointmentFormForm

from django.shortcuts import render, redirect
from .models import AppointmentForm
def generate_appointment_form_id():
    last_appointment = AppointmentForm.objects.all().order_by('appointment_form_id').last()
    if not last_appointment:
        return '0000'
    last_id = int(last_appointment.appointment_form_id)
    new_id = str(last_id + 1).zfill(4)
    return new_id


def booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        passenger_id = request.POST.get('passenger_id')
        driving_date = request.POST.get('driving_date')
        driving_week = request.POST.get('driving_week')
        route_number = request.POST.get('route_number')
        outbound_return = request.POST.get('outbound_return')
        departure_time = request.POST.get('departure_time')
        pick_up_location = request.POST.get('pick_up_location')
        drop_off_location = request.POST.get('drop_off_location')
        special_needs = request.POST.get('special_needs')

        # Here, you need to parse pick_up_location and drop_off_location into their respective x and y coordinates
        # For simplicity, we'll assume they are comma-separated values, e.g., "10.0,20.0"
        pick_up_location_x, pick_up_location_y = map(float, pick_up_location.split(','))
        drop_off_location_x, drop_off_location_y = map(float, drop_off_location.split(','))

        appointment = AppointmentForm(
            appointment_form_id=generate_appointment_form_id(),
            passenger_id=passenger_id,
            driving_date=driving_date,
            driving_week=driving_week,
            route_number=route_number,
            outbound_return=outbound_return,
            departure_time=departure_time,
            pick_up_location_x=pick_up_location_x,
            pick_up_location_y=pick_up_location_y,
            drop_off_location_x=drop_off_location_x,
            drop_off_location_y=drop_off_location_y,
            special_needs=int(special_needs) if special_needs else None
        )
        appointment.save()
        return redirect('bookingHistory')
    return render(request, 'booking.html')


def bookingHistory(request):
    appointments = AppointmentForm.objects.all()
    return render(request, 'bookingHistory.html', {'appointments': appointments})


def person(request):
    return render(request, 'person.html')

def properson(request):
    return render(request, 'properson.html')
def search(request):
    return render(request, 'search.html')


def bookingBus(request):
    if request.method == 'GET':
        # 獲取查詢參數
        drivingDate = request.GET.get('drivingDate')
        routeNumber = request.GET.get('routeNumber')
        lowFloor = request.GET.get('lowFloor')
        wheelchairUse = request.GET.get('wheelchairUse')
        waitingAreaSeats = request.GET.get('waitingAreaSeats')

        # 設置請求參數
        params = {}
        if drivingDate:
            params['drivingDate'] = drivingDate
        if routeNumber:
            params['routeNumber'] = routeNumber
        if lowFloor:
            params['lowFloor'] = lowFloor
        if wheelchairUse:
            params['wheelchairUse'] = wheelchairUse
        if waitingAreaSeats:
            params['waitingAreaSeats'] = waitingAreaSeats

        print(f"Params: {params}")

        try:
            if not params:
                response = requests.get('http://0.0.0.0:8080/actual_frequency_disability')
            else:
                response = requests.get('http://0.0.0.0:8080/actual_frequency_disability', params=params)

            response.raise_for_status()  # 檢查HTTP響應是否返回錯誤

            # 解析 Ktor API 返回的 JSON 數據
            buses = response.json()
            print(f"Parsed Buses: {buses}")

            # 準備要傳遞到模板的數據
            processed_buses = []
            for bus in buses:
                processed_bus = {
                    'drivingDate': bus.get('drivingDate'),
                    'departureTime': bus.get('departureTime'),
                    'drivingWeek': bus.get('drivingWeek'),
                    'jurisdictionUnit': bus.get('jurisdictionUnit'),
                    'routeNumber': bus.get('routeNumber'),
                    'driverId': bus.get('driverId'),
                    'vehicleLicensePlate': bus.get('vehicleLicensePlate'),
                }
                processed_buses.append(processed_bus)

            # 將數據傳遞到模板並渲染
            return render(request, 'bookingBus.html', {'buses': processed_buses})

        except requests.RequestException as e:
            # 打印異常以便調試
            print(f"Failed to fetch data from Ktor API: {str(e)}")
            return JsonResponse({'error': f'Failed to fetch data from Ktor API: {str(e)}'}, status=500)
    else:
        return render(request, 'search.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import AppointmentForm

def delete(request, appointment_id):
    appointment = get_object_or_404(AppointmentForm, pk=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('bookingHistory')
    return render(request, 'delete.html', {'appointment': appointment})

