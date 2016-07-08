
class clsPeople:
    count = 0
    paramString = 'Name, Age, Gender, Remarks'
    keyList = ['Name']
    paramList = ['Age', 'Gender', 'Remarks']
    fieldList = keyList + paramList
    SQLTableName = 'People'
    
    def __init__(self, Name, Age, Gender, Remarks):
        clsPeople.count += 1
        self.Name=Name
        self.Age=Age
        self.Gender=Gender
        self.Remarks=Remarks
        

    def ParaValue(self, FieldName):
        return eval("self.clsPeople".format(FieldName))

    def TotalCount(self):
        print clsPeople.count

