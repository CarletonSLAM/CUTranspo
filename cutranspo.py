import urllib
import urllib2

url = 'https://api.octranspo1.com/v1.2/GetNextTripsForStop'
values = {'appID' : 'bc2a6109', 'apiKey' : 'de7ab3747426061606ef26ec285c9df2', 'stopNo' : '5813', 'routeNo' : '104'}
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page