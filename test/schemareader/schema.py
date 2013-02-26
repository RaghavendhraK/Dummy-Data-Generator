'''
Created on 12-Feb-2013

@author: abhilash
'''
import unittest
from schemareader.reader import SchemaReader
from pprint import pprint


class SchemaReaderTest(unittest.TestCase):
    def setUp(self):
        self.schemaReader = SchemaReader('/media/WorkProject/work/generateData/schema.json');

    def tearDown(self):
        pass

    def testSchemaRead(self):
        self.schema = self.schemaReader.read()
        self.assertIsNotNone(self.schema, "Schema not read successfully ")
        pprint(self.schema)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()