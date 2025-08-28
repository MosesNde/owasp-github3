 import java.io.InputStream;
 import java.net.URL;
 import java.net.URLConnection;
 import java.util.Properties;
 
 import javax.servlet.ServletException;
 	@Override
 	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException
 	{
		String path = req.getPathInfo();
 		
 		if(path.startsWith("/action/"))
 		{
 		}
 		else
 		{
			path = req.getServletPath() + path;
 			URL res = getClass().getResource(path);
 			if (res != null)
 			{