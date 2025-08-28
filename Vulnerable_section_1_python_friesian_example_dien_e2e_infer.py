 import os
 import time
 import yaml
import pickle
 import random
 import numpy as np
 from argparse import ArgumentParser
     # Currently long id is not supported for add_negative_samples and add_value_features,
     # cast to int.
     with open(args.index_folder + "vocs/cat_voc.pkl", "rb") as f:
        category_df = sc.parallelize(list(pickle.load(f).items())).toDF(["category", "id"])
         category_index = StringIndex(category_df, "category").cast("id", "int")
     with open(args.index_folder + "vocs/mid_voc.pkl", "rb") as f:
        item_df = sc.parallelize(list(pickle.load(f).items())).toDF(["item", "id"])
         item_index = StringIndex(item_df, "item").cast("id", "int")
     with open(args.index_folder + "vocs/uid_voc.pkl", "rb") as f:
        user_df = sc.parallelize(list(pickle.load(f).items())).toDF(["user", "id"])
         user_index = StringIndex(user_df, "user").cast("id", "int")
     # user_index = StringIndex.read_parquet(args.index_folder + "user.parquet")
     # item_index = StringIndex.read_parquet(args.index_folder + "item.parquet")