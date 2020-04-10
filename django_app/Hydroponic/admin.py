from django.contrib import admin
from .models import WateringLog, TemperatureLog, HumidityLog

admin.site.register(WateringLog)
admin.site.register(TemperatureLog)
admin.site.register(HumidityLog)