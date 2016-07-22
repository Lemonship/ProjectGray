from clsObject import clsObject
from modSQLDAL import ModuleClass
class clsPeople(clsObject):
    count = 0
    keyList = ['Name', 'Serial']
    paramList = ['ObjMap', 'Age', 'Gender', 'Remarks']
    fieldList = keyList + paramList
    SQLTableName = 'People'
    ClassName = __name__
    
    def __init__(self, Name, Serial, ObjMap, Age, Gender, Remarks):
        clsPeople.count += 1
        self.Name=Name
        self.Serial=Serial
        self.ObjMap=ObjMap
        self.Age=Age
        self.Gender=Gender
        self.Remarks=Remarks
        
