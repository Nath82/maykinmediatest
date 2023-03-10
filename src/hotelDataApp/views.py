import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from requests.exceptions import ConnectionError
import requests
from hotelDataApp.models import City, Hotel




# Function to create the cities from the csv file retrieved via http
def get_cities_http(request):
    url = "http://rachel.maykinmedia.nl/djangocase/city.csv"

    payload={}
    headers = {
    'Authorization': 'Basic cHl0aG9uLWRlbW86Y2xhdzMwX2J1bXBz'
    }
    try:
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
                code = cities[i][0][1:-1] # we take the code of the city without brackets
                name = cities[i][1][1:-1] # same for the name
                city = City(code=code, name=name)
                city.save()  
            except IndexError:
                print("An item of cities is empty")
        return HttpResponse(response)
    except ConnectionError as e:
        return HttpResponse(e)



# Function to create the hotels from the csv file retrieved via http
def get_hotels_http(request):
    url = "http://rachel.maykinmedia.nl/djangocase/hotel.csv"

    payload={}
    headers = {
    'Authorization': 'Basic cHl0aG9uLWRlbW86Y2xhdzMwX2J1bXBz'
    }
    try:
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
    
    except ConnectionError as e:
        return HttpResponse(e)



# Function to show data
def show_data(request):
    context = {}
    context["cities"] = City.objects.all()
    return render(request, 'index.html', context=context)



# Get hotels for a city
def get_hotels(request, city):
    context={}
    code = City.objects.get(name=city)
    context = (Hotel.objects.filter(city_code=code).values())
    result = json.dumps(list(context))
    return HttpResponse(content=result)

def get_hotel(request, code):
    context = {}
    context["hotel"] = Hotel.objects.get(hotel_code=code)
    return render(request, 'hotel.html', context=context)
