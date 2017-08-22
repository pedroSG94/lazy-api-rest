import json
from json import JSONDecodeError


class RequestUsableParser:
    def __init__(self, request_string):
        self.request_string = request_string

    def get_url(self):
        return "\"url\":" + "\"" + self.request_string["url"] + "\""

    def get_headers(self):
        return "\"headers\":" + str(self.request_string["headerData"]).replace("\'", "\"").replace("True", "\"\"").replace("False", "\"\"")

    def get_method(self):
        return "\"method\":" + "\"" + self.request_string["method"] + "\""

    def get_querys(self):
        return "\"querys\":" + str(self.request_string["queryParams"]).replace("\'", "\"").replace("True", "\"\"").replace("False", "\"\"")

    def get_body(self):
        string_body = str(self.request_string["data"]).replace("\'", "\"").replace("True", "\"\"").replace("False", "\"\"")
        if string_body == "None":
            return ""
        else:
            return ", \n\"body\":" + string_body

    def create_request(self):
        return "{\n" + self.get_method() + ", \n" + self.get_url() \
                               + ", \n" + self.get_headers() + ", \n" + self.get_querys() + \
               self.get_body() + "\n}"