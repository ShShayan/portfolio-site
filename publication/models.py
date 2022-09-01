from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length = 300)
    authers = models.CharField(max_length = 300)
    year = models.CharField(max_length = 300)
    journal = models.CharField(max_length = 300)