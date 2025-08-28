 import os
 import io
 import shutil
 import random
 import requests
 import uuid
 from flask import current_app, request
 from werkzeug.utils import secure_filename
 
     return f'File not allowed {file.filename}'
 
 
 def use_file_url(file_url, filter_name):
    file_request = requests.get(file_url)
 
     name = uuid.uuid4().hex
     filename = secure_filename(name + '.png')