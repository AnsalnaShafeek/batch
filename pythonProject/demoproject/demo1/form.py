from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from demo1.models import ProjectData,UserBlog

class ProfileForm(forms.ModelForm):
    class Meta:
       model = ProjectData
       fields = '__all__'


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')


class UserImageForm(forms.ModelForm):
    class Meta:
        model = UserBlog
        fields = ('Topic','caption','blog_data','image')
