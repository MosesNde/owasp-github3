 import json
 import os
 import shutil
 import tarfile
 import tempfile
             "Can pass {0} as only one of: URL via query parameters, "
             "request body, multi-form or chunked.".format(data_type))
     try:
         with requests.get(url, stream=True, timeout=(5, None)) as resp:
             resp.raise_for_status()
             with open(archive_target_path, 'wb') as f: