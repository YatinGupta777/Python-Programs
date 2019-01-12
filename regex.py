#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 16:10:11 2018

@author: yatingupta
"""

import re

dataset = open("regex_sum_136887","r")
text = dataset.read()
x = list()
x.append(re.findall('[0-9]+',text))
sum = 0
for i in x:
    for j in i :
        sum += int(j)
    
print(sum)