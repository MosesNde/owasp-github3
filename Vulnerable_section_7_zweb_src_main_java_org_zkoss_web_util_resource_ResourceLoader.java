 		if (src.url != null) {
 			URLConnection conn = null;
 			try {
				conn = src.url.openConnection();
 				final long v = conn.getLastModified();
 				return v != -1 ? v : 0; //not to reload (5.0.6 for better performance)
 			} catch (Throwable ex) {