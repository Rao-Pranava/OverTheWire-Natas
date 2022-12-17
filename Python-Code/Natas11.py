#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re

#Declaring the Authentication
username = 'natas11'
password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'
url = 'http://%s.natas.labs.overthewire.org/' %username

#Functions
session = requests.session()
Cookie = {"data" : "MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz"}
response = session.post(url, auth = (username, password), cookies = Cookie)
content = response.text

#Printing the Source Code
#print(content)

#Printing only the Password
print(re.findall('natas12 is (.*)<br>', content)[0])