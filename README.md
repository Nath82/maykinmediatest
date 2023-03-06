# maykinmediatest


# Installation
1. I advise you to create a python virtual environment : `python -m venv env`
2. Clone the git repository
3. Activate your virtual environnement : `source env/bin/activate`
4. Move into maykinmediatest and install the requirements : `pip install -r requirements.txt`
5. Move into src and run the server : `python manage.py runserver`
6. Open a page in your browser and go to the address : `http://127.0.0.1:8000/`
7. Select a city and click on the "Ok" button to see hotels within it


# Model
- City
    - code
    - name

- Hotel
    - city
    - code
    - name


# Features
- [x] import csv data over authenticated HTTP
- [x] view/template to choose a city and show all hotels
- [x] unit tests
- [x] documentation and comments


# Optional
- [x] create a django admin interface
- [x] asynchronous request for the hotel data with js and automatically display the data
- [ ] bonus if auto-complete field to do the city section
- [x] cronjob for daily import (Linux)
- [x] share git
- [ ] create and interface for hotel managers (Users have access to all hotels in a single city), to add, update and remove hotels whithin their city
