 import java.net.URL;
 import java.net.URLConnection;
 import java.nio.file.Paths;
 
 import javax.servlet.ServletException;
 import javax.servlet.ServletOutputStream;
 @WebServlet("/rfb/*")
 public class ResourcesServlet extends HttpServlet
 {
 	private static final long serialVersionUID = 1L;
 
 	@Override
 		String path = req.getPathInfo();
 		if ("/".equals(path)) path = "/index.html";
 		path = Paths.get(req.getServletPath() + path).normalize().toString().replace('\\', '/');
		if (path.startsWith("/rfb/"))
 		{
 			URL res = getClass().getResource(path);
 			if (res != null)
 				resp.sendError(HttpServletResponse.SC_NOT_FOUND);
 			}
 		}
 	}
 }