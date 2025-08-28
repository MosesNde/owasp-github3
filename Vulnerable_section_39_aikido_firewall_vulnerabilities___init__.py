 from aikido_firewall.helpers.logging import logger
 from aikido_firewall.helpers.get_clean_stacktrace import get_clean_stacktrace
 from aikido_firewall.helpers.blocking_enabled import is_blocking_enabled
 from .sql_injection.context_contains_sql_injection import context_contains_sql_injection
 from .nosql_injection.check_context import check_context_for_nosql_injection
 from .ssrf.inspect_getaddrinfo_result import inspect_getaddrinfo_result
 from .path_traversal.check_context_for_path_traversal import (
     check_context_for_path_traversal,
 )
from aikido_firewall.background_process.ipc_lifecycle_cache import get_cache
 
 
 def run_vulnerability_scan(kind, op, args):
         logger.debug("Not running scans due to incomplete data %s : %s", kind, op)
         return
 
    if not comms or not lifecycle_cache:
         logger.debug("Not running scans due to incomplete data %s : %s", kind, op)
         return
 
             error_type = AikidoSSRF
             blocked_request = is_blocking_enabled() and injection_results
             if not blocked_request:
                # Report hostname and port to background process :
                get_comms().send_data_to_bg_process("HOSTNAMES_ADD", (args[1], args[2]))
         else:
             logger.error(
                 "Vulnerability type %s currently has no scans implemented", kind
         logger.debug("Injection results : %s", json.dumps(injection_results))
         blocked = is_blocking_enabled()
         stack = get_clean_stacktrace()
        comms.send_data_to_bg_process(
            "ATTACK", (injection_results, context, blocked, stack)
        )
         if blocked:
             raise error_type(*error_args)