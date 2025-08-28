 package dev.aikido.agent_api.collectors;
 
 import dev.aikido.agent_api.thread_cache.ThreadCache;
 import dev.aikido.agent_api.thread_cache.ThreadCacheObject;
 import dev.aikido.agent_api.helpers.logging.LogManager;
 
     private URLCollector() {}
     public static void report(URL url) {
        ThreadCacheObject threadCache = ThreadCache.get();
        if(threadCache != null && url != null) {
             if (!url.getProtocol().startsWith("http")) {
                 return; // Non-HTTP(S) URL 
             }
             logger.trace("Adding a new URL to the cache: %s", url);
             int port = getPortFromURL(url);
            threadCache.getHostnames().add(url.getHost(), port);
            ThreadCache.set(threadCache);
         }
     }
 }