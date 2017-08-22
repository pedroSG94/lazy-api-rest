import os
import json
import re
from shutil import copyfile
import utils


class GenerateLibraryAPIRest:
    def generateLibraryAPIRest(self, moduleName, packageName, codeFolder, listRequestJson):
        fileDestiny = codeFolder + os.sep + str(moduleName).title() + "ApiRest.java"
        copyfile("javafiles" + os.sep + "LibraryApiRest.java", fileDestiny)
        file = open(fileDestiny, "r")
        stringFile = file.read()
        stringFile = stringFile.replace("LibraryApiRest", str(moduleName).title() + "ApiRest").replace("com.example.library", packageName)
        file.flush()
        file.close()
        file = open(fileDestiny, "w")
        stringFile = stringFile.replace("add_data", self.generateApiRestMethods(listRequestJson, moduleName))
        file.write(stringFile)
        file.flush()
        file.close()

    def generateApiRestMethods(self, listRequestJson, moduleName):
        stringMethods = ""
        for i in listRequestJson:
            stringMethods += self.createMethod(i, moduleName)
        return stringMethods

    def generateCallbackResponseInMethod(self, moduleName):
        return ".enqueue(new Callback<Object>() {\n"\
      + "      @Override\n"\
      + "      public void onResponse(Call<Object> call, Response<Object> response) {\n"\
      + "        if (response.isSuccessful()) {\n"\
      + "          " + moduleName + "callback.onSuccess(response.toString());\n"\
      + "        } else {\n"\
      + "          " + moduleName + "callback.onError(new ErrorResponse(response.code(), response.message()));\n"\
      + "        }\n"\
      + "      }\n"\
      + "\n"\
      + "      @Override\n"\
      + "      public void onFailure(Call<Object> call, Throwable t) {\n"\
      + "        " + moduleName + "callback.onError(new ErrorResponse(-1, t.getMessage()));\n"\
      + "      }\n"\
      + "    });\n"

    def getMethodName(self, jsonCode):
        jsonEncoded = json.loads(jsonCode.replace("\n", ""))
        url = jsonEncoded["url"]
        regularExpresion = '\/(.*)\?'
        try:
            destiny = re.search(regularExpresion, url, re.I | re.U).group(0)
        except AttributeError:
            destiny = str(url)[str(url).index('/'):]
        destiny = destiny.replace("/", "").replace("?", "")
        return destiny

    def createMethod(self, jsonCode, moduleName):
        stringParameters = ""
        stringParametersToService = "("
        jsonEncoded = json.loads(jsonCode.replace("\n", ""))
        # add headers not final
        for h in jsonEncoded["headers"]:
            if not str(h["description"]) == "final":
                stringParameters += "String " + utils.reformatVariables(h["key"]) + ","
                stringParametersToService += h["key"] + ","
        # add querys
        for q in jsonEncoded["querys"]:
            stringParameters += "String " + q["key"] + ","
            stringParametersToService += q["key"] + ","
        # add bodies
        try:
            cont = 0
            for b in jsonEncoded["body"]:
                if b["type"] == "text":
                    if cont < 1:
                        stringClassBody = self.getMethodName(jsonCode)
                        stringParameters += stringClassBody.title() + "Body " + utils.reformatVariables(stringClassBody + "body") + ","
                        stringParametersToService += stringClassBody + "body,"
                    cont += 1
                elif b["type"] == "file":
                    stringParameters += "File " + utils.reformatVariables(b["key"]) + ","
                    stringParametersToService += "getMultiPart(" + b["key"] + ",\"" + b["key"] + "\"),"

        except KeyError:
                pass
        stringParametersToService += ")"
        stringParametersToService = stringParametersToService.replace(",)", ")")
        stringMethod = "  public void " + self.getMethodName(jsonCode) + "(" + stringParameters \
                       + "final " + str(moduleName).title() + "Callback " + utils.reformatVariables(moduleName + "callback") + ") {\n" \
                       + "    retrofit2Service." + self.getMethodName(jsonCode) + stringParametersToService \
                       + self.generateCallbackResponseInMethod(moduleName) + "  }\n\n"
        return stringMethod