import json


class RequestUsableParser():
    def getUrl(self, requestString):
        return "\"url\":" + "\"" + requestString["url"] + "\""

    def getHeaders(self, requestString):
        return "\"headers\":" + "\"" + str(requestString["headerData"]) + "\""

    def getMethod(self, requestString):
        return "\"method\":" + "\"" + requestString["method"] + "\""

    def getQuerys(self, requestString):
        return "\"querys\":" + "\"" + str(requestString["queryParams"]) + "\""

    def createRequest(self, requestString):
        return "{\n" + self.getMethod(requestString) + ", \n"  + self.getUrl(requestString) \
                               + ", \n" + self.getHeaders(requestString) + ", \n"  + self.getQuerys(requestString) + "\n}"