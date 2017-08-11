import json
from postmanfileutils.request_variable_usable_parser import RequestUsableParser


class RequestExtractor:
    def getAllRequest(self, jsonFilePath):
        file = open(jsonFilePath, "r")
        jsonEncoded = json.loads(file.read())
        requests = jsonEncoded["requests"]
        requestParsed = []
        requestUsableParser = RequestUsableParser()
        for i in requests:
            requestParsed.append(requestUsableParser.createRequest(i))
        return requestParsed