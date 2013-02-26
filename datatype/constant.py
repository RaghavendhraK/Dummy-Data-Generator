'''
Created on 12-Feb-2013

@author: abhilash
'''

class ConstantDataType():
    
    reqSource = False
    
    def __init__(self,coldefn):
        self.value = coldefn['value']
        
    def get(self, rowCount, data=[]):
        return self.value