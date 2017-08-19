import os

global moduleName
global packageName

def getMainFolder():
    return str(moduleName) + os.sep + "src" + os.sep + "main"

def getValuesFolder():
    return getMainFolder() + os.sep + "res" + os.sep + "values"

def getCodeFolder():
    return getMainFolder() + os.sep + "java" + os.sep + str(packageName).replace(".", os.sep)
