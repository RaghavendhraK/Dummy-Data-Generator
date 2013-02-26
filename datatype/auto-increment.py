'''
Created on 12-Feb-2013

@author: abhilash
'''

class AutoIncrementDataType():
    
    def __init__(self,coldefn=None):
        if(not(coldefn is None) and ('start' in coldefn.keys())):
            self.start = coldefn['start']
        else:
            self.start = 1
        
    def get(self, rowCount, data=[]):
        return str(rowCount + int(self.start))