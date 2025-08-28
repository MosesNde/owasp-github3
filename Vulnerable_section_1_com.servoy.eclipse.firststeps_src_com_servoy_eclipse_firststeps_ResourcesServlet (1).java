 import java.net.URL;
 import java.net.URLConnection;
 import java.nio.file.Paths;
import java.util.Properties;
 
 import javax.servlet.ServletException;
 import javax.servlet.ServletOutputStream;
 import javax.servlet.http.HttpServletRequest;
 import javax.servlet.http.HttpServletResponse;
 
import org.eclipse.swt.widgets.Display;

import com.servoy.eclipse.cheatsheets.OpenCheatSheet;
 import com.servoy.eclipse.firststeps.ui.actions.IAction;
 import com.servoy.eclipse.model.util.ServoyLog;
 import com.servoy.j2db.util.MimeTypes;
 @WebServlet("/firststeps/*")
 public class ResourcesServlet extends HttpServlet
 {
 	private static final long serialVersionUID = 1L;
 
 	@Override
 				idxClassNameEnd = path.length();
 			}
 
			String className = path.substring(8, idxClassNameEnd);
 			try
 			{
				Class<?> clazz = forName(className);
				Object actionInstance = clazz.newInstance();
				if(actionInstance instanceof IAction)
				{
					String argument = path.substring(idxClassNameEnd);
					((IAction)actionInstance).run(argument);
 				}
 			}
 			catch(Exception ex)