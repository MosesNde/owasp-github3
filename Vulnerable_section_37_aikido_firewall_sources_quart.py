     """
     # At this stage no middleware is called yet, running pre_response is
     # not what we need to do now, but we can store the body inside context :
    context = get_current_context()
    if context:
        if req.is_json:
            context.body = req.get_json()
        elif req.form:
            context.body = await req.form
        else:
            data = await req.data
            context.body = data.decode("utf-8")
        context.set_as_current_context()
 
     # Fetch response and run post_response handler :
     from werkzeug.exceptions import HTTPException
 
     try:
                 return await send_status_code_and_text(send, pre_response)
         return await former_asgi_app(quart_app, scope, receive, send)
 
     setattr(modified_quart.Quart, "__call__", aikido___call__)
     setattr(modified_quart.Quart, "handle_request", aikido_handle_request)
     setattr(modified_quart.Quart, "asgi_app", aikido_asgi_app)