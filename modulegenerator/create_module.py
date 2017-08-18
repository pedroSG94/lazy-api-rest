import os
from modulegenerator.create_folders import CreateFolders
from modulegenerator.create_gradle import CreateGradle
from modulegenerator.create_xml import CreateXML

class GenerateModule:
    def generateModule(self, moduleName, packageName):
        CreateFolders().createAllFolders(moduleName, packageName)
        CreateGradle().createGradle(moduleName)
        createXML = CreateXML()
        createXML.createAndroidManifestXML(moduleName + os.sep + "src" + os.sep + "main", packageName)
        createXML.createStringsXML(moduleName + os.sep + "src" + os.sep + "main" + os.sep + "res" + os.sep + "values", moduleName)
        print("module created")