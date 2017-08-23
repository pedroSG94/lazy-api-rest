import os
from shutil import copyfile
from utils import Utils


class GenerateBody:
    def __init__(self, body_folder, class_name, package_name, json_encoded):
        self.body_folder = body_folder
        self.class_name = class_name
        self.package_name = package_name
        self.json_encoded = json_encoded

    def create_body_class(self):
        file_path = self.body_folder + os.sep + self.class_name + ".java"
        copyfile("files" + os.sep + "java" + os.sep + "Body.java", file_path)
        Utils.replace_content_in_file(file_path, "com.example.library", self.package_name)
        string_data = self.__add_constructor_to_body()
        string_data += self.__add_attributes_setters_getters_to_body()
        Utils.replace_content_in_file(file_path, "add_data", string_data)

    def __add_constructor_to_body(self):
        string_data_body = "public " + self.class_name + "("
        for body in self.json_encoded["body"]:
            if body["type"] == "text":
                string_data_body += "String " + body["key"] + ","
                pass
        string_data_body += ") {\n"
        string_data_body = string_data_body.replace(",)", ")")
        for body in self.json_encoded["body"]:
            if body["type"] == "text":
                string_data_body += "  this." + body["key"] + " = " + body["key"] + ";\n"
        string_data_body += "}\n\n"
        return string_data_body

    def __add_attributes_setters_getters_to_body(self):
        string_data_body = ""
        for body in self.json_encoded["body"]:
            if body["type"] == "text":
                string_data_body += "private String " + body["key"] + ";\n\n"
                string_data_body += "public void set" + str(body["key"]).title() + "(String " + body["key"] + ") {\n" \
                                    + "  this." + body["key"] + " = " + body["key"] + ";\n}\n\n"
                string_data_body += "public String get" + str(body["key"]).title() + "() {\n" \
                                    + "  return " + body["key"] + ";\n}\n\n"
        return string_data_body
