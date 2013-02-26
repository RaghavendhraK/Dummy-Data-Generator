'''
Created on Feb 15, 2013

@author: openjuice
'''
import re

class Util(object):

    @staticmethod
    def getDTObjName(dtName):
        dtSuffix = 'DataType'
        
        ##remove the special characters and CamelCase with DT Suffix at the end
        pattern = re.compile('[\W_]+')
        dtObjName = pattern.sub(' ', dtName)
        dtObjName =''.join(x for x in dtObjName.title() if not x.isspace()) + dtSuffix
        
        return dtObjName