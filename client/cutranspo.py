import urllib
import urllib2
import json
from pprint import pprint
import sched, time

deviceName = 'rpi'
password = '1234'

s = sched.scheduler(time.time, time.sleep)

try:
	url = 'http://172.17.98.162:3000/api/Devices'
	values = {'deviceName' : deviceName,'password' : password, 'stopNo' : '5813'}
	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	print req
	response = urllib2.urlopen(req)
	login_json = response.read()
except urllib2.HTTPError:
	print "Already Registered"

def getNextTimes(sc):
	try:
		url = 'http://172.17.98.162:3000/api/Devices/login'
		values = {'deviceName' : deviceName,'password' : password}
		data = urllib.urlencode(values)
		req = urllib2.Request(url, data)
		print req
		response = urllib2.urlopen(req)
		access_token = response.read()
	except urllib2.HTTPError:
		print "Login failed"

	query = urllib.urlencode({"busNo" : "104,7,4,111"}, {"access_token" : access_token})

	req = urllib2.Request('http://172.17.98.162:3000/api/Devices/getTimes?' + query)


	# json_input = '{ "one": { "list": [ {"item":"A"},{"item":"B"} ] }, "two": { "list": [ {"item":"A"},{"item":"B"} ] } }'

	try:
	    decoded = json.loads(login_json)
	 
	    # pretty printing of json-formatted string
	    print json.dumps(decoded, sort_keys=True, indent=4)
	 
	    print "Device Name", decoded['deviceName']
	    print "Email", decoded['email']
	except (ValueError, KeyError, TypeError):
	    print "JSON format error"

s.enter(10, 1, getNextTimes, (s,))
s.run()