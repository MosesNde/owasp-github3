       if ( status == 200 ) {
         InputStream response = httpResponse.getEntity().getContent();
         try {
          byte[] buffer = new byte[ 2048 ];
           int size = response.read( buffer );
           while ( size > 0 ) {
             for ( int idx = 0; idx < size; idx++ ) {
              content.append( (char) buffer[ idx ] );
             }
             size = response.read( buffer );
           }
     HttpURLConnection connection = (HttpURLConnection) url.openConnection();
     connection.connect();
     InputStream in = connection.getInputStream();
    byte[] buffer = new byte[ 300 ];
     int n = buffer.length;
     while ( n > 0 ) {
       n = in.read( buffer );
       for ( int i = 0; i < n; i++ ) {
        content.append( (char) buffer[ i ] );
       }
     }
     n = in.read( buffer );
   }
 
   public static String getURLContent( final String uri ) {
    if ( !isValidURL(uri) ) {
       throw new IllegalArgumentException( INVALID_URL );
     }
     try {
   }
 
   public static InputStream getURLInputStream( final String uri ) {
      if ( !isValidURL(uri) ) {
        throw new IllegalArgumentException( INVALID_URL );
      }
     try {
       URL url = new URL( uri );
       HttpURLConnection connection = (HttpURLConnection) url.openConnection();
   }
 
   public static Reader getURLReader( final String uri ) {
    if ( !isValidURL(uri) ) {
       throw new IllegalArgumentException( INVALID_URL );
     }
     try {
     StringBuffer sb = new StringBuffer();
     String key;
     for ( StringTokenizer st = new StringTokenizer( s, "&" ); st.hasMoreTokens();
          rtn.put( key, valArray ) ) { //$NON-NLS-1$
       String pair = st.nextToken();
       int pos = pair.indexOf( '=' );
       if ( pos == -1 ) {
       String val = HttpUtil.parseName( pair.substring( pos + 1, pair.length() ), sb );
       if ( rtn.containsKey( key ) ) {
         String[] oldVals = rtn.get( key );
        valArray = new String[ oldVals.length + 1 ];
         System.arraycopy( oldVals, 0, valArray, 0, oldVals.length );
        valArray[ oldVals.length ] = val;
       } else {
        valArray = new String[ 1 ];
        valArray[ 0 ] = val;
       }
     }
     return rtn;
    */
 
   @VisibleForTesting
  protected static boolean isValidURL(String urlString) throws SecurityException {
     boolean allowedUrl = false;
    boolean checkSSRFProtectionEnable = "true".equals(PentahoSystem.get(ISystemConfig.class)
      .getProperty("system.ssrf-protection-enabled", "false"));
    if (!checkSSRFProtectionEnable) {
       return true;
     }
    String allowedHosts = PentahoSystem.get(ISystemConfig.class)
      .getProperty("server.alternative-fully-qualified-server-urls");
    if (allowedHosts != null) {
      String[] hosts = StringUtils.stripAll(allowedHosts.split(","));
       try {
        URL url = new URL(urlString);
        for (String host : hosts) {
          if (url.getHost().equals(new URL(host).getHost())) {
             allowedUrl = true;
             break;
           }
         }
      } catch (MalformedURLException e) {
         //Either no legal protocol could be found in the provided string or the string could not be parsed.
        Logger.error(HttpUtil.class.getName(), Messages.getInstance().getErrorString(
          "Malformed URL:", e.getMessage()), e); //$NON-NLS-1$
       }
     }
     return allowedUrl;