 import yaml
 
 from ayon_server.addons.addon import METADATA_KEYS, BaseServerAddon
from ayon_server.config import ayon_config
 from ayon_server.helpers.modules import classes_from_module, import_module
 from ayon_server.logging import log_traceback, logger
 from ayon_server.utils import slugify
         # the server-part of the addon directly from the git repository
         # on the server
 
        if ayon_config.use_git_suffix_for_addons:
             if os.path.exists(os.path.join(addon_dir, ".git")):
                 version = metadata["version"].split("-")[0]
                 version = version.split("+")[0]