 		if (src instanceof URL) {
 			URLConnection conn = null;
 			try {
				conn = ((URL) src).openConnection();
 				final long v = conn.getLastModified();
 				return v != -1 ? v : 0; //not to reload if unknown (5.0.6 for better performance)
 			} catch (Throwable ex) {