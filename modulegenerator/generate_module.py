import os
from shutil import copyfile
from utils import Utils


class GenerateModule:
    def generate_module(self, module_name, package_name, main_folder, code_folder, values_folder, bodies_folder, module_folder):
        self.create_all_folders(code_folder, values_folder, bodies_folder)
        self.create_gradle(module_folder)
        self.create_android_manifest_xml(main_folder, package_name)
        self.create_strings_xml(values_folder, module_name)
        print("generate_module finished")

    def create_all_folders(self, code_folder, values_folder, bodies_folder):
        try:
            os.makedirs(code_folder)
        except FileExistsError:
            print("code folders exists")
        try:
            os.makedirs(values_folder)
        except FileExistsError:
            print("values folders exists")
        try:
            os.makedirs(bodies_folder)
        except FileExistsError:
            print("bodies folders exists")

    def create_gradle(self, module_folder):
        copyfile("files" + os.sep + "gradle" + os.sep + "build.gradle", module_folder + os.sep + "build.gradle")

    def create_strings_xml(self, values_folder, module_name):
        file_path = "files" + os.sep + "xml" + os.sep + "strings.xml"
        copyfile(file_path, values_folder + os.sep + "strings.xml")
        Utils.replace_content_in_file(file_path, "library", module_name)

    def create_android_manifest_xml(self, main_folder, package_name):
        file_path = "files" + os.sep + "xml" + os.sep + "AndroidManifest.xml"
        copyfile(file_path, main_folder + os.sep + "AndroidManifest.xml")
        Utils.replace_content_in_file(file_path, "com.example.library", package_name)
