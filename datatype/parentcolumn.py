'''
Created on 12-Feb-2013

@author: abhilash
'''

class ParentColumnDataType():

    def __init__(self,coldefn):
        self.column = coldefn['column']
    
    
    def get(self,data={}):
        return data['parent-columns'][self.column]
    