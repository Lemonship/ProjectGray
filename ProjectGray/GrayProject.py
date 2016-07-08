import modObjectClassHandler
from modObjectClassHandler import ModuleClass

ClassName = 'clsPeople'
SQLTableName = 'People'
KeyList = ['Name']
ParameterList = ['Age', 'Gender', 'Remarks']
modObjectClassHandler.CreateObjectClass(ClassName, SQLTableName, KeyList, ParameterList)
ResultList = modObjectClassHandler.SQLGetObject(ClassName,SQLTableName)
print ResultList[0].__class__.__name__

##Print Result ========================================================================================================
for Item in ResultList:
    PrintResult = ''
    for FieldName in ModuleClass(ClassName).fieldList:
        PrintResult += ',' + eval('str(Item.{0}).decode("utf8")'.format(FieldName))

    PrintResult = PrintResult[1:]
    print PrintResult

