'''
Created on Feb 25, 2013

@author: openjuice
'''
import unittest
from pprint import pprint

class Test(unittest.TestCase):

    def setUp(self):
        module = __import__("controller.controller",fromlist=["DummyDataController"])
        self.obj = getattr(module, "DummyDataController")
    
    def testName(self):
        schemaPath = "/media/WorkProject/work/generateData/schema.json"
        contr = self.obj(schemaPath)
        contr.readSchema()
        contr.generateData()
        contr.formatData()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()