import sys
import os
import inspect
from modSQLDAL import Module
from modSQLDAL import ModuleClass

ProjectPath = os.path.dirname(os.path.realpath(__file__))

##print FolderList
##print PyFileList
##print inspect.getmembers(ModuleClass('clsPeople'), predicate=inspect.ismethod)
##print dir(ModuleClass('clsPeople'))




def InsertPath(PathList):
    for Path in PathList:
        sys.path.insert(0, Path)

def GetSystemFolderPathList(Path):
    PathList = [Path + "\\" + name for name in os.listdir(ProjectPath) if os.path.isdir(os.path.join(ProjectPath, name))]
    return PathList

def GetSystemFileList(Path, ExtList):
##    PyFileList = [fn for fn in os.listdir(ProjectPath) if any(fn.endswith(ext) for ext in included_extenstions)]
    included_extenstions = ['py']
    PyFileList = [os.path.splitext(fn)[0] for fn in os.listdir(Path) if any(fn.endswith(ext) for ext in ExtList)]
    return PyFileList

def GetFunctionList(ModuleName):
    
    FunctionList = inspect.getmembers(Module(ModuleName), predicate=inspect.ismethod)
##    print ModuleName
##    print FunctionList
    return FunctionList
##    print dir(ModuleClass('clsPeople'))

def GetClassList(ModuleName):
    ResultList = [ModuleName]
    for name, obj in inspect.getmembers(Module(ModuleName)):
        if inspect.isclass(obj):
            ResultList.append(ModuleName+'.'+name)
    return ResultList
