import os


class CreateGradle:
    def createGradle(self, folderRoute):
        file = open(str(folderRoute) + os.sep + "build.gradle", "w")
        file.write("apply plugin: 'com.android.library'\n"
      +"\n"
      +"android {\n"
      +"    compileSdkVersion 25\n"
      +"    buildToolsVersion \"25.0.2\"\n"
      +"\n"
      +"    defaultConfig {\n"
      +"        minSdkVersion 16\n"
      +"        targetSdkVersion 25\n"
      +"        versionCode 10\n"
      +"        versionName \"1.0\"\n"
      +"    }\n"
      +"    buildTypes {\n"
      +"        release {\n"
      +"            minifyEnabled false\n"
      +"            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'\n"
      +"        }\n"
      +"    }\n"
      +"}\n"
      +"\n"
      +"dependencies {\n"
      +"    compile 'com.squareup.retrofit2:retrofit:2.3.0'\n"
      +"    compile 'com.squareup.retrofit2:converter-gson:2.3.0'\n"
      +"    compile 'com.squareup.okhttp3:logging-interceptor:3.8.1'\n"
      +"}")
        file.close()
        print("gradles created")