#!flask/bin/python
from flask_wtf import Form
from wtforms import SelectField, StringField, BooleanField
from wtforms.validators import DataRequired
#from GetSearchResultsApp import list_states


class SearchPropertyForm(Form):
    list_states = [('AK', 'AK'), ('AS' ,'AS') ,('AZ', 'AZ') ,('AR', 'AR') ,('CA', 'CA') ,('CO', 'CO') ,
                   ('CT', 'CT') ,('DE', 'DE') ,('DC', 'DC') ,('FM', 'FM') ,('FL', 'FL') ,('GA', 'GA') ,
                   ('GU', 'GU') ,('HI', 'HI') ,('ID', 'ID') ,('IL', 'IL') ,('IN', 'IN') ,('IA', 'IA') ,
                   ('KS', 'KS') ,('KY', 'KY') ,('LA', 'LA') ,('ME', 'ME') ,('MH', 'MH') ,('MD', 'MD') ,
                   ('MA', 'MA') ,('MI', 'MI') ,('MN', 'MN') ,('MS', 'MS') ,('MO', 'MO') ,('MT', 'MT') ,
                   ('NE', 'NE') ,('NV', 'NV') ,('NH', 'NH') ,('NJ', 'NJ') ,('NM', 'NM') ,('NY', 'NY') ,
                   ('NC', 'NC') ,('ND', 'ND') ,('MP', 'MP') ,('OH', 'OH') ,('OK', 'OK') ,('OR', 'OR') ,
                   ('PW', 'PW') ,('PA', 'PA') ,('PR', 'PR') ,('RI', 'RI') ,('SC', 'SC') ,('SD', 'SD') ,
                   ('TN', 'TN') ,('TX', 'TX') ,('UT', 'UT') ,('VT', 'VT') ,('VI', 'VI') ,('VA', 'VA') ,
                   ('WA', 'WA') ,('WV', 'WV') ,('WI', 'WI') ,('WY', 'WY')]

    list_types = [("Buy", "Buy"), ("Rent", "Rent"), ("Sale", "Sale")]
    list_prices = [("$150,000 - $200,000", "$150,000 - $200,000"), ("$200,000 - $250,000", "$200,000 - $250,000"),
                ("$250,000 - $300,000", "$250,000 - $300,000"), ("$300,000 - above", "$300,000 - above")]

    address = StringField('property number, street name')
    city = StringField('City')
    states = SelectField(u'States', choices=list_states)
    types = SelectField(u'Types', choices=list_types)
    prices = SelectField(u'Prices', choices=list_prices)
