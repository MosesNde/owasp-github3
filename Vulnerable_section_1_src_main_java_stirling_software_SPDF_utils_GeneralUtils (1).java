 
     public static boolean isURLReachable(String urlStr) {
         try {
             URL url = URI.create(urlStr).toURL();
             HttpURLConnection connection = (HttpURLConnection) url.openConnection();
             connection.setRequestMethod("HEAD");
             int responseCode = connection.getResponseCode();
             return (200 <= responseCode && responseCode <= 399);
        } catch (MalformedURLException e) {
            return false;
        } catch (IOException e) {
            return false;
         }
     }
 