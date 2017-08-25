package com.example.library.callbacks;

import com.example.library.ErrorResponse;
import com.example.library.responses.*;

public interface Callback {

  void onSuccess(Object response);

  void onError(ErrorResponse errorResponse);
}
