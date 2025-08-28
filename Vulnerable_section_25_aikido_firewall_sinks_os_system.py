 
 import copy
 import importhook
from aikido_firewall.vulnerabilities import run_vulnerability_scan
 
 
 @importhook.on_import("os")
 
     former_system_func = copy.deepcopy(os.system)
 
    def aikido_new_system(*args, former_system_func=former_system_func, **kwargs):
        #  args[0]: Command
        run_vulnerability_scan(kind="shell_injection", op="os.system", args=(args[0],))
        return former_system_func(*args, **kwargs)
 
     setattr(os, "system", aikido_new_system)
     setattr(modified_os, "system", aikido_new_system)