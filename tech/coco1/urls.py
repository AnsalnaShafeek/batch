from django.urls import path
from coco1 import views

urlpatterns = [
    path('',views.registration),
    path('login',views.login),
    path('profile',views.profile),

]