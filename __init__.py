from modulegenerator.create_module import GenerateModule
from postmanfileutils.requests_extractor import RequestExtractor
from javagenerator.retrofitcodegenerator.generate_retrofit2_service import GenerateRetrofit2Service
from javagenerator.utilsgenerator.create_invariable_java_files import CreateInvariableJavaFiles
from javagenerator.apigenerator.generate_library_api_rest import GenerateLibraryAPIRest
import utils
import sys

def init():
    listRequestJson = []
    utils.moduleName = sys.argv[1]
    utils.packageName = sys.argv[2]
    utils.baseUrl = sys.argv[3]
    for i in RequestExtractor().getAllRequest(sys.argv[4]):
        listRequestJson.append(i)
    GenerateModule().generateModule(utils.moduleName, utils.packageName,
                                    utils.getMainFolder(), utils.getCodeFolder(), utils.getValuesFolder(), utils.getBodiesFolder())
    GenerateRetrofit2Service().createRetrofit2Service(utils.getCodeFolder(), utils.getBodiesFolder(), utils.packageName, listRequestJson)
    CreateInvariableJavaFiles().copyInvariableJavaFiles(utils.moduleName, utils.packageName, utils.getCodeFolder(), utils.baseUrl)
    GenerateLibraryAPIRest().generateLibraryAPIRest(utils.moduleName, utils.packageName, utils.getCodeFolder(), listRequestJson)

init()
