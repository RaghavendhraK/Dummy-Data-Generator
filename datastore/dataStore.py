'''
Created on Feb 20, 2013

@author: openjuice
'''
class DataStore(object):

    data = {}
    
    def __init__(self):
        pass
    
    def prepareData(self,table):
        for column in table.columns:
            self.addRequiredFields(column)
        return True                   
    
    def addRequiredFields(self,column):
        column.getDTObject()
        if hasattr(column.dtObj,"reqSource") and column.dtObj.reqSource:
            dtObj = column.dtObj
            res = column.resourceName
            if not self.data.has_key(res):
                self.data[res] = {}
            if not self.data[res].has_key(dtObj.srcResource):
                self.data[res][dtObj.srcResource] = {}
            if not self.data[res][dtObj.srcResource].has_key("requireFields"):
                self.data[res][dtObj.srcResource]['requireFields'] = dtObj.reqData
            else:
                remDuplFields = list(set(dtObj.reqData) - set(self.data[res][dtObj.srcResource]['requireFields']))
                self.data[res][dtObj.srcResource]['requireFields'] = self.data[res][dtObj.srcResource]['requireFields'] + remDuplFields
        
        