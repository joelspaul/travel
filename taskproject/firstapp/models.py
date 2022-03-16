from django.db import models


# Create your models here.
class star(models.Model):
    head = models.CharField(max_length=250)
    img = models.ImageField(upload_to='picz')
    des = models.TextField()
    def __str__(self):
        return self.head

class players(models.Model):
    name = models.CharField(max_length=250)
    imge = models.ImageField(upload_to='photos')
    desc = models.TextField()

