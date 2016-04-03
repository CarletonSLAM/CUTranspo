import urllib
import urllib2
import json
from pprint import pprint
import sched, time
from subprocess import call
import os
import time

deviceName = 'rpi'
password = '1234'

s = sched.scheduler(time.time, time.sleep)

try:
	url = 'https://cu-transpo.herokuapp.com/api/Devices'
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
		url = 'https://cu-transpo.herokuapp.com/api/Devices/login'
		values = {'deviceName' : deviceName,'password' : password}
		data = urllib.urlencode(values)
		req = urllib2.Request(url, data)
		print req
		response = urllib2.urlopen(req)
		#response.read()
		decoded = json.loads(response.read())
		access_token = decoded['id']
		print "Access Token: ", decoded['id']
	except urllib2.HTTPError:
		print "Login failed"

	query = urllib.urlencode({"access_token" : access_token})

	req_for_bus_timing = urllib2.Request('https://cu-transpo.herokuapp.com/api/Devices/getTimes?' + query)
	bus_timings_response = urllib2.urlopen(req_for_bus_timing)
	try:
		decoded = json.loads(bus_timings_response.read())
		destination = decoded['response']['data']['4'][1]['dest']
		times = decoded['response']['data']['4'][1]['times']
		print "Bus: 4"
		print "Destination: " + destination
		print "Times: " + times
	except (ValueError, KeyError, TypeError):
		print "JSON format error"

	stream = os.popen(" ".join(["sudo ./test2", "255,0,255", "60", "\"4 " + destination+"\"","\"", times[0] + "   " + times[1] + "   " + times[2]+"\""]),"w")


	time.sleep(5);
	rc = stream.close()
	if rc is not None and rc >> 8:
		print "There were some errors"


s.enter(10, 1, getNextTimes, (s,))
s.run()