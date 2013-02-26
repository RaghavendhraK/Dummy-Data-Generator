'''
Created on 12-Feb-2013

@author: abhilash
'''
import unittest
import time
from datatype.timedt import TimeDataType

class DateTimeTest(unittest.TestCase):

    def testDateTime(self):
        dtt = TimeDataType();
        retDate = dtt.get({});
        print "Date is " + retDate
        print "Comp-Old: " + getTime(retDate).__str__() + " - " + getTime('1990-1-1 12:00 AM').__str__()
        self.assertGreater(getTime(retDate),\
                            getTime('1990-1-1 12:00 AM'), \
                            "Returned time is too old");
        print "Comp-New: " + getTime(retDate).__str__() + " - " + time.time().__str__()
        self.assertLess(getTime(retDate), time.time(), "Returned time is too new")
        pass
    
    def testDateTimeWithRange(self):
        dtt = TimeDataType({"range":["1988-12-20 12:00 AM","1989-12-20 12:00 AM"]});
        retDate = dtt.get({});
        print "Date is " + retDate
        print "Comp-Old: " + getTime(retDate).__str__() + " - " + getTime("2012-12-20 12:00 AM").__str__()
        self.assertGreater(getTime(retDate),\
                            getTime("1988-12-20 12:00 AM"), \
                            "Returned time is too old");
        print "Comp-New: " + getTime(retDate).__str__() + " - " + time.time().__str__()
        self.assertLess(getTime(retDate), getTime("1989-12-20 12:00 AM"), "Returned time is too new")
        pass
    
    def testDateTimeOpFormat(self):
        dtt = TimeDataType({"format":"%d-%m-%Y %I:%M %p"});
        retDate = dtt.get({})
        print "Formatted date is: " + retDate
        self.assertRegexpMatches(retDate,'\d\d?-\d\d?-\d\d\d\d \d\d?:\d\d? [AP]M' ,'Format doesnt match')
        dtt = TimeDataType();
        retDate = dtt.get({})
        print "Un Formatted date is: " + retDate
        self.assertNotRegexpMatches(retDate,'\d\d?-\d\d?-\d\d\d\d \d\d?:\d\d? [AP]M' ,'Format doesnt match')
        pass
#    def testDateTimeWithRangeOpformat(self):
#        dtt = TimeDataType({"range":["2012-12-20 12:00 AM","now"]});
#        print dtt.get({});
#        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDateTime']
    unittest.main()
    
def getTime(timestr,tformat = TimeDataType.timeFormat):
    return time.mktime(time.strptime(timestr,tformat));