import os
import json

class GenerateRetrofit2Service:
    def createRetrofit2Service(self, moduleName, packageName, listRequestJson):
        folderRoute = str(moduleName) + os.sep + "src" + os.sep + "main" + os.sep + "java" + os.sep + str(packageName).replace(".", "/")
        file = open(str(folderRoute) + os.sep + "Retrofit2Service.java", "w")
        file.write("package " + str(packageName) + ";\n"
    +"\n"
    +"\n"
    + self.createImports(listRequestJson)
    +"public interface Retrofit2Service {\n"
    +"\n"
    + self.createRequests(listRequestJson)
    +"}")

    def createRequests(self, listRequestJson):
        stringRequest = ""
        cont = 0
        for i in listRequestJson:
            jsonEncoded = json.loads(i.replace("\n", ""))
            stringRequest += "@" + jsonEncoded["method"]
            stringRequest += "\n"
            stringRequest += "Call<Object> " + "method" + str(cont) + "("
            cont += 1
            # add headers to requests
            for h in jsonEncoded["headers"]:
                stringRequest += "@Header(\"" + str(h["key"]) + "\") String " + str(h["key"]) + ","
            # add querys to requests
            for q in jsonEncoded["querys"]:
                stringRequest += "@Query(\"" + str(q["key"]) + "\") String " + str(q["key"]) + ","
            stringRequest += ");\n"
            # delete last , to fix format code
        return stringRequest.replace(",)", ")")

    def createImports(self):
        stringImports = ""
        stringImports += "import retrofit2.Call;\n"
        stringImports += "import retrofit2.http.*;\n"
        stringImports += "\n"
        return stringImports