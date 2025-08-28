 
 		URLConnection conn = null;
 		try {
			final URL url = getExtendletContext().getResource(src);
 			if (url != null) {
 				conn = url.openConnection();
 				final long v = conn.getLastModified();
 				return v != -1 ? v : 0; //not to reload (5.0.6 for better performance)
 			//Due to Web server might cache the result, we use URL if possible
 			try {
 				URL real = getExtendletContext().getResource(path);
				if (real != null)
 					is = real.openStream();
 			} catch (Throwable ex) {
 				log.warn("Unable to read from URL: " + path, ex);
 			}