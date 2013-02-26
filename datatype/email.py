'''
Created on 12-Feb-2013

@author: abhilash
'''
class EmailDataType():
    reqSource = True
    srcResource = 'user_data'
    resource = '__user__'
    reqData = ['email']

    def __init__(self,coldefn = None):
        pass
    
    def get(self, rowCount, data = []):
        return data['email']