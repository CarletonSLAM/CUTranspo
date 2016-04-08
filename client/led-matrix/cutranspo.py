import urllib
import urllib2
import json
from pprint import pprint
import sched, time
from subprocess import Popen, PIPE
import os
import time

stopNo = '5813'
deviceName = 'rpi' + stopNo
password = '1234'

s = sched.scheduler(time.time, time.sleep)
PROGRAM_PATH = os.getcwd() + '/display-text'

try:
	url = 'https://cu-transpo.herokuapp.com/api/Devices'
	values = {'deviceName' : deviceName,'password' : password, 'stopNo' : stopNo}
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

		li = []

		for i in decoded['response']['data']:
			li.append(i)

		for i in li:
			if len(decoded['response']['data'][i][0]['times']) > 0:
				stream = Popen(["sudo", PROGRAM_PATH, "200,10,0", "80", i + decoded['response']['data'][i][0]['dest'], decoded['response']['data'][i][0]['times'][0] + "  " + decoded['response']['data'][i][0]['times'][1]], stdin=PIPE, stderr=PIPE, universal_newlines=True)
				time.sleep(5)
				print stream.terminate()
				print i + "   " + decoded['response']['data'][i][0]['dest']
				print decoded['response']['data'][i][0]['times']
			else:
				stream = Popen(["sudo", PROGRAM_PATH, "200,10,0", "80", i + decoded['response']['data'][i][1]['dest'], decoded['response']['data'][i][1]['times'][0] + "  " + decoded['response']['data'][i][1]['times'][1]], stdin=PIPE, stderr=PIPE, universal_newlines=True)
				time.sleep(5)
				print stream.terminate()
				print i + "   " + decoded['response']['data'][i][1]['dest']
				print decoded['response']['data'][i][1]['times']
		
	except (ValueError, KeyError, TypeError):
		print "JSON format error"

	# stream = Popen(["sudo", PROGRAM_PATH, "200,10,0", "80", "4 " + destination_4, times_4[0] + "  " + times_4[1]], stdin=PIPE, stderr=PIPE, universal_newlines=True)
	# print stream	
	# time.sleep(5);
	# print stream.terminate()
		
	# stream = Popen(["sudo", PROGRAM_PATH, "200,10,0", "80", "104 " + destination_104, times_104[0] + "  " + times_104[1]], stdin=PIPE, stderr=PIPE, universal_newlines=True)
	# time.sleep(5)
	# print stream.terminate()
	s.enter(0.05, 1,getNextTimes, (s,))
	s.run()
getNextTimes(s)