 from urllib.parse import urlparse
 
 
def get_port_from_url(url):
     """
     Tries to retrieve a port number from the given url
     """
    parsed_url = urlparse(url)
 
     # Check if the port is specified and is a valid integer
     if parsed_url.port is not None: