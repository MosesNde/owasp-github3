 `Django` source module for django-gunicorn, intercepts django import and adds Aikido middleware
 """
 
 import json
 import copy
 import importhook
from aikido_firewall.helpers.logging import logger
 from aikido_firewall.context import Context
 from aikido_firewall.background_process.packages import add_wrapped_package
 from .functions.request_handler import request_handler
     """Aikido middleware that handles ratelimiting"""
     response = request_handler(stage="pre_response")
     if response:
         from django.http import HttpResponse
 
         return HttpResponse(response[0], status=response[1])
 
 
 @importhook.on_import("django.core.handlers.base")
     Hook 'n wrap on `django.core.handlers.base`
     Our goal is to wrap the `load_middleware` function
     # https://github.com/django/django/blob/790f0f8868b0cde9a9bec1f0621efa53b00c87df/django/core/handlers/base.py#L140
    So we can wrap te `_middleware_chain` function; Returns : Modified django.core.handlers.base object
     """
     modified_django = importhook.copy_module(django)
 