from django.shortcuts import render
import requests
from django.http import HttpResponse
import csv

# Create your views here.
def get_hotel(request):
    url = "http://rachel.maykinmedia.nl/djangocase/hotel.csv"

    payload={}
    headers = {
    'Authorization': 'Basic cHl0aG9uLWRlbW86Y2xhdzMwX2J1bXBz'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)

    return HttpResponse(response)


def get_city(request):
    url = "http://rachel.maykinmedia.nl/djangocase/city.csv"

    payload={}
    headers = {
    'Authorization': 'Basic cHl0aG9uLWRlbW86Y2xhdzMwX2J1bXBz'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    
    print(response.text.encode)

    return HttpResponse(response)