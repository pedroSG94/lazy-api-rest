from modulegenerator.create_module import GenerateModule
from postmanfileutils.requests_extractor import RequestExtractor
from javagenerator.retrofitcodegenerator.generate_retrofit2_service import GenerateRetrofit2Service

def init():
    listRequestJson = []
    for i in RequestExtractor().getAllRequest("test.json"):
        print(i)
        listRequestJson.append(i)
    GenerateModule().generateModule("pedro", "com.example.library")
    GenerateRetrofit2Service().createRetrofit2Service("pedro", "com.example.library", listRequestJson)

init()