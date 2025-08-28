 import requests
 import tempfile
 import importlib
 import itertools
 import traceback
 import subprocess
     return url
 
 
 def get_xpath_value(
     element: etree.Element, xpath_expression: str, nsmap: typing.Optional[dict] = None
 ) -> typing.Optional[str]: