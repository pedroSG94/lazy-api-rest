package com.pedro.library;

import retrofit2.Call;
import retrofit2.http.*;

public interface Retrofit2Service {

  @DELETE("deleteFile")
  @Headers({})
  Call<Object> deleteFile(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("path") String path);

  @POST("shareFiles")
  @Headers({})
  Call<Object> shareFiles(@Header("Credentials-AccessToken") String Credentials-AccessToken);

  @POST("increaseCount")
  @Headers({})
  Call<Object> increaseCount();

  @GET("getMedia")
  @Headers({})
  Call<Object> getMedia(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("path") String path);

  @GET("getPublicFIle")
  @Headers({})
  Call<Object> getPublicFIle(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("key") String key);

  @GET("filesList")
  @Headers({})
  Call<Object> filesList(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("perPage") String perPage,@Query("page") String page,@Query("orderBy") String orderBy,@Query("order") String order,@Query("search") String search,@Query("path") String path);

  @DELETE("deleteAll")
  @Headers({})
  Call<Object> deleteAll(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("path") String path);

  @POST("addFile")
  @Headers({})
  Call<Object> addFile(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("path") String path);

  @GET("getPublicMedia")
  @Headers({})
  Call<Object> getPublicMedia(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("key") String key);

  @DELETE("deletePublicKey")
  @Headers({})
  Call<Object> deletePublicKey(@Header("Credentials-AccessToken") String Credentials-AccessToken);

  @DELETE("deleteAccess")
  @Headers({})
  Call<Object> deleteAccess(@Header("invited") String invited);

  @POST("refreshPublicKey")
  @Headers({})
  Call<Object> refreshPublicKey(@Header("Credentials-AccessToken") String Credentials-AccessToken);

  @POST("addDIr")
  @Headers({})
  Call<Object> addDIr(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("path") String path);

  @POST("createPublicKey")
  @Headers({})
  Call<Object> createPublicKey(@Header("Credentials-AccessToken") String Credentials-AccessToken);

  @POST("newAccess")
  @Headers({})
  Call<Object> newAccess(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Header("invited") String invited);

  @GET("getFile")
  @Headers({})
  Call<Object> getFile(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("path") String path);

  @POST("sendData")
  @Headers({})
  Call<Object> sendData(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("to") String to);


}