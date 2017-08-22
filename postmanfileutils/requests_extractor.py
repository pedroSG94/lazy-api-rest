import json
from postmanfileutils.request_variable_usable_parser import RequestUsableParser


class RequestExtractor:
    def get_all_request(self, json_file_path):
        file = open(json_file_path, "r")
        json_encoded = json.loads(file.read())
        requests = json_encoded["requests"]
        request_parsed = []
        for i in requests:
            request_parsed.append(RequestUsableParser(i).create_request())
        print("get_all_request finished")
        return request_parsed
