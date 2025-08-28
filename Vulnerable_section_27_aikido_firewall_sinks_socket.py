 
     def aik_new_func(*args, **kwargs):
         res = former_func(*args, **kwargs)
        if op is "getaddrinfo":
             run_vulnerability_scan(
                 kind="ssrf", op="socket.getaddrinfo", args=(res, args[0], args[1])
             )