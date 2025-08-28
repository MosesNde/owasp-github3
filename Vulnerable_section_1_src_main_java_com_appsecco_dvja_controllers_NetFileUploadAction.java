 package com.appsecco.dvja.controllers;
 
 import org.apache.struts2.ServletActionContext;
 
 import java.io.*;
 import java.net.MalformedURLException;
 import java.net.URL;
 import java.net.URLConnection;
         File serverFile = new File(dir.getAbsolutePath()+File.separator + "output.jpg");
 try{
     URL url = new URL(getUrl());
     //SSRF sink
     URLConnection conn = url.openConnection();
     in = conn.getInputStream();
 } catch (MalformedURLException e) {
     serverFile.delete();
     return "Not Valid URL";

 }
 finally {
     if (out != null) {