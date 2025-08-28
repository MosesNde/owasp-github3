 from mindsdb.utilities.config import Config
 from mindsdb.utilities.context import context as ctx
 from mindsdb.utilities import log
 
 logger = log.getLogger(__name__)
 
 
         def on_file(file):
             nonlocal file_object
            data["file"] = file.file_name.decode()
             file_object = file.file_object
 
         temp_dir_path = tempfile.mkdtemp(prefix="mindsdb_file_")
 
         if data.get("source_type") == "url":
             url = data["source"]
            data["file"] = data["name"]
 
             config = Config()
             is_cloud = config.get("cloud", False)
             if is_cloud is True and ctx.user_class != 1:
                 info = requests.head(url)
                 file_size = info.headers.get("Content-Length")
                     for chunk in r.iter_content(chunk_size=8192):
                         f.write(chunk)
 
        original_file_name = data.get("original_file_name")
 
         file_path = os.path.join(temp_dir_path, data["file"])
         lp = file_path.lower()