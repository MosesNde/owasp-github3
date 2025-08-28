 Aggregates from the different modules
 """
 
# Re-export set_current_user :
from aikido_firewall.context.users import set_user
 
 from dotenv import load_dotenv
 
 # Import logger
 from aikido_firewall.helpers.logging import logger
 
     - daemon_disabled : This will import sinks/sources but won't start a background process
     Protect user's application
     """
    if mode == "daemon" or mode == "daemon_only":
         start_background_process()
     if mode == "daemon_only":
         # Do not import sinks/sources