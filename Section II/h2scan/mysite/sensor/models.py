from django.db import models

# Create your models here.
class Sensor(models.Model):
    sensor_number = models.CharField(max_length=200)
    def __str__(self):
        return self.sensor_number
    
	
class SensorData(models.Model):
    Sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    TimeSys = models.CharField(max_length=200)
    TimeSec = models.DecimalField(max_digits=10, decimal_places=2)
    PcbAdc = models.IntegerField(default=0)
    TempAdc = models.IntegerField(default=0)
    HCurrent = models.DecimalField(max_digits=5, decimal_places=2)
    Res2Adc = models.IntegerField(default=0)
    Res1Adc = models.IntegerField(default=0)
    PcbTemp = models.DecimalField(max_digits=6, decimal_places=4)
    SnsrTemp = models.DecimalField(max_digits=7, decimal_places=5)
    Messages = models.CharField(max_length=200)
    line_number = models.IntegerField(default=0)
    file_name = models.CharField(max_length=200)
    config = models.CharField(max_length=200)
    sensor_number = models.CharField(max_length=200)

class Sensor2(models.Model):
    sensor_number = models.CharField(max_length=200)
    def __str__(self):
        return self.sensor_number
		

class Sensor2Data(models.Model):
    Sensor2 = models.ForeignKey(Sensor2, on_delete=models.CASCADE)
    TimeSys = models.CharField(max_length=200)
    TimeSec = models.DecimalField(max_digits=9, decimal_places=2)
    PcbTemp = models.DecimalField(max_digits=6, decimal_places=4)
    SnsrTemp = models.DecimalField(max_digits=8, decimal_places=5)
    HCurrent = models.DecimalField(max_digits=5, decimal_places=2)
    Res1Adc = models.IntegerField(default=0)
    AdjRes1 = models.IntegerField(default=0)
    ResZero = models.IntegerField(default=0)
    Percentage_H2_Res = models.DecimalField(max_digits=5, decimal_places=4)
    Percentage_H2 = models.DecimalField(max_digits=6, decimal_places=5)
    Messages = models.CharField(max_length=200)
    line_number = models.IntegerField(default=0)
    file_name = models.CharField(max_length=200)
    config = models.CharField(max_length=200)
    sensor_number = models.CharField(max_length=200)