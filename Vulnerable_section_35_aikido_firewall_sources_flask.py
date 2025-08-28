 Flask source module, intercepts flask import and adds Aikido middleware
 """
 
import copy
 import importhook
 from aikido_firewall.helpers.logging import logger
 from aikido_firewall.context import Context
 from aikido_firewall.background_process.packages import add_wrapped_package
from .functions.request_handler import request_handler
 from aikido_firewall.context import get_current_context
 
 
 def generate_aikido_view_func_wrapper(former_view_func):
     """
 
     def aikido_view_func(*args, **kwargs):
         from werkzeug.exceptions import HTTPException
         from flask.globals import request_ctx
 
         req = request_ctx.request
         # Set body :
        context = get_current_context()
        if context:
            if req.is_json:
                context.body = req.get_json()
            elif req.form:
                context.body = req.form
            else:
                context.body = req.data.decode("utf-8")
            context.set_as_current_context()
 
        pre_response = request_handler(stage="pre_response")
         if pre_response:
             return pre_response[0], pre_response[1]
         try:
         """
         return generate_aikido_view_func_wrapper(func)
 
     setattr(modified_flask.Flask, "__call__", aikido___call__)
     setattr(modified_flask.Flask, "ensure_sync", aikido_ensure_sync)
     add_wrapped_package("flask")