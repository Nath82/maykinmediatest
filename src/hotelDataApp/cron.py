import requests
from hotelDataApp.models import City, Hotel

def my_scheduled_job():
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
