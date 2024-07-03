from django.urls import path, include
from .views import WelcomeView
from rest_framework import routers


urlpatterns = [
    path('hello', WelcomeView.as_view(), name='welcome'),
    ]