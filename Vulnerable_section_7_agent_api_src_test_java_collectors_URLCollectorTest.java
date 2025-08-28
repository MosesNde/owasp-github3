 import java.net.URL;
 
 import static org.junit.jupiter.api.Assertions.assertEquals;
 import static utils.EmtpyThreadCacheObject.getEmptyThreadCacheObject;
 
 public class URLCollectorTest {
         assertEquals(1, hostnameArray.length);
         assertEquals(80, hostnameArray[0].getPort());
         assertEquals("app.local.aikido.io", hostnameArray[0].getHostname());
     }
 
     @SetEnvironmentVariable(key = "AIKIDO_TOKEN", value = "invalid-token")
         assertEquals(1, hostnameArray.length);
         assertEquals(443, hostnameArray[0].getPort());
         assertEquals("aikido.dev", hostnameArray[0].getHostname());
     }
 
     @SetEnvironmentVariable(key = "AIKIDO_TOKEN", value = "invalid-token")
         URLCollector.report(new URL("ftp://localhost:8080"));
         Hostnames.HostnameEntry[] hostnameArray = ThreadCache.get().getHostnames().asArray();
         assertEquals(0, hostnameArray.length);
     }
 }
\ No newline at end of file