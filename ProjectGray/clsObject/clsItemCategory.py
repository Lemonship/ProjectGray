from clsObject import clsObject
from modSQLDAL import ModuleClass
class clsItemCategory(clsObject):
    count = 0
    keyList = ['Tablename']
    paramList = ['Classname', 'Category', 'FieldInfo', 'ObjMap']
    fieldList = keyList + paramList
    SQLTableName = 'ItemCategory'
    ClassName = __name__
    
    def __init__(self, Tablename, Classname, Category, FieldInfo, ObjMap):
        clsItemCategory.count += 1
        self.Tablename=Tablename
        self.Classname=Classname
        self.Category=Category
        self.FieldInfo=FieldInfo
        self.ObjMap=ObjMap
        
