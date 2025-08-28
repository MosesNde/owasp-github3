 			}
 
 			URL url = toURL(uri);
			if (url != null)
 				return url.openStream();
 			return new ParsedURI(ctx, uri).getResourceAsStream();
 		} catch (Throwable ex) {
 			log.warn("Ignored: failed to load " + Encodes.encodeURI(uri), ex);