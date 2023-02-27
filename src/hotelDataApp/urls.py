from django.urls import path
from .views import *


urlpatterns = [
    path('hotel/', get_hotel),
    path('city/', get_city)
]