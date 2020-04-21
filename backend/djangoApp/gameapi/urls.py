# Author: Ryan Sreenivasam
# Description: Urls patterns that will direct users to information 
# throughout the database.  This file is referenced by djangoApp/urls.py
# to explain urls for the gameapi section of the app only.

from django.urls import include, path
from rest_framework import routers
from . import views

# Use the automatic URL routing from DjangoRestFramework to route requests 
router = routers.DefaultRouter()
router.register(r'api', views.GameViewSet)

# Additionally, we include login URLs for the browsable API.
urlpatterns = [
     # connection for the router's urls
    path('', include(router.urls)),
    # urls for the api's browser gui
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
