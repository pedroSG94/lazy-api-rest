import subprocess
import json
import re


class CheckerRequests:
    # send a curl command to get responses
    def do_request(self, list_request_json, url_base):
        list_response_json = []
        for i in list_request_json:
            json_encoded = json.loads(i.replace("\n", ""))
            # curl command with a url
            command = ['curl', '-X', json_encoded["method"]]
            string_url = url_base + "/"
            # add destiny
            regular_expression = '\/(.*)\?'
            url = json_encoded["url"]
            try:
                destiny = re.search(regular_expression, url, re.I | re.U).group(0)
            except AttributeError:
                destiny = str(url)[str(url).index('/'):]
            destiny = destiny.replace("/", "").replace("?", "")
            string_url += destiny
            cont = 0
            # add headers to command
            for h in json_encoded["headers"]:
                command.append('-H ' + h["key"] + ': ' + h["value"] + '')
            # add querys to command
            for q in json_encoded["querys"]:
                if cont == 0:
                    string_url += "?"
                else:
                    string_url += "&"
                string_url += q["key"] + '=' + q["value"]
            command.append(string_url)
            # TODO add bodies to command
            # for b in json_encoded["data"]:
            #     command.append('-d ' + b)
            response = subprocess.run(command, universal_newlines=False, stdout=subprocess.PIPE)
            if response.returncode == 200:
                print("request success")
                string_response = response.stdout.decode("utf-8").replace("\n", "")
                try:
                    json.loads(string_response)
                    list_response_json.append(string_response)
                except json.JSONDecodeError:
                    list_response_json.append("invalid json")
            else:
                print("request failed")
                list_response_json.append("invalid json")
        return list_response_json
