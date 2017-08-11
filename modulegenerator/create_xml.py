import os


class CreateXML:
    def createStringsXML(self, folderRoute, moduleName):
        file = open(str(folderRoute) + os.sep + "strings.xml", "w")
        file.write("<resources>\n"
      +"    <string name=\"app_name\">" + str(moduleName) + "</string>\n"
      +"</resources>")
        file.close()

    def createAndroidManifestXML(self, folderRoute, modulePackage):
        file = open(str(folderRoute) + os.sep + "AndroidManifest.xml", "w")
        file.write("<manifest xmlns:android=\"http://schemas.android.com/apk/res/android\"\n"
      +"    package=\"" + str(modulePackage) + "\"\n"
      +"    >\n"
      +"\n"
      +"  <application\n"
      +"      android:allowBackup=\"true\"\n"
      +"      android:label=\"@string/app_name\"\n"
      +"      android:supportsRtl=\"true\"\n"
      +"      />\n"
      +"</manifest>")
        file.close()
        print("XMLs created")