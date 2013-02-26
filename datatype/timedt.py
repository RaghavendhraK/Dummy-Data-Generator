'''
Created on 12-Feb-2013

@author: abhilash
'''
import random
import time

class TimedtDataType():
 
    reqSource = False
    timeFormat = '%Y-%m-%d %I:%M %p'
    
    def __init__(self,coldefn={}):
        self.start = time.mktime(time.strptime('1990-1-1 12:00 AM', self.timeFormat))
        self.end = time.time()
        self.opFormat = self.timeFormat
        if('range' in coldefn):
            self.start = self.getTimeFrom(coldefn['range'][0])
            self.end   = self.getTimeFrom(coldefn['range'][1])
        if('format' in coldefn):
            self.opFormat = coldefn['format']
        
    def get(self, rowCount, data=[]):
        return time.strftime(self.opFormat, time.localtime( \
                        self.start + random.random() * (self.end - self.start) \
                    ))
    
    def getTimeFrom(self,datestr):
        if(datestr == 'now'):
            return time.time()
        return time.mktime(time.strptime(datestr,self.timeFormat))