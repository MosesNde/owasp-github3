 # limitations under the License.
 #
 
import pickle
 import string
 import numpy as np
 import math
     for file, obj in [(args.dict_path, item_dict)]:
         with open(file, "wb") as f:
             print('saving to: {}'.format(file))
            pickle.dump(obj, f)
     # https://github.com/matsui528/faiss_tips#io
 
     with open(args.index_save_path, "wb") as f:
         print('saving to: {}'.format(args.index_save_path))
         # serialize the index into binary array (np.array).
         # You can save/load it via numpy IO functions.
         chunk = faiss.serialize_index(index_faiss)
        pickle.dump(chunk, f)
 
     if args.verbose:
         # sample
         print(f"loading {args.dict_path}")
 
         with open(args.dict_path, "rb") as f:
            item_dict_loaded = pickle.load(f)
         print(item_dict_loaded.shape)
         print(item_dict_loaded[:10])
 
         q_vec = emb_vecs[[0, ]]
         print(q_vec.shape)
 
         with open(args.index_save_path, "rb") as f:
            index_loaded = faiss.deserialize_index(pickle.load(f))
             search_sample(index_loaded, q_vec)
 
 