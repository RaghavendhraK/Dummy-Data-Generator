'''
Created on Feb 21, 2013

@author: openjuice
'''
from schemareader.reader import SchemaReader
from tabledata.generator import TableDataGenerator
from dataformatter.sqlformatter import SqlFormatter
from pprint import pprint

class DummyDataController(object):

    def __init__(self, schemaPath):
        self.schemaPath = schemaPath
        self.schemaPath = '/media/WorkProject/work/generateData/schema.json'
    
    def readSchema(self):
        #read schema
        schemaReader = SchemaReader(self.schemaPath);
        self.schema = schemaReader.read()
        
    def generateData(self):
        #get data for schema
        generator = TableDataGenerator(self.schema)
        self.data = generator.generateData()
        pprint(self.data)
    
    def formatData(self):
        #format the generated data
        self.formattedData = []
        for table in self.schema.tables:
            sqlFormatter = SqlFormatter(table)
            if(self.data[table.tableName]):
                self.formattedData.append(sqlFormatter.getInsertRecordsQuery(self.data[table.tableName]))
            else:
                print("Error happened for table `{0}`".format(table.tableName))
        pprint(self.formattedData)        