     query = urlparse(url)
     hostname = query.hostname or ""
     video_id = None
 
     if "youtu" not in hostname:
         return None
 
     if hostname == "youtu.be":
         return query.path[1:]
 
    if "youtube.com" in hostname:
         if query.path == "/watch":
             video_id = parse_qs(query.query)["v"][0]
         elif query.path[:7] == "/embed/":