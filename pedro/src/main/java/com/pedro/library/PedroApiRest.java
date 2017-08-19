package com.pedro.library;


public class PedroApiRest.java {

  private Retrofit2Service retrofit2Service;

  public PedroApiRest.java(boolean log) {
    retrofit2Service = new Retrofit2ServiceImp(Constants.BASE_URL, log).getRetrofit().create(Retrofit2Service.class);
  }

add_data
}
