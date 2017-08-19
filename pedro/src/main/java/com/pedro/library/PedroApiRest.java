package com.pedro.library;

import com.pedro.library.bodies.*;
import java.io.File;
import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class PedroApiRest {

  private Retrofit2Service retrofit2Service;

  public PedroApiRest(boolean log) {
    retrofit2Service = new Retrofit2ServiceImp(Constants.BASE_URL, log).getRetrofit().create(Retrofit2Service.class);
  }

  private MultipartBody.Part getMultiPart(File file, String key) {
    RequestBody requestFile = RequestBody.create(MediaType.parse("multipart/form-data"), file);
    MultipartBody.Part body =
        MultipartBody.Part.createFormData(key, file.getName(), requestFile);
    return body;
  }

  public void deleteFile(String Credentials-AccessToken,String path,final PedroCallback pedrocallback) {
    retrofit2Service.deleteFile(Credentials-AccessToken,path).enqueue(new Callback<Object>() {
      @Override
      public void onResponse(Call<Object> call, Response<Object> response) {
        if (response.isSuccessful()) {
          pedrocallback.onSuccess(response.toString());
        } else {
          pedrocallback.onError(new ErrorResponse(response.code(), response.message()));
        }
      }

      @Override
      public void onFailure(Call<Object> call, Throwable t) {
        pedrocallback.onError(new ErrorResponse(-1, t.getMessage()));
      }
    });
  }

  public void shareFiles(String Credentials-AccessToken,SharefilesBody shareFilesbody,final PedroCallback pedrocallback) {
    retrofit2Service.shareFiles(Credentials-AccessToken,shareFilesbody).enqueue(new Callback<Object>() {
      @Override
      public void onResponse(Call<Object> call, Response<Object> response) {
        if (response.isSuccessful()) {
          pedrocallback.onSuccess(response.toString());
        } else {
          pedrocallback.onError(new ErrorResponse(response.code(), response.message()));
        }
      }

      @Override
      public void onFailure(Call<Object> call, Throwable t) {
        pedrocallback.onError(new ErrorResponse(-1, t.getMessage()));
      }
    });
  }

  public void increaseCount(IncreasecountBody increaseCountbody,final PedroCallback pedrocallback) {
    retrofit2Service.increaseCount(increaseCountbody).enqueue(new Callback<Object>() {
      @Override
      public void onResponse(Call<Object> call, Response<Object> response) {
        if (response.isSuccessful()) {
          pedrocallback.onSuccess(response.toString());
        } else {
          pedrocallback.onError(new ErrorResponse(response.code(), response.message()));
        }
      }

      @Override
      public void onFailure(Call<Object> call, Throwable t) {
        pedrocallback.onError(new ErrorResponse(-1, t.getMessage()));
      }
    });
  }

  public void getMedia(String Credentials-AccessToken,String path,final PedroCallback pedrocallback) {
    retrofit2Service.getMedia(Credentials-AccessToken,path).enqueue(new Callback<Object>() {
      @Override
      public void onResponse(Call<Object> call, Response<Object> response) {
        if (response.isSuccessful()) {
          pedrocallback.onSuccess(response.toString());
        } else {
          pedrocallback.onError(new ErrorResponse(response.code(), response.message()));
        }
      }

      @Override
      public void onFailure(Call<Object> call, Throwable t) {
        pedrocallback.onError(new ErrorResponse(-1, t.getMessage()));
      }
    });
  }

  public void getPublicFIle(String Credentials-AccessToken,String key,final PedroCallback pedrocallback) {
    retrofit2Service.getPublicFIle(Credentials-AccessToken,key).enqueue(new Callback<Object>() {
      @Override
      public void onResponse(Call<Object> call, Response<Object> response) {
        if (response.isSuccessful()) {
          pedrocallback.onSuccess(response.toString());
        } else {
          pedrocallback.onError(new ErrorResponse(response.code(), response.message()));
        }
      }

      @Override
      public void onFailure(Call<Object> call, Throwable t) {
        pedrocallback.onError(new ErrorResponse(-1, t.getMessage()));
      }
    });
  }

  public void filesList(String Credentials-AccessToken,String perPage,String page,String orderBy,String order,String search,String path,final PedroCallback pedrocallback) {
    retrofit2Service.filesList(Credentials-AccessToken,perPage,page,orderBy,order,search,path).enqueue(new Callback<Object>() {
      @Override
      public void onResponse(Call<Object> call, Response<Object> response) {
        if (response.isSuccessful()) {
          pedrocallback.onSuccess(response.toString());
        } else {
          pedrocallback.onError(new ErrorResponse(response.code(), response.message()));
        }
      }

      @Override
      public void onFailure(Call<Object> call, Throwable t) {
        pedrocallback.onError(new ErrorResponse(-1, t.getMessage()));
      }
    });
  }

  public void deleteAll(String Credentials-AccessToken,String path,final PedroCallback pedrocallback) {
    retrofit2Service.deleteAll(Credentials-AccessToken,path).enqueue(new Callback<Object>() {
      @Override
      public void onResponse(Call<Object> call, Response<Object> response) {
        if (response.isSuccessful()) {
          pedrocallback.onSuccess(response.toString());
        } else {
          pedrocallback.onError(new ErrorResponse(response.code(), response.message()));
        }
      }

      @Override
      public void onFailure(Call<Object> call, Throwable t) {
        pedrocallback.onError(new ErrorResponse(-1, t.getMessage()));
      }
    });
  }

  public void addFile(String Credentials-AccessToken,String path,File image,final PedroCallback pedrocallback) {
    retrofit2Service.addFile(Credentials-AccessToken,path,getMultiPart(image,"image")).enqueue(new Callback<Object>() {
      @Override
      public void onResponse(Call<Object> call, Response<Object> response) {
        if (response.isSuccessful()) {
          pedrocallback.onSuccess(response.toString());
        } else {
          pedrocallback.onError(new ErrorResponse(response.code(), response.message()));
        }
      }

      @Override
      public void onFailure(Call<Object> call, Throwable t) {
        pedrocallback.onError(new ErrorResponse(-1, t.getMessage()));
      }
    });
  }

  public void getPublicMedia(String Credentials-AccessToken,String key,final PedroCallback pedrocallback) {
    retrofit2Service.getPublicMedia(Credentials-AccessToken,key).enqueue(new Callback<Object>() {
      @Override
      public void onResponse(Call<Object> call, Response<Object> response) {
        if (response.isSuccessful()) {
          pedrocallback.onSuccess(response.toString());
        } else {
          pedrocallback.onError(new ErrorResponse(response.code(), response.message()));
        }
      }

      @Override
      public void onFailure(Call<Object> call, Throwable t) {
        pedrocallback.onError(new ErrorResponse(-1, t.getMessage()));
      }
    });
  }

  public void deletePublicKey(String Credentials-AccessToken,DeletepublickeyBody deletePublicKeybody,final PedroCallback pedrocallback) {
    retrofit2Service.deletePublicKey(Credentials-AccessToken,deletePublicKeybody).enqueue(new Callback<Object>() {
      @Override
      public void onResponse(Call<Object> call, Response<Object> response) {
        if (response.isSuccessful()) {
          pedrocallback.onSuccess(response.toString());
        } else {
          pedrocallback.onError(new ErrorResponse(response.code(), response.message()));
        }
      }

      @Override
      public void onFailure(Call<Object> call, Throwable t) {
        pedrocallback.onError(new ErrorResponse(-1, t.getMessage()));
      }
    });
  }

  public void deleteAccess(String invited,final PedroCallback pedrocallback) {
    retrofit2Service.deleteAccess(invited).enqueue(new Callback<Object>() {
      @Override
      public void onResponse(Call<Object> call, Response<Object> response) {
        if (response.isSuccessful()) {
          pedrocallback.onSuccess(response.toString());
        } else {
          pedrocallback.onError(new ErrorResponse(response.code(), response.message()));
        }
      }

      @Override
      public void onFailure(Call<Object> call, Throwable t) {
        pedrocallback.onError(new ErrorResponse(-1, t.getMessage()));
      }
    });
  }

  public void refreshPublicKey(String Credentials-AccessToken,RefreshpublickeyBody refreshPublicKeybody,final PedroCallback pedrocallback) {
    retrofit2Service.refreshPublicKey(Credentials-AccessToken,refreshPublicKeybody).enqueue(new Callback<Object>() {
      @Override
      public void onResponse(Call<Object> call, Response<Object> response) {
        if (response.isSuccessful()) {
          pedrocallback.onSuccess(response.toString());
        } else {
          pedrocallback.onError(new ErrorResponse(response.code(), response.message()));
        }
      }

      @Override
      public void onFailure(Call<Object> call, Throwable t) {
        pedrocallback.onError(new ErrorResponse(-1, t.getMessage()));
      }
    });
  }

  public void addDIr(String Credentials-AccessToken,String path,AdddirBody addDIrbody,final PedroCallback pedrocallback) {
    retrofit2Service.addDIr(Credentials-AccessToken,path,addDIrbody).enqueue(new Callback<Object>() {
      @Override
      public void onResponse(Call<Object> call, Response<Object> response) {
        if (response.isSuccessful()) {
          pedrocallback.onSuccess(response.toString());
        } else {
          pedrocallback.onError(new ErrorResponse(response.code(), response.message()));
        }
      }

      @Override
      public void onFailure(Call<Object> call, Throwable t) {
        pedrocallback.onError(new ErrorResponse(-1, t.getMessage()));
      }
    });
  }

  public void createPublicKey(String Credentials-AccessToken,CreatepublickeyBody createPublicKeybody,final PedroCallback pedrocallback) {
    retrofit2Service.createPublicKey(Credentials-AccessToken,createPublicKeybody).enqueue(new Callback<Object>() {
      @Override
      public void onResponse(Call<Object> call, Response<Object> response) {
        if (response.isSuccessful()) {
          pedrocallback.onSuccess(response.toString());
        } else {
          pedrocallback.onError(new ErrorResponse(response.code(), response.message()));
        }
      }

      @Override
      public void onFailure(Call<Object> call, Throwable t) {
        pedrocallback.onError(new ErrorResponse(-1, t.getMessage()));
      }
    });
  }

  public void newAccess(String Credentials-AccessToken,String invited,final PedroCallback pedrocallback) {
    retrofit2Service.newAccess(Credentials-AccessToken,invited).enqueue(new Callback<Object>() {
      @Override
      public void onResponse(Call<Object> call, Response<Object> response) {
        if (response.isSuccessful()) {
          pedrocallback.onSuccess(response.toString());
        } else {
          pedrocallback.onError(new ErrorResponse(response.code(), response.message()));
        }
      }

      @Override
      public void onFailure(Call<Object> call, Throwable t) {
        pedrocallback.onError(new ErrorResponse(-1, t.getMessage()));
      }
    });
  }

  public void getFile(String Credentials-AccessToken,String path,final PedroCallback pedrocallback) {
    retrofit2Service.getFile(Credentials-AccessToken,path).enqueue(new Callback<Object>() {
      @Override
      public void onResponse(Call<Object> call, Response<Object> response) {
        if (response.isSuccessful()) {
          pedrocallback.onSuccess(response.toString());
        } else {
          pedrocallback.onError(new ErrorResponse(response.code(), response.message()));
        }
      }

      @Override
      public void onFailure(Call<Object> call, Throwable t) {
        pedrocallback.onError(new ErrorResponse(-1, t.getMessage()));
      }
    });
  }

  public void sendData(String Credentials-AccessToken,String to,File image,SenddataBody sendDatabody,final PedroCallback pedrocallback) {
    retrofit2Service.sendData(Credentials-AccessToken,to,getMultiPart(image,"image"),sendDatabody).enqueue(new Callback<Object>() {
      @Override
      public void onResponse(Call<Object> call, Response<Object> response) {
        if (response.isSuccessful()) {
          pedrocallback.onSuccess(response.toString());
        } else {
          pedrocallback.onError(new ErrorResponse(response.code(), response.message()));
        }
      }

      @Override
      public void onFailure(Call<Object> call, Throwable t) {
        pedrocallback.onError(new ErrorResponse(-1, t.getMessage()));
      }
    });
  }


}
