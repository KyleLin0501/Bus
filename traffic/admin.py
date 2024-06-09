from django.contrib import admin
from .models import Bus
from .models import HistoricalArrivals
from .models import ActualFrequency
from .models import Route
from .models import AppointmentForm
from .models import Dirver
from .models import Passenger
from .models import Schedules
from .models import Station
from .models import VehicleMaintenanceRecords



admin.site.register(Bus)
admin.site.register(HistoricalArrivals)
admin.site.register(ActualFrequency)
admin.site.register(Route)
admin.site.register(AppointmentForm)
admin.site.register(Dirver)
admin.site.register(Passenger)
admin.site.register(Schedules)
admin.site.register(Station)
admin.site.register(VehicleMaintenanceRecords)


# Register your models here.
