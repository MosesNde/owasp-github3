 )
 from aikido_firewall.helpers.check_env_for_blocking import check_env_for_blocking
 from aikido_firewall.helpers.token import get_token_from_env
from aikido_firewall.background_process.api.http_api import ReportingApiHTTP
 from .commands import process_incoming_command
 
 EMPTY_QUEUE_INTERVAL = 5  # 5 seconds
     """
     Aikido's background process consists of 2 threads :
     - (main) Listening thread which listens on an IPC socket for incoming data
    - (spawned) reporting thread which will collect the IPC data and send it to a CloudConnectionManager
     """
 
     def __init__(self, address, key):
         )  # Create an event scheduler
         self.send_to_connection_manager(event_scheduler)
 
        api = ReportingApiHTTP("https://guard.aikido.dev/")
         # We need to pass along the scheduler so that the heartbeat also gets sent
         self.connection_manager = CloudConnectionManager(
             block=check_env_for_blocking(),