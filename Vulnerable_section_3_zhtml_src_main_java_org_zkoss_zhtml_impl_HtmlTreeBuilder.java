 		try {
 			if (log.isDebugEnabled())
 				log.debug("Parsing file: [" + url.toString() + "]");
 			inStream = url.openStream();
 			return convertToIDOM(
 					Zsoup.parse(inStream, "UTF-8", url.getFile(), Parser.xhtmlParser()));