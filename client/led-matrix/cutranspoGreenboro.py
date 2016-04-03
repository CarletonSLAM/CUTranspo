#!/usr/bin/env python
import urllib
import urllib2
import json
from pprint import pprint
import sched, time
from subprocess import Popen, PIPE
import os
import time

deviceName = 'rpiG'
password = '12345'

s = sched.scheduler(time.time, time.sleep)
PROGRAM_PATH = os.getcwd() + '/display-text'

try:
	url = 'https://cu-transpo.herokuapp.com/api/Devices'
	values = {'deviceName' : deviceName,'password' : password, 'stopNo' : '3037'}
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
		destination_1 = decoded['response']['data']['1'][1]['dest']
		times_1 = decoded['response']['data']['1'][1]['times']

		destination_87 = decoded['response']['data']['87'][1]['dest']
		times_87 = decoded['response']['data']['87'][1]['times']

		print "Bus: 1"
		print "Destination: " + destination_1
		#print "Times: " + times_4
		print "Bus: 87"
		print "Desination: " + destination_87
	except (ValueError, KeyError, TypeError):
		print "JSON format error"

	stream = Popen(["sudo", PROGRAM_PATH, "200,10,0", "80", "1 " + destination_1, times_1[0] + "  " + times_1[1]], stdin=PIPE, stderr=PIPE, universal_newlines=True)
	print stream
	
	time.sleep(5);
	print stream.terminate()
	#if rc is not None and rc >> 8:
	#	print "There were some errors"
	stream = Popen(["sudo", PROGRAM_PATH, "200,10,0", "80", "87 " + destination_87, times_87[0] + "  " + times_87[1]], stdin=PIPE, stderr=PIPE, universal_newlines=True)
	time.sleep(5)
	print stream.terminate()
	s.enter(0.05, 1,getNextTimes, (s,))
	s.run()	
getNextTimes(s)
