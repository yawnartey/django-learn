from django.urls import path 
from . import views 

#define list that contains different addresses and their associated views
urlpatterns = [
    path ('function', views.hello_world), 
    path ('class', views.HelloEthiopia.as_view()),
    path ('reservation', views.home),
]