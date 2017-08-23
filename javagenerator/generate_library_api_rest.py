import os
import json
import re
from shutil import copyfile
from utils import Utils


class GenerateLibraryAPIRest:
    def generate_library_api_rest(self, module_name, package_name, code_folder, list_request_json):
        file_destiny = code_folder + os.sep + str(module_name).title() + "ApiRest.java"
        copyfile("files" + os.sep + "java" + os.sep + "LibraryApiRest.java", file_destiny)
        file = open(file_destiny, "r")
        string_file = file.read()
        string_file = string_file.replace("LibraryApiRest", str(module_name).title() + "ApiRest").replace(
            "com.example.library", package_name)
        file.flush()
        file.close()
        file = open(file_destiny, "w")
        string_file = string_file.replace("add_data", self.__generate_api_rest_methods(list_request_json, module_name))
        file.write(string_file)
        file.flush()
        file.close()
        print("generate_library_API_rest finished")

    def __generate_api_rest_methods(self, list_request_json, module_name):
        string_methods = ""
        for i in list_request_json:
            string_methods += self.__create_method(i, module_name)
        return string_methods

    def __generate_callback_response_in_method(self, module_name):
        return ".enqueue(new Callback<Object>() {\n" \
               + "      @Override\n" \
               + "      public void onResponse(Call<Object> call, Response<Object> response) {\n" \
               + "        if (response.isSuccessful()) {\n" \
               + "          " + module_name + "callback.onSuccess(response.toString());\n" \
               + "        } else {\n" \
               + "          " + module_name + "callback.onError(new ErrorResponse(response.code(), response.message()));\n" \
               + "        }\n" \
               + "      }\n" \
               + "\n" \
               + "      @Override\n" \
               + "      public void onFailure(Call<Object> call, Throwable t) {\n" \
               + "        " + module_name + "callback.onError(new ErrorResponse(-1, t.getMessage()));\n" \
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

    def __create_method(self, json_code, module_name):
        string_parameters = ""
        string_parameters_to_service = "("
        json_encoded = json.loads(json_code.replace("\n", ""))
        # add headers not final
        for h in json_encoded["headers"]:
            if not str(h["description"]) == "final":
                string_parameters += "String " + Utils.reformat_variables(h["key"]) + ","
                string_parameters_to_service += h["key"] + ","
        # add querys
        for q in json_encoded["querys"]:
            string_parameters += "String " + q["key"] + ","
            string_parameters_to_service += q["key"] + ","
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
                    string_parameters_to_service += "getMultiPart(" + b["key"] + ",\"" + b["key"] + "\"),"

        except KeyError:
            pass
        string_parameters_to_service += ")"
        string_parameters_to_service = string_parameters_to_service.replace(",)", ")")
        string_method = "  public void " + self.__get_method_name(json_code) + "(" + string_parameters \
                        + "final " + str(module_name).title() + "Callback " + Utils.reformat_variables(
            module_name + "callback") + ") {\n" \
                        + "    retrofit2Service." + self.__get_method_name(json_code) + string_parameters_to_service \
                        + self.__generate_callback_response_in_method(module_name) + "  }\n\n"
        return string_method
