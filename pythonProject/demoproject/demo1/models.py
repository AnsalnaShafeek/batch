from django.db import models
from django.contrib.auth.models import User

# Create your models he

class ProjectData(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    cpassword = models.CharField(max_length=20)


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    DOB = models.DateField()
    address = models.CharField(max_length=25)
    city = models.CharField(max_length=20)
    profile_pic = models.ImageField(upload_to='profileimg',null=True)


class UserBlog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Topic = models.CharField(max_length=100)
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blogimg')
    blog_data = models.CharField(max_length=800)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True)
