import os
from shutil import copyfile
from utils import Utils


class GenerateInvariableJavaFiles:
    def copy_invariable_java_files(self, module_name, package_name, code_folder, base_url):
        source_java_files_folder = "files" + os.sep + "java"
        copyfile(source_java_files_folder + os.sep + "ErrorResponse.java", code_folder + os.sep + "ErrorResponse.java")
        copyfile(source_java_files_folder + os.sep + "LibraryCallback.java", code_folder + os.sep + str(module_name).title().replace(" ", "") + "Callback.java")
        copyfile(source_java_files_folder + os.sep + "Retrofit2ServiceImp.java", code_folder + os.sep + "Retrofit2ServiceImp.java")
        copyfile(source_java_files_folder + os.sep + "Constants.java", code_folder + os.sep + "Constants.java")
        self.__modify_package(module_name, package_name, code_folder, base_url)
        print("copy_invariable_java_files finished")

    def __modify_package(self, module_name, package_name, code_folder, base_url):
        Utils.replace_content_in_file(code_folder + os.sep + "ErrorResponse.java", "com.example.library", package_name)

        Utils.replace_content_in_file(code_folder + os.sep + str(module_name).title().replace(" ", "") + "Callback.java", "com.example.library", package_name)
        Utils.replace_content_in_file(code_folder + os.sep + str(module_name).title().replace(" ", "") + "Callback.java", "Library", str(module_name).title().replace(" ", ""))

        Utils.replace_content_in_file(code_folder + os.sep + "Retrofit2ServiceImp.java", "com.example.library", package_name)

        Utils.replace_content_in_file(code_folder + os.sep + "Constants.java", "com.example.library", package_name)
        Utils.replace_content_in_file(code_folder + os.sep + "Constants.java", "http://exampleurl.com", base_url)
