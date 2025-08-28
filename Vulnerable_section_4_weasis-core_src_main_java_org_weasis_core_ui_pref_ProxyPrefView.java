 package org.weasis.core.ui.pref;
 
 import java.awt.FlowLayout;
import java.net.Authenticator;
import java.net.PasswordAuthentication;
import java.nio.charset.StandardCharsets;
 import java.text.NumberFormat;
 import javax.swing.ButtonGroup;
import javax.swing.JCheckBox;
 import javax.swing.JFormattedTextField;
 import javax.swing.JLabel;
 import javax.swing.JPanel;
import javax.swing.JPasswordField;
 import javax.swing.JRadioButton;
 import javax.swing.JTextField;
 import javax.swing.text.DefaultFormatterFactory;
 import javax.swing.text.NumberFormatter;
 import net.miginfocom.swing.MigLayout;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
 import org.weasis.core.Messages;
 import org.weasis.core.api.gui.util.AbstractItemDialogPage;
import org.weasis.core.api.gui.util.CryptoHandler;
 import org.weasis.core.api.gui.util.GuiUtils;
 import org.weasis.core.api.service.WProperties;
 import org.weasis.core.util.StringUtil;
 
 public class ProxyPrefView extends AbstractItemDialogPage {
  private static final Logger LOGGER = LoggerFactory.getLogger(ProxyPrefView.class);
 
   private static final String PROXY_MANUAL = "proxy.manual";
   private static final String PROXY_EXCEPTIONS = "proxy.exceptions";
   private static final String PROXY_SOCKS_HOST = "proxy.socks.host";
   private static final String PROXY_SOCKS_PORT = "proxy.socks.port";
 
  private static final String PROXY_AUTH_REQUIRED = "proxy.auth";
  private static final String PROXY_AUTH_USER = "proxy.auth.user";
  private static final String PROXY_AUTH_PWD = "proxy.auth.pwd"; // NOSONAR key for proxy

   private final JRadioButton directConnectionRadio =
       new JRadioButton(Messages.getString("ProxyPrefView.direct"));
   private final JRadioButton proxyConnectionRadio =
   private final JLabel lblAddress = new JLabel(Messages.getString("ProxyPrefView.host"));
   private final JLabel lblPort = new JLabel(Messages.getString("ProxyPrefView.port"));
 
  private final JCheckBox proxyAuthCheckBox =
      new JCheckBox(Messages.getString("ProxyPrefView.authentication"));

   private final JTextField proxyHostHttp = new JTextField(20);
   private final JFormattedTextField proxyPortHttp = new JFormattedTextField();
   private final JTextField proxyHostSecure = new JTextField(20);
   private final JLabel proxyLabelExceptions =
       new JLabel(Messages.getString("ProxyPrefView.exceptions") + StringUtil.COLON);
 
  private final JLabel userLabel =
      new JLabel(Messages.getString("ProxyPrefView.user") + StringUtil.COLON);
  private final JLabel passLabel =
      new JLabel(Messages.getString("ProxyPrefView.pwd") + StringUtil.COLON);
  private final JTextField proxyUser = new JTextField(15);
  private final JPasswordField proxyPass = new JPasswordField(15);

   public ProxyPrefView() {
     super(Messages.getString("ProxyPrefView.proxy"), 110);
     initialize();
     this.buttonGroup.add(proxyConnectionRadio);
     directConnectionRadio.addActionListener(e -> proxyConnectionAction(false));
     proxyConnectionRadio.addActionListener(e -> proxyConnectionAction(true));
    proxyAuthCheckBox.addActionListener(
        e -> {
          proxyAuthenticationAction(proxyAuthCheckBox.isSelected());
          if (!proxyAuthCheckBox.isSelected()) {
            proxyUser.setText(null);
            proxyPass.setText(null);
          }
        });
     initState();
 
     add(GuiUtils.boxYLastElement(5));
     proxyHostSocks.setText(p.getProperty(PROXY_SOCKS_HOST));
     proxyPortSocks.setValue(p.getIntProperty(PROXY_SOCKS_PORT, 1080));
 
    String user = p.getProperty(PROXY_AUTH_USER);
    String pass = "";
    try {
      byte[] pwd = p.getByteArrayProperty(PROXY_AUTH_PWD, null);
      if (pwd != null) {
        pwd = CryptoHandler.decrypt(pwd, PROXY_AUTH_REQUIRED);
        if (pwd != null && pwd.length > 0) {
          pass = new String(pwd, StandardCharsets.UTF_8);
        }
      }
    } catch (Exception e) {
      LOGGER.error("Cannot store the proxy password", e);
     }
 
    proxyUser.setText(user);
    proxyPass.setText(pass);
    proxyAuthCheckBox.setSelected(p.getBooleanProperty(PROXY_AUTH_REQUIRED, false));

     if (p.getBooleanProperty(PROXY_MANUAL, false)) proxyConnectionRadio.doClick();
     else directConnectionRadio.doClick();
   }
 
     dataPanel.add(proxyLabelExceptions, GuiUtils.NEWLINE);
     dataPanel.add(proxyExceptions, "spanx 2"); // NON-NLS
    dataPanel.add(proxyAuthCheckBox, "newline, spanx, alignx leading, gaptop 15lp"); // NON-NLS
    dataPanel.add(userLabel, GuiUtils.NEWLINE);
    dataPanel.add(proxyUser);
    dataPanel.add(passLabel, GuiUtils.NEWLINE);
    dataPanel.add(proxyPass);
     return dataPanel;
   }
 
     proxyPortSocks.setEnabled(enable);
     proxyLabelExceptions.setEnabled(enable);
     proxyExceptions.setEnabled(enable);

    proxyAuthCheckBox.setEnabled(enable);
    proxyAuthenticationAction(enable ? proxyAuthCheckBox.isSelected() : enable);
  }

  public void proxyAuthenticationAction(boolean auth) {
    userLabel.setEnabled(auth);
    proxyUser.setEnabled(auth);
    passLabel.setEnabled(auth);
    proxyPass.setEnabled(auth);
   }
 
   @Override
       p.putIntProperty(PROXY_SOCKS_PORT, port.intValue());
       applyProxyPortProperty("socksProxyPort", port.intValue(), val, mproxy);
     }

    boolean auth = proxyAuthCheckBox.isSelected();
    p.putBooleanProperty(PROXY_AUTH_REQUIRED, auth);
    val = proxyUser.getText();
    p.setProperty(PROXY_AUTH_USER, val);
    try {
      char[] pwd = proxyPass.getPassword();
      if (pwd != null && pwd.length > 0) {
        if (auth) {
          String authPassword = new String(pwd);
          applyPasswordAuthentication(val, authPassword);
          applyProxyProperty("http.proxyUser", val, mproxy);
          applyProxyProperty("http.proxyPassword", authPassword, mproxy);
        }
        byte[] b = new byte[pwd.length];
        for (int i = 0; i < b.length; i++) {
          b[i] = (byte) pwd[i];
        }
        p.putByteArrayProperty(PROXY_AUTH_PWD, CryptoHandler.encrypt(b, PROXY_AUTH_REQUIRED));
      } else {
        p.putByteArrayProperty(PROXY_AUTH_PWD, null);
      }
    } catch (Exception ex) {
      LOGGER.error("Cannot store the proxy user", ex);
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