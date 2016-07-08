import sys
import inspect
import modSetting

ProjectPath = modSetting.ProjectPath + '\\clsObject'
sys.path.insert(0, modSetting.ProjectPath + '\\clsObject')

def CreateObjectClass(ClassName, SQLTableName, KeyList, ParamList):
    strParaAssign = ""
    strParaInput = ""
    strParaList = ""
    strKeyList = ""
    strKeyValue = ""

    for KeyName in KeyList:
        strParaInput += ", " + KeyName
        strKeyList += ", '" + KeyName + "'"
        strParaAssign += """self.{0}={0}
        """.format(KeyName)

    
    for ParamName in ParamList:
        strParaInput += ", " + ParamName
        strParaList += ", '" + ParamName + "'"
        strParaAssign += """self.{0}={0}
        """.format(ParamName)

        
    strParaInput = strParaInput[2:]
    strKeyList = strKeyList[2:]
    strParaList = strParaList[2:]
    strKeyValue = strKeyValue[2:]
    strClassBuilder = """
class {0}:
    count = 0
    paramString = '{2}'
    keyList = [{3}]
    paramList = [{4}]
    fieldList = keyList + paramList
    SQLTableName = '{5}'
    
    def __init__(self, {2}):
        {0}.count += 1
        {1}

    def ParaValue(self, FieldName):
        return eval("self.{0}".format(FieldName))

    def TotalCount(self):
        print {0}.count

""".format(ClassName,strParaAssign, strParaInput, strKeyList, strParaList,  SQLTableName)
    file = open(ProjectPath + '\\' + ClassName+'.py', 'w+')
    file.write(strClassBuilder)
    file.close()

    sSQL = "INSERT INTO [ItemCategory] VALUES('{0}', '{1}', '{2}', '{3}', '{4}')"
    sSQL = sSQL.format(SQLTableName, ClassName, "None", strParaInput, "N/A")
    ms = modSetting.MainDB
    ms.ExecNonQuery("DELETE FROM [ItemCategory] WHERE [TableName] = '{0}'".format(SQLTableName))
    ms.ExecNonQuery(sSQL)
    
def Module(ClassName):
    components = ClassName.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

def ModuleClass(ClassName):
    ResultObject = eval(" Module(ClassName).{0}".format(ClassName))
    return ResultObject


def SQLGetObject(ClassName, TableName):
    ParamString = ModuleClass(ClassName).paramString
    sSQL = "SELECT {1} FROM {0}".format(ModuleClass(ClassName).SQLTableName, ParamString)
    ms = modSetting.MainDB
    resList = ms.ExecQuery(sSQL)
    ItemList = []

    strSetObject = """
for ({0}) in resList:
    ItemList.append(ModuleClass(ClassName)({0}))
    """.format(ParamString)
    exec(strSetObject)
    return ItemList

def SQLUpdateObject(InstantObj, TableName):
    ClassName = InstantObj.__class__.__name__
    sSQL = """
merge [{0}] as target
using (values ('M', '40', 'Remarks'))
    as source (Gender, Age, Remarks)
    on target.[Name] = 'Tony Man'
when matched then
    update
    set Gender = source.Gender,
        Age = source.Age,
        Remarks = source.Remarks
when not matched then
    insert ( Name, Gender, Age, Remarks)
    values ( 'Tony Man',  source.Gender, source.Age, source.Remarks);
""".format(ClassName)

def ConvertParaValue(FieldList, ValueList, Type)
    Result = ""
    for i in range(0, len(ValueList))
        
        if Type = ParaType.NoQuotedValue
            Result += ",{0}".format(ValueList[i])
        elif Type = ParaType.QuotedValue
            Result += ",'{0}'".format(ValueList[i])
        elif Type = ParaType.AssignValue
            Result += ",{1}='{0}'".format(ValueList[i], FieldList[i])
    
def func(a, b, c):
    frame = inspect.currentframe()
    args, _, _, values = inspect.getargvalues(frame)
    print 'function name "%s"' % inspect.getframeinfo(frame)[2]
    for i in args:
        print "    %s = %s" % (i, values[i])
    return [(i, values[i]) for i in args]

    
from enum import Enum
class ParaType(Enum)
    NoQuotedValue = 0
    QuotedValue = 1
    AssignValue = 2
    
