'''
Created on 12-Feb-2013

@author: abhilash
'''

class NameDataType(object):
    reqSource = True
    srcResource = 'user_data'
    resource = '__user__'
    reqData = ['first_name','middle_name','last_name']
    nameType = 'first last'

    def __init__(self,coldefn = None):
        if(coldefn is not None):
            self.nameType = coldefn['name-type']

    def get(self, rowIndex, data = []):
        value = self.nameType
        if('first_name' in data):
            value = value.replace('first',data['first_name'])
        if('middle_name' in data):
            value = value.replace('middle',data['middle_name'])
        if('last_name' in data):
            value = value.replace('last',data['last_name']);
        return value
        