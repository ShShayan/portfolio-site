from django.db import models

class Blog(models.Model):
    # title
    title = models.CharField(max_length= 255)

    # date
    date = models.DateTimeField()

    # body
    body = models.TextField()

    # image
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title        

    def summary(self):
        return self.body[:200] + ' ...'
    
    def pub_date(self):
        return self.date.strftime('%b-%e-%Y')