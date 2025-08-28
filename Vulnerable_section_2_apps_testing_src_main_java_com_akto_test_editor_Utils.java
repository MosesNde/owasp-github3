             if(System.getenv("SSRF_SERVICE_NAME") != null && System.getenv("SSRF_SERVICE_NAME").length() > 0){
                 hostName = System.getenv("SSRF_SERVICE_NAME");
             }
            requestUrl = hostName + url;
         }
 
         Request request = new Request.Builder()