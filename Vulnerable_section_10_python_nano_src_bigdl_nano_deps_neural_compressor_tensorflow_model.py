 # limitations under the License.
 #
 import os
import pickle
 import yaml
 from pathlib import Path
 from typing import Sequence, Any, Union, Dict
                     else:
                         kwargs["weighted_metrics"] = weighted_metrics._name
             with open(path / self.status['compile_path'], "wb") as f:
                pickle.dump(kwargs, f)
 
     @staticmethod
     def _load(path, model=None):
 
         if os.path.exists(Path(path) / status['compile_path']):
             with open(Path(path) / status['compile_path'], "rb") as f:
                kwargs = pickle.load(f)
                 model.compile(**kwargs)
         return model