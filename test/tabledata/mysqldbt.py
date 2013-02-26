'''
Created on Feb 13, 2013

@author: openjuice
'''
import unittest

from schemareader.reader import SchemaReader
from dbtype.mysqldbt import MySQLDBType

from pprint import pprint


class Test(unittest.TestCase):


    def setUp(self):
        schemaReader = SchemaReader('/media/WorkProject/work/generateData/schema.json');
        self.schema = schemaReader.read()
        pass

    def tearDown(self):
        pass

#    def testCreateTable(self):
#        mydqldbt = MySQLDBType(self.schema)
#        for table in self.schema.tables:
#            mysql = mydqldbt.createTableQuery(table)
#            pprint(mysql)
        
    def testInsertRecords(self):
        mydqldbt = MySQLDBType(self.schema)
        for table in self.schema.tables:
            mysql = mydqldbt.insertRecordsQuery(table)
            pprint(mysql)   


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()