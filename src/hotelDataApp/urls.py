from django.urls import path
from .views import *


urlpatterns = [
    path('', show_data), # URL to choose display the first page and choose city
    path('hotel/', get_hotel_http), # URL to collect hotel data from HTTP, it will be deleted for cronjob later
    path('city/', get_city_http),   # URL to collect city data from HTTP, it will be deleted for cronjob later
    path('hotelsfromcity/<str:city>', get_hotels) # URL to get and display hotels in a city 
]