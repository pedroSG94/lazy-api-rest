import os
from shutil import copyfile
from utils import Utils


class GenerateCallback:
    def __init__(self, callback_folder, class_name, package_name):
        self.callback_folder = callback_folder
        self.class_name = class_name
        self.package_name = package_name

    def create_callback_class(self, object_name_returned):
        source_java_files_folder = "files" + os.sep + "java"
        file_path = self.callback_folder + os.sep + self.class_name + ".java"
        copyfile(source_java_files_folder + os.sep + "Callback.java",
                 self.callback_folder + os.sep + self.class_name + ".java")
        Utils.replace_content_in_file(file_path, "com.example.library", self.package_name)
        Utils.replace_content_in_file(file_path, "Callback", self.class_name)
        Utils.replace_content_in_file(file_path, "Object", object_name_returned)
