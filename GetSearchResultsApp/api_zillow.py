#!flask/bin/python
import requests
from xml.etree import ElementTree
from GetSearchResultsApp import *

# //______________________________________________________________________________
# //------------------------------------------------------------------------------
#     \fn         get_property_info
#
#     \brief      Query Zillow public API GetSearchResults and get JSON or XML values
#                 Below is an example of calling the API for the address "2114 Bigelow Ave", "Seattle, WA":
#                 .i.e: http://www.zillow.com/webservice/GetSearchResults.htm?zws-id
#                       =<ZWSID>&address=2114+Bigelow+Ave&citystatezip=Seattle%2C+WA
#
#     \param      address - Input from user.i.e: 2114 Bigelow Ave
#                 city    - Input from user
#                 state   - Value obtained from a list, value always formatted to 2 letters (.i.e : CA)
#
#     \Warning:   The xml.etree.ElementTree module is not secure against maliciously constructed data.
#                 If you need to parse untrusted or unauthenticated data see XML vulnerabilities.
#
#     \return   status - True is succeed, False is fail
#               List of dictionaries with information of all succesfull searched made by user
# //______________________________________________________________________________
# //------------------------------------------------------------------------------
def get_property_info(address, city, state):
    address = address.replace(' ', '+').replace(',', '')
    city = city.replace(' ', '+').replace(',', '')

    url = "http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=%s&address=%s&citystatezip=%s%s+%s" % (zillow_id, address, city, "%2C", state)

    response = requests.get(url)
    status = False

    if response.ok:
        dict_tmp = parse_response(response)
        if len(dict_tmp) > 0:
            list_properties.append(dict_tmp)
            status = True

    return status, list_properties


# //______________________________________________________________________________
# //------------------------------------------------------------------------------
#     \fn         parse_response
#
#     \brief      Get a response from the Zillow APIs in bytes. Transform it to string and
#                 fill a dictionary of its content.
#
#     \param      response - Response from the Zillow APIs in bytes
#
#     \return     list of dictionary
# //______________________________________________________________________________
# //------------------------------------------------------------------------------
def parse_response(response):
    xml_str = str(response.content,'utf-8')
    tree = ElementTree.fromstring(xml_str)

    dict_content={}
    for child in tree:
        if child.tag == "response":
            items = child.getiterator()
            for item in items:
                if item.text is not None:
                    dict_content[item.tag] = item.text

    return dict_content


if __name__ == "__main__":
    get_property_info("2114 Bigelow Ave", "Seattle", "WA")
