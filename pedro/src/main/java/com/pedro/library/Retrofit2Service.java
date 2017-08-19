package com.pedro.library;

import com.pedro.library.bodies.*;
import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.http.*;

public interface Retrofit2Service {

  @DELETE("deleteFile")
  @Headers({})
  Call<Object> deleteFile(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("path") String path);

  @POST("shareFiles")
  @Headers({})
  Call<Object> shareFiles(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Body SharefilesBody shareFilesbody);

  @POST("increaseCount")
  @Headers({})
  Call<Object> increaseCount(@Body IncreasecountBody increaseCountbody);

  @GET("getMedia")
  @Headers({})
  Call<Object> getMedia(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("path") String path);

  @GET("getPublicFIle")
  @Headers({})
  Call<Object> getPublicFIle(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("key") String key);

  @GET("filesList")
  @Headers({"Content-Type: application/json"})
  Call<Object> filesList(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("perPage") String perPage,@Query("page") String page,@Query("orderBy") String orderBy,@Query("order") String order,@Query("search") String search,@Query("path") String path);

  @DELETE("deleteAll")
  @Headers({})
  Call<Object> deleteAll(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("path") String path);

  @POST("addFile")
  @Multipart
  @Headers({})
  Call<Object> addFile(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("path") String path,@Part MultipartBody.Part image);

  @GET("getPublicMedia")
  @Headers({})
  Call<Object> getPublicMedia(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("key") String key);

  @DELETE("deletePublicKey")
  @Headers({})
  Call<Object> deletePublicKey(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Body DeletepublickeyBody deletePublicKeybody);

  @DELETE("deleteAccess")
  @Headers({"invited: alfonsos"})
  Call<Object> deleteAccess();

  @POST("refreshPublicKey")
  @Headers({})
  Call<Object> refreshPublicKey(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Body RefreshpublickeyBody refreshPublicKeybody);

  @POST("addDIr")
  @Headers({})
  Call<Object> addDIr(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("path") String path,@Body AdddirBody addDIrbody);

  @POST("createPublicKey")
  @Headers({})
  Call<Object> createPublicKey(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Body CreatepublickeyBody createPublicKeybody);

  @POST("newAccess")
  @Headers({"invited: alfonsos"})
  Call<Object> newAccess(@Header("Credentials-AccessToken") String Credentials-AccessToken);

  @GET("getFile")
  @Headers({})
  Call<Object> getFile(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("path") String path);

  @POST("sendData")
  @Multipart
  @Headers({})
  Call<Object> sendData(@Header("Credentials-AccessToken") String Credentials-AccessToken,@Query("to") String to,@Part MultipartBody.Part image,@Body SenddataBody sendDatabody);


}