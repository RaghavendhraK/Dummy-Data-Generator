'''
Created on 12-Feb-2013

@author: abhilash
'''
from model.dgModel  import DGModel
from model.column import Column
from model.relation import Relation

class Table(DGModel):

    def __init__(self,data):
        self.name = data['name']
        if('count' in data.keys()):
            self.count =  data['count']
            
        self.tableName = data['table']
        self.columns = []
        self.relations = []
        for col in data['columns']:
            colObj = Column(col);
            colObj.setParent(self)
            self.columns.append(colObj)
        
        if 'relations' in data.keys():        
            for rel in data['relations']:
                relObj = Relation(rel);
                relObj.setParent(self)
                self.relations.append(relObj)
        
    def getCount(self):
        if(not(hasattr(self, 'count'))): self.count = self.parent.getCount() 
        return self.count
        