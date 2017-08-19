import json
from json import JSONDecodeError


class RequestUsableParser:
    def getUrl(self, requestString):
        return "\"url\":" + "\"" + requestString["url"] + "\""

    def getHeaders(self, requestString):
        return "\"headers\":" + str(requestString["headerData"]).replace("\'", "\"").replace("True", "\"\"").replace("False", "\"\"")

    def getMethod(self, requestString):
        return "\"method\":" + "\"" + requestString["method"] + "\""

    def getQuerys(self, requestString):
        return "\"querys\":" + str(requestString["queryParams"]).replace("\'", "\"").replace("True", "\"\"").replace("False", "\"\"")

    def getBody(self, requestString):
        stringBody = str(requestString["data"]).replace("\'", "\"").replace("True", "\"\"").replace("False", "\"\"")
        if stringBody == "None":
            return ""
        else:
            return ", \n\"body\":" + stringBody

    def createRequest(self, requestString):
        return "{\n" + self.getMethod(requestString) + ", \n"  + self.getUrl(requestString) \
                               + ", \n" + self.getHeaders(requestString) + ", \n"  + self.getQuerys(requestString) + \
               self.getBody(requestString) + "\n}"