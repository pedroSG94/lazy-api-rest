package com.casdac.lib;

import okhttp3.OkHttpClient;
import okhttp3.logging.HttpLoggingInterceptor;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class Retrofit2ServiceImp {

  private Retrofit retrofit;

  public Retrofit2ServiceImp(String baseUrl, boolean log) {
    retrofit = new Retrofit.Builder().baseUrl(baseUrl)
        .client(getInterceptor(log))
        .addConverterFactory(GsonConverterFactory.create())
        .build();
  }

  public Retrofit getRetrofit() {
    return retrofit;
  }

  private OkHttpClient getInterceptor(boolean log) {
    HttpLoggingInterceptor logging = new HttpLoggingInterceptor();
    logging.setLevel(log ? HttpLoggingInterceptor.Level.BODY : HttpLoggingInterceptor.Level.NONE);
    OkHttpClient.Builder httpClient = new OkHttpClient.Builder();
    httpClient.addInterceptor(logging);
    return httpClient.build();
  }
}