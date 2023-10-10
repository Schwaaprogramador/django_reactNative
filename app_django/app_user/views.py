from django.shortcuts import render

# pip install djangorestframework
# Documentacion : https://www.django-rest-framework.org/
# quickStart: https://www.django-rest-framework.org/tutorial/quickstart/
"""
INSTALLED_APPS = [
    ...
    'rest_framework',
]
Any global settings for a REST framework API are kept in a single configuration dictionary named REST_FRAMEWORK. Start off by adding the following to your settings.py module:

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
"""
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class TestView(APIView):
    def get(self, request, format=None):
        print("API Was Called")
        return Response("You Made It", status=200)