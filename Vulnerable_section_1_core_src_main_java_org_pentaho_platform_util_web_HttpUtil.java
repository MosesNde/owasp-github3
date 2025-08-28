 
 package org.pentaho.platform.util.web;
 
 import org.apache.commons.lang.StringUtils;
 import org.apache.http.HttpResponse;
 import org.apache.http.client.HttpClient;
 import org.apache.http.client.methods.HttpGet;
 import org.pentaho.di.core.util.HttpClientManager;
 import org.pentaho.platform.util.logging.Logger;
 import org.pentaho.platform.util.messages.Messages;
 
   //3 seconds
   public static final int CONNECTION_TIMEOUT = 3_000;
 
   private static HttpClientManager httpClientManager = HttpClientManager.getInstance();
   private static HttpClientManager.HttpClientBuilderFacade clientBuilder = httpClientManager.createBuilder();
 
 
   public static void getURLContent_old( final String uri, final StringBuffer content ) throws MalformedURLException,
     IOException {

     URL url = new URL( uri );
     HttpURLConnection connection = (HttpURLConnection) url.openConnection();
     connection.connect();
   }
 
   public static String getURLContent( final String uri ) {

     try {
       StringBuffer content = new StringBuffer();
       HttpUtil.getURLContent( uri, content );
   }
 
   public static InputStream getURLInputStream( final String uri ) {

     try {
       URL url = new URL( uri );
       HttpURLConnection connection = (HttpURLConnection) url.openConnection();
   }
 
   public static Reader getURLReader( final String uri ) {

     try {
       URL url = new URL( uri );
       HttpURLConnection connection = (HttpURLConnection) url.openConnection();
     return sb.toString();
   }
 
 }