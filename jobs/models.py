from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length = 200)
    employer = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    start = models.DateField()
    end = models.DateField()

    def startyear(self):
        return self.start.strftime('%B %Y')

    def endyear(self):
        return self.end.strftime('%B %Y')