import sys

from javagenerator.generate_invariable_java_files import GenerateInvariableJavaFiles
from javagenerator.generate_library_api_rest import GenerateLibraryAPIRest
from javagenerator.generate_retrofit2_service import GenerateRetrofit2Service
from modulegenerator.generate_module import GenerateModule
from postmanfileutils.requests_extractor import RequestExtractor
from utils import Utils


def init():
    utility = Utils(sys.argv[1], sys.argv[2])
    base_url = sys.argv[3]
    list_request_json = RequestExtractor().get_all_request(sys.argv[4])
    GenerateModule().generate_module(utility.module_name, utility.package_name,
                                     utility.get_main_folder(), utility.get_code_folder(), utility.get_values_folder(), utility.get_bodies_folder(), utility.get_module_folder())
    GenerateRetrofit2Service().create_Retrofit2Service(utility.get_code_folder(), utility.get_bodies_folder(), utility.package_name, list_request_json)
    GenerateInvariableJavaFiles().copy_invariable_java_files(utility.module_name, utility.package_name, utility.get_code_folder(), base_url)
    GenerateLibraryAPIRest().generate_library_api_rest(utility.module_name, utility.package_name, utility.get_code_folder(), list_request_json)
    print("script finished")

init()
# list_request_json = RequestExtractor().get_all_request(sys.argv[4])
# base_url = sys.argv[3]
# print(CheckerRequests().do_request(list_request_json, base_url))
