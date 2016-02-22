from google.appengine.api import urlfetch
from google.appengine.ext import db
import webapp2
import json

    
class MainPage(webapp2.RequestHandler):
    def get(self):
        apiKey = "e9554b45d938eba3af70e453dbfbc3c2"
        units = self.request.get("units")
        lat = self.request.get("lat", '0')
        lng = self.request.get("lng", '0')

        url = "https://api.forecast.io/forecast/" + apiKey + "/" + lat + "," + lng + "/?"
        if units == "si":
            url += "&units=si"
        elif units == "us":
            url += "&units=us"
        else:
            print "EzeServer: Unit not recognized"

        self.response.headers.add_header("Access-Control-Allow-Origin", "*")
        self.response.headers['Content-Type'] = 'application/json'

        rpc = urlfetch.create_rpc()
        urlfetch.make_fetch_call(rpc, url)

        try:
            result = rpc.get_result()
            if result.status_code == 200:
                weatherForecastText = result.content
                weatherForecastJson = json.loads(weatherForecastText)
                self.response.write(weatherForecastJson)
                                    
        except urlfetch.DownloadError:
            print "Download Error"



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ], debug=True)
            
            
