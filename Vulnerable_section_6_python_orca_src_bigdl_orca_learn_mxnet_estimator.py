         modified_env.update(env)
         # Need to contain system env to run bash
         # TODO: Need to kill this process manually?
        subprocess.Popen("python -c 'import mxnet'", shell=True, env=modified_env)
 
         ray.get([
             runner.setup_distributed.remote(envs[i], self.config,