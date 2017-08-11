import os


class CreateFolders:
    def createAllFolders(self, moduleName, modulePackage):
        mainFolder = str(moduleName) + os.sep + "src" + os.sep + "main"
        packageFolders = str(modulePackage).replace(".", os.sep)
        try:
            os.makedirs(mainFolder + os.sep + "java" + os.sep + str(packageFolders))
        except FileExistsError:
            pass
        try:
            os.makedirs(mainFolder + os.sep + "res" + os.sep + "values")
        except FileExistsError:
            pass
        print("folders created")