'''
Created on Feb 13, 2013

@author: openjuice
'''
class SqlFormatter(object):

    def __init__(self,table):
        self.table = table
    
    def getCreateTableQuery(self):
        query = "CREATE TABLE IF NOT EXISTS {0} (".format(self.table.tableName)
        for col in self.table.columns:
            colType = self.__getMySQLConstants(col.colType)
            query += "{0} {1},".format(col.colName,colType)
        query = query[:-1] + ")"
        return query
    
    def getInsertRecordsQuery(self, data):
        colNames = [col.colName for col in self.table.columns]
        recordValues = []
        for row in data:
            recordValues.append("'" + "','".join(row) + "'")
        colValues = "(" + "),(".join(recordValues) + ")"
        query = "INSERT INTO {0} ({1}) VALUES {2}".format(self.table.tableName, "`" + "`,`".join(colNames) + "`", colValues)
        return query
    
    def __getMySQLConstants(self, colType):
        try:
            DBType = {"name":"VARCHAR(50)","auto-increment":"INT","email":"VARCHAR(100)"}
            return DBType[colType]
        except:
            return "VARCHAR(255)"