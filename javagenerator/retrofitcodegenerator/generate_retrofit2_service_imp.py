import os
from javagenerator.retrofitcodegenerator.generate_retrofit2 import GenerateRetrofit2Base


class GenerateRetrofit2ServiceImp(GenerateRetrofit2Base):
    def createRetrofit2ServiceImp(self, codeFolder, packageName):
        file = open(codeFolder + os.sep + "Retrofit2ServiceImp.java", "w")
        file.write(self.addPackage(packageName)
                   + self.createImports()
                   + "public class Retrofit2ServiceImp {\n"
                   + "\n"
                   + self.createRetrofitInstace()
                   + "}")

    def createImports(self):
        stringImport = ""
        stringImport += "import okhttp3.OkHttpClient;\n"
        stringImport += "import okhttp3.logging.HttpLoggingInterceptor;\n"
        stringImport += "import retrofit2.Retrofit;\n"
        stringImport += "import retrofit2.converter.gson.GsonConverterFactory;\n"
        stringImport += "\n\n"
        return stringImport

    def createRetrofitInstace(self):
        return "    private Retrofit retrofit;\n" \
               + "\n"\
               + "    public Retrofit2ServiceImp(String baseUrl, boolean log) {\n" \
               + "        retrofit = new Retrofit.Builder()\n" \
               + "                .baseUrl(baseUrl)\n" \
               + "                .client(getInterceptor(log))\n" \
               + "                .addConverterFactory(GsonConverterFactory.create())\n" \
               + "                .build();\n" \
               + "\n" \
               + "    }\n" \
               + "\n" \
               + "\n" \
               + "    public Retrofit getRetrofit() {\n" \
               + "        return retrofit;\n" \
               + "    }" \
               + "\n" \
               + "\n" \
               + self.createInterceptor()

    def createInterceptor(self):
        return "    private OkHttpClient getInterceptor(boolean log) {\n" \
               + "        HttpLoggingInterceptor logging = new HttpLoggingInterceptor();\n" \
               + "        logging.setLevel(log ? HttpLoggingInterceptor.Level.BODY : HttpLoggingInterceptor.Level.NONE);\n" \
               + "        OkHttpClient.Builder httpClient = new OkHttpClient.Builder();\n" \
               + "        httpClient.addInterceptor(logging);\n" \
               + "        return httpClient.build();\n" \
               + "    }\n"
