import os
from shutil import copyfile

class CreateInvariableJavaFiles:
    def copyInvariableJavaFiles(self, moduleName, packageName, codeFolder):
        sourceJavaFilesFolder = "javagenerator" + os.sep + "utilsgenerator"
        copyfile(sourceJavaFilesFolder + os.sep + "ErrorResponse.java", codeFolder + os.sep + "ErrorResponse.java")
        copyfile(sourceJavaFilesFolder + os.sep + "LibraryCallback.java", codeFolder + os.sep + moduleName + "Callback.java")
        copyfile(sourceJavaFilesFolder + os.sep + "Retrofit2ServiceImp.java", codeFolder + os.sep + "Retrofit2ServiceImp.java")
        self.modifyPackage(moduleName, packageName, codeFolder)

    def modifyPackage(self, moduleName, packageName, codeFolder):
        file1 = open(codeFolder + os.sep + "ErrorResponse.java", "r")
        stringFile1 = file1.read().replace("com.example.library", packageName)
        file1.flush()
        file1.close()
        file1 = open(codeFolder + os.sep + "ErrorResponse.java", "w")
        print(stringFile1)
        file1.write(stringFile1)
        file1.flush()
        file1.close()

        file2 = open(codeFolder + os.sep + moduleName + "Callback.java", "r")
        stringFile2 = file2.read().replace("com.example.library", packageName)
        file2.flush()
        file2.close()
        file2 = open(codeFolder + os.sep + moduleName + "Callback.java", "w")
        file2.write(stringFile2)
        file2.flush()
        file2.close()

        file3 = open(codeFolder + os.sep + "Retrofit2ServiceImp.java", "r")
        stringFile3 = file3.read().replace("com.example.library", packageName)
        file3.flush()
        file3.close()
        file3 = open(codeFolder + os.sep + "Retrofit2ServiceImp.java", "w")
        file3.write(stringFile3)
        file3.flush()
        file3.close()
