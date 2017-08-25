import os
import json
import re
from shutil import copyfile
from utils import Utils


class GenerateLibraryAPIRest:
    def generate_library_api_rest(self, module_name, package_name, code_folder, list_request_json, dict_response_json):
        file_destiny = code_folder + os.sep + str(module_name).title() + "ApiRest.java"
        copyfile("files" + os.sep + "java" + os.sep + "LibraryApiRest.java", file_destiny)
        file = open(file_destiny, "r")
        string_file = file.read()
        string_file = string_file.replace("LibraryApiRest", str(module_name).title() + "ApiRest").replace(
            "com.example.library", package_name)
        file.flush()
        file.close()
        file = open(file_destiny, "w")
        string_file = string_file.replace("add_data",
                                          self.__generate_api_rest_methods(list_request_json, dict_response_json))
        file.write(string_file)
        file.flush()
        file.close()
        print("generate_library_API_rest finished")

    def __generate_api_rest_methods(self, list_request_json, dict_response_json):
        string_methods = ""
        for i in list_request_json:
            string_methods += self.__create_method(i, dict_response_json)
        return string_methods

    def __generate_callback_response_in_method(self, method_name, dict_response_json):
        string_response_name = "Object"
        if dict_response_json.get(method_name) != "invalid json":
            string_response_name = str(method_name).title() + "Response"
        return ".enqueue(new Callback<" + string_response_name + ">() {\n" \
               + "      @Override\n" \
               + "      public void onResponse(Call<" + string_response_name + "> call, Response<" + string_response_name + "> response) {\n" \
               + "        if (response.isSuccessful()) {\n" \
               + "          callback.onSuccess(response.body());\n" \
               + "        } else {\n" \
               + "          callback.onError(new ErrorResponse(response.code(), response.message()));\n" \
               + "        }\n" \
               + "      }\n" \
               + "\n" \
               + "      @Override\n" \
               + "      public void onFailure(Call<" + string_response_name + "> call, Throwable t) {\n" \
               + "        callback.onError(new ErrorResponse(-1, t.getMessage()));\n" \
               + "      }\n" \
               + "    });\n"

    def __get_method_name(self, json_code):
        json_encoded = json.loads(json_code.replace("\n", ""))
        url = json_encoded["url"]
        regular_expresion = '\/(.*)\?'
        try:
            destiny = re.search(regular_expresion, url, re.I | re.U).group(0)
        except AttributeError:
            destiny = str(url)[str(url).index('/'):]
        destiny = destiny.replace("/", "").replace("?", "")
        return destiny

    def __create_method(self, json_code, dict_response_json):
        string_parameters = ""
        string_parameters_to_service = "("
        json_encoded = json.loads(json_code.replace("\n", ""))
        # add headers not final
        for h in json_encoded["headers"]:
            if not str(h["description"]) == "final":
                string_parameters += "String " + Utils.reformat_variables(h["key"]) + ","
                string_parameters_to_service += Utils.reformat_variables(h["key"]) + ","
        # add querys
        for q in json_encoded["querys"]:
            string_parameters += "String " + Utils.reformat_variables(q["key"]) + ","
            string_parameters_to_service += Utils.reformat_variables(q["key"]) + ","
        # add bodies
        try:
            cont = 0
            for b in json_encoded["body"]:
                if b["type"] == "text":
                    if cont < 1:
                        string_class_body = self.__get_method_name(json_code)
                        string_parameters += string_class_body.title() + "Body " + Utils.reformat_variables(
                            string_class_body + "body") + ","
                        string_parameters_to_service += string_class_body + "body,"
                    cont += 1
                elif b["type"] == "file":
                    string_parameters += "File " + Utils.reformat_variables(b["key"]) + ","
                    string_parameters_to_service += "getMultiPart(" + Utils.reformat_variables(b["key"]) + ",\"" + b[
                        "key"] + "\"),"

        except KeyError:
            pass
        string_callback_name = "DefaultCallback"
        if dict_response_json.get(self.__get_method_name(json_code)) != "invalid json":
            string_callback_name = str(self.__get_method_name(json_code)).title() + "Callback"
        string_parameters_to_service += ")"
        string_parameters_to_service = string_parameters_to_service.replace(",)", ")")
        string_method = "  public void " + self.__get_method_name(json_code) + "(" + string_parameters \
                        + "final " + string_callback_name + " callback) {\n" \
                        + "    retrofit2Service." + self.__get_method_name(json_code) + string_parameters_to_service \
                        + self.__generate_callback_response_in_method(self.__get_method_name(json_code),
                                                                      dict_response_json) + "  }\n\n"
        return string_method
