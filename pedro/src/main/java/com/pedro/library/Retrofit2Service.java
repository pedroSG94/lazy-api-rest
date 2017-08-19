package com.pedro.library;


import retrofit2.Call;
import retrofit2.http.*;


public interface Retrofit2Service {

@DELETE("deleteFile")
Call<Object> deleteFile(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("path") String path);

@POST("shareFiles")
Call<Object> shareFiles(@Header("Credentials-AccessToken") String Credentials-AccessToken);

@POST("increaseCount")
Call<Object> increaseCount();

@GET("getMedia")
Call<Object> getMedia(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("path") String path);

@GET("getPublicFIle")
Call<Object> getPublicFIle(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("key") String key);

@GET("filesList")
Call<Object> filesList(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("perPage") String perPage,@Query("page") String page,@Query("orderBy") String orderBy,@Query("order") String order,@Query("search") String search,@Query("path") String path);

@DELETE("deleteAll")
Call<Object> deleteAll(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("path") String path);

@POST("addFile")
Call<Object> addFile(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("path") String path);

@GET("getPublicMedia")
Call<Object> getPublicMedia(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("key") String key);

@DELETE("deletePublicKey")
Call<Object> deletePublicKey(@Header("Credentials-AccessToken") String Credentials-AccessToken);

@DELETE("deleteAccess")
Call<Object> deleteAccess(@Header("invited") String invited);

@POST("refreshPublicKey")
Call<Object> refreshPublicKey(@Header("Credentials-AccessToken") String Credentials-AccessToken);

@POST("addDIr")
Call<Object> addDIr(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("path") String path);

@POST("createPublicKey")
Call<Object> createPublicKey(@Header("Credentials-AccessToken") String Credentials-AccessToken);

@POST("newAccess")
Call<Object> newAccess(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Header("invited") String invited);

@GET("getFile")
Call<Object> getFile(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("path") String path);

@POST("sendData")
Call<Object> sendData(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("to") String to);

}