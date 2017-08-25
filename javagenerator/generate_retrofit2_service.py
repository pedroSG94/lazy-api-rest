import os
import json
import re
from shutil import copyfile
from utils import Utils
from javagenerator.generate_body import GenerateBody
from javagenerator.generate_response import GenerateResponse
from javagenerator.generate_callback import GenerateCallback


class GenerateRetrofit2Service:
    def create_Retrofit2Service(self, code_folder, bodies_folder, package_name, list_request_json, dict_response_json,
                                response_folder, callback_folder):
        copyfile("files" + os.sep + "java" + os.sep + "Retrofit2Service.java",
                 code_folder + os.sep + "Retrofit2Service.java")
        file = open(code_folder + os.sep + "Retrofit2Service.java", "r")
        string_file = file.read().replace("com.example.library", package_name)
        string_file = string_file.replace("add_data",
                                          self.__create_requests(list_request_json, package_name, bodies_folder,
                                                                 dict_response_json, response_folder, callback_folder))
        file.flush()
        file.close()
        file = open(code_folder + os.sep + "Retrofit2Service.java", "w")
        file.write(string_file)
        file.flush()
        file.close()
        print("create_Retrofit2Service finished")

    def __create_requests(self, list_request_json, package_name, bodies_folder, dict_response_json, response_folder, callback_folder):
        string_request = ""
        for i in list_request_json:
            json_encoded = json.loads(i.replace("\n", ""))
            url = json_encoded["url"]
            regular_expresion = '\/(.*)\?'
            try:
                destiny = re.search(regular_expresion, url, re.I | re.U).group(0)
            except AttributeError:
                destiny = str(url)[str(url).index('/'):]
            destiny = destiny.replace("/", "").replace("?", "")
            string_request += "  @" + json_encoded["method"] + \
                              "(\"" + destiny + "\")\n"
            # add @Multipart to request if needed
            try:
                for body in json_encoded["body"]:
                    if body["type"] == "file":
                        string_request += "  @Multipart\n"
                        break
            except KeyError:
                pass
            string_request += "  @Headers({"
            # add headers without values to requests
            for header in json_encoded["headers"]:
                # add final header in @Headers({})
                if str(header["description"]) == "final":
                    string_request += "\"" + str(header["key"]) + ": " + header["value"] + "\","
            string_request += "})\n"
            # fix last iteration of headers
            string_request = string_request.replace(",}", "}")
            response_class_name = destiny.title() + "Response"
            callback_class_name = destiny.title() + "Callback"
            json_response = dict_response_json.get(destiny)
            if json_response != "invalid json":
                GenerateResponse(response_folder, response_class_name, package_name,
                                 json.loads(json_response)).create_response_class()
                GenerateCallback(callback_folder, callback_class_name, package_name).create_callback_class(response_class_name)
                string_request += "  Call<" + response_class_name + "> " + destiny + "("
            else:
                print("response error in request, retrofit return a Object")
                string_request += "  Call<Object> " + destiny + "("
            # add headers  with values to requests
            for header in json_encoded["headers"]:
                # header not final add header to method
                if not str(header["description"]) == "final":
                    string_request += "@Header(\"" + str(header["key"]) + "\") String " + Utils.reformat_variables(
                        str(header["key"])) + ","
            # add querys to requests
            for query in json_encoded["querys"]:
                string_request += "@Query(\"" + str(query["key"]) + "\") String " + Utils.reformat_variables(
                    str(query["key"])) + ","
            try:
                string_body_class_name = destiny.title() + "Body"
                body_class_needed = False
                # add bodies
                cont = 0
                for body in json_encoded["body"]:
                    if body["type"] == "text":
                        if cont < 1:
                            string_request += "@Body " + string_body_class_name + " " + Utils.reformat_variables(
                                destiny + "body") + ","
                            body_class_needed = True
                        cont += 1
                    elif body["type"] == "file":
                        string_request += "@Part MultipartBody.Part " + Utils.reformat_variables(body["key"]) + ","
                if body_class_needed:
                    GenerateBody(bodies_folder, string_body_class_name, package_name, json_encoded).create_body_class()
            except KeyError:
                pass
            string_request += ");\n\n"
            # fix last iteration headers with values and querys
            string_request = string_request.replace(",)", ")")
        return string_request
