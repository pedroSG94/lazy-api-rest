package com.casdac.lib.bodies;


public class SharefilesBody {

public SharefilesBody(String from,String path) {
  this.from = from;
  this.path = path;
}

private String from;

public void setFrom(String from) {
  this.from = from;
}

public String getFrom() {
  return from;
}

private String path;

public void setPath(String path) {
  this.path = path;
}

public String getPath() {
  return path;
}


}
