from django.urls import path
from .views import *


urlpatterns = [
    path('', show_data), # URL to choose display the first page and choose city
    path('hotel/', get_hotels_http), # URL to collect hotel data from HTTP, we can also use cronjob
    path('city/', get_cities_http),   # URL to collect city data from HTTP, we can also use cronjob
    path('hotelsfromcity/<str:city>', get_hotels, name='hotels-from-city'), # URL to get and display hotels in a city 
    path('singlehotel/<str:code>', get_hotel, name='single-hotel')
]