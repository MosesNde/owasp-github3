 
     def aikido_new_func(*args, op=op, former_func=former_func, **kwargs):
         logger.debug("Wrapper - `subprocess` on %s() function", op)
         if isinstance(args[0], list):
             command = " ".join(args[0])
         else:
             command = args[0]
        run_vulnerability_scan(
            kind="shell_injection",
            op=f"subprocess.{op}",
            args=(command,),
        )
         return former_func(*args, **kwargs)
 
     return aikido_new_func