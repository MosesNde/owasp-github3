   public static final String PARAM_ARGUMENT = "arg"; // NON-NLS
   public static final String PARAM_PROPERTY = "pro"; // NON-NLS
   public static final String PARAM_CODEBASE = "cdb"; // NON-NLS
  public static final String PARAM_CODEBASE_EXT = "cdb-ext"; // NON-NLS
   public static final String PARAM_AUTHORIZATION = "auth"; // NON-NLS
 
   private final List<String> arguments = new ArrayList<>();
       if (Utils.hasText(val)) {
         applyProxyProperty("socksProxyPort", p.getProperty("proxy.socks.port"), mproxy); // NON-NLS
       }

      boolean auth = Utils.getEmptyToFalse(p.getProperty("proxy.auth"));
      if (auth) {
        String authUser = p.getProperty("proxy.auth.user");
        String authPassword;
        try {
          byte[] pwd = Utils.getByteArrayProperty(p, "proxy.auth.pwd", null);
          if (pwd != null) {
            pwd = Utils.decrypt(pwd, "proxy.auth");
            if (pwd != null && pwd.length > 0) {
              authPassword = new String(pwd, StandardCharsets.UTF_8);
              applyPasswordAuthentication(authUser, authPassword);
              applyProxyProperty("http.proxyUser", authUser, mproxy);
              applyProxyProperty("http.proxyPassword", authPassword, mproxy);
            }
          }
        } catch (Exception e) {
          LOGGER.error("Cannot store the proxy password", e);
        }
      }
     }
   }
 
  private static void applyPasswordAuthentication(
      final String authUser, final String authPassword) {
    Authenticator.setDefault(
        new Authenticator() {
          @Override
          public PasswordAuthentication getPasswordAuthentication() {
            return new PasswordAuthentication(authUser, authPassword.toCharArray());
          }
        });
  }

   private static void applyProxyProperty(String key, String value, boolean manual) {
     if (manual && Utils.hasText(value)) {
       System.setProperty(key, value);