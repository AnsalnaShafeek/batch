from django.urls import path
from demo1 import views


urlpatterns = [
    path('',views.Userlogin),
    path('register',views.UserRegister),
    path('logout',views.User_logout),
    path('home',views.home),
    path('reset',views.Forgot_Password),
    path('test',views.testing),
    path('create',views.CreateBlog),
    path('viewblog',views.ViewBlog),
    path('createprofile',views.createprofile),
]