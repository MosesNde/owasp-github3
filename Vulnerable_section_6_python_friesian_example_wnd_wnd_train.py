 import os
 import math
 import tempfile
import pickle
 from time import time
 from argparse import ArgumentParser
 
         get_remote_file_to_local(os.path.join(data_dir, "meta/categorical_sizes.pkl"),
                                  os.path.join(local_path, "categorical_sizes.pkl"))
         with open(os.path.join(local_path, "categorical_sizes.pkl"), 'rb') as f:
            cat_sizes_dict = pickle.load(f)
         get_remote_file_to_local(os.path.join(data_dir, "meta/cross_sizes.pkl"),
                                  os.path.join(local_path, "cross_sizes.pkl"))
         with open(os.path.join(local_path, "cross_sizes.pkl"), 'rb') as f:
            cross_sizes_dict = pickle.load(f)
 
     wide_cols = [col for col in CAT_COLS if cat_sizes_dict[col] <= 10]
     wide_dims = [cat_sizes_dict[col] for col in wide_cols]