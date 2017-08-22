import subprocess
import json
import re


class CheckerRequests:
    # send a curl command to get responses
    def do_request(self, list_request_json, url_base):
        for i in list_request_json:
            json_encoded = json.loads(i.replace("\n", ""))
            # curl command with a url
            command = ['curl', '-X', json_encoded["method"]]
            # add headers to command
            for h in json_encoded["headers"]:
                command.append('-H ' + h["key"] + ': ' + h["value"] + '')
            # add bodies to command
            # for b in jsonEncoded["data"]:
            #     command.append('-d')
            #     command.append("")

            string_url = url_base + "/"
            # add destiny
            regular_expresion = '\/(.*)\?'
            url = json_encoded["url"]
            try:
                destiny = re.search(regular_expresion, url, re.I | re.U).group(0)
            except AttributeError:
                destiny = str(url)[str(url).index('/'):]
            destiny = destiny.replace("/", "").replace("?", "")
            string_url += destiny
            cont = 0
            # add querys to command
            for q in json_encoded["querys"]:
                if cont == 0:
                    string_url += "?"
                else:
                    string_url += "&"
                string_url += q["key"] + '=' + q["value"]
            command.append(string_url)
            print(command)
            response = subprocess.run(command)
            if response.stderr != None:
                print("all ok")
            else:
                print("command failed")


