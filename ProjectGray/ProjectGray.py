import modDAL
from modDAL import ModuleClass

ClassName = 'clsPeople'
SQLTableName = 'People'
KeyList = ['Name']
ParameterList = ['Age', 'Gender', 'Remarks']
modDAL.CreateObjectClass(ClassName, SQLTableName, KeyList, ParameterList)
ResultList = modDAL.SQLGetObject(ClassName,SQLTableName)
print ResultList[0].__class__.__name__

##Print Result ========================================================================================================
print len(ResultList)
for Item in ResultList:
    PrintResult = ''
    for FieldName in ModuleClass(ClassName).fieldList:
        PrintResult += ',' + eval('str(Item.{0}).decode("utf8")'.format(FieldName))

    PrintResult = PrintResult[1:]
    print PrintResult

