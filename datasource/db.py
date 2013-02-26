'''
Created on Feb 18, 2013

@author: openjuice
'''

import MySQLdb

class DB(object):
    
    SERVER = "127.0.0.1"
    USER_NAME = "root"
    PASSWORD = ""
    DB_NAME = "dummy_data_gen"
    
    def __init__(self):
        if(not hasattr(self,'dbObj')):
            self.dbObj = MySQLdb.connect(self.SERVER, self.USER_NAME, self.PASSWORD, self.DB_NAME)
            self.cursor = self.dbObj.cursor()
            self.query = None
            self.result = None
    
    def execute(self):
        self.result = []
        self.cursor.execute(self.query)
        results = self.cursor.fetchall()
        columnNames = tuple( [d[0].decode('utf8') for d in self.cursor.description] )
        for row in results:
            self.result.append(dict(zip(columnNames, row)))
        return self.cursor.rowcount
    
    def prepareQuery(self, srcResource, reqFields, limit):
        self.reqFields = reqFields
        CSFields = "`,`".join(reqFields)
        self.query = "SELECT `{0}` FROM {1} ORDER BY RAND() LIMIT {2}".format(CSFields, srcResource, limit)        
    
    def close_db(self):
        self.dbObj.close()