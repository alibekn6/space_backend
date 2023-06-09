from django.urls import path
from . import views


app_name = 'spaceteam'

urlpatterns = [
    path('', views.spaceteam, name='team')
]