 from optparse import OptionParser
 from time import time
 import tempfile
import pickle
 
 from bigdl.orca import init_orca_context, stop_orca_context
 from bigdl.orca.data.file import exists, makedirs
         get_remote_file_to_local(os.path.join(data_dir, "meta/categorical_sizes.pkl"),
                                  os.path.join(local_path, "categorical_sizes.pkl"))
         with open(os.path.join(local_path, "categorical_sizes.pkl"), 'rb') as f:
            cat_sizes_dic = pickle.load(f)
 
     indicator_sizes = [cat_sizes_dic[c] for c in indicator_cols]
     print("indicator sizes: ", indicator_sizes)