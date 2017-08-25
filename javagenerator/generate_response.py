import os

from shutil import copyfile
from utils import Utils
import json


class GenerateResponse:
    def __init__(self, response_folder, class_name, package_name, json_encoded):
        self.response_folder = response_folder
        self.class_name = class_name
        self.package_name = package_name
        self.json_encoded = json_encoded

    def create_response_class(self):
        file_path = self.response_folder + os.sep + self.class_name + ".java"
        copyfile("files" + os.sep + "java" + os.sep + "Response.java", file_path)
        Utils.replace_content_in_file(file_path, "com.example.library", self.package_name)
        Utils.replace_content_in_file(file_path, "Response", self.class_name)
        string_data = self.__add_constructor_to_response()
        string_data += self.__add_attributes_setters_getters_to_response()
        Utils.replace_content_in_file(file_path, "add_data", string_data)

    def __add_constructor_to_response(self):
        string_data_response = "  public " + self.class_name + "("
        for key, value in self.json_encoded.items():
            if str(value).startswith("{"):
                name_object = str(key).title()
                string_data_response += name_object + " " + key + ","
                self.__create_internal_object(name_object, str(value).replace("'", "\""))
            else:
                string_data_response += "String " + key + ","
        string_data_response += ") {\n"
        for key, value in self.json_encoded.items():
            string_data_response += "    this." + key + " = " + key + ";\n"
        string_data_response += "  }\n\n"
        return string_data_response.replace(",)", ")")

    def __add_attributes_setters_getters_to_response(self):
        string_data_response = ""
        # attributes
        for key, value in self.json_encoded.items():
            if str(value).startswith("{"):
                string_data_response += "  private " + str(key).title() + " " + key + ";\n"
            else:
                string_data_response += "  private String " + key + ";\n"
        string_data_response += "\n"
        # setters
        for key, value in self.json_encoded.items():
            if str(value).startswith("{"):
                string_data_response += "  public void set" + str(key).title() + "(" + str(
                    key).title() + " " + key + ") { \n    this." + key + " = " + key + ";\n  }\n\n"
            else:
                string_data_response += "  public void set" + str(
                    key).title() + "(String " + key + ") { \n    this." + key + " = " + key + ";\n  }\n\n"
        # getters
        for key, value in self.json_encoded.items():
            if str(value).startswith("{"):
                string_data_response += "  public " + str(key).title() + " get" + str(
                    key).title() + "() { \n    return " + key + ";\n  }\n\n"
            else:
                string_data_response += "  public String get" + str(
                    key).title() + "() { \n    return " + key + ";\n  }\n\n"
        return string_data_response

    def __create_internal_object(self, name_object, json_data):
        print("generate internal object response: " + name_object)
        json_object_encoded = json.loads(json_data.replace("\n", ""))
        response = GenerateResponse(self.response_folder, name_object, self.package_name, json_object_encoded)
        response.create_response_class()
