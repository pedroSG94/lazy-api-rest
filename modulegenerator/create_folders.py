import os


class CreateFolders:
    def createAllFolders(self, codeFolder, valuesFolder, bodiesFolder):
        try:
            os.makedirs(codeFolder)
        except FileExistsError:
            print("code folders exists")
        try:
            os.makedirs(valuesFolder)
        except FileExistsError:
            print("values folders exists")
        print("folders created")
        try:
            os.makedirs(bodiesFolder)
        except FileExistsError:
            print("bodies folders exists")
