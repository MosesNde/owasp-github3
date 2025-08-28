  */
 package org.weasis.launcher;
 
 import java.io.BufferedInputStream;
 import java.io.ByteArrayInputStream;
 import java.io.ByteArrayOutputStream;
 
   public static URLConnection getAdaptedConnection(URL url, boolean useCaches) throws IOException {
     URLConnection connection = url.openConnection();
    // Prevent caching of Java WebStart.
     connection.setUseCaches(useCaches);
    // Support for http proxy authentication.
     String protocol = url.getProtocol();
     String pauth = System.getProperty("http.proxyAuth", null);
     if (hasProxyProperty(pauth, protocol)) {
       String base64 = Util.base64Encode(pauth);
       connection.setRequestProperty("Proxy-Authorization", "Basic " + base64); // NON-NLS
     }
 
    String auth = System.getProperty("http.authorization", null);
     if (hasProxyProperty(auth, protocol)) {
       connection.setRequestProperty("Authorization", auth);
     }