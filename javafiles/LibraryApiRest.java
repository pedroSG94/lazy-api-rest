package com.example.library;

import com.pedro.library.bodies.*;
import java.io.File;
import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class LibraryApiRest {

  private Retrofit2Service retrofit2Service;

  public LibraryApiRest(boolean log) {
    retrofit2Service = new Retrofit2ServiceImp(Constants.BASE_URL, log).getRetrofit().create(Retrofit2Service.class);
  }

  private MultipartBody.Part getMultiPart(File file, String key) {
    RequestBody requestFile = RequestBody.create(MediaType.parse("multipart/form-data"), file);
    MultipartBody.Part body =
        MultipartBody.Part.createFormData(key, file.getName(), requestFile);
    return body;
  }

add_data
}
