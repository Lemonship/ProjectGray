import modSQLDAL
from modSQLDAL import ModuleClass
from clsObjMap import clsObjMap
class clsObject(object):
    count = 0

        
    def GetValue(self, FieldName):
        if FieldName in self.fieldList:
            return eval("self.{0}".format(FieldName))
        else:
            return None

    def GetValueList(self, FieldList):
        strCommand = ""
        for FieldName in FieldList:
            strCommand += ",self.{0}".format(FieldName)
        Result = eval('[{0}]'.format(strCommand[1:]))
        return Result
        
    def Update(self):
        modSQLDAL.SQLAddAndUpdateObject(self)
        return self

    def AddObjMap(self, TypeName, MapObject):
        MapObj = clsObjMap(self.ObjMap)
        MapObj.AddElement(TypeName,MapObject)
        self.ObjMap = MapObj.ToString()
        return self
    
        

