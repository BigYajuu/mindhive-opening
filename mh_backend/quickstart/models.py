from django.db import models

# Create your models here.
class Branch(models.Model):
    name = models.TextField()
    address = models.TextField()
    operating_hours = models.TextField()
    waze_link = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()

    class Meta:
        ordering = ['name']
        