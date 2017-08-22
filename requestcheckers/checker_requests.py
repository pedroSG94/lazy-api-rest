import subprocess
import json
import re


class CheckerRequests:
    # send a curl command to get responses
    def doRequest(self, listRequestJson, urlBase):
        for i in listRequestJson:
            jsonEncoded = json.loads(i.replace("\n", ""))
            # curl command with a url
            command = ['curl', '-X', jsonEncoded["method"]]
            # add headers to command
            for h in jsonEncoded["headers"]:
                command.append('-H ' + h["key"] + ': ' + h["value"] + '')
            # add bodies to command
            # for b in jsonEncoded["data"]:
            #     command.append('-d')
            #     command.append("")

            stringUrl = 'https://file.streye.com/'
            # add destiny
            regularExpresion = '\/(.*)\?'
            url = jsonEncoded["url"]
            try:
                destiny = re.search(regularExpresion, url, re.I | re.U).group(0)
            except AttributeError:
                destiny = str(url)[str(url).index('/'):]
            destiny = destiny.replace("/", "").replace("?", "")
            stringUrl += destiny
            cont = 0
            # add querys to command
            for q in jsonEncoded["querys"]:
                if cont == 0:
                    stringUrl += "?"
                else:
                    stringUrl += "&"
                stringUrl += q["key"] + '=' + q["value"]
            command.append(stringUrl)
            print(command)
            response = subprocess.run(command)
            if (response.stderr != None):
                print("all ok")
            else:
                print("command failed")


