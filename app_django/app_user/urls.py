
from django.contrib import admin
from django.urls import path
from .views import TestView

urlpatterns = [
    path('test', TestView.as_view()),
    # Esta ruta quedaria: 'localhost:8000/api/v1.0/user/test'
]
