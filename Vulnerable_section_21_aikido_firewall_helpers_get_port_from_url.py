     # Determine the default port based on the protocol
     if parsed_url.scheme == "https":
         return 443
    elif parsed_url.scheme == "http":
         return 80