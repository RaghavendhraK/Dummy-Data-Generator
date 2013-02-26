'''
Created on 12-Feb-2013

@author: abhilash
'''
from model.dgModel import DGModel
from model.postprocess import ColumnPostProcess
from model.colcheck import ColumnCheck
from util.util import Util

class Column(DGModel):
    
    __DTPath = "datatype."
    __DefResName = "__user__"
    
    def __init__(self,data):
        self.colName = data.keys().pop()
        self.details = data.values().pop();
        self.colType = self.details['type']; 
        
        if('post-process' in self.details):
            self.postProcess = ColumnPostProcess(self.details['post-process'])
        if('check' in self.details):
            self.postProcess = ColumnCheck(self.details['check'])
        if('resource' in self.details):
            self.resourceName = self.details['resource']
        else:
            self.resourceName = self.__DefResName
    
    def getDTObject(self):
        if(not hasattr(self, 'dtObj')):    
            dtObjName = Util.getDTObjName(self.colType)
            
            try:
                # import the module
                module = __import__(self.__DTPath + self.colType,fromlist=[dtObjName])
                dtObj = getattr(module, dtObjName)
            except:
                raise Exception("module {0} not implemented yet".format(dtObjName))
            
            try:
                self.dtObj = dtObj(self.details)
            except:
                print("Exception in DataType initialization")
            
        return self.dtObj
    
    def get(self, rowIndex, data):
        return self.dtObj.get(rowIndex, data)
