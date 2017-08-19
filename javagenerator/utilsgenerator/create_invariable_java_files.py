import os
from shutil import copyfile

class CreateInvariableJavaFiles:
    def copyInvariableJavaFiles(self, moduleName, packageName, codeFolder, baseUrl):
        sourceJavaFilesFolder = "javafiles"
        copyfile(sourceJavaFilesFolder + os.sep + "ErrorResponse.java", codeFolder + os.sep + "ErrorResponse.java")
        copyfile(sourceJavaFilesFolder + os.sep + "LibraryCallback.java", codeFolder + os.sep + str(moduleName).title().replace(" ", "") + "Callback.java")
        copyfile(sourceJavaFilesFolder + os.sep + "Retrofit2ServiceImp.java", codeFolder + os.sep + "Retrofit2ServiceImp.java")
        copyfile(sourceJavaFilesFolder + os.sep + "Constants.java", codeFolder + os.sep + "Constants.java")
        self.modifyPackage(moduleName, packageName, codeFolder, baseUrl)

    def modifyPackage(self, moduleName, packageName, codeFolder, baseUrl):
        file1 = open(codeFolder + os.sep + "ErrorResponse.java", "r")
        stringFile1 = file1.read().replace("com.example.library", packageName)
        file1.flush()
        file1.close()
        file1 = open(codeFolder + os.sep + "ErrorResponse.java", "w")
        file1.write(stringFile1)
        file1.flush()
        file1.close()

        file2 = open(codeFolder + os.sep + str(moduleName).title().replace(" ", "") + "Callback.java", "r")
        stringFile2 = file2.read().replace("com.example.library", packageName).replace("Library", str(moduleName).title().replace(" ", ""))
        file2.flush()
        file2.close()
        file2 = open(codeFolder + os.sep + str(moduleName).title().replace(" ", "") + "Callback.java", "w")
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

        file4 = open(codeFolder + os.sep + "Constants.java", "r")
        stringFile4 = file4.read().replace("com.example.library", packageName).replace("http://exampleurl.com", baseUrl)
        file4.flush()
        file4.close()
        file4 = open(codeFolder + os.sep + "Constants.java", "w")
        file4.write(stringFile4)
        file4.flush()
        file4.close()
