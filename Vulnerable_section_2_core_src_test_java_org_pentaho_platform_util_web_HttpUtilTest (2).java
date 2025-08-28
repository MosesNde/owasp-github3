 import static org.mockito.Mockito.when;
 
 public class HttpUtilTest {


   HttpUtil httpUtil = mock( HttpUtil.class );
 
   @Test
   public void testIsValidURLMatchingURL() {
    try ( MockedStatic<PentahoSystem> pentahoSystemMockedStatic = mockStatic(PentahoSystem.class ) ) {
       ISystemConfig systemSettings = mock( ISystemConfig.class );
      pentahoSystemMockedStatic.when( () -> PentahoSystem.get(ISystemConfig.class )).thenReturn(systemSettings);
      when(systemSettings.getProperty("system.ssrf-protection-enabled", "false" ) )
        .thenReturn("true" );
      when(systemSettings.getProperty( "server.alternative-fully-qualified-server-urls" ) )
        .thenReturn(
          "http://www.google.com, http://192.168.10.1:8080/pentaho/, https://192.168.10.1:8443/pentaho/, "
            + "http://localhost" );
      assertTrue(systemSettings.getProperty("system.ssrf-protection-enabled",
        "false").equals("true"));
      assertTrue(httpUtil.isValidURL("https://192.168.10.1"));
     }
   }
 
   @Test
   public void testIsValidURLNoMatchingURL() {
    try ( MockedStatic<PentahoSystem> pentahoSystemMockedStatic = mockStatic(PentahoSystem.class ) ) {
       ISystemConfig systemSettings = mock( ISystemConfig.class );
      pentahoSystemMockedStatic.when(() -> PentahoSystem.get(ISystemConfig.class)).thenReturn(systemSettings);
      when(systemSettings.getProperty( "system.ssrf-protection-enabled", "false" ) )
        .thenReturn("true" );
      when(systemSettings.getProperty("server.alternative-fully-qualified-server-urls" ))
        .thenReturn("http://www.google.com, http://192.168.10.1:8080/pentaho/, https://192.168.10.1:8443/pentaho/" );
      assertEquals("true", systemSettings.getProperty("system.ssrf-protection-enabled",
        "false"));
      assertFalse(httpUtil.isValidURL("http://www.pentaho.com"));
     }
   }
 
   @Test
   public void testIllegalArgumentExceptionDueToMalformedURL() {
    try ( MockedStatic<PentahoSystem> pentahoSystemMockedStatic = mockStatic(PentahoSystem.class ) ) {
       ISystemConfig systemSettings = mock( ISystemConfig.class );
      pentahoSystemMockedStatic.when(() -> PentahoSystem.get(ISystemConfig.class)).thenReturn(systemSettings);
      when(systemSettings.getProperty("system.ssrf-protection-enabled", "false") )
        .thenReturn("true");
      when(systemSettings.getProperty("server.alternative-fully-qualified-server-urls" ) )
        .thenReturn("http://www.google.com, http://192.168.10.1:8080/pentaho/, https://192.168.10.1:8443/pentaho/" );
      assertEquals("true", systemSettings.getProperty("system.ssrf-protection-enabled",
        "false"));
      assertThrows(IllegalArgumentException.class, () -> {
        httpUtil.getURLInputStream("pentaho.com" );
      });
     }
   }
 
   @Test
   public void testIsValidURLNoSsrfProtection() {
    try (MockedStatic<PentahoSystem> pentahoSystemMockedStatic = mockStatic( PentahoSystem.class ) ) {
       ISystemConfig systemSettings = mock( ISystemConfig.class );
      pentahoSystemMockedStatic.when(() -> PentahoSystem.get(ISystemConfig.class)).thenReturn(systemSettings);
      when(systemSettings.getProperty("system.ssrf-protection-enabled","false" ) )
        .thenReturn("false");
      assertEquals("false", systemSettings.getProperty("system.ssrf-protection-enabled",
        "false"));
      assertTrue(httpUtil.isValidURL("http://www.anydomain.com") );
     }
   }
 }