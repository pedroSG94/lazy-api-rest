package com.example.library.callbacks;

import com.example.library.ErrorResponse;

public interface Callback {

  void onSuccess(Object response);

  void onError(ErrorResponse errorResponse);
}
