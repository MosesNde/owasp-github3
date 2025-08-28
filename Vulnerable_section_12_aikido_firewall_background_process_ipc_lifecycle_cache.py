 """
 
 import threading
from .comms import get_comms
 
 #  cache needs to be per thread, not shared in the entire process
local = threading.local()
 
 
 def get_cache():
     """Returns the current cache"""
     try:
        return local.ipc_lifecycle_cache
    except AttributeError:
         return None
 
 
     def populate(self, context):
         """Fetches data over IPC"""
         # Fetch bypassed ips:
        res = get_comms().send_data_to_bg_process(
             action="FETCH_INITIAL_METADATA",
             obj={"route_metadata": context.get_route_metadata()},
             receive=True,
 
     def save(self):
         """Save the current cache"""
        local.ipc_lifecycle_cache = self