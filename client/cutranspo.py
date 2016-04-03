import urllib
import urllib2
import json
from pprint import pprint
import sched, time
from subprocess import call

# deviceName = 'rpi'
# password = '1234'

# s = sched.scheduler(time.time, time.sleep)

# try:
# 	url = 'http://172.17.98.162:3000/api/Devices'
# 	values = {'deviceName' : deviceName,'password' : password, 'stopNo' : '5813'}
# 	data = urllib.urlencode(values)
# 	req = urllib2.Request(url, data)
# 	print req
# 	response = urllib2.urlopen(req)
# 	login_json = response.read()
# except urllib2.HTTPError:
# 	print "Already Registered"

# #def getNextTimes(sc):
# try:
# 	url = 'http://172.17.98.162:3000/api/Devices/login'
# 	values = {'deviceName' : deviceName,'password' : password}
# 	data = urllib.urlencode(values)
# 	req = urllib2.Request(url, data)
# 	print req
# 	response = urllib2.urlopen(req)
# 	#response.read()
# 	decoded = json.loads(response.read())
# 	access_token = decoded['id']
# 	print "Access Token: ", decoded['id']
# except urllib2.HTTPError:
# 	print "Login failed"

# query = urllib.urlencode({"access_token" : access_token})

# req_for_bus_timing = urllib2.Request('http://172.17.98.162:3000/api/Devices/getTimes?' + query)
# bus_timings_response = urllib2.urlopen(req_for_bus_timing)
# try:
# 	decoded = json.loads(bus_timings_response.read())
# 	destination = decoded['response']['data']['4'][1]['dest']
# 	times = decoded['response']['data']['4'][1]['times']
# 	print "Bus: 4"
# 	print "Destination: " + destination
# 	print "Times: " + times
# except (ValueError, KeyError, TypeError):
#     print "JSON format error"
####################################################################3
# try:
#     decoded = json.loads(login_json)
 
#     # pretty printing of json-formatted string
#     print json.dumps(decoded, sort_keys=True, indent=4)
 
#     print "Device Name", decoded['deviceName']
#     print "Email", decoded['email']


# s.enter(10, 1, getNextTimes, (s,))
# s.run()
call(["./test2", "255,0,255", "60", "4   " + "Rideau", "5:10   5:15:   5:20"])
#call(["./test2", "255,0,255", "60", "4    " + destination, times[0] + "   " + times[1] + "   " + times[2]])