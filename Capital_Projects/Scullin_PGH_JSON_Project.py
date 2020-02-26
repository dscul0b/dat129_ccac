#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:13:43 2020

@author: Dan Scullin

1. For this module, I will import a CSV file, and using a JSON interface, I will:
    a) loop through the csv file to see which projects (proj) match inputed search 
    paramaters. 
    b) create a file of Project IDs that have a blank in certain fields
    

"""
import csv
import json


def log_list_of_filters (project):
    with open ('log_filtered_list', 'a') as log:
        log.write(project['id'])
        log.write('/n')
    
def log_malformed_list (project):
    with open('log_malformed_list', 'a') as log:
        log.write(project['id'])
        log.write('\n')
        
with open ('Pgh_JSON.txt', 'r') as filters:
    Pgh_JSON = json.load(filters)
    """
    Now the variable 'Pgh_JSON' contains the JSON File that has the parameters we 
    need to do the search. 
    """

with open ("Capital_Projects.csv", 'r') as proj:
    reader = csv.DictReader(proj)
    """
    This opens the Capital_Projects csv into python as the variable 'reader'.
    """
    for row in reader:
        if row['area']=="":
            "if the row is blank"
            log_malformed_list(row)  
        if row['fiscal_year'] == Pgh_JSON['fiscal_year']:
            """If the row in the CSV for fiscal_year matches the value in the JSON
            file for fiscal_year
            """
            log_list_of_filters(row)

            
