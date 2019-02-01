# GetSearchResultApi

### Heroku
The application is deployed on [Heroku](https://flask-zillow.herokuapp.com/home).

## Features

### Not Implemented
Some of the features that appear on the main page have not been implemented:
* Login
* Caroussel for the previous search is not working properly
* Search by Price Range and by Rent, Buy, Sale
* The picture of the property, for the moment, it is just showing a static picture

### Implemented
* A search by (Addres, City, State)
* As soon as you search for a second property, the previous search will appear in the right bottom corner of your browser

### What is the goal of this application:

Create a simple web app that allows a user to enter an address for a home and then see details for that home from Zillow's GetSearchResults API (API key: X1-ZWz1dyb53fdhjf_6jziz). The output should be a cleanly-displayed representation of whatever came back in the API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

This Web Application was developed on Windows 7 with the latest Python V3.6.2

Here a list of all Python packages installed:
* certifi==2017.7.27.1
* chardet==3.0.4
* click==6.7
* Flask>=0.12.3
* Flask-WTF==0.14.2
* gunicorn==19.7.1
* itsdangerous==0.24
* Jinja2==2.9.6
* MarkupSafe==1.0
* requests>=2.20.0
* selenium==3.5.0
* urllib3>=1.23
* Werkzeug==0.12.2
* WTForms==2.1

### Installing

* [Python 3.6.2](https://www.python.org/downloads/) - Install Python 3.6
* [Install Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows) - A Python IDE, if you don't already have one
* Install Flask by running the command - pip3 install Flask
* Install requests by running the command - pip3 install requests
* Install WTForms by running the command - pip3 install WTForms
* Install requests by running the command - pip3 install gunicorn


## Running the tests

Testing the browser with Selenium is not implemented and would be an important testing feature to add.

To run the unittest, execute the GetSearchResultTest/unittest_api_zillow.py 

I wrote only 2 unit tests testing the function parsing the response received from GetSearchResult Api.

## Authors

* **Vince Lessard** - *Initial work* - [Linkedin](https://www.linkedin.com/in/vlbca/)

## License

This project is not under any licence
