import os
import json
import re
from shutil import copyfile
from utils import Utils


class GenerateRetrofit2Service:
    def create_Retrofit2Service(self, code_folder, bodies_folder, package_name, list_request_json):
        copyfile("files" + os.sep + "java" + os.sep + "Retrofit2Service.java", code_folder + os.sep + "Retrofit2Service.java")
        file = open(code_folder + os.sep + "Retrofit2Service.java", "r")
        string_file = file.read().replace("com.example.library", package_name)
        string_file = string_file.replace("add_data", self.create_requests(list_request_json, package_name, bodies_folder))
        file.flush()
        file.close()
        file = open(code_folder + os.sep + "Retrofit2Service.java", "w")
        file.write(string_file)
        file.flush()
        file.close()
        print("create_Retrofit2Service finished")

    def create_requests(self, list_request_json, package_name, bodies_folder):
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
            string_request += "  Call<Object> " + destiny + "("
            # add headers  with values to requests
            for header in json_encoded["headers"]:
                # header not final add header to method
                if not str(header["description"]) == "final":
                    string_request += "@Header(\"" + str(header["key"]) + "\") String " + Utils.reformat_variables(str(header["key"])) + ","
            # add querys to requests
            for query in json_encoded["querys"]:
                string_request += "@Query(\"" + str(query["key"]) + "\") String " + Utils.reformat_variables(str(query["key"])) + ","
            try:
                string_body_class_name = destiny.title() + "Body"
                body_class_needed = False
                # add bodies
                cont = 0
                for body in json_encoded["body"]:
                    if body["type"] == "text":
                        if cont < 1:
                            string_request += "@Body " + string_body_class_name + " " + Utils.reformat_variables(destiny + "body") + ","
                            body_class_needed = True
                        cont += 1
                    elif body["type"] == "file":
                        string_request += "@Part MultipartBody.Part " + Utils.reformat_variables(body["key"]) + ","
                if body_class_needed:
                    self.create_body_class(bodies_folder, string_body_class_name, package_name)
                    file = open(bodies_folder + os.sep + string_body_class_name + ".java", "r")
                    string_body = file.read()
                    file.flush()
                    file.close()
                    file = open(bodies_folder + os.sep + string_body_class_name + ".java", "w")
                    # add constructor to body
                    string_data_body = self.add_constructor_to_body(json_encoded, string_body_class_name)
                    # add attributes with setters and getters to body
                    string_data_body += self.add_attributes_setters_getters_to_body(json_encoded)
                    file.write(string_body.replace("add_data", string_data_body))
                    file.flush()
                    file.close()
            except KeyError:
                pass
            string_request += ");\n\n"
            # fix last iteration headers with values and querys
            string_request = string_request.replace(",)", ")")
        return string_request

    def create_body_class(self, bodies_folder, body_class_name, package_name):
        copyfile("files" + os.sep + "java" + os.sep + "Body.java", bodies_folder + os.sep + body_class_name + ".java")
        file = open(bodies_folder + os.sep + body_class_name + ".java", "r")
        string_body = file.read()
        string_body = string_body.replace("Body", body_class_name).replace("com.example.library", package_name)
        file.flush()
        file.close()
        file = open(bodies_folder + os.sep + body_class_name + ".java", "w")
        file.write(string_body)
        file.flush()
        file.close()

    def add_constructor_to_body(self, json_encoded, string_body_class_name):
        string_data_body = "public " + string_body_class_name + "("
        for body in json_encoded["body"]:
            if body["type"] == "text":
                string_data_body += "String " + body["key"] + ","
                pass
        string_data_body += ") {\n"
        string_data_body = string_data_body.replace(",)", ")")
        for body in json_encoded["body"]:
            if body["type"] == "text":
                string_data_body += "  this." + body["key"] + " = " + body["key"] + ";\n"
        string_data_body += "}\n\n"
        return string_data_body

    def add_attributes_setters_getters_to_body(self, json_encoded):
        string_data_body = ""
        for body in json_encoded["body"]:
            if body["type"] == "text":
                string_data_body += "private String " + body["key"] + ";\n\n"
                string_data_body += "public void set" + str(body["key"]).title() + "(String " + body["key"] + ") {\n" \
                                  + "  this." + body["key"] + " = " + body["key"] + ";\n}\n\n"
                string_data_body += "public String get" + str(body["key"]).title() + "() {\n" \
                                  + "  return " + body["key"] + ";\n}\n\n"
        return string_data_body
