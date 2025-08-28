 
 
 def faiss_search(faiss_index_pkl, item_dict_pkl, cluster_mode, batch_size=65536, k=200):
    import pickle
     import faiss
 
     if cluster_mode == 'yarn':
 
     def do_search(partition):
         with open_pickle(faiss_index_pkl, load_SPARK) as index_pkl:
            faiss_idx = faiss.deserialize_index(pickle.load(index_pkl))
 
         with open_pickle(item_dict_pkl, load_SPARK) as f:
            item_dict = pickle.load(f)
 
         buffer = []
         for record in partition: