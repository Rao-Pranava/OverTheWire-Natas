#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re

#Declaring the Authentication
username = 'natas1'
password = 'g9D9cREhslqBKtcA2uocGHPfMZVzeFK6'
url = 'http://%s.natas.labs.overthewire.org/' %username

#Functions
response = requests.get(url, auth = (username, password))
content = response.text

#Printing the Source Code
#print(content)

#Printing only the Password
print(re.findall('natas2 is (.*) -->', content)[0])