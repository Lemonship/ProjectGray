import modSQLDAL
from modSQLDAL import ModuleClass
from modSQLDAL import SQLDataType as Type


##Testing Data ========================================================================================================
def RunTestingData():
    ##Item = modSQLDAL.SQLGetObject(ClassName)[0]
    People = ModuleClass('clsPeople')('Kenneth Tse',0,'',30,'M','Remarks').Update()
    People = ModuleClass('clsPeople')('Tim Li',0,'',28,'M','Remarks').Update()
    People = ModuleClass('clsPeople')('Gary Li',0,'',35,'M','Remarks').Update()
    People = ModuleClass('clsPeople')('Tony Man',0,'',40,'M','Remarks').Update()

    People = modSQLDAL.SQLGetObject("clsPeople", "WHERE [Name] = 'Kenneth Tse'")
    Item = ModuleClass('clsUnClassObj')('Item1',0,'','Item1 Description')
    Item = Item.AddObjMap('Friend',People[0]).Update()
    People = modSQLDAL.SQLGetObject("clsPeople", "WHERE [Name] = 'Gary Li'")
    Item = Item.AddObjMap('Teammate',People[0]).Update()
    People = modSQLDAL.SQLGetObject("clsPeople", "WHERE [Name] = 'Kenneth Tse'")
    ModuleClass('clsUnClassObj')('Item2',0,'','Item2 Description').AddObjMap('Teammate',People[0]).Update()
    People = modSQLDAL.SQLGetObject("clsPeople", "WHERE [Name] = 'Kenneth Tse'")
    ModuleClass('clsUnClassObj')('Item3',0,'','Item3 Description').AddObjMap('Teammate',People[0]).Update()



####Create SQL Table =================================================================================================

def CreateSQLTable():
    MAX = 'MAX'

    SQLTableName = 'People'
    ClassName = 'cls' + SQLTableName
    KeyList = ['Name','Serial']
    KeyType = [Type.Nvarchar(50),Type.Integer]
    ParaList = ['ObjMap', 'Age', 'Gender', 'Remarks']
    ParaType = [Type.Xml,Type.Integer,Type.Nvarchar(5),Type.Nvarchar(MAX)]
####    modSQLDAL.SQLDropTable(SQLTableName)
    if (not modSQLDAL.SQLTableExist(SQLTableName)):
        modSQLDAL.SQLCreateTable(SQLTableName,KeyList,KeyType,ParaList,ParaType)    
        
    SQLTableName = 'UnClassObj'
    ClassName = 'cls' + SQLTableName
    KeyList = ['Name','Serial']
    KeyType = [Type.Nvarchar(50),Type.Integer]
    ParaList = ['ObjMap','Description']
    ParaType = [Type.Xml,Type.Nvarchar(MAX)]
####    modSQLDAL.SQLDropTable(SQLTableName)
    if (not modSQLDAL.SQLTableExist(SQLTableName)):
        modSQLDAL.SQLCreateTable(SQLTableName,KeyList,KeyType,ParaList,ParaType)




        
