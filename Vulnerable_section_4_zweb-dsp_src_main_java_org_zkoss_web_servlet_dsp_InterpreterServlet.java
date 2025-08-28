 		}
 
 		protected Interpretation parse(String path, URL url, Object extra) throws Exception {
 			InputStream is = url.openStream();
 			if (is != null)
 				is = new BufferedInputStream(is);