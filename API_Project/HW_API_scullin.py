#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 21:19:12 2020

@author: 412foodrescue
"""

import requests, json

def url_toJSON(url):
    req = requests.get(url)
    if (int(req.status_code == 200)):
        #if thestatus code is 200 and everything works, then
        #load it into the variable apiDict
        apiDict = json.loads(req.text)
        #There is now this json file with the information from the API
        with open ('apiDict.txt', 'w') as f:
            json.dump(apiDict, f)
        #writes a txt file in the same directory that the program exists in
        print("There are", len(apiDict), "jobs including the term 'programmer'.")
        return apiDict


if __name__ == '__main__':
    url_toJSON('http://api.dataatwork.org/v1/jobs/autocomplete?ends_with="programmer"')

    