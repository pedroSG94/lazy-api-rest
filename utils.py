import os


class Utils:
    def __init__(self, module_name, package_name):
        self.module_name = module_name
        self.package_name = package_name

    def get_module_folder(self):
        return ".." + os.sep + str(self.module_name)

    def get_main_folder(self):
        return self.get_module_folder() + os.sep + "src" + os.sep + "main"

    def get_values_folder(self):
        return self.get_main_folder() + os.sep + "res" + os.sep + "values"

    def get_code_folder(self):
        return self.get_main_folder() + os.sep + "java" + os.sep + str(self.package_name).replace(".", os.sep)

    def get_bodies_folder(self):
        return self.get_code_folder() + os.sep + "bodies"

    def get_responses_folder(self):
        return self.get_code_folder() + os.sep + "responses"

    def get_callbacks_folder(self):
        return self.get_code_folder() + os.sep + "callbacks"

    @staticmethod
    def reformat_variables(variable_name):
        valid_variable = variable_name
        # delete no valid characters
        for ch in {"-", "*", "+", "/"}:
            if ch in valid_variable:
                valid_variable = str(valid_variable).replace(ch, "")
        # check if start with a number, in this case add "a" letter to the variable
        try:
            int(variable_name[:1])
            return "a" + valid_variable
        except ValueError:
            return valid_variable

    @staticmethod
    def replace_content_in_file(file_path, old_content, new_content):
        f = open(file_path, "r")
        new_file_content = f.read().replace(old_content, new_content)
        f.flush()
        f.close()
        f = open(file_path, "w")
        f.write(new_file_content)
        f.flush()
        f.close()
