'''
Created on 12-Feb-2013

@author: abhilash
'''
import unittest
from datatype.parentcolumn import ParentColumnDataType


class Test(unittest.TestCase):


    def testParentColumn(self):
        pcdt = ParentColumnDataType({'column':'user'})
        self.assertEqual('Abhi', pcdt.get({'parent-columns':{'user':'Abhi'}}), "Unexpected result.")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()