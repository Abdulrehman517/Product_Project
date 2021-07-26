from django.db import models
# from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=50,default='')
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.CharField(max_length=50,default='')
    handle = models.CharField(max_length=44, default='')
    body = models.CharField(max_length=55, default='')




    def __str__(self):
        return self.title


