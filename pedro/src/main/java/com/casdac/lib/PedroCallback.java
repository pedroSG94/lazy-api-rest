package com.casdac.lib;

public interface PedroCallback {

  void onSuccess(String response);

  void onError(ErrorResponse errorResponse);
}
