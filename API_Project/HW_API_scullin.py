#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 21:19:12 2020

@author: 412foodrescue
"""

import json
import requests


def log_result(data):
    """Return formatted log of job counts"""
    msg = f'There are {len(data)} jobs including the term \'programmer\''
    print(msg)


def create_url(keyword):
    """Create API call URL string"""
    url = (f'http://api.dataatwork.org/v1/jobs/' +
           f'autocomplete?ends_with="{keyword}"')
    return url


def url_toJSON(url):
    """Calls API and writes queried data into a JSON file

    Args:
        url: URL string which contain the parameter of the query
    """
    req = requests.get(url)
    if (int(req.status_code == 200)):
        apiDict = json.loads(req.text)
        with open ('apiDict.txt', 'w') as f:
            json.dump(apiDict, f, indent=4)
        log_result(apiDict)
        return apiDict


if __name__ == '__main__':
    api_query = create_url('programmer')
    url_toJSON(api_query)
