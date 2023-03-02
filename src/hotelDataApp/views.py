from django.shortcuts import render
import requests
from django.http import HttpResponse

from hotelDataApp.models import City, Hotel



# Function to create the cities from the csv file retrieved via http
def get_city_http(request):
    url = "http://rachel.maykinmedia.nl/djangocase/city.csv"

    payload={}
    headers = {
    'Authorization': 'Basic cHl0aG9uLWRlbW86Y2xhdzMwX2J1bXBz'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    
    text = response.text.split(sep='\n')
    
    # text retrieves the raw data in string so we have to process it to extract attributs of objects
    cities = []
    for i in range(len(text)):
        cities.append(text[i].split(';'))

    # Now we can create objects
    for i in range(len(cities)):
        # There may be an input error in the csv, such as a box filled only with a space, 
        # which is not visible to the naked eye when filling the document, 
        # to avoid recording the wrong data we catch the error
        try:
            code = cities[i][0][1:-1] # we take the first argument of the i line on hotels without brackets
            name = cities[i][1][1:-1]
            city = City(code=code, name=name)
            city.save()  
        except IndexError:
            print("An item of cities is empty")
    
    return HttpResponse(response)



# Function to create the hotels from the csv file retrieved via http
def get_hotel_http(request):
    url = "http://rachel.maykinmedia.nl/djangocase/hotel.csv"

    payload={}
    headers = {
    'Authorization': 'Basic cHl0aG9uLWRlbW86Y2xhdzMwX2J1bXBz'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    text = response.text.split(sep='\n')

    # text retrieves the raw data in string so we have to process it to extract attributs of objects
    hotels = []
    for i in range(len(text)):
        hotels.append(text[i].split(';'))

    # Now we can create objects
    for i in range(len(hotels)):
        city_code = City.objects.get(code=hotels[i][0][1:-1])
        hotel_code = hotels[i][1][1:-1]
        name = hotels[i][2][1:-1]
        hotel = Hotel(city_code=city_code, hotel_code=hotel_code, name=name)
        hotel.save()

    return HttpResponse(response)



# Function to show data
def show_data(request):
    context = {}
    context["cities"] = City.objects.all()
    return render(request, 'index.html', context=context)



# Get hotels for a city
def get_hotels(request):
    city = request.GET['city']
    context={}
    code = City.objects.get(name=city)
    context["hotels"] = Hotel.objects.filter(city_code=code)
    context["city"] = city
    return render(request, 'hotels.html', context=context)