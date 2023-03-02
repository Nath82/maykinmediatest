from django.urls import path
from .views import *


urlpatterns = [
    path('', show_data),
    path('hotel/', get_hotel_http),
    path('city/', get_city_http),
    path('hotelsfromcity/', get_hotels)
]