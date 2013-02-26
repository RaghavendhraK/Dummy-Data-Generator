'''
Created on 12-Feb-2013

@author: abhilash
'''
import json
from model.schema import Schema

class SchemaReader():
    def __init__(self,filePath):
        self.filePath = filePath
        
    def read(self):
        fileObj = open(self.filePath);
        schema = json.load(fileObj)
        fileObj.close()
        return Schema(schema)     
    