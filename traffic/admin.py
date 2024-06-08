from django.contrib import admin
from .models import Bus
from .models import HistoricalArrivals
admin.site.register(Bus)
admin.site.register(HistoricalArrivals)

# Register your models here.
