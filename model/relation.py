'''
Created on 12-Feb-2013

@author: abhilash
'''
from model.dgModel import DGModel 
from model.column import Column

class Relation(DGModel):
    ONE_TO_ONE = 'one-to-one'
    ONE_TO_MANY = 'one-to-many'
    MANY_TO_ONE = 'many-to-one'
    MANY_TO_MANY = 'many-to-many'
    
    def __init__(self,data):
        self.table = data['table']
        self.type = data['type']
        if('count' in data.keys()): self.count = data['count']
        self.columns = []
        for col in data['columns']:
            colOjb = Column(col)
            colOjb.setParent(self)
            self.columns.append(colOjb)
            
    def getCount(self):
        if(self.type in [self.ONE_TO_ONE, self.MANY_TO_ONE]):
            return 1;
        elif(hasattr(self,'count')):
            return self.count
        else:
            return self.parent.getCount();