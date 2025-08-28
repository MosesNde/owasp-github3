             modified_env = os.environ.copy()
             modified_env.update(env)
             # For servers, just import mxnet and no need to do anything else.
            subprocess.Popen("python -c 'import mxnet'", shell=True, env=modified_env)
 
     def train(self, train_data, epochs=1, batch_size=32,
               validation_data=None, train_resize_batch_num=None):