from modulegenerator.create_folders import CreateFolders
from modulegenerator.create_gradle import CreateGradle
from modulegenerator.create_xml import CreateXML

class GenerateModule:
    def generateModule(self, moduleName, packageName, mainFolder, codeFolder, valuesFolder):
        CreateFolders().createAllFolders(codeFolder, valuesFolder)
        CreateGradle().createGradle(moduleName)
        createXML = CreateXML()
        createXML.createAndroidManifestXML(mainFolder, packageName)
        createXML.createStringsXML(valuesFolder, moduleName)
        print("module created")