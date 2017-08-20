package com.casdac.lib.bodies;


public class RefreshpublickeyBody {

public RefreshpublickeyBody(String idFile,String limitDown) {
  this.idFile = idFile;
  this.limitDown = limitDown;
}

private String idFile;

public void setIdfile(String idFile) {
  this.idFile = idFile;
}

public String getIdfile() {
  return idFile;
}

private String limitDown;

public void setLimitdown(String limitDown) {
  this.limitDown = limitDown;
}

public String getLimitdown() {
  return limitDown;
}


}
