from django.db import models

class WateringLog(models.Model):
    history = models.CharField(max_length=100)

    def __str__(self):
        return '<Friend:id' + str(self.id) + ',' + \
            self.history + '>'

class TemperatureLog(models.Model):
    history = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return '<Friend:id' + str(self.id) + ',' + \
            self.history + '(' + str(self.temperature) + ')' + '>'

class HumidityLog(models.Model):
    history = models.CharField(max_length=100)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return '<Friend:id' + str(self.id) + ',' + \
            self.history + '(' + str(self.humidity) + ')' + '>'

class PictureLog(models.Model):
    history = models.CharField(max_length=100)
    fileName = models.CharField(max_length=100)
    
    def __str__(self):
        return '<Friend:id' + str(self.id) + ',' + \
            self.history + '(' + self.fileName + ')' + '>'

class ColorLog(models.Model):
    history = models.CharField(max_length=100)
    red = models.DecimalField(max_digits=10, decimal_places=2)
    green = models.DecimalField(max_digits=10, decimal_places=2)
    blue = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '<Friend:id' + str(self.id) + ',' + \
            self.history + ','+ \
            '(' + str(self.red) + ')' + ','+ \
            '(' + str(self.green) + ')' + ','+ \
            '(' + str(self.blue) + ')' + '>'

class Temperature(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return '<Friend:id' + str(self.id) + ',' + \
            '(' + str(self.value) + ')' + '>'

class Humidity(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return '<Friend:id' + str(self.id) + ',' + \
            '(' + str(self.value) + ')' + '>'

class Growth(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    targetColor = models.CharField(max_length=100)

    def __str__(self):
        return '<Friend:id' + str(self.id) + ',' + \
            '(' + str(self.value) + ')' + ',' + \
            '(' + str(self.targetColor) + ')' + '>'

class TimeSetting(models.Model):
    name = models.CharField(max_length=100)
    time = models.IntegerField()

    def __str__(self):
        return '<Friend:id' + str(self.id) + ',' + \
            '(' + str(self.name) + ')' + ',' + \
            '(' + str(self.time) + ')' + '>'

class LineSetting(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return '<Friend:id' + str(self.id) + ',' + \
            '(' + str(self.name) + ')' + ',' + \
            '(' + str(self.value) + ')' + '>'

class WaterSetting(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '<Friend:id' + str(self.id) + ',' + \
            '(' + str(self.name) + ')' + ',' + \
            '(' + str(self.value) + ')' + '>'