from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    customer_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ModelData(models.Model):
    model_name = models.CharField(max_length=100)
    glue = models.FloatField()
    water = models.FloatField()
    roving = models.FloatField()
    roller_temperature = models.FloatField()
    tool_temp_top = models.FloatField()
    tool_temp_middle = models.FloatField()
    tool_temp_bottom = models.FloatField()
    wjc_pressure = models.FloatField()
    date = models.DateField()
    shift = models.CharField(max_length=10)

    def __str__(self):
        return self.model_name
