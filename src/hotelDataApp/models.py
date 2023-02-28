from django.db import models

# Create your models here.
class City(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.code


class Hotel(models.Model):
    city_code = models.ForeignKey(City, on_delete=models.CASCADE)
    hotel_code = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.hotel_code
