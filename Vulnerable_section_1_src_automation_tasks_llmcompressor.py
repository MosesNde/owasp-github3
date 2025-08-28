         if self.dataset_loader is not None:
             configs["dataset loader"] = serialize_callable(self.dataset_loader)
         if self.data_collator is not None:
            configs["dataset collator"] = serialize_callable(self.data_collator)
         return configs
 
 