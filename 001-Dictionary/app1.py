#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:57:29 2019

@author: azwri
"""

import json
from difflib import get_close_matches

myData = json.load(open("data.json"))

def printDef():
    x = input("Enter a word ...\n")
    x = x.lower()
    if x.capitalize() in myData:
        return myData[x.capitalize()]
    elif x.upper() in myData:
        return myData[x.upper()]
    elif x.lower() in myData:
        return myData[x.lower()]
    elif get_close_matches(x, myData.keys(), cutoff=0.8):
        x = get_close_matches(x, myData.keys())
        x = x[0]
        yn = input("Did you mean {} instaed? Enter Y if Yes, or N if No ... ".format(x))
        yn = yn.lower()
        if yn == 'y':
            return myData[x]
        elif yn == 'n':
            return 'The word dosen\'t exsit. Please duble check it.'
        else:
            return 'Sorry, we didn\'t understand you.'      
    else:
        return "The word did not exist. Please double check it."

while True:
    output = printDef()
    if type(output) == list:
        print("========================================")
        for i in output:
            print (i)
        print("========================================")

    else:
        print("========================================")
        print(output)
        print("========================================")
