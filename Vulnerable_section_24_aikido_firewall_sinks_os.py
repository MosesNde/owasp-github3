 
 import copy
 import importhook
from aikido_firewall.vulnerabilities import run_vulnerability_scan
 
 # File functions :
 OS_FILE_FUNCTIONS = [
     "remove",
     "symlink",
     "link",
    "makedirs",
     "walk",
 ]
 OS_PATH_FUNCTIONS = [
     """
 
     def aikido_new_func(*args, op=op, former_func=former_func, **kwargs):
        #  args[0] : filename
        run_vulnerability_scan(kind="path_traversal", op=f"os.{op}", args=(args[0],))
         return former_func(*args, **kwargs)
 
     return aikido_new_func