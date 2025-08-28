 import java.net.URISyntaxException;
 import java.net.URL;
 import java.nio.charset.StandardCharsets;
import java.security.GeneralSecurityException;
 import java.util.ArrayList;
 import java.util.Base64;
 import java.util.Collections;
 import java.util.List;
import java.util.Objects;
 import java.util.Properties;
 import java.util.regex.Matcher;
 import java.util.regex.Pattern;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
 import org.slf4j.LoggerFactory;
 
 public class Utils {
     return result;
   }
 
  public static byte[] decrypt(byte[] input, String strKey) throws GeneralSecurityException {
    SecretKeySpec skeyspec =
        new SecretKeySpec(
            Objects.requireNonNull(strKey).getBytes(StandardCharsets.UTF_8), "Blowfish"); // NON-NLS
    Cipher cipher = Cipher.getInstance("Blowfish"); // NON-NLS
    cipher.init(Cipher.DECRYPT_MODE, skeyspec);
    return cipher.doFinal(input);
  }

   public static void openInDefaultBrowser(URL url) {
     if (url != null) {
       if (SystemInfo.isLinux) {