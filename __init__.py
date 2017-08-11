from modulegenerator.create_module import GenerateModule
from postmanfileutils.requests_extractor import RequestExtractor


def init():
    for i in RequestExtractor().getAllRequest("test.json"):
        print(i)
    GenerateModule.generateModule("pedro", "com.example.library")

init()