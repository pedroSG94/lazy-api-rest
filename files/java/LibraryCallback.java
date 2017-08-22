package com.example.library;

public interface LibraryCallback {

  void onSuccess(String response);

  void onError(ErrorResponse errorResponse);
}
