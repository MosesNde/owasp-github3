 import java.net.URL;
 import java.net.URLConnection;
 import java.nio.file.Paths;
import java.util.regex.Pattern;
 
 import javax.servlet.ServletException;
 import javax.servlet.ServletOutputStream;
 @WebServlet("/rfb/*")
 public class ResourcesServlet extends HttpServlet
 {
	private static final Pattern PATH_PATTERN = Pattern.compile("^/([a-zA-Z0-9_-]+/)*[a-zA-Z0-9_-]+$");

 	private static final long serialVersionUID = 1L;
 
 	@Override
 		String path = req.getPathInfo();
 		if ("/".equals(path)) path = "/index.html";
 		path = Paths.get(req.getServletPath() + path).normalize().toString().replace('\\', '/');
		if (isValidPath(path) && path.startsWith("/rfb/"))
 		{
 			URL res = getClass().getResource(path);
 			if (res != null)
 				resp.sendError(HttpServletResponse.SC_NOT_FOUND);
 			}
 		}
		else
		{
			resp.sendError(HttpServletResponse.SC_NOT_FOUND);
		}
	}

	private boolean isValidPath(String path)
	{
		return PATH_PATTERN.matcher(path).matches();
 	}
 }