import xml.etree.ElementTree as ET
##import xml.dom.minidom
import modSQLDAL
import re


class clsObjMap:
    def __init__(self, XMLString = ""):
        ET.register_namespace('ObjMap','http://www.testing.com')
        if len(XMLString) > 0:
            try:
                self.Root = ET.fromstring(XMLString)
            except:
                self.Root = ET.Element("Root")
        else:
            self.Root = ET.Element("Root")
            
    def GetNamespace(self, element):
        m = re.match('\{.*\}', element.tag)
        return m.group(0) if m else ''
    
    def ConvertFrom(self, XMLString):
        self.Root = ET.fromstring(XMLString)
        
    def AddElement(self, ObjType, TargetObject):
        Node = ET.SubElement(self.Root, TargetObject.SQLTableName, Type=ObjType)
        for Key in TargetObject.keyList:
            ET.SubElement(Node, Key).text = str(TargetObject.GetValue(Key))
            
    def FindAllObject(self, Type = ""):
        ResultList = []
        for Item in self.Root:
            if len(Type) > 0:
                if Item.get('Type') == Type:
                    ResultList.append(modSQLDAL.SQLGetFromXML(Item))
            else:
                ResultList.append(modSQLDAL.SQLGetFromXML(Item))
        return ResultList

    def FindClassObject(self, ClassName, Type = ""):
        SQLTableName = modSQLDAL.ModuleClass(ClassName).SQLTableName
        ResultList = []
        if len(SQLTableName)>0:
            for Item in self.Root.findall(SQLTableName):
                if len(Type) > 0:
                    if Item.get('Type') == Type:
                        ResultList.append(modSQLDAL.SQLGetFromXML(Item))
                else:
                    ResultList.append(modSQLDAL.SQLGetFromXML(Item))
                ResultList.append(GetObj)
        return ResultList

    def FindByFieldToObject(self, ClassName, Field, Value, Type = ""):
        SQLTableName = modSQLDAL.ModuleClass(ClassName).SQLTableName
        ResultList = []
        if len(SQLTableName)>0:
            for Item in self.Root.findall(SQLTableName):
                if len(Type) > 0:
                    if Item.get('Type') == Type:
                        GetObj = modSQLDAL.SQLGetFromXML(Item)
                    else:
                        GetObj = None
                else:
                    GetObj = modSQLDAL.SQLGetFromXML(Item)
                if not GetObj is None and GetObj.GetValue(Field) == Value:
                    ResultList.append(modSQLDAL.SQLGetFromXML(Item))
        return ResultList

    def FindByTextToObject(self, Value):
        ResultList = []
        for Item in self.Root:
            if Value in ET.tostring(Item):
                ResultList.append(modSQLDAL.SQLGetFromXML(Item))
        return ResultList

    def ToString(self):
        return ET.tostring(self.Root)

    


##    def FindElements(self, Category, Type):
##        ResultList = []
##        for Item in self.Root.findall(Category):
##            if Item.get('Type') == Type:
##                ResultList.append(ET.tostring(Item))
####                print ET.tostring(Item)
####                print(Item.tag, Item.attrib)
##        return ResultList
##    def FindByFieldToXML(self, Category, Field, Value):
##        ResultList = []
##        for Item in self.Root.findall(Category):
##            if Item.find(Field).text == Value:
##                ResultList.append(ET.tostring(Item))
##                print ET.tostring(Item)
##        return ResultList    
##    def FindByTextToXML(self, Value):
##        ResultList = []
##        for Item in self.Root:
##            if Value in ET.tostring(Item):
##                ResultList.append(ET.tostring(Item))
##        return ResultList

##    def FindType(self, SearchString):
        

