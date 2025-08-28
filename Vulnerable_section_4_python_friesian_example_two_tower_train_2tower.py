 # limitations under the License.
 #
 
import pickle
 import argparse
 import math
 from model import *
         get_remote_file_to_local(os.path.join(args.data_dir, "meta/categorical_sizes.pkl"),
                                  local_path)
         with open(os.path.join(local_path, "categorical_sizes.pkl"), 'rb') as f:
            cat_sizes_dict = pickle.load(f)
             for col in id_cols:
                 if col not in embed_in_dims:
                     embed_in_dims[col] = cat_sizes_dict[col]