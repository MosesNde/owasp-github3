 
 import copy
 import importhook
from aikido_firewall.vulnerabilities import run_vulnerability_scan
 
 
 @importhook.on_import("builtins")
 
     def aikido_new_open(*args, **kwargs):
         #  args[0] is the filename
        run_vulnerability_scan(
            kind="path_traversal", op="builtins.open", args=(args[0],)
        )
         return former_open(*args, **kwargs)
 
     # pylint: disable=no-member