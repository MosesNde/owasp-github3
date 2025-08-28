 from aikido_firewall.background_process.ipc_lifecycle_cache import get_cache
 from .sql_injection.context_contains_sql_injection import context_contains_sql_injection
 from .nosql_injection.check_context import check_context_for_nosql_injection
from .ssrf import scan_for_ssrf_in_request
 from .shell_injection.check_context_for_shell_injection import (
     check_context_for_shell_injection,
 )
     context = get_current_context()
     comms = get_comms()
     lifecycle_cache = get_cache()
    if not context or not lifecycle_cache:
        logger.debug("Not running a vulnerability scan due to incomplete data.")
        logger.debug("%s : %s", kind, op)
         return
 
     if lifecycle_cache.protection_forced_off():
             )
             error_type = AikidoPathTraversal
         elif kind == "ssrf":
            # args[0] : URL object, args[1] : Port
            # Report hostname and port to background process :
            injection_results = scan_for_ssrf_in_request(args[0], args[1], op, context)
             error_type = AikidoSSRF
             blocked_request = is_blocking_enabled() and injection_results
             if not blocked_request: