#!flask/bin/python
import requests
from flask import render_template, request

from GetSearchResultsApp import *
from .forms import *
from .api_zillow import get_property_info


# //______________________________________________________________________________
# //------------------------------------------------------------------------------
#     \fn         home():
#
#     \brief      Provide home page to user
#
#     \return     void
# //______________________________________________________________________________
# //------------------------------------------------------------------------------
@app.route('/home', methods=['GET', 'POST'])
def home():
    tmp_list_properties = []
    form = SearchPropertyForm()

    if form.validate_on_submit():
        status, tmp_list_properties = get_property_info(request.form['address'], request.form['city'],request.form['states'])
        if status is True:
                return render_template(os.path.join(PATH_TEMPLATES, 'index.html').replace(os.path.sep, '/'), form=form, status=True,  list=tmp_list_properties, property=tmp_list_properties[-1])
    return render_template(os.path.join(PATH_TEMPLATES, 'index.html').replace(os.path.sep, '/'), form=form, status=False, list=tmp_list_properties)
