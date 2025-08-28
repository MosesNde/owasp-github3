 
 
 import os
import pickle
 from pathlib import Path
 from typing import Sequence, Any, Union, Dict
 from tempfile import TemporaryDirectory
                                       input_sample=None,
                                       onnxruntime_session_options=onnxruntime_session_options)
         with open(Path(path) / status['attr_path'], "rb") as f:
            attrs = pickle.load(f)
         for attr_name, attr_value in attrs.items():
             setattr(model, attr_name, attr_value)
         if os.path.exists(Path(path) / status['compile_path']):
             with open(Path(path) / status['compile_path'], "rb") as f:
                kwargs = pickle.load(f)
                 model.compile(**kwargs)
         return model
 
         attrs = {"_mode": self._mode,
                  "_inputs_dtypes": self._inputs_dtypes}
         with open(path / self.status['attr_path'], "wb") as f:
            pickle.dump(attrs, f)
 
         if self._is_compiled:
             kwargs = {"run_eagerly": self._run_eagerly,
                     else:
                         kwargs["weighted_metrics"] = weighted_metrics._name
             with open(path / self.status['compile_path'], "wb") as f:
                pickle.dump(kwargs, f)