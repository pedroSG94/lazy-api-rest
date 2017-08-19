import os


class CreateXML:
    def createStringsXML(self, valuesFolder, moduleName):
        file = open(valuesFolder + os.sep + "strings.xml", "w")
        file.write("<resources>\n"
                   + "    <string name=\"app_name\">" + moduleName + "</string>\n"
                   + "</resources>")
        file.close()

    def createAndroidManifestXML(self, mainFolder, packageName):
        file = open(mainFolder + os.sep + "AndroidManifest.xml", "w")
        file.write("<manifest xmlns:android=\"http://schemas.android.com/apk/res/android\"\n"
                   + "    package=\"" + packageName + "\"\n"
                   + "    >\n"
                   + "\n"
                   + "  <application\n"
                   + "      android:allowBackup=\"true\"\n"
                   + "      android:label=\"@string/app_name\"\n"
                   + "      android:supportsRtl=\"true\"\n"
                   + "      />\n"
                   + "</manifest>")
        file.close()
        print("XMLs created")
