'''
Created on 12-Feb-2013

@author: abhilash
'''
import unittest
from datatype.name import NameDataType


class Test(unittest.TestCase):


    def testNameDatasource(self):
        nds = NameDataType();
        self.assertEqual('Abhilash Hebbar', nds.get(
                {'first_name':'Abhilash','middle_name':'S','last_name':'Hebbar'}
            ), 'Unexpected name')
    
#    def testNameDataSourceWithFN(self):
#        nds = NameDataType({'name-type':'last, first'});
#        self.assertEqual('Abhi', nds.get(), 'Unexpected name');


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNameDatasource']
    unittest.main()