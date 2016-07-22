import modSysFile
import modSQLDAL
from modSQLDAL import Module
from modSQLDAL import SQLDataType as Type



##Init System Files ==========================================================================================
def InitSystemFiles():
    modSysFile.InsertPath(modSysFile.GetSystemFolderPathList(modSysFile.ProjectPath))

    for ModuleFileName in modSysFile.GetSystemFileList(modSysFile.ProjectPath, ['py']):
        if not ModuleFileName == "ProjectGray":
            print ModuleFileName
            FunctionList = []
            for ModuleName in Module('modSysFile').GetClassList(ModuleFileName):
                FunctionList+=modSysFile.GetFunctionList(ModuleName)
            print FunctionList


##Recreate Object Class ======================================================================================
def CreateAllObjectClass():    
    modSQLDAL.CreateClassFromDBTable('clsItemCategory','ItemCategory')
    ClassList = modSQLDAL.SQLGetObject("clsItemCategory")
    for Class in ClassList:
##        print Class.Classname,Class.Tablename
        modSQLDAL.CreateClassFromDBTable(Class.Classname,Class.Tablename)

def CreateSystemTable():
##ItemCategory ===============================================================================================
    SQLTableName = 'ItemCategory'
    ClassName = 'cls' + SQLTableName
    KeyList = ['Tablename']
    KeyType = [Type.Nvarchar(100)]
    ParaList = ['Classname', 'Category', 'FieldInfo', 'ObjMap']
    ParaType = [Type.Nvarchar(100),Type.Nvarchar(200),Type.Xml,Type.Xml]
    if (not modSQLDAL.SQLTableExist(SQLTableName)):
        modSQLDAL.SQLCreateTable(SQLTableName,KeyList,KeyType,ParaList,ParaType)
    
