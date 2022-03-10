"""
Lab 126-File Handlers and modules
"""
import json

def readJsonFile(fileName):
    data=""
    with open('files/insulin.json') as json_file:
        data=json.load(json_file)
    return data


    