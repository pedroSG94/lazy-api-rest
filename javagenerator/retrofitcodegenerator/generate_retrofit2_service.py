import os
import json
import re
from javagenerator.retrofitcodegenerator.generate_retrofit2 import GenerateRetrofit2Base


class GenerateRetrofit2Service(GenerateRetrofit2Base):
    def createRetrofit2Service(self, codeFolder, packageName, listRequestJson):
        file = open(codeFolder + os.sep + "Retrofit2Service.java", "w")
        file.write(self.addPackage(packageName)
                   + self.createImports()
                   + "public interface Retrofit2Service {\n"
                   + "\n"
                   + self.createRequests(listRequestJson)
                   + "}")

    def createRequests(self, listRequestJson):
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
            stringRequest += "@" + jsonEncoded["method"] + \
                             "(\"" + destiny + "\")"
            stringRequest += "\n"
            stringRequest += "Call<Object> " + destiny + "("
            # add headers to requests
            for header in jsonEncoded["headers"]:
                stringRequest += "@Header(\"" + str(header["key"]) + "\") String " + str(header["key"]) + ","
            # add querys to requests
            for query in jsonEncoded["querys"]:
                stringRequest += "@Query(\"" + str(query["key"]) + "\") String " + str(query["key"]) + ","
            stringRequest += ");\n\n"
            # delete last , to fix format code
        return stringRequest.replace(",)", ")")

    def createImports(self):
        stringImports = ""
        stringImports += "import retrofit2.Call;\n"
        stringImports += "import retrofit2.http.*;\n"
        stringImports += "\n\n"
        return stringImports
