 from bigdl.nano.pytorch.context_manager import generate_context_manager, BaseContextManager
 from bigdl.nano.utils.pytorch import get_input_example, get_forward_args, \
     patch_attrs_from_model_to_object, MetaData
import pickle
 
 
 class PytorchOpenVINOModel(AcceleratedLightningModule):
             output_metadata = None
         else:
             with open(path / status['metadata_path'], "rb") as f:
                output_metadata = pickle.load(f)
         return PytorchOpenVINOModel(xml_path,
                                     config=config,
                                     thread_num=thread_num,
         save(self.ov_model.ie_network, xml_path)
         # save metadata
         with open(path / self.status['metadata_path'], "wb") as f:
            pickle.dump(self.output_metadata, f)
 
     def async_predict(self,
                       input_data: Union[DataLoader, List[torch.Tensor], List[List[torch.Tensor]]],