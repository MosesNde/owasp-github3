 		{
 			
 			path = Paths.get(req.getServletPath()).normalize().toString().replace('\\', '/') + path;
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