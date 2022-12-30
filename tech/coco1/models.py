from django.db import models
# Create your models here.

class member(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    passwd = models.CharField(max_length=25)
    cpasswd = models.CharField(max_length=25)


class ProfileData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=100)



