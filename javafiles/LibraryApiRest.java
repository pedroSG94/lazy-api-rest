package com.example.library;

import com.pedro.library.bodies.*;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class LibraryApiRest {

  private Retrofit2Service retrofit2Service;

  public LibraryApiRest(boolean log) {
    retrofit2Service = new Retrofit2ServiceImp(Constants.BASE_URL, log).getRetrofit().create(Retrofit2Service.class);
  }

add_data
}
