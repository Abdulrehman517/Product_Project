from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50,default='')
    tags = models.CharField(max_length=50,default='')
    handle = models.CharField(max_length=44, default='')
    body = models.CharField(max_length=55, default='')




    def __str__(self):
        return self.title


