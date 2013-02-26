'''
Created on 12-Feb-2013

@author: abhilash
'''
import unittest

class Test(unittest.TestCase):
    
    __DTPath = "datatype.auto-increment"
    __ObjName = "AutoIncrementDataType"

    def setUp(self):
        module = __import__(self.__DTPath,fromlist=[self.__ObjName])
        self.dtObj = getattr(module, self.__ObjName)
    
    def testAutoIncDataSource(self):
        aids = self.dtObj({});
        self.assertEqual("1", aids.get(0), 'Unexpected value from AIDS');
        self.assertEqual("2", aids.get(1), 'Unexpected value from AIDS');
        self.assertEqual("3", aids.get(2), 'Unexpected value from AIDS');
        self.assertEqual("4", aids.get(3), 'Unexpected value from AIDS');
        pass
    
    def testAutoIncDataSourceWithInit(self):
        aids = self.dtObj({'start':10});
        self.assertEqual("11", aids.get(1), 'Unexpected value from AIDS');
        self.assertEqual("12", aids.get(2), 'Unexpected value from AIDS');
        self.assertEqual("13", aids.get(3), 'Unexpected value from AIDS');
        self.assertEqual("14", aids.get(4), 'Unexpected value from AIDS');
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAutoIncDataSource']
    unittest.main()