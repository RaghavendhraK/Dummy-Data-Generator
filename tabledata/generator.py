'''
Created on 12-Feb-2013

@author: abhilash
'''

from datastore.dataStore import DataStore
from datasource.db import DB

class TableDataGenerator():
    
    def __init__(self, schema):
        self.schema = schema

    def generateData(self):
        tableDatas = {}
        for table in self.schema.tables:
            tableDatas[table.tableName] = self.__generateRowDatasForTable(table)
        return tableDatas
    
    def __generateRowDatasForTable(self, table):
        self.totalCount = table.columns[0].parent.getCount()
        
        self.dStore = DataStore()
        if(self.dStore.prepareData(table)):
            dbData = self.__getDBData()            

            rowValues = []
            for i in range(0,self.totalCount):
                rowVal = []
                for col in table.columns:                 
                    rowData = dbData[col.resourceName].values().pop()
                    colValue = col.get(i,rowData[i])
                    rowVal.append(colValue)
                rowValues.append(rowVal)
            return rowValues
        else:
            return False
        
    def __getDBData(self):
        db = DB() 
        dbData = {}           
        user_data_names = self.dStore.data.keys()
        for user_data_name in user_data_names:
            srcResources = self.dStore.data[user_data_name].keys()
            for srcRes in srcResources:
                reqFields = self.dStore.data[user_data_name][srcRes]['requireFields']
                db.prepareQuery(srcRes, reqFields, self.totalCount)
                if db.execute():
                    if not dbData.has_key(user_data_name):
                        dbData[user_data_name] = {}
                    dbData[user_data_name][srcRes] = db.result
        return dbData
        