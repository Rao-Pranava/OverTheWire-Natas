#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re

#Declaring the Authentication
username = 'natas8'
password = 'a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB'
url = 'http://%s.natas.labs.overthewire.org/' %username

#Functions
session = requests.session()
response = session.post(url, auth = (username, password), data = {"secret" : "oubWYf2kBq", "submit" : "submit"})
content = response.text

#Printing the Source Code
#print(content)

#Printing only the Password
print(re.findall('natas9 is (.*)', content)[0])