'''
    Create.py module contains classes for creating various objects
    for the agency mission from json templates which are in the
    `../templates/` directory.
    
    methods
    =======

    create.mission.default(template_path)
'''
import json


# class definitions

class mission():

    def dictionary_from(path):
        ''' 
           Load the blank json template from the file in the path.
           This is a generic method that converts a json file to
           a python dictionary and returns the dictionary.
        ''' 
        
        with open(path, 'r') as f:
            template_dict = json.load(f)
            
        return template_dict
