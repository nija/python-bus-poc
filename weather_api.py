'''API wrapper class'''
# pylint: disable=I0011,C0103
import json
import urllib
import urllib2


class WeatherApi:


    @staticmethod
    def get_weather(api_key, location):

        # uri = "http://api.openweathermap.org/data/2.5/weather?zip={},us{}".format(location, api_key)
        # print uri
        # response = urllib2.urlopen(uri)
        # print response.read()
        # resp = json.loads(response.read())

        # Function stub for testing
        response = '{"coord":{"lon":-122.08,"lat":37.39},"weather":[{"id":721,"main":"Haze","description":"haze","icon":"50d"}],"base":"cmc stations","main":{"temp":296.92,"pressure":1014,"humidity":34,"temp_min":288.15,"temp_max":304.15},"wind":{"speed":2.6,"deg":280},"clouds":{"all":5},"dt":1464381831,"sys":{"type":1,"id":480,"message":0.0063,"country":"US","sunrise":1464353436,"sunset":1464405667},"id":5375480,"name":"Mountain View","cod":200}'
        resp = json.loads(response)

        return resp
    