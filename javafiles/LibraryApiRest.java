package com.example.library;


public class LibraryApiRest {

  private Retrofit2Service retrofit2Service;

  public LibraryApiRest(boolean log) {
    retrofit2Service = new Retrofit2ServiceImp(Constants.BASE_URL, log).getRetrofit().create(Retrofit2Service.class);
  }

add_data
}
