     # This only works for anaconda3
     import subprocess
     pro = subprocess.Popen(
        "conda info",
         shell=True,
         stdout=subprocess.PIPE,
         stderr=subprocess.PIPE)
         return [remove_batch(s) for s in shape]
     else:
         return list(shape[1:])