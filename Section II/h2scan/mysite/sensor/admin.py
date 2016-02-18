from django.contrib import admin

# Register your models here.
from .models import Sensor, SensorData, Sensor2, Sensor2Data

#admin.site.register(Sensor)

class SensorDataInLine(admin.TabularInline):
    model = SensorData
    extra = 0


class SensorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,    {'fields': ['sensor_number']}),
    ]
    inlines = [SensorDataInLine]

class Sensor2DataInLine(admin.TabularInline):
    model = Sensor2Data
    extra = 0


class Sensor2Admin(admin.ModelAdmin):
    fieldsets = [
        (None,    {'fields': ['sensor_number']}),
    ]
    inlines = [Sensor2DataInLine]

admin.site.register(Sensor, SensorAdmin)
admin.site.register( Sensor2, Sensor2Admin)			