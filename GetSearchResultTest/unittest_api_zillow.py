#!flask/bin/python
import requests
import unittest
from GetSearchResultsApp.api_zillow import parse_response

class TestCase(unittest.TestCase):
    def setUp(self):
        return

    def tearDown(self):
        return

    # //______________________________________________________________________________
    # //------------------------------------------------------------------------------
    #     \fn         test_parse_response_fail():
    #
    #     \brief      Test that the parser will not returns a dictionary with garbage if
    #                 it cannot parse the response
    #
    #     \return     void
    # //______________________________________________________________________________
    # //------------------------------------------------------------------------------
    def test_parse_response_fail(self):
        response = "Is a string, but function expects a Requests element"
        dict_tmp = parse_response(response)
        self.assertEqual(len(dict_tmp), 0)

    # //______________________________________________________________________________
    # //------------------------------------------------------------------------------
    #     \fn         test_parse_response_ok():
    #
    #     \brief      Test that the parser is working and will return a dictionary
    #                 filled with values
    #
    #     \return     void
    # //______________________________________________________________________________
    # //------------------------------------------------------------------------------
    def test_parse_response_ok(self):
        response = requests.get('http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=X1-ZWz192n187q8ln_2rqd6&address=2114+Bigelow+Ave&citystatezip=Seattle%2C+WA')
        dict_tmp = parse_response(response)
        self.assertGreater(len(dict_tmp), 0)

    # //______________________________________________________________________________
    # //------------------------------------------------------------------------------
    #     \fn         test_parse_response_ok():
    #
    #     \brief      Test that the parser is working and will return a dictionary
    #                 filled with values
    #
    #     \return     void
    # //______________________________________________________________________________
    # //------------------------------------------------------------------------------
    def test_parse_response_ok(self):
        response = requests.get('http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=X1-ZWz192n187q8ln_2rqd6&address=2114+Bigelow+Ave&citystatezip=Seattle%2C+WA')
        dict_tmp = parse_response(response)
        self.assertGreater(len(dict_tmp), 0)

if __name__ == '__main__':
    unittest.main()
