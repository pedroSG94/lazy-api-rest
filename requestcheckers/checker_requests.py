import subprocess
import json
import re


class CheckerRequests:
    # send a curl command to get responses
    def do_request(self, list_request_json, url_base):
        dict_response_json = {}
        for i in list_request_json:
            json_encoded = json.loads(i.replace("\n", ""))
            # curl command with a url
            command = "curl -X " + json_encoded["method"]
            # command = ['curl', '-X', json_encoded["method"]]
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
                command += " -H " + h["key"] + ": " + h["value"]
                # command.append('-H ' + h["key"] + ': ' + h["value"] + '')
            # add querys to command
            for q in json_encoded["querys"]:
                if cont == 0:
                    string_url += "?"
                else:
                    string_url += "&"
                string_url += q["key"] + '=' + q["value"]
            command += " " + string_url
            console = ConsoleCommand()
            print(command)
            response = console.execute_console_command(command)
            print(response)
            if response == "command error":
                print("request failed")
                dict_response_json[destiny] = "invalid json"
            else:
                print("request success")
                try:
                    json.loads(response)
                    dict_response_json[destiny] = response
                except json.JSONDecodeError:
                    dict_response_json[destiny] = "invalid json"
            # command.append(string_url)
            # TODO add bodies to command
            # for b in json_encoded["data"]:
            #     command.append('-d ' + b)
            # response = subprocess.run(command, universal_newlines=False, stdout=subprocess.PIPE)
            # string_response = response.stdout.decode("utf-8").replace("\n", "")
            # print(string_response)
            # if response.returncode == 200:
            #     print("request success")
            #     try:
            #         json.loads(string_response)
            #         dict_response_json[destiny] = string_response
            #     except json.JSONDecodeError:
            #         dict_response_json[destiny] = "invalid json"
            # else:
            #     print("request failed")
            #     dict_response_json[destiny] = "invalid json"
        return dict_response_json


class ConsoleCommand:
    def __init__(self):
        pass

    def execute_sudo_console_command(self, password, command):
        command_list = ["sudo", "-S"]
        command_list.extend(command.split(" "))
        p = subprocess.Popen(command_list, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, err = p.communicate(str(password + "\n").encode())
        if out is not None:
            return out.decode("utf-8")
        else:
            return err.decode("utf-8")

    def execute_console_command(self, command):
        try:
            command_list = []
            command_list.extend(command.split(" "))
            result = subprocess.check_output(command_list)
            return result.decode("utf-8")
        except subprocess.CalledProcessError:
            return "command error"