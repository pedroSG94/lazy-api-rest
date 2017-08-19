import os
from shutil import copyfile


class GenerateLibraryAPIRest:
    def generateLibraryAPIRest(self, moduleName, packageName, codeFolder, listRequestJson):
        fileDestiny = codeFolder + os.sep + str(moduleName).title() + "ApiRest.java"
        copyfile("javafiles" + os.sep + "LibraryApiRest.java", fileDestiny)
        file = open(fileDestiny, "r")
        stringFile = file.read()
        stringFile = stringFile.replace("LibraryApiRest", str(moduleName).title() + "ApiRest.java").replace("com.example.library", packageName)
        file.flush()
        file.close()
        file = open(fileDestiny, "w")
        file.write(stringFile)
        file.flush()
        file.close()

    def generateApiRestMethods(self):
        pass