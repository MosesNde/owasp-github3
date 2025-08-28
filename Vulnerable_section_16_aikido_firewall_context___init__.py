 Provides all the functionality for contexts
 """
 
import threading
 from urllib.parse import parse_qs
 
 from aikido_firewall.helpers.build_route_from_url import build_route_from_url
 from .asgi import set_asgi_attributes_on_context
 
 UINPUT_SOURCES = ["body", "cookies", "query", "headers", "xml"]
local = threading.local()
 
 WSGI_SOURCES = ["django", "flask"]
 ASGI_SOURCES = ["quart"]
 def get_current_context():
     """Returns the current context"""
     try:
        return local.current_context
    except AttributeError:
         return None
 
 
         """
         Set the current context
         """
        local.current_context = self
 
     def get_route_metadata(self):
         """Returns a route_metadata object"""