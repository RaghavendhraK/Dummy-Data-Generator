'''
Created on 12-Feb-2013

@author: abhilash
'''
from model.table import Table
from model.dgModel import DGModel

class Schema(DGModel):

    def __init__(self,data):
        self.name = data['name']
        self.dataCount = data['data-count']
        self.tables = []
        for tbl in data['data-defns']:
            tblObj = Table(tbl)
            tblObj.setParent(self)
            self.tables.append(tblObj)
            
    def getCount(self):
        return self.dataCount