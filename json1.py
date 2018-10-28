#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 19:08:25 2018

@author: yatingupta
"""

import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter location: ')

uh = urllib.request.urlopen(url)
data = uh.read()
info = json.loads(data)
sum = 0
for item in info['comments']:
    sum += item['count']
    
print(sum)    