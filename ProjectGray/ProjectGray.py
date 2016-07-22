import modSQLDAL
from modSQLDAL import Module
from modSQLDAL import ModuleClass
from modSQLDAL import SQLDataType as Type
import modSysFile
import modTestingData
##modTestingData.CreateSQLTable()

##Initization ==================================================================================
Module('modInitization').InitSystemFiles()
print Module('modSysFile').GetFunctionList('modSQLDAL.modSQLDAL')

##modSysFile.InsertPath(modSysFile.GetSystemFolderPathList(modSysFile.ProjectPath))
##for ModuleFile in modSysFile.GetSystemFileList(modSysFile.ProjectPath, ['py']):
##    if not ModuleFile == "ProjectGray":
##        print ModuleFile
##        FunctionList = []
##        for ModuleName in Module('modSysFile').GetClassList(ModuleFile):
##            FunctionList+=modSysFile.GetFunctionList(ModuleName)
##        print FunctionList
##Module('modSysFile').GetFunctionList('clsMSSQL')

##print Module('modSysFile').GetFunctionList('clsMSSQL.MSSQL')


##Module('modInitization').CreateSystemTable()
##Module('modInitization').CreateAllObjectClass()

##Data Preparation =============================================================================
##modTestingData.RunTestingData()


##Item = modSQLDAL.SQLGetObject("clsUnClassObj", "WHERE [Name] = 'Item1'")[0]
##Connection = ModuleClass('clsObjMap')(Item[0].ObjMap)



##ResultList = Connection.FindByTextToObject('Gary')
##for Item in ResultList:
##    print Item.GetValueList(Item.fieldList)
##ResultList = Connection.FindByFieldToObject('clsPeople','Name','Kenneth Tse')
##for Item in ResultList:
##    print Item.GetValueList(Item.fieldList)
##ResultList = Connection.FindClassObject('clsPeople')
##for Item in ResultList:
##    print Item.GetValueList(Item.fieldList)
##ResultList = Connection.FindAllObject("Teammate")

##for Item in ModuleClass('clsObjMap')(Item.ObjMap).FindAllObject("Teammate"):
##    print Item.GetValueList(Item.fieldList)
    
##Print Result ========================================================================================================
##ResultList = modSQLDAL.SQLGetObject('clsUnClassObj')
##for Item in ResultList:
##    print Item.GetValueList(Item.fieldList)
##
##ResultList = modSQLDAL.SQLGetObject('clsPeople')
##for Item in ResultList:
##    print Item.GetValueList(Item.fieldList)
##
##



