#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 12:16:56 2018

@author: hannaholdorf
"""

#%% SOng Lyrics

import requests
json_data = requests.get("https://api.lyrics.ovh/v1/George Ezra/Budapest").json()


print (json_data)
#%% Long and Lat of ISS

import requests

ISS = requests.get("http://api.open-notify.org/iss-now.json").json()


print (ISS["iss_position"]["longitude"])
print (ISS["iss_position"]["latitude"]) 
