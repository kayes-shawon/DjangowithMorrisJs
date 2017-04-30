from django.db import models

# Create your models here.
class Atmos(models.Model):
    date = models.CharField(max_length=20)
    sensor1_temp = models.CharField(max_length=100)
    sensor2_temp = models.CharField(max_length=100)
    sensor3_temp = models.CharField(max_length=100)
    sensor4_temp = models.CharField(max_length=100)

    def __str__(self):
        return self.date