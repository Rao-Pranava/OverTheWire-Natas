#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re

#Declaring the Authentication
username = 'natas0'
password = 'natas0'
url = 'http://%s.natas.labs.overthewire.org/' %username

#Functions
response = requests.get(url, auth = (username, password))
content = response.text

#Printing the Source Code
#print(content)

#Printing only the Password
print(re.findall('natas1 is (.*) -->', content)[0])