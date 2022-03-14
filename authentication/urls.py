from unicodedata import name
from django.urls import path 
from . import views




urlpatterns=[
    path('register/',views.RegisterView.as_view(),name="register"),
    path('email-verify/',views.verifyEmail.as_view(),name="email-verify"),
   
   ]