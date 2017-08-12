#!flask/bin/python
import os
from flask import Flask
from jinja2 import Environment, FileSystemLoader

# Global variables
list_properties = []    # List of dictionaries with information of all succesfull searched made by user
zillow_id = 'X1-ZWz192n187q8ln_2rqd6' #Not secure, id is exposed in code


# Path variables
PATH = os.path.dirname(os.path.abspath(__file__))
PATH_TEMPLATES = os.path.join('templates')

TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, PATH_TEMPLATES)),
    trim_blocks=False)

# App Initialization
app = Flask(__name__, template_folder=PATH)
app.config.from_object('config')


from GetSearchResultsApp import views

if __name__ == "__main__":
    app.run()
