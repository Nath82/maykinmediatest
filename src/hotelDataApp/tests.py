from django.test import TestCase, Client
from django.urls import reverse
from hotelDataApp.models import *
from hotelDataApp.views import *
import json


# I do not think it is useful to test Django's functionality
# So I will focus on testing my own code

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        City.objects.create(
            name='Amsterdam',
            code='AMS'
        )
        Hotel.objects.create(
            city_code= City.objects.get(code='AMS'),
            hotel_code='AMS01',
            name='Ibis Amsterdam Airport'
        )
        
    
    def test_show_data(self):
        # Test
        response = self.client.get(reverse(show_data))
        
        # Assertions
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_hotels(self):
        # Test
        response = self.client.get(reverse('hotels-from-city', args=['Amsterdam']))
        
        # Assertions
        self.assertEquals(response.status_code, 200)

    def test_get_hotel(self):
        # Test
        response = self.client.get(reverse('single-hotel', args=['AMS01']))
        
        # Assertions
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hotel.html')
        