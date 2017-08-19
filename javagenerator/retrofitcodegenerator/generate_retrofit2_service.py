import os
import json
import re
from shutil import copyfile
from javagenerator.retrofitcodegenerator.generate_retrofit2 import GenerateRetrofit2Base


class GenerateRetrofit2Service(GenerateRetrofit2Base):
    def createRetrofit2Service(self, codeFolder, bodiesFolder, packageName, listRequestJson):
        copyfile("javafiles" + os.sep + "Retrofit2Service.java", codeFolder + os.sep + "Retrofit2Service.java")
        file = open(codeFolder + os.sep + "Retrofit2Service.java", "r")
        stringfile = file.read().replace("com.example.library", packageName)
        stringfile = stringfile.replace("add_data", self.createRequests(listRequestJson, packageName, bodiesFolder))
        file.flush()
        file.close()
        file = open(codeFolder + os.sep + "Retrofit2Service.java", "w")
        file.write(stringfile)
        file.flush()
        file.close()

    def createRequests(self, listRequestJson, packageName, bodiesFolder):
        stringRequest = ""
        for i in listRequestJson:
            jsonEncoded = json.loads(i.replace("\n", ""))
            url = jsonEncoded["url"]
            regularExpresion = '\/(.*)\?'
            try:
                destiny = re.search(regularExpresion, url, re.I | re.U).group(0)
            except AttributeError:
                destiny = str(url)[str(url).index('/'):]
            destiny = destiny.replace("/", "").replace("?", "")
            stringRequest += "  @" + jsonEncoded["method"] + \
                             "(\"" + destiny + "\")\n"
            # add @Multipart to request if needed
            try:
                for body in jsonEncoded["body"]:
                    if body["type"] == "file":
                        stringRequest += "  @Multipart\n"
                        break
            except KeyError:
                pass
            stringRequest += "  @Headers({"
            # add headers  without values to requests
            for header in jsonEncoded["headers"]:
                # header value empty add header in @Headers({})
                if not str(header["value"]):
                    stringRequest += "\"" + str(header["key"]) + "\","
            stringRequest += "})\n"
            # fix last iteration of headers
            stringRequest = stringRequest.replace(",}", "}")
            stringRequest += "  Call<Object> " + destiny + "("
            # add headers  with values to requests
            for header in jsonEncoded["headers"]:
                # header not value empty add header to method
                if str(header["value"]):
                    stringRequest += "@Header(\"" + str(header["key"]) + "\") String " + str(header["key"]) + ","
            # add querys to requests
            for query in jsonEncoded["querys"]:
                stringRequest += "@Query(\"" + str(query["key"]) + "\") String " + str(query["key"]) + ","
            try:
                stringBodyClassName = destiny.title() + "Body"
                bodyClassNeeded = False
                # add bodies
                cont = 0
                for body in jsonEncoded["body"]:
                    if body["type"] == "text":
                        if cont < 1:
                            stringRequest += "@Body " + stringBodyClassName + " " + destiny + "body,"
                            bodyClassNeeded = True
                        cont += 1
                    elif body["type"] == "file":
                        stringRequest += "@Part MultipartBody.Part " + body["key"] + ","
                if bodyClassNeeded:
                    self.createBodyClass(bodiesFolder, stringBodyClassName, packageName)
                    file = open(bodiesFolder + os.sep + stringBodyClassName + ".java", "r")
                    stringBody = file.read()
                    file.flush()
                    file.close()
                    file = open(bodiesFolder + os.sep + stringBodyClassName + ".java", "w")
                    # add constructor to body
                    stringDataBody = self.addConstructorToBody(jsonEncoded, stringBodyClassName)
                    # add attributes with setters and getters to body
                    stringDataBody += self.addAttributesSettersGettersToBody(jsonEncoded)
                    file.write(stringBody.replace("add_data", stringDataBody))
                    file.flush()
                    file.close()
            except KeyError:
                pass
            stringRequest += ");\n\n"
            # fix last iteration headers with values and querys
            stringRequest = stringRequest.replace(",)", ")")
        return stringRequest

    def createBodyClass(self, bodiesFolder, bodyClassName, packageName):
        copyfile("javafiles" + os.sep + "Body.java", bodiesFolder + os.sep + bodyClassName + ".java")
        file = open(bodiesFolder + os.sep + bodyClassName + ".java", "r")
        stringBody = file.read()
        stringBody = stringBody.replace("Body", bodyClassName).replace("com.example.library", packageName)
        file.flush()
        file.close()
        file = open(bodiesFolder + os.sep + bodyClassName + ".java", "w")
        file.write(stringBody)
        file.flush()
        file.close()

    def addConstructorToBody(self, jsonEncoded, stringBodyClassName):
        stringDataBody = "public " + stringBodyClassName + "("
        for body in jsonEncoded["body"]:
            if body["type"] == "text":
                stringDataBody += "String " + body["key"] + ","
                pass
        stringDataBody += ") {\n"
        stringDataBody = stringDataBody.replace(",)", ")")
        for body in jsonEncoded["body"]:
            if body["type"] == "text":
                stringDataBody += "  this." + body["key"] + " = " + body["key"] + ";\n"
        stringDataBody += "}\n\n"
        return stringDataBody

    def addAttributesSettersGettersToBody(self, jsonEncoded):
        stringDataBody = ""
        for body in jsonEncoded["body"]:
            if body["type"] == "text":
                stringDataBody += "private String " + body["key"] + ";\n\n"
                stringDataBody += "public void set" + str(body["key"]).title() + "(String " + body["key"] + ") {\n" \
                                  + "  this." + body["key"] + " = " + body["key"] + ";\n}\n\n"
                stringDataBody += "public String get" + str(body["key"]).title() + "() {\n" \
                                  + "  return " + body["key"] + ";\n}\n\n"
        return stringDataBody

    def createImports(self):
        stringImports = ""
        stringImports += "import retrofit2.Call;\n"
        stringImports += "import retrofit2.http.*;\n"
        stringImports += "\n\n"
        return stringImports
