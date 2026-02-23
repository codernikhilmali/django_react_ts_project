from django.urls import path
from .views import *
# 
urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("me/", MeAPIView.as_view(), name="me"),
    path("login/", LoginAPIView.as_view(), name="login"),
]