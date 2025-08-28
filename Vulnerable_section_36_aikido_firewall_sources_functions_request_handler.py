 
         # Create a lifecycle cache
         IPCLifecycleCache(get_current_context())

    elif stage == "pre_response":
         return pre_response()
    elif stage == "post_response":
         return post_response(status_code)
 
 
 def pre_response():
     if ratelimit_res["success"] and ratelimit_res["data"]["block"]:
 
         message = "You are rate limited by Aikido firewall"
        if ratelimit_res["data"]["trigger"] is "ip":
             message += f" (Your IP: {context.remote_address})"
         return (message, 429)
 