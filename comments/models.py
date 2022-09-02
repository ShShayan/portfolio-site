from django.db import models

# Create your models here.
class Comment(models.Model):
    subject = models.CharField(max_length = 200,  )
    email = models.CharField(max_length = 200, )
    name = models.CharField(max_length = 200, )
    text = models.CharField(max_length = 500)