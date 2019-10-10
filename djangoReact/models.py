from django.db import models

# Create your models here.


class temperature(models.Model):
    station = models.CharField(max_length=200)
    temp = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now=False)
    published_date = models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.station