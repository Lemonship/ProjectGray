import sys
import inspect
import xml.etree.ElementTree as ET
import modSetting

ProjectPath = modSetting.ProjectPath + '\\clsObject'
##sys.path.insert(0, modSetting.ProjectPath + '\\clsObject')
    
def Module(ClassName):
    components = ClassName.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

def ModuleClass(ClassName):
    ResultObject = eval(" Module(ClassName).{0}".format(ClassName))
    return ResultObject

def CreateObjectClass(ClassName, SQLTableName, KeyList, ParamList):
    strParaAssign = ""
    strParaInput = ""
    strParaList = ""
    strKeyList = ""
    strKeyValue = ""
    strParaValueList = ""
    for KeyName in KeyList:
        strParaInput += ", " + KeyName
        strKeyList += ", '" + KeyName + "'"
        strParaValueList += ",self.{0}".format(KeyName)
        strParaAssign += """self.{0}={0}
        """.format(KeyName)

    
    for ParamName in ParamList:
        strParaInput += ", " + ParamName
        strParaList += ", '" + ParamName + "'"
        strParaValueList += ",self.{0}".format(ParamName)
        strParaAssign += """self.{0}={0}
        """.format(ParamName)

        
    strParaInput = strParaInput[2:]
    strKeyList = strKeyList[2:]
    strParaList = strParaList[2:]
    strKeyValue = strKeyValue[2:]
    strParaValueList = strParaValueList[1:]
    strClassBuilder = """from clsObject import clsObject
from modSQLDAL import ModuleClass
class {0}(clsObject):
    count = 0
    keyList = [{3}]
    paramList = [{4}]
    fieldList = keyList + paramList
    SQLTableName = '{5}'
    ClassName = __name__
    
    def __init__(self, {2}):
        {0}.count += 1
        {1}
""".format(ClassName,strParaAssign, strParaInput, strKeyList, strParaList,  SQLTableName, strParaValueList)
    file = open(ProjectPath + '\\' + ClassName+'.py', 'w+')
    file.write(strClassBuilder)
    file.close()

    sSQL = "INSERT INTO [ItemCategory] VALUES('{0}', '{1}', '{2}', '{3}', '{4}')"
    sSQL = sSQL.format(SQLTableName, ClassName, "None", strParaInput, "N/A")
    ms = modSetting.MainDB
    ms.ExecNonQuery("DELETE FROM [ItemCategory] WHERE [TableName] = '{0}'".format(SQLTableName))
    ms.ExecNonQuery(sSQL)

def CreateClassFromDBTable(ClassName, SQLTableName):
    CreateObjectClass(ClassName, SQLTableName, SQLGetKeyField(SQLTableName), SQLGetParaField(SQLTableName))

def SQLTableExist(TableName):
    sSQL = "SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE [TABLE_NAME] = '{0}'".format(TableName)
    ms = modSetting.MainDB
    Result = (ms.ExecQuery(sSQL)[0][0] == 1)
    return Result

def SQLFindClassName(TableName):
    sWHERE = "WHERE [Tablename] = '{0}'".format(TableName)
    Item = SQLGetObject("clsItemCategory",sWHERE)
    return Item[0].Classname
    
def SQLCreateTable(TableName, KeyList, KeyTypeList, ParaList, ParaTypeList):
    sFieldString = ""
    sKeyString = ""

    for i in range(len(KeyList)):
        sFieldString += """[{0}] {1} NOT NULL,
        """.format(KeyList[i], KeyTypeList[i])
        sKeyString += """
        [{0}] ASC,""".format(KeyList[i])
        
    for i in range(len(ParaList)):
        sFieldString += """[{0}] {1} NULL,
        """.format(ParaList[i], ParaTypeList[i]) 
    
    sFieldString = sFieldString[:-3]
    sKeyString = sKeyString[:-1]
    sSQL = """
CREATE TABLE [dbo].[{0}](
	{1}
 CONSTRAINT [PK_{0}] PRIMARY KEY CLUSTERED 
(       {2}
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]""".format(TableName, sFieldString, sKeyString)

    if any('MAX' in s for s in ParaTypeList) or any('MAX' in s for s in KeyTypeList):
        sSQL += " TEXTIMAGE_ON [PRIMARY]"

    ms = modSetting.MainDB
    ms.ExecNonQuery(sSQL)
##    print sSQL 

def SQLGetObject(ClassName, Filter = ""):
    ParamString = ConvertParaValue(ParaType.NoQuotedValue, ModuleClass(ClassName).fieldList)
    sSQL = "SELECT {1} FROM {0} ".format(ModuleClass(ClassName).SQLTableName, ParamString)
    if len(Filter) > 0:
        sSQL += Filter
    ms = modSetting.MainDB
    resList = ms.ExecQuery(sSQL)
    ItemList = []

    strSetObject = """
for ({0}) in resList:
    ItemList.append(ModuleClass(ClassName)({0}))
    """.format(ParamString)
##    print strSetObject
    exec(strSetObject)
    return ItemList

def SQLSelectInto(TargetTable, SourceTable, TargetField, SourceField):
    if SQLTableExist(TargetTable) and SQLTableExist(SourceTable):
        sSQL = " INSERT INTO {0} ({2}) SELECT {3} FROM {1} WITH (HOLDLOCK TABLOCKX)"
        sSQL = sSQL.format(TargetTable,
                           SourceTable,
                           ConvertParaValue(ParaType.NoQuotedValue,TargetField),
                           ConvertParaValue(ParaType.NoQuotedValue, SourceField))
        ms = modSetting.MainDB
        ms.ExecNonQuery(sSQL)

def SQLDropTable(TableName):
    if SQLTableExist(TableName):
        sSQL = " DROP TABLE {0} ".format(TableName)
        ms = modSetting.MainDB
        ms.ExecNonQuery(sSQL)
        
def SQLTableAddField(TableName, OrgFieldList, NewFieldList, Type):
    SQLCreateTable(TableName, KeyList, KeyTypeList, ParaList, ParaTypeList)
          

def SQLAddAndUpdateObject(Item):
    ClassName = Item.__class__.__name__
    TableName = Item.SQLTableName
    sSubString = ""
    for key in Item.keyList:
        sSubString += "and target.[{0}] = source.{0} ".format(key)
    sSubString = "on" + sSubString[3:]
    sSQL = """
merge [{0}] as target
using (values ({1}))
    as source ({2})
    {3}""".format(TableName,
                  ConvertParaValue(ParaType.QuotedValue, Item.GetValueList(Item.fieldList)),
                  ConvertParaValue(ParaType.NoQuotedValue,Item.fieldList),
                  sSubString)

    sSubString = ""
    for Field in Item.paramList:
        sSubString += """
        {0} = source.{0},""".format(Field)
    sSubString = sSubString[:-1]
    sSubStringA = ""
    for Field in Item.fieldList:
        sSubStringA += "source.{0},".format(Field)
    sSubStringA = sSubStringA[:-1]
    sSQL += """
when matched then
    update set {0}
when not matched then
    insert ({1})
    values ({2});
""".format(sSubString,
           ConvertParaValue(ParaType.NoQuotedValue, Item.fieldList),
           ConvertParaValue(ParaType.QuotedValue, Item.GetValueList(Item.fieldList)),
           sSubStringA)
    ms = modSetting.MainDB
    ms.ExecNonQuery(sSQL)
##    print sSQL
                            
def SQLGetKeyField(TableName):
    sSQL = "SELECT [COLUMN_NAME] FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE [Table_Name] = '{0}'".format(TableName)
    ms = modSetting.MainDB
    resList = ms.ExecQuery(sSQL)
    Result = []
    for item in resList:
        Result.append(str(item)[3:-3])
    return Result

def SQLGetParaField(TableName):
    sSQL = """SELECT [COLUMN_NAME] from INFORMATION_SCHEMA.COLUMNS WHERE [TABLE_NAME] = '{0}' AND [COLUMN_NAME] NOT IN (
SELECT [COLUMN_NAME] FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE [Table_Name] = '{0}')""".format(TableName)
    ms = modSetting.MainDB
    resList = ms.ExecQuery(sSQL)
    Result = []
    for item in resList:
        Result.append(str(item)[3:-3])
    return Result

def SQLGetFromXML(XMLItem):
    sWHERE = ""
    ClassName = SQLFindClassName(XMLItem.tag)
    for SubItem in XMLItem:
        sWHERE += "AND {0} = '{1}'".format(SubItem.tag, SubItem.text)
    sWHERE = "WHERE" + sWHERE[3:]
    ResultList = SQLGetObject(ClassName, sWHERE)
    if len(ResultList)>0:
        ResultObject = ResultList[0]
    else:
        ResultObject = ""
    return ResultObject
def ConvertParaValue(Type, List, SubList = []):
    Result = ""
    for i in range(len(List)):
        
        if Type == ParaType.NoQuotedValue:
            Result += ",{0}".format(List[i])
        elif Type == ParaType.QuotedValue:
            Result += ",'{0}'".format(List[i])
        elif Type == ParaType.AssignValue:
            Result += ",{1}='{0}'".format(List[i], SubList[i])
    return Result[1:]

    
def func(a, b, c):
    frame = inspect.currentframe()
    args, _, _, values = inspect.getargvalues(frame)
    print 'function name "%s"' % inspect.getframeinfo(frame)[2]
    for i in args:
        print "    %s = %s" % (i, values[i])
    return [(i, values[i]) for i in args]

    
class ParaType:
    NoQuotedValue = 0
    QuotedValue = 1
    AssignValue = 2

class SQLDataType:
    Integer = "Int"
    Float = "float"
    Double = "double"
    @staticmethod
    def Varchar(Length):
        return "varchar({0})".format(Length)
    @staticmethod
    def Nvarchar(Length):
        return "nvarchar({0})".format(Length)
    Xml = "xml"
