from clsObject import clsObject
from modSQLDAL import ModuleClass
class clsUnClassObj(clsObject):
    count = 0
    keyList = ['Name', 'Serial']
    paramList = ['ObjMap', 'Description']
    fieldList = keyList + paramList
    SQLTableName = 'UnClassObj'
    ClassName = __name__
    
    def __init__(self, Name, Serial, ObjMap, Description):
        clsUnClassObj.count += 1
        self.Name=Name
        self.Serial=Serial
        self.ObjMap=ObjMap
        self.Description=Description
        
