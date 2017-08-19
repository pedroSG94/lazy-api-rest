package com.pedro.library;

public interface PedroCallback {

  void onSuccess(String response);

  void onError(ErrorResponse errorResponse);
}
