package com.example.library;


import retrofit2.Call;
import retrofit2.http.*;

public interface Retrofit2Service {

@DELETE
Call<Object> method0(@Header("Credentials-AccessToken") String credentials-accesstoken,@Query("path") String path);
@POST
Call<Object> method1(@Header("Credentials-AccessToken") String credentials-accesstoken);
@POST
Call<Object> method2();
@GET
Call<Object> method3(@Header("Credentials-AccessToken") String credentials-accesstoken,@Query("path") String path);
@GET
Call<Object> method4(@Header("Credentials-AccessToken") String credentials-accesstoken,@Query("key") String key);
@GET
Call<Object> method5(@Header("Credentials-AccessToken") String credentials-accesstoken,@Query("perPage") String perpage,@Query("page") String page,@Query("orderBy") String orderby,@Query("order") String order,@Query("search") String search,@Query("path") String path);
@DELETE
Call<Object> method6(@Header("Credentials-AccessToken") String credentials-accesstoken,@Query("path") String path);
@POST
Call<Object> method7(@Header("Credentials-AccessToken") String credentials-accesstoken,@Query("path") String path);
@GET
Call<Object> method8(@Header("Credentials-AccessToken") String credentials-accesstoken,@Query("key") String key);
@DELETE
Call<Object> method9(@Header("Credentials-AccessToken") String credentials-accesstoken);
@DELETE
Call<Object> method10(@Header("invited") String invited);
@POST
Call<Object> method11(@Header("Credentials-AccessToken") String credentials-accesstoken);
@POST
Call<Object> method12(@Header("Credentials-AccessToken") String credentials-accesstoken,@Query("path") String path);
@POST
Call<Object> method13(@Header("Credentials-AccessToken") String credentials-accesstoken);
@POST
Call<Object> method14(@Header("Credentials-AccessToken") String credentials-accesstoken,@Header("invited") String invited);
@GET
Call<Object> method15(@Header("Credentials-AccessToken") String credentials-accesstoken,@Query("path") String path);
@POST
Call<Object> method16(@Header("Credentials-AccessToken") String credentials-accesstoken,@Query("to") String to);
}