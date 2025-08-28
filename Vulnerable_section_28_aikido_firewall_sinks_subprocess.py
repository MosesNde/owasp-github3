 
 import copy
 import importhook
from aikido_firewall.helpers.logging import logger
from aikido_firewall.vulnerabilities import run_vulnerability_scan
 
 SUBPROCESS_OPERATIONS = ["call", "run", "check_call", "Popen", "check_output"]
 
     """
 
     def aikido_new_func(*args, op=op, former_func=former_func, **kwargs):
        logger.debug("Wrapper - `subprocess` on %s() function", op)
         shell_enabled = kwargs.get("shell")
 
        if isinstance(args[0], list):
             command = " ".join(args[0])
        else:
             command = args[0]
 
         # For all operations above: call, run, check_call, Popen, check_output, default value
         # of the shell property is False.
        if shell_enabled is True:
            run_vulnerability_scan(
                 kind="shell_injection",
                 op=f"subprocess.{op}",
                 args=(command,),