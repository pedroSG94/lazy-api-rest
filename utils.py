import os

global moduleName
global packageName
global baseUrl


def getMainFolder():
    return ".." + os.sep + str(moduleName) + os.sep + "src" + os.sep + "main"


def getValuesFolder():
    return getMainFolder() + os.sep + "res" + os.sep + "values"


def getCodeFolder():
    return getMainFolder() + os.sep + "java" + os.sep + str(packageName).replace(".", os.sep)


def getBodiesFolder():
    return getCodeFolder() + os.sep + "bodies"


def reformatVariables(variableName):
    validVariable = variableName
    # delete no valid characters
    for ch in {"-", "*", "+", "/"}:
        if ch in validVariable:
            validVariable = str(validVariable).replace(ch, "")
    # check if start with a number, in this case add "a" letter to the variable
    try:
        int(variableName[:1])
        return "a" + validVariable
    except ValueError:
        return validVariable
