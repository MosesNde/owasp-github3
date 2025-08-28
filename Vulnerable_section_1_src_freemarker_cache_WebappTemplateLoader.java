             ;// ignore
         }
             
        // If it fails, try to open it with servletContext.getResource.
        URL url = null;
        try {
            url = servletContext.getResource(fullPath);
        } catch(MalformedURLException e) {
            logger.warn("Could not retrieve resource " + StringUtil.jQuoteNoXSS(fullPath),
                    e);
            return null;
        }
        return url == null ? null : new URLTemplateSource(url);
     }
     
     public long getLastModified(Object templateSource) {