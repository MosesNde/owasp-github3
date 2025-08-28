 import java.io.InputStream;
 import java.net.URL;
 import java.net.URLConnection;
 
 import javax.servlet.ServletException;
 import javax.servlet.ServletOutputStream;
 	{
 		String path = req.getPathInfo();
 		if ("/".equals(path)) path = "/index.html";
		path = req.getServletPath() + path;
		URL res = getClass().getResource(path);
		if (res != null)
 		{
			URLConnection uc = res.openConnection();
			resp.setContentLength(uc.getContentLength());
			resp.setContentType(MimeTypes.guessContentTypeFromName(path));
			InputStream in = uc.getInputStream();
			ServletOutputStream outputStream = resp.getOutputStream();
			Utils.streamCopy(in, outputStream);
			outputStream.flush();
			Utils.close(in);
 		}
 		else
 		{