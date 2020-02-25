#!/usr/bin/python3
""" Geolocation via IP Lookup """
from urllib import request
import json

try:
    data = json.load(request.urlopen('http://ipinfo.io/json'))
except Exception as e:
    print(e)
else:
    print('Your IP Address: {}'.format(data['ip']))
    print('     You are near: {city}, {region}, {country}'.format(**data))
    print('     Lat/Lng: {}E'.format(data['loc'].replace(',','N, ')))