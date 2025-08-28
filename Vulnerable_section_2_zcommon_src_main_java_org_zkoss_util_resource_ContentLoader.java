 	public String load(Object src) throws Exception {
 		final InputStream is;
 		if (src instanceof URL) {
			is = ((URL)src).openStream();
 		} else if (src instanceof File) {
 			is = new FileInputStream((File)src);
 		} else if (src == null) {