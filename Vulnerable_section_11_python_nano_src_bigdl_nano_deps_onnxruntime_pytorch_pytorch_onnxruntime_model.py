 from bigdl.nano.pytorch.context_manager import generate_context_manager, BaseContextManager
 from bigdl.nano.utils.pytorch import patch_attrs_from_model_to_object, \
     MetaData
import pickle
 
 
 class PytorchONNXRuntimeModel(ONNXRuntimeModel, AcceleratedLightningModule):
             output_metadata = None
         else:
             with open(path / status['metadata_path'], "rb") as f:
                output_metadata = pickle.load(f)
         return PytorchONNXRuntimeModel(str(onnx_path),
                                        onnxruntime_session_options=onnxruntime_session_options,
                                        output_tensors=output_tensors,
         super()._save_model(onnx_path)
         # save metadata
         with open(path / self.status['metadata_path'], "wb") as f:
            pickle.dump(self.output_metadata, f)